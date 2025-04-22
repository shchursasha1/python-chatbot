from .base_agent import BaseAgent

class EduBot(BaseAgent):
    def __init__(self, llm_client):
        super().__init__(
            name="EduBot",
            role_description="AI-Powered Tutor",
            llm_client=llm_client
        )
