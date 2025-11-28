from typing import Any, List

from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

AGENT_NAME = "BlueHatAgent"
PROMPT_FILENAME = "blue_hat_prompt.txt"
OUTPUT_KEY = "blue_hat_final_plan"

class BlueHatFactory:
    """
    Factory for creating the Blue Hat Agent (Manager/Coordinator).
    """

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
        """
        Construct the tools for the Blue Hat.
        
        Currently empty. The Blue Hat acts as the manager/synthesizer.
        If you later decide to give the Blue Hat specific tools (e.g., 
        a tool to explicitly query other hats rather than receiving their 
        output in context), they would go here.
        """
        return []