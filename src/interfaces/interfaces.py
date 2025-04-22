from abc import ABC, abstractmethod

# Interface classes which give opportunity to change implementation of components without changing core code

class LLMClientProtocol(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

class SummarizerProtocol(ABC):
    @abstractmethod
    def summarize(self, conversation: list) -> str:
        pass

class LoggerProtocol(ABC):
    @abstractmethod
    def log(self, role: str, message: str):
        pass
