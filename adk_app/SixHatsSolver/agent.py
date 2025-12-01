import logging
import sys
from dataclasses import dataclass, field
from typing import List

import litellm
from google.adk.agents import ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

# Custom Hat Factories
from agents_intensive_capstone.agents import (
    black_hat_factory,
    blue_hat_factory,
    green_hat_factory,
    red_hat_factory,
    white_hat_factory,
    yellow_hat_factory,
)

# ==========================================
# LOGGING & CONFIGURATION
# ==========================================

def setup_logging():
    """Configures logging to show timestamps and levels in ADK logs."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger("SixHatsAgent")

logger = setup_logging()

@dataclass
class AgentConfig:
    """Central configuration for models and retries."""
    # # Models
    gemini_model: str = "gemini-2.5-flash-lite"
    gpt_model: str = "gpt-oss-20b"
    enable_proxy: bool = True
    
    # Retry Logic
    retry_attempts: int = 5
    retry_base: int = 7
    retry_codes: List[int] = field(default_factory=lambda: [429, 500, 503, 504])

    @property
    def http_retry_options(self) -> types.HttpRetryOptions:
        return types.HttpRetryOptions(
            attempts=self.retry_attempts,
            exp_base=self.retry_base,
            initial_delay=1,
            http_status_codes=self.retry_codes,
        )

# ==========================================
# FACTORY HELPER
# ==========================================

class ModelBuilder:
    """Helper to initialize models with consistent settings."""
    def __init__(self, config: AgentConfig):
        self.config = config
        
        # Set global LiteLLM settings
        litellm.use_litellm_proxy = self.config.enable_proxy
        if self.config.enable_proxy:
            logger.info("LiteLLM Proxy enabled.")

    def create_gemini(self) -> Gemini:
        logger.debug(f"Creating Gemini model: {self.config.gemini_model}")
        return Gemini(
            model=self.config.gemini_model,
            retry_options=self.config.http_retry_options,
        )

    def create_litellm(self) -> LiteLlm:
        logger.debug(f"Creating LiteLLM model: {self.config.gpt_model}")
        return LiteLlm(model=self.config.gpt_model)

# ==========================================
# WORKFLOW ASSEMBLY
# ==========================================

def build_six_hats_agent() -> SequentialAgent:
    """Instantiates all hats and assembles the Parallel->Sequential workflow."""
    logger.info("Initializing Six Hats Agent Workflow...")
    
    config = AgentConfig()
    builder = ModelBuilder(config)
    
    # Instantiate Models
    gemini = builder.create_gemini()
    gpt = builder.create_litellm()

    try:
        # --- Instantiate The 6 Hats ---
        
        # WHITE HAT: Facts & Data
        white_hat = white_hat_factory.WhiteHatFactory.create(model=gemini)
        
        # RED HAT: Emotions & Intuition
        red_hat = red_hat_factory.RedHatFactory.create(model=gemini)
        
        # BLACK HAT: Caution & Risk
        black_hat = black_hat_factory.BlackHatFactory.create(model=gemini)
        
        # YELLOW HAT: Optimism & Benefits
        yellow_hat = yellow_hat_factory.YellowHatFactory.create(
            model=gemini, 
            search_model=gemini
        )
        
        # GREEN HAT: Creativity & Alternatives
        green_hat = green_hat_factory.GreenHatFactory.create(model=gemini)
        
        # BLUE HAT: The Manager/Synthesizer
        blue_hat = blue_hat_factory.BlueHatFactory.create(model=gemini)

        logger.info("All Hat sub-agents created successfully.")

    except Exception as e:
        logger.critical(f"Error creating sub-agents: {e}")
        raise e

    # --- Define Topology ---

    # Step 1: Brainstorm (Parallel)
    thinking_team = ParallelAgent(
        name="SixHatsBrainstorm",
        sub_agents=[white_hat, red_hat, black_hat, yellow_hat, green_hat]
    )

    # Step 2: Solve (Sequential)
    # The Blue Hat takes the output of the thinking_team and finalizes it
    main_agent = SequentialAgent(
        name="SixHatsSolver",
        sub_agents=[thinking_team, blue_hat]
    )
    
    logger.info("Agent assembly complete. Ready to serve.")
    return main_agent

# ==========================================
# EXPORT FOR ADK WEBUI
# ==========================================

# The WebUI expects an 'agent' object to exist in the global scope.
try:
    root_agent = build_six_hats_agent()
except Exception as e:
    logger.critical("Failed to load agent for WebUI.", exc_info=True)
    raise e