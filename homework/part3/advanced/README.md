# AI Proxy Agent with Gradio Web Interface

This project demonstrates a **Proxy Pattern** architecture for building AI agent interfaces that can seamlessly switch between different backend implementations while maintaining a consistent frontend experience.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│         Frontend (Gradio UI)            │
│  - Chat Interface                       │
│  - Model Selection                      │
│  - Backend Strategy Selection           │
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│         Proxy Agent Layer               │
│  - Routes requests to backends          │
│  - Abstracts implementation details     │
│  - Strategy pattern implementation      │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌─────────────────┐
│   OpenAI-    │  │   LangChain     │
│  Compatible  │  │   LCEL          │
│   Strategy   │  │   Strategy      │
└──────┬───────┘  └────────┬────────┘
       │                   │
       └─────────┬─────────┘
                 ↓
        ┌────────────────┐
        │  Ollama Server │
        │  (localhost)   │
        └────────────────┘
```

## Key Design Patterns

### 1. Proxy Pattern
The `AIProxyAgent` class acts as a proxy between the frontend and various backend implementations. The frontend doesn't need to know which backend is being used - it just calls the proxy, which routes the request appropriately.

**Benefits:**
- **Flexibility**: Easy to add new backends without changing frontend code
- **Abstraction**: Frontend is decoupled from backend implementation details
- **Consistency**: Uniform interface regardless of backend

### 2. Strategy Pattern
Each backend (OpenAI-Compatible, LangChain) is implemented as a strategy that inherits from `AIBackendStrategy`. This allows runtime switching between different implementations.

**Benefits:**
- **Extensibility**: Add new strategies by implementing the interface
- **Maintainability**: Each strategy is independently testable
- **Runtime Selection**: Switch backends on the fly without restart

## Features

### Backend Strategies

#### 1. OpenAI-Compatible Strategy
- **Direct API calls** to Ollama's OpenAI-compatible endpoint
- Uses the official OpenAI Python client
- Endpoint: `http://localhost:11434/v1`
- Minimal overhead, fast responses

#### 2. LangChain LCEL Strategy
- Uses **LangChain Expression Language** (LCEL)
- Demonstrates the power of chain composition
- Pattern: `prompt | model | parser`
- Supports advanced features like chat history and custom prompts

### Frontend Features

- **Chat Interface**: Clean, intuitive chat UI with message history
- **Model Selection**: Choose from available Ollama models
- **Strategy Switching**: Toggle between backends in real-time
- **Custom System Prompts**: Modify AI behavior on the fly
- **Example Prompts**: Quick-start examples for testing

## Installation & Setup

### Prerequisites

1. **Python 3.11+** with virtual environment
2. **Ollama** installed and running locally

### Step 1: Install Ollama

```bash
# Download from https://ollama.ai
# Or use homebrew on macOS
brew install ollama
```

### Step 2: Pull a Model

```bash
ollama pull llama3.2
# or
ollama pull qwen2
# or
ollama pull mistral
```

### Step 3: Ensure Ollama is Running

```bash
# Ollama usually starts automatically, but you can check with:
ollama list

# Or explicitly start the server:
ollama serve
```

### Step 4: Install Python Dependencies

```bash
# From the repository root
source venv/bin/activate

# If not already installed:
pip install gradio langchain-community langchain-core langchain-ollama openai
```

## Usage

### Running the Web Interface

```bash
# Navigate to the advanced directory
cd homework/part3/advanced

# Activate virtual environment
source ../../../venv/bin/activate

# Launch the Gradio app
python gradio_ai_proxy.py
```

The interface will be available at: **http://127.0.0.1:7860**

### Running the Test Suite

```bash
# Test both backend strategies
python test_proxy.py
```

## How It Works

### 1. Frontend Layer (Gradio)
```python
# User sends a message through Gradio UI
def chat_interface(message, history, system_prompt, model, backend):
    proxy_agent.set_strategy(backend)  # Select strategy
    response = proxy_agent.chat(...)   # Call proxy
    return response
```

### 2. Proxy Layer
```python
class AIProxyAgent:
    def chat(self, message, history, system_prompt, model):
        # Route to current strategy
        strategy = self.strategies[self.current_strategy]
        return strategy.generate_response(...)
```

