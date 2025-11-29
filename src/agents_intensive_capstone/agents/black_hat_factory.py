from typing import Any, List

from . import factory

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

AGENT_NAME = "BlackHatAgent"
PROMPT_FILENAME = "black_hat_prompt.txt"
OUTPUT_KEY = "black_hat_plan"

class BlackHatFactory:
    """
    Factory for creating the Black Hat Agent (Risk Analyst/Critic).
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
        Construct the tools for the Black Hat.
        
        Currently empty. The Black Hat primarily analyzes the context
        provided by the Blue Hat/Manager. If you need it to look up
        safety regulations or historical failure data, add those tools here.
        """
        return []