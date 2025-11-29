import logging
from importlib import resources

logger = logging.getLogger(__name__)

def load_prompt_text(filename: str) -> str:
    """Load a prompt from the bundled ``agents_intensive_capstone.prompts`` package.

    Raises
    ------
    FileNotFoundError
        If the prompt file is missing.
    RuntimeError
        For any other I/O problem.
    """
    logger.info("Attempting to load prompt %r", filename)

    try:
        text = resources.read_text(__package__, filename, encoding="utf-8").strip()
        logger.debug("Prompt %r loaded (length=%d)", filename, len(text))
        return text
    except FileNotFoundError as exc:
        logger.warning(
            "Prompt file %r not found in package resources – no default will be used.",
            filename,
        )
        raise
    except OSError as exc:
        logger.error(
            "Unexpected I/O error while loading prompt %r: %s",
            filename,
            exc,
            exc_info=True,
        )
        raise RuntimeError(f"Failed to load prompt '{filename}'") from exc