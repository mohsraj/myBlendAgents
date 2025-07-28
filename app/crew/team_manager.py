from pydantic import BaseModel
from app.logging_utils import logger
from app.db import get_submission
from app.crew.agent_base import get_base_agent, run_agent
from agents import (
    Agent,
    ToolCallItem,
    ToolCallOutputItem,
    MessageOutputItem,
    ItemHelpers,
)
from app.crew.customer_profiling_agent import profiler_tool
from app.crew.formula_creation_agent import perfumer_tool


def get_agent_prompt() -> str:
    """Get the system prompt for a manager agent that oversees team operations"""
    return """You are a team manager responsible for overseeing the workflow of specialized agents that perform tasks related to customer profiling and fragrance generation.
You have access to a set of sepcialized agents that can perform these tasks.
You will be provided with a the customer questionnaire data. 

Your task is to manage the workflow and ensure that each step is completed successfully.
You will need to:
1. Extract the personality profile from the questionnaire using the customer_profiler agent.
2. Generate the fragrance using the fragrance_generator agent.
3. Draft the scent and personality paragraphs using the wirter agent.

You can use the tools as much as you need to complete the tasks, but you must run each agent once at least in the right order.

You are responsible for the final outcome and must ensure that the final formula matches the customer profile and fragrance preferences.

"""


name = "team_manager"


def get_agent() -> Agent:
    """Retrieve an agent by name"""

    ag = get_base_agent(name, get_agent_prompt())
    ag.tools = [profiler_tool, perfumer_tool]

    return ag


if __name__ == "__main__":
    logger.info("Team manager Agent initialized with system prompt.")
    submission_id = "919ee68f-61c9-4d61-b601-0ce8024758d0"
    questionier = get_submission(submission_id)

    ag = get_agent()
    result, final_output, trace_id = run_agent(ag, questionier)

    logger.info(f"Final output: {final_output}")
    logger.debug("log details")
    for item in result.new_items:
        if isinstance(item, ToolCallItem):
            call = item.raw_item  # ResponseFunctionToolCall
            logger.debug(f"[{item.agent.name}] → tool {call.name}({call.arguments})")
        elif isinstance(item, ToolCallOutputItem):
            logger.debug(f"[tool result] {item.output}")
        elif isinstance(item, MessageOutputItem):
            logger.debug(f"[{item.agent.name}] {ItemHelpers.text_message_output(item)}")
