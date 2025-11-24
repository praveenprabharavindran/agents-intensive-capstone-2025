import os
from dotenv import load_dotenv
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from agents_intensive_capstone.agents.blue_hat_agent import BlueHatAgent
from agents_intensive_capstone.agents.green_hat_agent import GreenHatAgent
from pathlib import Path

import os, litellm 
from google.adk.models.lite_llm import LiteLlm 
litellm.use_litellm_proxy = True 
model = LiteLlm( model="gpt-oss-20b")

# Define the 5 "Thinking" Agents (The Team)
# WHITE HAT: Facts & Data
white_hat = Agent(
    name="WhiteHat",
    model=model,
    instruction="You are the White Hat. Focus ONLY on available data, facts, and information gaps. Be objective and neutral. Do not offer opinions, only verifiable facts or questions about missing data.",
)

# RED HAT: Emotions & Intuition
red_hat = Agent(
    name="RedHat",
    model=model,
    instruction="You are the Red Hat. Focus on intuition, hunches, and emotional reaction. How does this problem make users or the team feel? You do not need to justify your feelings with logic.",
)

# BLACK HAT: Caution & Risk
black_hat = Agent(
    name="BlackHat",
    model=model,
    instruction="You are the Black Hat. Play the devil's advocate. Identify specific risks, potential failure points, downsides, and why this idea might NOT work. Be critical.",
)

# YELLOW HAT: Optimism & Benefits
yellow_hat = Agent(
    name="YellowHat",
    model=model,
    instruction="You are the Yellow Hat. Focus on the positives. What are the benefits? What is the best-case scenario? Why will this work?",
)

# GREEN HAT: Creativity & Alternatives
green_hat = GreenHatAgent.create(
    model=model,
    prompt_folder=Path("./src/agents_intensive_capstone/prompts"),
)

# Create the Parallel Group
# This runs all 5 agents at the same time on the user prompt
thinking_team = ParallelAgent(
    name="SixHatsBrainstorm",
    sub_agents=[white_hat, red_hat, black_hat, yellow_hat, green_hat]
)

# 4. Define the Blue Hat (The Manager)
# This agent sees the combined output of the team and makes the plan
blue_hat = BlueHatAgent.create(
    model=model,
    prompt_folder=Path("./src/agents_intensive_capstone/prompts"),
)

# Create the Final Workflow
# First run the team (Parallel), then run the manager (Sequential)
# Root agent
root_agent = SequentialAgent(
    name="SixHatsSolver",
    sub_agents=[thinking_team, blue_hat]
)


