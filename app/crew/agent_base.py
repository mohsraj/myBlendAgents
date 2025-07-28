from agents import Agent, Runner, trace, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import yaml, json, os
from app.logging_utils import logger
import asyncio
from app.test import get_submission


def load_config(path: str = "./agent_configs.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


agent_config = load_config()


def get_base_agent(name, instructions) -> Agent:
    """Retrieve an agent by name"""
    logger.debug(f"Retrieving agent: {name}")
    if name not in agent_config:
        raise ValueError(f"Agent '{name}' not found in configuration.")

    if agent_config[name].get("enabled", True) is False:
        raise ValueError(f"Agent '{name}' is disabled in configuration.")

    provider = (
        agent_config.get(name, {}).get("llm_config", {}).get("provider", "openai")
    )
    if provider == "openai":

        os.environ["OPENAI_API_KEY"] = (
            agent_config.get(name, {}).get("llm_config", {}).get("api_key")
        )
        logger.debug(f"Using OpenAI API key: {os.environ['OPENAI_API_KEY']}")

        return Agent(
            name=name,
            model=agent_config.get(name, {}).get("llm_config", {}).get("model"),
            instructions=instructions,
        )

    ai_client = AsyncOpenAI(
        base_url=agent_config.get(name, {}).get("llm_config", {}).get("base_url"),
        api_key=agent_config.get(name, {}).get("llm_config", {}).get("api_key"),
    )

    ai_model = OpenAIChatCompletionsModel(
        model=agent_config.get(name, {}).get("llm_config", {}).get("model"),
        openai_client=ai_client,
    )
    return Agent(name=name, instructions=instructions, model=ai_model)


def run_agent(agent, input_data):
    """Run the agent with the provided questionnaire data"""

    async def run():
        thread_id = "newthread-12345"
        with trace(workflow_name="Conversation", group_id=thread_id) as span:
            logger.info(f"trace id: {span.trace_id}")
            result = await Runner.run(
                starting_agent=agent,
                input=[input_data],
                max_turns=agent_config.get(agent.name, {})
                .get("llm_config", {})
                .get("max_turns"),
            )
            return result, result.final_output, span.trace_id

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())
