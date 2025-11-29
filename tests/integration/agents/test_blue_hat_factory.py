from __future__ import annotations

import logging

import litellm
import pytest
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from agents_intensive_capstone.agents.blue_hat_factory import BlueHatFactory


@pytest.fixture
def main_model() -> LiteLlm:
    litellm.use_litellm_proxy = True
    return LiteLlm(model="gpt-oss-20b")

@pytest.mark.integration
def test_blue_hat_factory_create_happy_path(
    main_model: LiteLlm,
    caplog: pytest.LogCaptureFixture,
) -> None:

    caplog.set_level(logging.INFO, logger="agents_intensive_capstone.agents.blue_hat_factory")

    agent = BlueHatFactory.create(
        model=main_model
    )

    assert isinstance(agent, LlmAgent)

    assert agent.name == "BlueHatAgent"

    assert "You are the Blue Hat" in agent.instruction