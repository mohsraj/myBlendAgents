from pydantic import BaseModel
from app.logging_utils import logger
from app.db import get_submission
from app.crew.agent_base import get_base_agent, run_agent
import uuid
from agents import WebSearchTool
from app.crew.customer_profiling_agent import (
    get_agent_prompt as profiler_agent_prompt,
    get_tool_prompt as profiler_tool_prompt,
    CustomerProfilingAgent,
)
from app.crew.personality_quality_checker import (
    get_agent_prompt as checker_agent_prompt,
    get_tool_prompt as checker_tool_prompt,
)
from app.crew.formula_creation_agent import (
    get_agent_prompt as perfumer_agent_prompt,
    get_tool_prompt as perfumer_tool_prompt,
    get_ingredient,
)
from app.crew.quality_control_agent import (
    get_agent_prompt as quality_controlor_agent_prompt,
    get_tool_prompt as quality_controlor_tool_prompt,
)

from app.crew.writer_agent import (
    get_agent_prompt as writer_agent_prompt,
    get_tool_prompt as writer_tool_prompt,
)


def generate_personality(submission_id, run_id, submission):
    """Generate a personality profile from the customer submission."""

    personality_checker = get_base_agent("personality_checker", checker_agent_prompt())
    personality_checkertool = personality_checker.as_tool(
        "personality_checker", checker_tool_prompt()
    )

    customer_profiler = get_base_agent("customer_profiler", profiler_agent_prompt())
    customer_profiler.tools=[personality_checkertool]
    customer_profiler.output_type

    logger.info("starting customer profiling agent")
    result, personality, trace_id = run_agent(customer_profiler, submission, "Profiler:"+run_id)
    logger.debug(f"Final output: {personality}")

    return personality, trace_id

def generate_formula(submission_id, run_id, personality):
    """Generate a fragrance formula based on the personality profile."""
    quality_controlor = get_base_agent(
        "quality_controlor", quality_controlor_agent_prompt()
    )
    quality_controlor.tools=[WebSearchTool(search_context_size="low"), get_ingredient]
    quality_controlor_tool = quality_controlor.as_tool(
        "quality_controlor", quality_controlor_tool_prompt()
    )

    formula_creator = get_base_agent("formula_creator", perfumer_agent_prompt())
    formula_creator.tools = [get_ingredient, quality_controlor_tool, WebSearchTool(search_context_size="low")]

    messages = {"role": "user", "content": personality}
    logger.info("starting perfumer agent")
    formula_result, formula, trace_id = run_agent(formula_creator, messages, "Perfumer:"+run_id)
    logger.debug(f"Final output: {formula}")

    return formula, trace_id


def generate_scent (submission_id, run_id):
    logger.info(f"Starting Submission: {submission_id}, Run:{run_id}")
    submission = get_submission(submission_id)
    if not submission:
        raise ValueError(f"Submission {submission_id} not found")
    
    personality, personality_trace_id=generate_personality(submission_id, run_id, submission)
    logger.info(f"Personality: {personality}")
    
    formula, formula_trace_id=generate_formula(submission_id, run_id, personality)
    logger.info(f"Formula: {formula}")

    writer = get_base_agent("writer", writer_agent_prompt())
    messages = {
        "role": "user", 
        "content": f"""
Questionier: {submission}
Generated formula: {formula}
Generated personality profile: {personality}
        """
      }
    logger.info("starting writer agent")
    additional_result, additional, additional_trace_id = run_agent(writer, messages, "writer:"+run_id)
    logger.info(f"Final output: {additional}")

if __name__ == "__main__":
    run_id = str(uuid.uuid4())
    submission_id = "919ee68f-61c9-4d61-b601-0ce8024758d0"
    
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
