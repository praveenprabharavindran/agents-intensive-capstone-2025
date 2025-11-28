
import litellm
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from agents_intensive_capstone.agents import (
    blue_hat_factory,
    green_hat_factory,
    yellow_hat_factory,
)

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

litellm.use_litellm_proxy = True
main_model = LiteLlm(model="gpt-oss-20b")

search_model = Gemini(
    model="gemini-2.5-flash-lite",
    retry_options=retry_config,
)

# main_model = search_model

# Define the 5 "Thinking" Agents (The Team)
# WHITE HAT: Facts & Data
white_hat = Agent(
    name="WhiteHat",
    model=main_model,
    instruction="You are the White Hat. Focus ONLY on available data, facts, and information gaps. Be objective and neutral. Do not offer opinions, only verifiable facts or questions about missing data.",
    output_key="white_hat_plan"
)

# RED HAT: Emotions & Intuition
red_hat = Agent(
    name="RedHat",
    model=main_model,
    instruction="You are the Red Hat. Focus on intuition, hunches, and emotional reaction. How does this problem make users or the team feel? You do not need to justify your feelings with logic.",
    output_key="red_hat_plan"
)

# BLACK HAT: Caution & Risk
black_hat = Agent(
    name="BlackHat",
    model=main_model,
    instruction="You are the Black Hat. Play the devil's advocate. Identify specific risks, potential failure points, downsides, and why this idea might NOT work. Be critical.",
    output_key="black_hat_plan"
)

# YELLOW HAT: Optimism & Benefits
yellow_hat_factory = yellow_hat_factory.YellowHatFactory.create(
    model=search_model,
    search_model=search_model
)

# GREEN HAT: Creativity & Alternatives
green_hat = green_hat_factory.GreenHatFactory.create(
    model=main_model
)

# Create the Parallel Group
# This runs all 5 agents at the same time on the user prompt
thinking_team = ParallelAgent(
    name="SixHatsBrainstorm",
    sub_agents=[white_hat, red_hat, black_hat, yellow_hat_factory, green_hat]
)

# 4. Define the Blue Hat (The Manager)
# This agent sees the combined output of the team and makes the plan
# blue_hat = blue_hat_agent.BlueHatAgent.create(
#     model=main_model,
#     prompt_folder=Path("./src/agents_intensive_capstone/prompts"),
# )

blue_hat = blue_hat_factory.BlueHatFactory.create(
    model=main_model
)

# Create the Final Workflow
# First run the team (Parallel), then run the manager (Sequential)
# Root agent
root_agent = SequentialAgent(
    name="SixHatsSolver",
    sub_agents=[thinking_team, blue_hat]
)


