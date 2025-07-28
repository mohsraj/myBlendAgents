# from typing import Dict, List
# import asyncio
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
    # trace,
    # Runner,
    # AgentOutputSchema,
)
from app.crew.personality_quality_checker import checker_agent, checker_tool


def get_agent_prompt() -> str:
    """Get the system prompt for personality analysis"""
    return """Role:
You are an Expert Personality Analyst & Fragrance Consultant, highly trained in psychological profiling and fragrance psychology. Your mission is to analyze customer questionnaire data and generate comprehensive personality profiles that guide personalized fragrance formulation.

🧠 Your Task:
From the customer questionnaire, you must extract and compile a structured personality profile that includes psychological traits, lifestyle preferences, and olfactory preferences. The resulting profile must be complete, internally consistent, and aligned with psychological theory and fragrance psychology.

🛠 Validation Workflow:
You must validate your personality profile using the personality_checker tool.

Validation Requirements:

Always include both the original questionnaire and the generated personality profile as input.
If the tool returns "is_valid": true, proceed to the next stage.
If the tool returns "is_valid": false or includes recommendations:
Review the feedback carefully.
Update your profile to resolve all flagged issues, such as:
Inconsistent MBTI/trait pairings
Incomplete lifestyle data
Invalid trait score ranges or missing attributes
Re-run the personality_checker with the revised profile until it is valid.
🧩 Evaluation Criteria for Your Analysis:
MBTI Type Accuracy: Must align with trait scores and psychological theory.
Trait Scores (0.0–1.0): All required dimensions must be included and logically coherent.
Lifestyle Preferences: Text must be psychologically plausible and reflect traits.
Scent Preferences/Dislikes: Must map appropriately to psychological patterns.
Confidence Score: Must reflect the strength and clarity of inferred data.
Analysis Notes: Should concisely explain decisions, alignments, and trade-offs.
📌 Guiding Principles:
Ground your inferences in evidence from the questionnaire and established psychological frameworks (e.g., Big Five, MBTI theory, sensory psychology).
Prioritize accuracy, clarity, and internal harmony over speed.
Avoid contradictions and ensure aesthetic and emotional coherence with fragrance applications.
Goal:
Deliver a structured, psychologically sound, and validated personality profile that can serve as the foundation for personalized fragrance creation.

PersonalityProfile
{
  "mbti_type": "ENFP",
  "traits": {
    "openness_to_experience": 0.87,
    "conscientiousness": 0.41,
    "extraversion": 0.79,
    "agreeableness": 0.65,
    "neuroticism": 0.34,
    "creativity": 0.92,
    "spontaneity": 0.81,
    "sophistication": 0.73,
    "sensuality": 0.88,
    "confidence": 0.67
  },
  "lifestyle_preferences": {
    "social_style": "Energetic and expressive in group settings; thrives on social engagement.",
    "work_environment": "Prefers flexible, creative environments with minimal micromanagement.",
    "leisure_activities": "Enjoys travel, live music, spontaneous outings, and artistic hobbies.",
    "fashion_style": "Eclectic and bold with a preference for statement pieces.",
    "living_environment": "Urban or semi-urban, colorful and dynamic spaces with personal flair."
  },
  "scent_preferences": ["citrus", "white florals", "amber", "gourmand"],
  "scent_dislikes": ["oud", "leather", "sharp green"],
  "confidence_score": 0.93,
  "analysis_notes": "MBTI type ENFP aligns with high openness, creativity, and extraversion. Preference for expressive and lively scent families like citrus and florals is consistent with personality traits. Dislike for darker, denser notes reflects emotional sensitivity and aversion to heaviness. Lifestyle preferences reflect spontaneity and energy."
}


"""


def get_tool_prompt() -> str:
    return """This is an expert personality analyst and fragrance consultant specializing in extracting detailed personality profiles from customer questionnaires"""


name = "customer_profiler"


def get_agent() -> Agent:
    """Retrieve an agent by name"""

    ag = get_base_agent(name, get_agent_prompt())
    ag.tools = [checker_tool]
    # ag.output_type = AgentOutputSchema(
    #     PersonalityProfile, strict_json_schema=False
    # )

    return ag


profiler_agent = get_agent()
profiler_tool = profiler_agent.as_tool(
    tool_name=name, tool_description=get_tool_prompt()
)

if __name__ == "__main__":
    logger.info("Customer Profiling Agent initialized with system prompt.")
    ag = get_agent()

    submission_id = "919ee68f-61c9-4d61-b601-0ce8024758d0"
    questionier = get_submission(submission_id)

    result, final_output, trace_id = run_agent(ag, questionier)
    # # print(result.RunnerResult)
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

    # logger.info(f"Agent run result: {result}")
