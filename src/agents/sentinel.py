from src.agents.base_agent import BaseAgent

class Sentinel(BaseAgent):
    def __init__(self, llm_client):
        super().__init__(
            name="Sentinel",
            role_description="Cybersecurity Advisor",
            llm_client=llm_client
        )
