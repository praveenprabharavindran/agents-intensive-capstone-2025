from typing import Any, List, Optional

from google.adk.tools import AgentTool, google_search

from agents_intensive_capstone.tools.tools import get_positive_data

# Internal Project Imports
from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

# Main Agent Config
AGENT_NAME = "YellowHatAgent"
PROMPT_FILENAME = "yellow_hat_prompt.txt"
OUTPUT_KEY = "yellow_hat_plan"

# Sub-Agent Config
SEARCH_AGENT_NAME = "google_optimist"
SEARCH_PROMPT_FILENAME = "yellow_hat_search_prompt.txt"
SEARCH_OUTPUT_KEY = "yellow_hat_search_output" 

class YellowHatFactory:
    
    @classmethod
    def create(cls, model: Any, search_model: Optional[Any] = None, **kwargs) -> Any:
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
        # Using factory to build the sub-agent
        google_agent = factory.build_agent(
            name=SEARCH_AGENT_NAME,
            model=model,
            tools=[google_search],
            prompt_filename=SEARCH_PROMPT_FILENAME,
            
            # The sub-agent will store its final answer in this key
            output_key=SEARCH_OUTPUT_KEY 
        )

        return [
            get_positive_data,
            AgentTool(agent=google_agent),
        ]