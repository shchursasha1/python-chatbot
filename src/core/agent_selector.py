from src.utils.input_sanitizer import sanitize_input
from src.utils.logger import Logger
from src.config.prompts import agent_selector_prompt

class AgentSelector:
    """
    Agent selector class that uses LLM to route user questions to the most appropriate specialized agent.
    """
    def __init__(self, agents, llm_client, trigger_map=None):
        self.logger = Logger()
        self.agents = agents
        self.llm_client = llm_client
        self.last_agent = None

        # Configurable map of trigger tokens to agent keys instead of hard-coded if else
        self.trigger_map = trigger_map or {
            '@sentinel': 'sentinel',
            '@finguide': 'finguide',
            '@edubot': 'edubot',
        }

    def select_agent(self, user_input):
        lowered_input = sanitize_input(user_input.lower())
        agent = None

        for trigger, key in self.trigger_map.items():
            if trigger in lowered_input:
                agent = self.agents.get(key)
                break

        if agent is None:
            # Use LLM to select the agent
            prompt = agent_selector_prompt.format(lowered_input=lowered_input)
            agent_name = self.llm_client.generate_response(prompt).strip()
            agent_name = agent_name.split()[0]
            agent_map = {
                'Sentinel': 'sentinel',
                'FinGuide': 'finguide',
                'EduBot': 'edubot'
            }
            agent_key = agent_map.get(agent_name, 'edubot')
            agent = self.agents[agent_key]
            self.logger.log('AgentSelector', f"Selected agent: {agent.name}")

        switched = agent != self.last_agent
        self.last_agent = agent
        return agent, switched
