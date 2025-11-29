from typing import Any, List

from google.adk.tools import google_search

# Internal Project Imports
from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

AGENT_NAME = "RedHatAgent"
PROMPT_FILENAME = "red_hat_prompt.txt"
OUTPUT_KEY = "red_hat_plan"

class RedHatFactory:
    
    @classmethod
    def create(cls, model: Any, **kwargs) -> Any:
        # We don't need a separate search_model here since we aren't 
        # creating a sub-agent.
        tools = cls._build_tools()

        return factory.build_agent(
            name=AGENT_NAME,
            model=model,
            tools=tools,
            prompt_filename=PROMPT_FILENAME,
            output_key=OUTPUT_KEY,
            **kwargs
        )

    @staticmethod
    def _build_tools() -> List[Any]:
        # Return google_search directly as a simple tool
        return [
            google_search,
        ]