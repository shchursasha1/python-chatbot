from data.conversation_buffer import ConversationBuffer

class ConversationManager:
    def __init__(self, buffer_size=5):
        self.buffer = ConversationBuffer(buffer_size=buffer_size)

    def add_message(self, role, message):
        self.buffer.add_message(role, message)

    def get_context(self):
        return self.buffer.get_context()

    def get_user_questions(self):
        return self.buffer.get_user_questions()

    def reset(self):
        self.buffer.reset()
