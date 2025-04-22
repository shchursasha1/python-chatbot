from src.data.summarizer import Summarizer
from src.utils.logger import Logger
from src.utils.input_sanitizer import sanitize_input
from src.utils.tokenizer import count_tokens

class ConversationBuffer:
    """Conversation buffer for managing conversation history and summaries.
    Uses token length rather than number of interactions to determine when to flush interactions.
    """

    _IGNORED_USER_MSGS = frozenset({"ok", "thanks", "hello", "hi"}) # to optimize memory usage

    def __init__(self, max_tokens=512, summarizer=None, logger=None):
        self.max_tokens = max_tokens
        self.messages = []
        self.summary = ""
        self.user_questions = []
        self.summarizer = summarizer or Summarizer()
        self.logger = logger or Logger()
        self._current_tokens = 0
        self._count_tokens = count_tokens

    def add_message(self, role, message):
        """
        Adds a new message to the conversation buffer.
        If the buffer exceeds the max token limit, oldest messages are summarized and removed.
        """
        try:
            sanitized_message = sanitize_input(message).strip().lower()

            if sanitized_message in self._IGNORED_USER_MSGS:
                return

            self.messages.append((role, sanitized_message))
            if role.lower() == "user":
                self.user_questions.append(sanitized_message)

            self._current_tokens += self._count_tokens(sanitized_message)
            self._trim_messages_by_tokens()
        except Exception as e:
            self.logger.log('ConversationBuffer', f"Error adding message: {e}")

    def _trim_messages_by_tokens(self):
        # Remove and summarize oldest messages until under max_tokens
        while self._current_tokens > self.max_tokens and self.messages:
            old = self.messages.pop(0)
            self._current_tokens -= self._count_tokens(old[1])
            self._summarize_message(old)

    def _summarize_message(self, message_tuple):
        """
        Summarizes the conversation messages using the injected Summarizer. Appends the summary to self.summary.
        """
        # Take last N messages (including the one just removed)
        last_msgs = self.messages[-(self.buffer_size - 1):] if len(self.messages) >= (self.buffer_size - 1) else self.messages[:]
        last_msgs = last_msgs + [message_tuple]

        try:
            summary = self.summarizer.summarize(last_msgs)
            self.summary += summary + "\n"
        except Exception as e:
            self.logger.log('ConversationBuffer', f"Summarization failed: {e}")

    def get_context(self):
        if self.is_empty():
            return "Conversation just started. No previous messages.\n"

        context = self.summary
        for role, message in self.messages:
            context += f"{role}: {message}\n"
        return context

    def is_empty(self):
        """Returns True if there are no user messages in the conversation."""
        return len(self.user_questions) == 0

    def get_user_questions(self):
        return self.user_questions.copy()

    def reset(self):
        self.messages = []
        self.summary = ""
        self.user_questions = []
