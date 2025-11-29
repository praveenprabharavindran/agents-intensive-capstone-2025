from __future__ import annotations

import logging

import pytest
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from agents_intensive_capstone.agents.white_hat_factory import WhiteHatFactory


@pytest.fixture
def main_model() -> Gemini:
    retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
    )
    return Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config,
    )
    

@pytest.mark.integration
def test_white_hat_factory_create_happy_path(
    main_model: LiteLlm,
    caplog: pytest.LogCaptureFixture,
) -> None:

    caplog.set_level(logging.INFO, logger="agents_intensive_capstone.agents.white_hat_factory")

    agent = WhiteHatFactory.create(
        model=main_model
    )

    assert isinstance(agent, LlmAgent)

    assert agent.name == "WhiteHatAgent"

    assert "White Hat" in agent.instruction