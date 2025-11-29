
import litellm
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from agents_intensive_capstone.agents import (
    black_hat_factory,
    blue_hat_factory,
    green_hat_factory,
    white_hat_factory,
    yellow_hat_factory,
)

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

litellm.use_litellm_proxy = True
gpt_model = LiteLlm(model="gpt-oss-20b")

gemini_model = Gemini(
    model="gemini-2.5-flash-lite",
    retry_options=retry_config,
)

# main_model = search_model

# WHITE HAT: Facts & Data
white_hat = white_hat_factory.WhiteHatFactory.create(
    model=gemini_model
)

# RED HAT: Emotions & Intuition
red_hat = Agent(
    name="RedHat",
    model=gpt_model,
    instruction="You are the Red Hat. Focus on intuition, hunches, and emotional reaction. How does this problem make users or the team feel? You do not need to justify your feelings with logic.",
    output_key="red_hat_plan"
)

# BLACK HAT: Caution & Risk
black_hat = black_hat_factory.BlackHatFactory.create(
    model=gpt_model
)

# YELLOW HAT: Optimism & Benefits
yellow_hat = yellow_hat_factory.YellowHatFactory.create(
    model=gemini_model,
    search_model=gemini_model
)

# GREEN HAT: Creativity & Alternatives
green_hat = green_hat_factory.GreenHatFactory.create(
    model=gpt_model
)

# Create the Parallel Group
# This runs all 5 agents at the same time on the user prompt
thinking_team = ParallelAgent(
    name="SixHatsBrainstorm",
    sub_agents=[white_hat, red_hat, black_hat, yellow_hat, green_hat]
)

# 4. Define the Blue Hat (The Manager)
# This agent sees the combined output of the team and makes the plan
blue_hat = blue_hat_factory.BlueHatFactory.create(
    model=gpt_model
)

# Create the Final Workflow
# First run the team (Parallel), then run the manager (Sequential)
# Root agent
root_agent = SequentialAgent(
    name="SixHatsSolver",
    sub_agents=[thinking_team, blue_hat]
)


