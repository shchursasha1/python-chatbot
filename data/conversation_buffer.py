class ConversationBuffer:
    def __init__(self, buffer_size=5):
        self.buffer_size = buffer_size
        self.messages = []
        self.summary = ""
        self.user_questions = []

    def add_message(self, role, message):
        self.messages.append((role, message))
        if role.lower() == "user":
            self.user_questions.append(message)
        if len(self.messages) > self.buffer_size: # TODO: remove trimming approach, do LLM summarization instead
            old = self.messages.pop(0)
            self._summarize_message(old)

    def _summarize_message(self, message_tuple):
        # Very simple summary for now; replace with LLM summarization
        role, message = message_tuple
        self.summary += f"{role}: {message[:30]}...\n"

    def get_context(self):
        context = self.summary
        for role, message in self.messages:
            context += f"{role}: {message}\n"
        return context

    def get_user_questions(self):
        return self.user_questions.copy()

    def reset(self):
        self.messages = []
        self.summary = ""
        self.user_questions = []