### 3. Backend Strategies

#### OpenAI-Compatible
```python
class OpenAICompatibleStrategy:
    def generate_response(self, message, ...):
        client = OpenAI(base_url='http://localhost:11434/v1')
        response = client.chat.completions.create(...)
        return response.choices[0].message.content
```

#### LangChain LCEL
```python
class LangChainStrategy:
    def generate_response(self, message, ...):
        # Build LCEL chain
        chain = prompt | model | parser
        response = chain.invoke({...})
        return response
```

## Configuration

### Available Models
Edit `AVAILABLE_MODELS` in `gradio_ai_proxy.py`:
```python
AVAILABLE_MODELS = [
    "llama3.2",
    "mistral",
    "phi",
    "gemma",
    "qwen2.5",
]
```

### Default System Prompt
Modify `DEFAULT_SYSTEM_PROMPT`:
```python
DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant..."
```

### Server Configuration
Change port or host in the launch configuration:
```python
demo.launch(
    server_name="127.0.0.1",
    server_port=7860,
    share=False  # Set to True for public URL
)
```

## Extending the Application

### Adding a New Backend Strategy

1. Create a new strategy class:
```python
class MyCustomStrategy(AIBackendStrategy):
    def generate_response(self, message, history, system_prompt, model):
        # Your implementation
        return response

    def get_name(self):
        return "My Custom Strategy"
```

2. Register it in the proxy:
```python
def __init__(self):
    self.strategies = {
        "openai": OpenAICompatibleStrategy(),
        "langchain": LangChainStrategy(),
        "custom": MyCustomStrategy()  # Add here
    }
```

3. Update the Gradio interface:
```python
backend = gr.Radio(
    choices=["openai", "langchain", "custom"],
    # ...
)
```

## Troubleshooting

### "Error: Connection refused"
- Ensure Ollama is running: `ollama serve`
- Check if port 11434 is open: `curl http://localhost:11434/api/tags`

### "Model not found"
- Pull the model: `ollama pull llama3.2`
- List available models: `ollama list`

### "LangChain deprecation warning"
- This is just a warning, the app still works
- To silence it, upgrade: `pip install -U langchain-ollama`
- Update imports: `from langchain_ollama import ChatOllama`

## File Structure

```
advanced/
├── gradio_ai_proxy.py    # Main application
├── test_proxy.py         # Test suite
└── README.md            # This file
```

## Technical Details

### Why Proxy Pattern?

The proxy pattern is ideal for this use case because:

1. **Interface Translation**: The frontend speaks "Gradio", backends speak different APIs (OpenAI, LangChain)
2. **Lazy Loading**: Strategies are only initialized when first used
3. **Caching**: LangChain strategy caches chains for better performance
4. **Access Control**: Could add authentication, rate limiting, etc. at proxy level

### Performance Considerations

- **OpenAI-Compatible**: Lower latency, direct HTTP calls
- **LangChain**: Slightly higher overhead but more features (memory, tools, etc.)
- **Chain Caching**: LangChain chains are cached per model/prompt combination

### Scalability

To scale this application:
1. Add connection pooling for Ollama API calls
2. Implement request queuing for high traffic
3. Add caching layer (Redis) for common queries
4. Deploy with Gunicorn/Uvicorn for production

## Learning Outcomes

This project demonstrates:
- ✅ **Proxy Pattern**: Abstracting backend implementations
- ✅ **Strategy Pattern**: Runtime algorithm selection
- ✅ **Ollama Integration**: Using local LLMs with OpenAI-compatible API
- ✅ **LangChain LCEL**: Building composable AI chains
- ✅ **Gradio**: Creating interactive ML interfaces
- ✅ **Clean Architecture**: Separation of concerns (UI, Logic, Data)

## License

This project is part of a homework assignment for an LLM and AI Agents course.

## References

- [Ollama Documentation](https://ollama.ai)
- [LangChain LCEL](https://python.langchain.com/docs/expression_language/)
- [Gradio Documentation](https://gradio.app/docs/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Design Patterns: Proxy](https://refactoring.guru/design-patterns/proxy)