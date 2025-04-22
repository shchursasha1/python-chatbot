from src.utils.input_sanitizer import sanitize_input
from src.config.prompts import agent_selector_prompt

class AgentSelector:
    """
    Agent selector class that uses LLM to route user questions to the most appropriate specialized agent.
    """
    def __init__(self, agents, llm_client):
        self.agents = agents
        self.llm_client = llm_client
        self.last_agent = None

    def select_agent(self, user_input):
        lowered_input = sanitize_input(user_input.lower())

        if "@sentinel" in lowered_input:
            agent = self.agents['sentinel']
        elif "@finguide" in lowered_input:
            agent = self.agents['finguide']
        elif "@edubot" in lowered_input:
            agent = self.agents['edubot']
        else:
            prompt = agent_selector_prompt.format(lowered_input=lowered_input)
            agent_name = self.llm_client.generate_response(prompt).strip()
            agent_key = agent_name.lower()

            if agent_key == 'sentinel':
                agent = self.agents['sentinel']
            elif agent_key == 'finguide':
                agent = self.agents['finguide']
            elif agent_key == 'edubot':
                agent = self.agents['edubot']
            else:
                agent = self.last_agent or self.agents['edubot']
        switched = agent != self.last_agent
        self.last_agent = agent
        return agent, switched