import logging
from typing import Any, Optional

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.genai.types import HttpRetryOptions

logger = logging.getLogger(__name__)

class SummarizerAgent(LlmAgent):
    """
    A specialized Agent that receives a string of research findings
    and returns a short bulleted summary.
    """

    # -------------------------------------------------------------------------
    # Pydantic Fields (Configuration)
    # -------------------------------------------------------------------------
    name: str = "SummarizerAgent"
    
    # Default Model Configuration
    model: Gemini = Gemini(
        model="gemini-2.5-flash-lite"
    )

    # The prompt template. 
    # The agent expects the input state to contain the key 'research_findings'.
    instruction: str = """Read the user provided contnet and create a concise summary as a bulleted list with 3-5 key points.
"""

    output_key: str = "final_summary"

    # -------------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------------
    def __init__(
        self,
        *,
        retry_config: Optional[HttpRetryOptions] = None,
        **kwargs: Any,
    ) -> None:
        
        # Initialize the parent LlmAgent first (sets up defaults)
        super().__init__(**kwargs)

        # If a custom retry config is provided, update the model instance.
        # Note: usage of model_copy vs copy depends on Pydantic version. 
        # Modern Google SDKs usually use Pydantic v2.
        if retry_config is not None:
            if hasattr(self.model, "model_copy"):
                 # Pydantic v2 approach
                self.model = self.model.model_copy(update={"retry_options": retry_config})
            else:
                # Fallback/Pydantic v1 approach
                self.model = self.model.copy(update={"retry_options": retry_config})