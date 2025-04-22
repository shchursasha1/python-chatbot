from ollama import chat, ChatResponse

class LLMClient:
    """LLM client for generating responses using OpenAI API."""
    def __init__(self, model="gemma3"):
        self.model = model

    def generate_response(self, prompt: str) -> str:
        try:
            response: ChatResponse = chat(model=self.model, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ])
            return response['message']['content']
        except Exception as e:
            return f"Raised exception: {e}"
