import logging
from typing import Any, List

from google.adk.agents import LlmAgent

from agents_intensive_capstone.prompts import load_prompt_text

logger = logging.getLogger(__name__)


def build_agent(
    name: str,
    model: Any,
    tools: List[Any],
    prompt_filename: str,
    output_key: str,
    **kwargs
) -> LlmAgent:
    """
    Generic constructor that ensures all Hats are built identically.
    """
    instruction = load_prompt_text(prompt_filename)
    
    return LlmAgent(
        name=name,
        model=model,
        tools=tools,
        instruction=instruction,
        output_key=output_key,
        **kwargs
    )