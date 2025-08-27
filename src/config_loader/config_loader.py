import json
from pydantic import BaseModel, Field
from typing import Optional

class OpenAIModelConfig(BaseModel):
    system_prompt: str = Field(..., description="System prompt for the travel assistant")
    model_name: str = Field(..., description="OpenAI model name")
    temperature: Optional[float] = Field(default=0.6, description="Temperature for response generation")

class Config(BaseModel):
    destinations_filename: str = Field(..., description="Excel file containing destinations details")
    openAI_model_config: OpenAIModelConfig

def config_loader(config_path: str) -> Config:
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return Config(**data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find config file: {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in config file: {config_path}")