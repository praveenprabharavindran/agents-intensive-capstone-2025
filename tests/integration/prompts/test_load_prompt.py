"""
Integration tests for the ``load_prompt_text`` helper that lives in
``agents_intensive_capstone.prompts.loader`` and is re‑exported from
``agents_intensive_capstone.prompts``.
"""

from __future__ import annotations

import logging
import pathlib
import sys

import pytest

# ----------------------------------------------------------------------
# Import the public façade – this is what production code uses.
# ----------------------------------------------------------------------
from agents_intensive_capstone.prompts import __all__, load_prompt_text  # type: ignore


@pytest.mark.integration
def test_load_existing_prompt(caplog: pytest.LogCaptureFixture) -> None:
    """The loader must return the exact contents of a bundled prompt."""
    caplog.set_level(logging.INFO)

    text = load_prompt_text("blue_hat_prompt.txt")

    assert isinstance(text, str)
    # The first line of the bundled file is known from the repository.
    assert text.startswith("You are the Blue Hat")
    # ``strip()`` removes the final newline – ensure it really happened.
    assert not text.endswith("\n")

    # ------------------------------------------------------------------
    # Logging assertions
    # ------------------------------------------------------------------
    msgs = [rec.getMessage() for rec in caplog.records]
    assert any("Attempting to load prompt 'blue_hat_prompt.txt'" in m for m in msgs)
    
@pytest.mark.integration
def test_missing_prompt_raises_warning(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.WARNING)

    missing_name = "does_not_exist.txt"
    with pytest.raises(FileNotFoundError):
        load_prompt_text(missing_name)

    msgs = [rec.getMessage() for rec in caplog.records]
    expected = (
        f"Prompt file '{missing_name}' not found in package resources – no default will be used."
    )
    assert any(expected in m for m in msgs)