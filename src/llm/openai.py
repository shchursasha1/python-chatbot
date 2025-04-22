import os
import openai
from src.interfaces.interfaces import LLMClientProtocol

class OpenAIClient(LLMClientProtocol):
    """
    LLM client for OpenAI backend. Fully interchangeable with other LLMClientProtocol implementations.
    """
    def __init__(self, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")):
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def generate_response(self, prompt: str) -> str:
        messages = [
            {'role': 'user', 'content': prompt}
        ]
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"[OpenAI error: {e}]"
