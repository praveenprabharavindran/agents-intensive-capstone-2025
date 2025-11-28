from __future__ import annotations

import logging
from pathlib import Path

import litellm
import pytest
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from agents_intensive_capstone.agents.yellow_hat_factory import YellowHatFactory


# ----------------------------------------------------------------------
# 3️⃣  Fixture that creates a temporary prompt folder
# ----------------------------------------------------------------------
@pytest.fixture
def prompt_folder(tmp_path: Path) -> Path:
    """
    Creates a temporary directory containing a minimal Yellow‑Hat prompt.
    """
    prompt_file = tmp_path / "yellow_hat_prompt.txt"
    prompt_file.write_text(
        "You are the Yellow Hat. "
        "Your role is to highlight optimism and constructive possibilities."
    )
    return tmp_path

@pytest.fixture
def main_model() -> None:
    litellm.use_litellm_proxy = True
    return LiteLlm(model="gpt-oss-20b")

@pytest.fixture
def search_model() -> None:
    
    retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)
    model = Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config,
    )
    return model


@pytest.mark.integration
def test_yellow_hat_factory_create_happy_path(
    main_model: LiteLlm,
    search_model: Gemini,
    caplog: pytest.LogCaptureFixture,
) -> None:

    # Capture INFO‑level logs from the factory module
    caplog.set_level(logging.INFO, logger="agents_intensive_capstone.agents.yellow_hat")


    agent = YellowHatFactory.create(
        model=main_model,
        search_model=search_model
    )

    assert isinstance(agent, LlmAgent)

    assert agent.name == "YellowHatAgent"

    assert "You are the Yellow Hat" in agent.instruction

