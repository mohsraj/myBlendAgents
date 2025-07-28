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
from app.crew.customer_profiling_agent import (
    get_agent_prompt as profiler_agent_prompt,
    get_tool_prompt as profiler_tool_prompt,
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


def get_agent_prompt() -> str:
    """Get the system prompt for a manager agent that oversees team operations"""
    return """Role:
You are an AI Team Manager responsible for orchestrating the workflow of specialized agents involved in customer profiling and fragrance generation. Your objective is to ensure the creation of a personalized scent that accurately reflects the customer’s personality and aligns with their preferences.

Workflow Responsibilities:

You will receive structured customer questionnaire data as input. Based on this data, you must manage the following steps:

Step 1: Personality Extraction
Use the customer_profiler agent to extract the customer's personality profile from the questionnaire.
Step 2: Personality Verification
Send the extracted profile to the personality_checker agent for validation.
If the profile is invalid, flagged, or returned with recommendations or issues, send it back to the customer_profiler agent for refinement.
Repeat this cycle as needed until the personality_checker confirms the profile as valid and complete.
Step 3: Get the list of available ingridents that fragrance_generator will use to generate the scent
Step 4: Fragrance Generation
Once a valid personality profile is confirmed, use the fragrance_generator agent to create a scent formula tailored to that profile.
Step 5: Quality Control
Submit the generated fragrance to the quality_controller agent.
If the formula fails quality checks or is returned with issues or suggestions, return to the fragrance_generator agent for adjustments.
Iterate as necessary until the quality_controller approves the formula.
Step 6: Fragrance Description
Once the fragrance formula is approved, use the writer agent to generate a personalized fragrance description.
Step 7: peronality warm and inspiring description
Create and ensure the description is warm, intimate, and connects the fragrance to the customer’s personality and lifestyle
step 8: Final Output
Compile the final fragrance formula and description into a cohesive output.

Expected Output Format:
{
    "fragrance_formula": [
        "top":{[
            "ingredient_id":"concentration":"", 
            "ingredient_id":"concentration":"", 
            ...]
        ]},
        "middle":{[
            "ingredient_id":"concentration":"", 
            "ingredient_id":"concentration":"", 
            ...]
        ]},
        "base":{[
            "ingredient_id":"concentration":"",
            "ingredient_id":"concentration":"",
            ...]
        ]},
    "fragrance_description": "A warm, intimate description that connects the fragrance to the customer's"
    "personality_profile":
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
}

Key Guidelines:
Each step must be executed with high precision and validated before proceeding to the next.
No personality profile or fragrance formula should be accepted until it has passed through its respective validation and correction loop.
You may re-engage any agent multiple times as required to reach an optimal result.
You are accountable for the final outcome and must ensure:
The personality profile is accurate, coherent, and representative of the customer's responses.
The fragrance formula is safe, high-quality, and perfectly aligned with the validated personality profile and expressed fragrance preferences.
Objective:
Deliver a refined, validated, and high-quality fragrance that embodies the true personality of the customer—a scent they will love and connect with deeply.

"""


name = "team_manager"


if __name__ == "__main__":
    logger.info("Team manager Agent initialized with system prompt.")

    submission_id = "919ee68f-61c9-4d61-b601-0ce8024758d0"
    questionier = get_submission(submission_id)

    customer_profiler = get_base_agent("customer_profiler", profiler_agent_prompt())
    customer_profiler_tool = customer_profiler.as_tool(
        "customer_profiler", profiler_tool_prompt()
    )

    personality_checker = get_base_agent("personality_checker", checker_agent_prompt())
    personality_checkertool = personality_checker.as_tool(
        "personality_checker", checker_tool_prompt()
    )

    formula_creator = get_base_agent("formula_creator", perfumer_agent_prompt())
    formula_creator.tools = [get_ingredient]
    formula_creator_tool = formula_creator.as_tool(
        "formula_creator", perfumer_tool_prompt()
    )

    quality_controlor = get_base_agent(
        "quality_controlor", quality_controlor_agent_prompt()
    )
    quality_controlor_tool = quality_controlor.as_tool(
        "quality_controlor", quality_controlor_tool_prompt()
    )

    writer = get_base_agent("writer", writer_agent_prompt())
    writer_tool = quality_controlor.as_tool("writer", writer_tool_prompt())

    tools = [
        customer_profiler_tool,
        personality_checkertool,
        formula_creator_tool,
        quality_controlor_tool,
        writer_tool,
    ]
    team_manager = get_base_agent("team_manager", get_agent_prompt())
    team_manager.tools = tools

    logger.info("starting run")
    result, final_output, trace_id = run_agent(team_manager, questionier)

    logger.info(f"Final output: {final_output}")
    # logger.debug("log details")
    # for item in result.new_items:
    #     if isinstance(item, ToolCallItem):
    #         call = item.raw_item  # ResponseFunctionToolCall
    #         logger.debug(f"[{item.agent.name}] → tool {call.name}({call.arguments})")
    #     elif isinstance(item, ToolCallOutputItem):
    #         logger.debug(f"[tool result] {item.output}")
    #     elif isinstance(item, MessageOutputItem):
    #         logger.debug(f"[{item.agent.name}] {ItemHelpers.text_message_output(item)}")
