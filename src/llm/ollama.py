from ollama import chat, ChatResponse, ResponseError
from src.interfaces.interfaces import LLMClientProtocol
from src.config.prompts import system_prompt

class OllamaClient(LLMClientProtocol):
    """
    LLM client for Ollama backend. Fully interchangeable with other LLMClientProtocol implementations.
    """
    def __init__(self, model="gemma3"):
        self.model = model

    def generate_response(self, messages) -> str:
        """
        Generates a response using a list of messages (system, few-shot, context, user) in OpenAI/Ollama format.
        """
        try:
            response: ChatResponse = chat(model=self.model, messages=messages)
            return response['message']['content']
        except ResponseError as e:
            self.logger.log('LLMClient', f"LLM call failed: {e}")
            return f"[LLM error: {e}]"
