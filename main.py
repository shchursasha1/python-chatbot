import time
from src.agents.sentinel import Sentinel
from src.agents.finguide import FinGuide
from src.agents.edubot import EduBot
from src.llm.llm_client import LLMClient
from src.llm.ollama import OllamaClient
from src.core.conversation_manager import ConversationManager
from src.core.agent_selector import AgentSelector
from src.ui.console_ui import ConsoleUI
from src.utils.logger import Logger


def main():
    llm_client = LLMClient(backend=OllamaClient())
    agents = {
        'sentinel': Sentinel(llm_client),
        'finguide': FinGuide(llm_client),
        'edubot': EduBot(llm_client)
    }
    agent_selector = AgentSelector(agents, llm_client)
    conversation_manager = ConversationManager(max_tokens=512)
    ui = ConsoleUI()
    logger = Logger()

    ui.display("Welcome to the Agent Chatbot! Type 'reset' to restart, or 'exit' to quit.")
    while True:
        user_input = ui.prompt()

        if user_input.strip().lower() == 'exit':
            logger.record_performance()
            logger.dump_logs()
            break

        if user_input.strip().lower() == 'reset':
            conversation_manager.reset()
            ui.display("[Conversation reset]")
            continue

        agent, switched = agent_selector.select_agent(user_input)
        if switched:
            ui.notify_agent_switch(agent.name)

        conversation_manager.add_message('User', user_input)
        context = conversation_manager.get_context()

        start_time = time.time()
        response = agent.generate_response(user_input, context)
        end_time = time.time()
        logger.record_response_time(start_time, end_time)
        
        conversation_manager.add_message(agent.name, response)
        
        ui.display(response)
        logger.log('User', user_input)
        logger.log(agent.name, response)

if __name__ == "__main__":
    main()
