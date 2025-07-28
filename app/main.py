from dotenv import load_dotenv

# Load environment variables from .env in service root
load_dotenv(override=True)

from app.crew.agent_base import get_agent
from logging_utils import logger

if __name__ == "__main__":
    logger.info("myBlend Agent initialized with system prompt.")
    agent = get_agent(name="myBlendAgent", type="customer_profiler")
    logger.debug(f"Retrieved agent: {agent}")
