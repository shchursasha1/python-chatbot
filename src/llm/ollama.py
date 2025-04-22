from ollama import chat, ChatResponse, ResponseError
from src.interfaces.interfaces import LLMClientProtocol
from src.config.prompts import system_prompt

class OllamaClient(LLMClientProtocol):
    """
    LLM client for Ollama backend. Fully interchangeable with other LLMClientProtocol implementations.
    """
    def __init__(self, model="gemma3"):
        self.model = model

    def generate_response(self, user_prompt: str) -> str:
        """
        Generates a response using both a system prompt (instructions/context) and a user prompt (actual question).
        """
        try:
            messages = [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}    
            ]
            response: ChatResponse = chat(model=self.model, messages=messages)
            return response['message']['content']
        except ResponseError as e:
            self.logger.log('LLMClient', f"LLM call failed: {e}")
            return f"[LLM error: {e}]"
