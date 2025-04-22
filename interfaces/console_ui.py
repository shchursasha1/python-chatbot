class ConsoleUI:
    def display(self, message):
        print(message)

    def prompt(self):
        return input("User: ")

    def notify_agent_switch(self, agent_name):
        print(f"[Agent switched to {agent_name}]")
