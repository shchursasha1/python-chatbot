from src.data.conversation_buffer import ConversationBuffer

class ConversationManager:
    """
    Conversation manager class that handles the conversation buffer and manages the conversation flow.
    """
    def __init__(self, max_tokens=512):
        self.buffer = ConversationBuffer(max_tokens=max_tokens)

    def add_message(self, role, message):
        self.buffer.add_message(role, message)

    def get_context(self):
        return self.buffer.get_context()

    def get_user_questions(self):
        return self.buffer.get_user_questions()

    def reset(self):
        self.buffer.reset()
