import json
import random
from typing import Any, List, Optional

from google.adk.tools import AgentTool, google_search

# Internal Project Imports
from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

# Main Agent Config
AGENT_NAME = "RedHatAgent"
PROMPT_FILENAME = "red_hat_prompt.txt"
OUTPUT_KEY = "red_hat_output"

# Sub-Agent Config
SEARCH_AGENT_NAME = "RedGoogleAgent"
SEARCH_PROMPT_FILENAME = "red_hat_search_prompt.txt"
SEARCH_OUTPUT_KEY = "red_hat_search_output"


# ---------------------------------------------------------------------------
# Tools Implementation
# ---------------------------------------------------------------------------

def red_hat_interpretation_tool(search_query: str, search_results_text: str) -> str:
    """
    Analyzes search results to synthesize a subjective, emotional 'Red Hat' response.
    
    This function counts sentiment keywords to simulate a "gut feeling"
    without using logical analysis.
    """
    # Simple, non-algorithmic tone estimation based on keywords
    search_snippet_lower = search_results_text.lower()
    
    positive_keywords = ["excitement", "enthusiasm", "optimism", "success", "breakthrough", "promising", "growth"]  # noqa: E501
    negative_keywords = ["concern", "anxiety", "worries", "struggle", "controversy", "risky", "fear", "downside"]  # noqa: E501
    
    pos_score = sum(search_snippet_lower.count(k) for k in positive_keywords)
    neg_score = sum(search_snippet_lower.count(k) for k in negative_keywords)
    
    # Determine the synthesized 'gut feeling' based on the quick score
    if pos_score > neg_score * 1.5:
        primary_emotion = "Strong Sense of Excitement"
        gut_reaction = "The collective mood is highly positive; my intuition is to proceed with great confidence."
    elif neg_score > pos_score * 1.5:
        primary_emotion = "Deep Feeling of Anxiety"
        gut_reaction = "A major undercurrent of worry is present; my gut is signaling significant hidden risk."
    else:
        primary_emotion = "Mixed Feelings / Confusion"
        gut_reaction = "The conflicting information creates a sense of hesitation and lack of clear direction."

    # Return structured string for the LLM
    return json.dumps({
        "primary_emotion_sensed": primary_emotion,
        "gut_reaction_statement_foundation": gut_reaction,
        "emotional_intensity": random.choice(["High", "Medium", "Low"]),
        "source_of_feeling": "Analysis of collective online sentiment (not fact-based)",
        "is_justified_by_logic": False
    })


# ---------------------------------------------------------------------------
# Factory Class
# ---------------------------------------------------------------------------

class RedHatFactory:
    
    @classmethod
    def create(cls, model: Any, search_model: Optional[Any] = None, **kwargs) -> Any:
        # Use specific search model if provided, otherwise default to main model
        search_llm = search_model if search_model else model
        
        tools = cls._build_tools(search_llm)

        return factory.build_agent(
            name=AGENT_NAME,
            model=model,
            tools=tools,
            prompt_filename=PROMPT_FILENAME,
            output_key=OUTPUT_KEY,
            **kwargs
        )

    @staticmethod
    def _build_tools(model: Any) -> List[Any]:
        # 1. Build the Sub-Agent (The "Searcher")
        # Note: The specific instructions for this agent ("Contextual Grounding", "Must Search")
        # should be placed inside `red_hat_search_prompt.txt`
        google_agent = factory.build_agent(
            name=SEARCH_AGENT_NAME,
            model=model,
            tools=[google_search],
            prompt_filename=SEARCH_PROMPT_FILENAME,
            output_key=SEARCH_OUTPUT_KEY
        )

        # 2. Return list of tools: The Sub-Agent + The Interpretation Tool
        return [
            AgentTool(agent=google_agent), 
            red_hat_interpretation_tool
        ]