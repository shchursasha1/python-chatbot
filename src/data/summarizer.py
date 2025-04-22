from src.interfaces.logger import Logger
from src.config.prompts import summarizer_prompt

class Summarizer:
    """Class for summarizing conversation history."""
    def __init__(self, llm_client=None, logger=None):
        self.llm_client = llm_client
        self.logger = logger or Logger()

    def summarize(self, messages):
        chat_text = "\n".join(f"{role}: {msg}" for role, msg in messages)
        prompt = summarizer_prompt.format(chat_text)
        
        try:
            summary = self.llm_client.generate_response(prompt)
            return summary.strip()
        except Exception as e:
            self.logger.log('Summarizer', f"LLM summarization failed: {e}")
            return f"[Summary unavailable: {e}]"