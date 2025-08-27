import gradio as gr
import os
from dotenv import load_dotenv, find_dotenv

from src.utils.logger_config import logger
from src.config_loader.config_loader import config_loader
from src.openai_agent.travel_assistant import TravelAssistant

# Set up logging
with open("logs/app.log", "w") as log_file:
    pass
logger.info("Logging setup complete")

# Load API keys from .env file
load_dotenv(find_dotenv(), override=True)
api_key = os.getenv("OPENAI_API_KEY")
logger.info("API key loaded")

# Load configuration file
config_path="config/config.json"
config = config_loader(config_path=config_path)
logger.info(f"Configuration loaded from: {config_path}")

# Initialize OpenAI Agent
travel_assistant = TravelAssistant(api_key=api_key, config=config.openAI_model_config)
logger.info(f"Travel Agent initialized")

# Gradio Interface
gr.ChatInterface(fn=travel_assistant.chat).launch()

