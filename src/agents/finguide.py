from src.agents.base_agent import BaseAgent

class FinGuide(BaseAgent):
    def __init__(self, llm_client):
        super().__init__(
            name="FinGuide",
            role_description="Financial Consultant",
            llm_client=llm_client
        )
