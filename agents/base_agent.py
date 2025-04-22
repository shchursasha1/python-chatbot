class BaseAgent:
    def __init__(self, name, role_description, llm_client):
        self.name = name
        self.role_description = role_description
        self.llm_client = llm_client

    def generate_response(self, prompt, conversation_context):
        """Generate a response using the LLM client. To be implemented by subclasses if needed."""
        return self.llm_client.generate_response(self._build_prompt(prompt, conversation_context))

    def _build_prompt(self, user_input, conversation_context):
        """
        Builds a prompt for the LLM that enforces the agent's identity and role, using few-shot examples and chain-of-thought reasoning.
        """
        # Few-shot examples for each agent
        examples = {
            "Sentinel": (
                "User: How do I protect my online accounts?\n"
                "Sentinel: To protect your online accounts, use strong, unique passwords, enable two-factor authentication, and avoid clicking suspicious links."
                "\nUser: Should I trust public Wi-Fi?\n"
                "Sentinel: Public Wi-Fi can be risky. Avoid accessing sensitive information on it, and use a VPN for added security."
            ),
            "FinGuide": (
                "User: How can I start saving money?\n"
                "FinGuide: Begin by tracking your expenses, setting a monthly budget, and automating transfers to a savings account."
                "\nUser: What is a mutual fund?\n"
                "FinGuide: A mutual fund is a pooled investment vehicle managed by professionals, allowing you to invest in a diversified portfolio."
            ),
            "EduBot": (
                "User: What is machine learning?\n"
                "EduBot: Machine learning is a branch of AI where computers learn from data to make predictions or decisions without being explicitly programmed."
                "\nUser: Can you explain photosynthesis simply?\n"
                "EduBot: Photosynthesis is how plants convert sunlight, water, and carbon dioxide into food and oxygen."
            ),
        }
        agent_examples = examples.get(self.name, "")
        return (
            f"You are {self.name}, a {self.role_description}. Remain strictly in this role—never refer to yourself as any other agent or prefix answers with your name.\n"
            f"Below are example interactions that illustrate your style and expertise:\n"
            f"{agent_examples}\n"
            f"If the user's question is complex, think step by step and explain your reasoning clearly before giving the answer.\n"
            f"User question: {user_input}\n"
            f"Conversation context: {conversation_context}\n"
            f"Provide a clear and short, precise, and helpful answer."
        )
