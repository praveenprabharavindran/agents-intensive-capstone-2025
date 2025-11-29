from __future__ import annotations

import logging

import pytest
from google.adk.models.google_llm import Gemini
from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)
from google.adk.runners import InMemoryRunner
from google.genai import types

from agents_intensive_capstone.agents.red_hat_factory import RedHatFactory


def get_model():
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

@pytest.fixture
def main_model() -> None:
    return get_model()

@pytest.fixture
def search_model() -> None:
    return get_model()

# @pytest.mark.integration
@pytest.mark.asyncio
async def test_red_hat_factory_create_happy_path(
    main_model: Gemini,
    search_model: Gemini,
    caplog: pytest.LogCaptureFixture,
) -> None:

    # Capture INFO‑level logs from the factory module
    caplog.set_level(logging.INFO, logger="agents_intensive_capstone.agents.red_hat_factory")


    agent = RedHatFactory.create(
        model=main_model,
        search_model=search_model
    )

    runner = InMemoryRunner(
    agent=agent,
    plugins=[
        LoggingPlugin()
    ], 
    )

    response = await runner.run_debug("Should we switch our backend database from PostgreSQL to a NoSQL solution for our startup?")  # noqa: E501
    print(response)

