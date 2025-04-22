from src.interfaces.interfaces import LLMClientProtocol

class LLMClient(LLMClientProtocol):
    """
    LLM client facade. Delegates all LLM calls to an injected backend (Ollama, OpenAI, etc).
    """
    def __init__(self, backend: LLMClientProtocol):
        self.backend = backend

    def generate_response(self, messages) -> str:
        """
        Accepts a string (prompt), a dict (single message), or a list of message dicts.
        Always passes a list of dicts to the backend.
        """
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        elif isinstance(messages, dict):
            messages = [messages]

        return self.backend.generate_response(messages)
