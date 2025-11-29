from typing import Any, List

from google.adk.tools import google_search

# Internal Project Imports
from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

# Main Agent Config
AGENT_NAME = "WhiteHatAgent"
PROMPT_FILENAME = "white_hat_prompt.txt"
OUTPUT_KEY = "whitehat_findings"

class WhiteHatFactory:
    
    @classmethod
    def create(cls, model: Any, **kwargs) -> Any:
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
        return [
            google_search,
        ]