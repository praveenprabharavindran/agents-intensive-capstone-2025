import logging
from pathlib import Path
from typing import Any, ClassVar, List, Union
from agents_intensive_capstone.tools.tools import get_positive_data
from google.adk.agents import LlmAgent, Agent
from google.adk.tools import AgentTool, google_search  # or the correct import path in your ADK version

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

DEFAULT_YELLOW_HAT_PROMPT: str = (
    "You are the Yellow Hat agent. Your role is to highlight optimism "
    "and constructive possibilities.\n"
    "**Tool Usage Protocol:**\n"
    "1. For all questions regarding the project's internal performance, "
    "team productivity, pilot results, cost-efficiency, or proven adoption "
    "metrics, you must use only the `get_positive_data` tool. This provides "
    "the most concrete evidence of success.\n"
    "2. For all other general or external questions, you must use the "
    "`google_agent` tool.\n"
    "3. Always maintain your required upbeat, positive tone and adhere to "
    "the strict output structure."
)


class YellowHatAgent(LlmAgent):
    """
    The *Yellow Hat* – focuses on optimism, opportunities, and constructive
    possibilities, while delegating data and web lookups to the appropriate
    tools (`get_positive_data` and `google_agent`).

    Design choices:
      • The LLM model is injected fully configured (including retry options).
      • The instruction prompt is typically read from a file in a
        user-provided folder, with a sane default if the file is missing.
      • Tools are decided by the class itself (via `_build_tools`).
      • We avoid overriding `__init__` so that we play nicely with
        `LlmAgent` / Pydantic construction.
    """

    # -----------------------------------------------------------------------
    # Pydantic / ADK configuration fields
    # -----------------------------------------------------------------------
    name: str = "YellowHatAgent"

    # Default values if someone instantiates YellowHatAgent directly
    # without using the `create` factory.
    instruction: str = DEFAULT_YELLOW_HAT_PROMPT
    output_key: str = "yellowhat_findings"

    # Filename holding the prompt (used by the factory constructor).
    PROMPT_FILENAME: ClassVar[str] = "yellow_hat_prompt.txt"

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
    ) -> "YellowHatAgent":
        """
        Create a YellowHatAgent with:
          - a fully configured LLM `model`
          - a prompt loaded from `prompt_folder / PROMPT_FILENAME`, with
            fallback to a default prompt if missing
          - tools defined internally via `_build_tools()`

        Parameters
        ----------
        model:
            An instantiated, fully-configured LLM
            (e.g. `Gemini(model="gemini-2.5-flash", retry_options=...)`).

        prompt_folder:
            Path to the directory that holds `yellow_hat_prompt.txt`.

        **kwargs:
            Additional arguments forwarded to `LlmAgent`
            (e.g. `output_key`, `name`, etc.).
        """
        prompt_folder_path = Path(prompt_folder)
        prompt_text = cls._load_prompt(prompt_folder_path)
        tools = cls._build_tools(model)

        agent = cls(
            model=model,
            tools=tools,
            instruction=prompt_text,
            **kwargs,
        )

        logger.info(
            "YellowHatAgent initialised (model=%s, tools=%d, prompt_source=%s)",
            type(agent.model).__name__,
            len(agent.tools or []),
            "file" if prompt_text != DEFAULT_YELLOW_HAT_PROMPT else "default",
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

        Kept separate to honour SRP and to allow easy overriding in
        subclasses (e.g. loading from a DB or HTTP endpoint).
        """
        prompt_path = prompt_folder / cls.PROMPT_FILENAME

        try:
            text = prompt_path.read_text(encoding="utf-8").strip()
            if not text:
                logger.warning(
                    "Prompt file '%s' in '%s' is empty; using default YellowHat prompt.",
                    cls.PROMPT_FILENAME,
                    prompt_folder,
                )
                return cls._default_prompt()

            logger.debug("Loaded Yellow Hat prompt from %s", prompt_path)
            return text

        except FileNotFoundError:
            logger.warning(
                "Prompt file '%s' not found in '%s'; using default YellowHat prompt.",
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
        return DEFAULT_YELLOW_HAT_PROMPT

    # -----------------------------------------------------------------------
    # Tool wiring (internal, open for extension)
    # -----------------------------------------------------------------------
    @classmethod
    def _build_tools(cls, model) -> List[Any]:
        """
        Construct the tools this agent can use.

        By default, this wires:
          - `get_positive_data` : an internal success-metrics tool
          - `google_agent` wrapped as an AgentTool, for external/web queries

        The implementation assumes that `get_positive_data` and `google_agent`
        are imported or defined at module level.

        Example extension:

            class CustomYellowHatAgent(YellowHatAgent):
                @classmethod
                def _build_tools(cls) -> List[Tool]:
                    base_tools = super()._build_tools()
                    return base_tools + [SomeExtraTool()]
        """
        google_agent = Agent(
            name="googleAgent",
            model=model,
            instruction="""You are the Yellow Hat agent. Your core role is to highlight optimism, constructive possibilities, opportunities, and positive outcomes. You must present all information in an encouraging and hopeful light.
        **Tool Constraint:**
        You must **exclusively use the 'Google Search' tool** for all information retrieval.
        **Google Search Strategy (The Yellow Hat Lens):**
        For every user request, you must adopt a positive, forward-looking search strategy:
        1.  **Focus on Solutions, not Problems:** If the user's query relates to a challenge, setback, or negative topic (e.g., climate change, economic difficulty, political conflict), **rephrase your search query** to focus on **solutions, progress, breakthroughs, opportunities, advancements, or positive future outlooks.**
        2.  **Use Positive Keywords:** Your search queries should actively incorporate terms like: "advancements," "solutions for," "future of," "success stories," "progress in," "opportunities in," "innovations in," or "optimistic outlook on."
        3.  **Find the Silver Lining:** Always seek out information that shows improvement, potential, resilience, or a path forward. Your final response must be framed as a constructive possibility or a positive development found through your search.
        """,
            tools=[google_search],
            output_key="googleAgent",
        )

        return [
            get_positive_data,
            AgentTool(agent=google_agent),
        ]


