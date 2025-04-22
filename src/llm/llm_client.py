from src.interfaces.interfaces import LLMClientProtocol

class LLMClient(LLMClientProtocol):
    """
    LLM client facade. Delegates all LLM calls to an injected backend (Ollama, OpenAI, etc).
    """
    def __init__(self, backend: LLMClientProtocol):
        self.backend = backend

    def generate_response(self, prompt: str) -> str:
        return self.backend.generate_response(prompt)
