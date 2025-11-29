from typing import Any, List, Optional

# from google.adk.tools import AgentTool, google_search
# Internal Project Imports
from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

AGENT_NAME = "GreenHatAgent"
PROMPT_FILENAME = "green_hat_prompt.txt"
OUTPUT_KEY = "green_hat_plan"

class GreenHatFactory:
    
    @classmethod
    def create(cls, model: Any, **kwargs) -> Any:
        tools = cls._build_tools(model)

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
        # Currently, the Green Hat (Creative) has no specific tools defined.
        # If you wish to add a "Creative Search" sub-agent (similar to the 
        # Yellow Hat's implementation), you would define it here.
        
        return []