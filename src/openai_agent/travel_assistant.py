from openai import OpenAI, RateLimitError
from src.config_loader.config_loader import OpenAIModelConfig

class TravelAssistant:
    def __init__(self, api_key, config: OpenAIModelConfig):
        self.client = OpenAI(api_key=api_key)
        self.system_prompt = config.system_prompt
        self.model = config.model_name
        self.temperature = config.temperature
    
    # --- Chat ---
    def chat(self, message, chat_history):
        messages = [{"role": "system", "content": self.system_prompt}]
        if chat_history:
            for human, assistant in chat_history:
                messages.append({"role": "user", "content": human})
                messages.append({"role": "assistant", "content": assistant})
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature
            )
            answer = response.choices[0].message.content
            return answer

        except RateLimitError as e:
            return "Error: OpenAI quota exceeded. Please check your plan and try again."