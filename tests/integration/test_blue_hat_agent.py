import os
from pathlib import Path
from dotenv import load_dotenv
import litellm 
from google.adk.models.lite_llm import LiteLlm 
import pytest

# ----------------------------------------------------------------------
# 1️⃣  Import the class under test
# ----------------------------------------------------------------------
from agents_intensive_capstone.agents.blue_hat_agent import BlueHatAgent

load_dotenv()

litellm.use_litellm_proxy = True 
model = LiteLlm( model="gpt-oss-20b")

# ----------------------------------------------------------------------
# 3️⃣  Fixture that creates a temporary prompt folder
# ----------------------------------------------------------------------
@pytest.fixture
def prompt_folder(tmp_path: Path) -> Path:
    """
    Creates a temporary folder containing a valid prompt file.
    """
    prompt_file = tmp_path / "blue_hat_prompt.txt"
    prompt_file.write_text(
        "You are the Blue Hat. Synthesize and resolve conflicts.\n"
        "This is a *test* prompt.\n",
        encoding="utf-8",
    )
    return tmp_path


# ----------------------------------------------------------------------
# 4️⃣  The actual test cases
# ----------------------------------------------------------------------
@pytest.mark.integration
def test_prompt_is_loaded(prompt_folder: Path):
    """The agent should read the prompt file we created."""
    agent = BlueHatAgent.create(
        model=model,
        prompt_folder=prompt_folder,
        # output_key="final_plan"
        )
    assert "You are the Blue Hat" in agent.instruction
    # The default prompt should **not** be used because the file exists
    assert "fallback" not in agent.instruction.lower()

@pytest.mark.integration
def test_fallback_prompt_when_file_missing(tmp_path: Path):
    """When the file is absent the built‑in default must be used."""
    agent = BlueHatAgent.create(
        model=model,
        prompt_folder=tmp_path,  # empty folder → FileNotFoundError inside _load_prompt
    )
    # The default prompt is defined in the class; we just check a known snippet.
    assert "You are the Blue Hat in the Six Thinking Hats framework" in agent.instruction