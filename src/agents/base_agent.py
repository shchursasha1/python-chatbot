from config.prompts import PROMPT_TEMPLATES

class BaseAgent:
    def __init__(self, name, role_description, llm_client):
        self.name = name
        self.role_description = role_description
        self.llm_client = llm_client
        # Load prompts for this agent from config
        self.prompts = PROMPT_TEMPLATES.get(name.lower())

    def generate_response(self, prompt, conversation_context):
        """Generate a response using the LLM client. To be implemented by subclasses if needed."""
        return self.llm_client.generate_response(self._build_prompt(prompt, conversation_context))

    def _build_prompt(self, user_input, conversation_context):
        """
        Builds a prompt for the LLM using config-based system prompt and few-shot examples.
        """
        system_prompt = self.prompts['system']
        examples = self.prompts.get('examples', [])
        examples_str = "\n".join(f"User: {example['input']}\n {self.name}: {example['output']}" for example in examples)
            
        return (
            f"{system_prompt}\n"
            f"Below are example interactions that illustrate your style and expertise:\n"
            f"{examples_str}\n"
            f"If the user's question is complex, think step by step and explain your reasoning clearly before giving the answer.\n"
            f"User question: {user_input}\n"
            f"Conversation context: {conversation_context}\n"
            f"Provide a clear and short, precise, and helpful answer."
        )