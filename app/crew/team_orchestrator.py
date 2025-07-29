from pydantic import BaseModel
from app.logging_utils import logger
from app.db import get_submission
from app.crew.agent_base import run_agent
import uuid


def generate_scent(submission_id, run_id):
    submission = get_submission(submission_id)

    from app.crew.personality_profiler import personality_profiler

    logger.info("starting customer profiling agent")
    result, personality, trace_id = run_agent(
        personality_profiler, submission, "Profiler:" + run_id
    )
    logger.debug(f"Final Personality: {personality.model_dump_json(indent=2)}")

    messages = {
        "role": "user",
        "content": personality.model_dump_json(indent=2),
    }

    from app.crew.formula_designer import formula_designer

    logger.info("starting perfumer agent")
    formula_result, formula, trace_id = run_agent(
        formula_designer, messages, "Perfumer:" + run_id
    )
    logger.debug(formula.model_dump_json(indent=2))

    from app.crew.writer import writer

    messages = {
        "role": "user",
        "content": f"""
Questionier: {submission}
Generated formula: {formula.model_dump_json(indent=2)}
Generated personality profile: {personality.model_dump_json(indent=2)}
        """,
    }
    logger.info("starting writer agent")
    additional_result, additional, additional_trace_id = run_agent(
        writer, messages, "writer:" + run_id
    )
    logger.info(f"Final output: {additional}")


if __name__ == "__main__":
    run_id = str(uuid.uuid4())
    submission_id = "919ee68f-61c9-4d61-b601-0ce8024758d0"

    logger.info(f"Run: {run_id}")

    generate_scent(submission_id, run_id)

    # logger.debug("log details")
    # for item in result.new_items:
    #     if isinstance(item, ToolCallItem):
    #         call = item.raw_item  # ResponseFunctionToolCall
    #         logger.debug(f"[{item.agent.name}] → tool {call.name}({call.arguments})")
    #     elif isinstance(item, ToolCallOutputItem):
    #         logger.debug(f"[tool result] {item.output}")
    #     elif isinstance(item, MessageOutputItem):
    #         logger.debug(f"[{item.agent.name}] {ItemHelpers.text_message_output(item)}")
