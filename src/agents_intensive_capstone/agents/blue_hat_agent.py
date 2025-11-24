import logging
from pathlib import Path
from typing import Any, ClassVar, List, Union

from google.adk.agents import LlmAgent
# from google.adk.tools import Tool  # Uncomment and use instead of Any in _build_tools if available.

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

DEFAULT_BLUE_HAT_PROMPT: str = (
    "You are the Blue Hat in the Six Thinking Hats framework. "
    "Your job is to coordinate and synthesise the outputs of the "
    "other hats into a clear, structured final plan. "
    "Summarise key points, highlight risks, and propose next steps."
)


class BlueHatAgent(LlmAgent):
    """
    The *Blue Hat* – a manager that synthesises the output of several
    thinking-hat agents and produces a final plan.

    Design choices:
      • The LLM model is injected fully configured (including retry options).
      • The instruction prompt is typically read from a file inside a
        user-provided folder, with a sane default if the file is missing.
      • Tools are decided by the class itself (via `_build_tools`).
      • We avoid overriding `__init__` so that we play nicely with
        `LlmAgent` / Pydantic construction.
    """

    # -----------------------------------------------------------------------
    # Pydantic / ADK configuration fields
    # -----------------------------------------------------------------------
    name: str = "BlueHatAgent"

    # These default values are used if a caller constructs BlueHatAgent
    # directly without the convenience constructor.
    instruction: str = DEFAULT_BLUE_HAT_PROMPT
    output_key: str = "final_plan"

    # Filename that holds the prompt (used by the factory constructor).
    PROMPT_FILENAME: ClassVar[str] = "blue_hat_prompt.txt"

    # -----------------------------------------------------------------------
    # Public factory constructor
    # -----------------------------------------------------------------------
    @classmethod
    def create(
        cls,
        *,
        model: Any,
        prompt_folder: Union[str, Path],
        **kwargs: Any,
    ) -> "BlueHatAgent":
        """
        Create a BlueHatAgent with:
          - a fully configured LLM `model`
          - a prompt loaded from `prompt_folder / PROMPT_FILENAME`, with
            fallback to a default prompt if missing
          - tools defined internally via `_build_tools()`

        Parameters
        ----------
        model:
            An instantiated, fully-configured LLM
            (e.g. `Gemini(model="gemini-2.5-flash-lite", retry_options=...)`).

        prompt_folder:
            Path to the directory that holds `blue_hat_prompt.txt`.

        **kwargs:
            Additional arguments forwarded to `LlmAgent`
            (e.g. `output_key`, `name`, etc.).
        """
        prompt_folder_path = Path(prompt_folder)
        prompt_text = cls._load_prompt(prompt_folder_path)
        tools = cls._build_tools()

        agent = cls(
            model=model,
            tools=tools,
            instruction=prompt_text,
            **kwargs,
        )

        logger.info(
            "BlueHatAgent initialised (model=%s, tools=%d, prompt_source=%s)",
            type(agent.model).__name__,
            len(agent.tools or []),
            "file" if prompt_text != DEFAULT_BLUE_HAT_PROMPT else "default",
        )

        return agent

    # -----------------------------------------------------------------------
    # Prompt handling (can be overridden in subclasses)
    # -----------------------------------------------------------------------
    @classmethod
    def _load_prompt(cls, prompt_folder: Path) -> str:
        """
        Load the instruction prompt from a file, falling back to a built-in
        default if the file is missing.

        This is kept as a separate method to honour SRP and to allow easy
        overriding in subclasses (e.g. loading from a DB or HTTP endpoint).
        """
        prompt_path = prompt_folder / cls.PROMPT_FILENAME

        try:
            text = prompt_path.read_text(encoding="utf-8").strip()
            if not text:
                logger.warning(
                    "Prompt file '%s' in '%s' is empty; using default BlueHat prompt.",
                    cls.PROMPT_FILENAME,
                    prompt_folder,
                )
                return cls._default_prompt()

            logger.debug("Loaded Blue Hat prompt from %s", prompt_path)
            return text

        except FileNotFoundError:
            logger.warning(
                "Prompt file '%s' not found in '%s'; using default BlueHat prompt.",
                cls.PROMPT_FILENAME,
                prompt_folder,
            )
            return cls._default_prompt()

        except OSError as exc:
            logger.error(
                "Failed to read prompt file '%s' in '%s': %s; using default prompt.",
                cls.PROMPT_FILENAME,
                prompt_folder,
                exc,
            )
            return cls._default_prompt()

    @staticmethod
    def _default_prompt() -> str:
        """Fallback prompt used when the external prompt file is missing."""
        return DEFAULT_BLUE_HAT_PROMPT

    # -----------------------------------------------------------------------
    # Tool wiring (internal, open for extension)
    # -----------------------------------------------------------------------
    @classmethod
    def _build_tools(cls) -> List[Any]:
        """
        Construct the tools this agent can use.

        By default, no tools are attached. Subclasses can override this
        method to define their own tool sets while keeping the public
        API (`create`) unchanged.

        Example:

            class AggregatingBlueHatAgent(BlueHatAgent):
                @classmethod
                def _build_tools(cls) -> List[Tool]:
                    return [AggregationTool(), TraceCollectorTool()]
        """
        # Example placeholder:
        # return [AggregationTool(), TraceCollectorTool()]
        return []
