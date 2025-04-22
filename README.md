# Agent Chatbot

A modular, console-based AI chatbot supporting multiple specialized agents and LLM backends.

## Project Structure
```
chatbot v1/
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies (install openai or ollama depend on your choice of LLM)
├── .env.example            # Example environment variables
├── src/
│   ├── agents/              # Agent definitions (Sentinel, FinGuide, EduBot)
│   ├── core/                # Core logic (agent selector, conversation manager)
│   ├── llm/                 # LLM client wrappers (Ollama, OpenAI)
│   ├── data/                # Data handling and summarization
│   ├── interfaces/          # Interface definitions
│   ├── ui/                  # Console UI
│   ├── utils/               # Utility functions (logging, tokenizing)
│   └── config/              # Prompt and config files
```

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/shchursasha1/python-chatbot
   cd python-chatbot
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Copy `.env.example` to `.env` and fill in your OpenAI API key if using OpenAI backend.

## Usage
Run the chatbot from the project root:
```bash
python main.py
```

- Type `reset` to clear the conversation.
- Type `exit` to quit.

## Notes
- The default LLM backend is Ollama. To use OpenAI, modify the backend in `main.py` and set up your API key in .env file.
- You can add new agents by extending the `BaseAgent` class in `src/agents/base_agent.py`.

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com/) (if using Ollama backend)
- OpenAI API key (if using OpenAI backend)

## Ollama Local Setup (Optional)
If you want to use a local LLM backend with Ollama, follow these steps:

### 1. Install Ollama
- Download and install Ollama from the official site: https://ollama.com/download

### 2. Run Ollama
- Start the Ollama server (it runs in the background):
  ```bash
  ollama serve
  ```

### 3. Download a Model (Recommended: gemma3)
- Pull a small, efficient model to get started. For example, to use gemma3 model:
  ```bash
  ollama pull gemma3
  ```
- You can explore other models at https://ollama.com/library

### 4. Verify Ollama is Running
- You can check available models:
  ```bash
  ollama list
  ```
- The chatbot will now be able to connect to your local Ollama server using the pulled model.

---
*For more details, see the [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/README.md).*
