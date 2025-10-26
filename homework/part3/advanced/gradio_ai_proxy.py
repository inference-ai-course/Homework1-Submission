"""
gradio_ai_proxy.py

Description:
Gradio AI Proxy Agent Interface
================================
This application demonstrates a proxy pattern for AI agent interfaces,
where the frontend (Gradio) communicates through a proxy layer that can
route requests to different AI backends (Ollama via OpenAI API or LangChain).

Architecture:
    Frontend (Gradio UI)
        ↓
    Proxy Agent Layer
        ↓
    Backend Strategies:
        - OpenAI-Compatible Strategy (Direct Ollama API)
        - LangChain Strategy (LCEL chains)

Usage:
    python gradio_ai_proxy.py

Dependencies:
    - gradio
    - openai
    - langchain-core
    - langchain-ollama

Author: Christine Zhao
Version: 1.0.0
Created: 2025-10-25
"""


import gradio as gr
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import time


# ============================================================================
# Backend Strategy Pattern (Proxy Layer)
# ============================================================================

class AIBackendStrategy(ABC):
    """Abstract base class for AI backend strategies"""

    @abstractmethod
    def generate_response(self, message: str, history: List[Dict[str, str]],
                         system_prompt: str, model: str) -> str:
        """Generate a response using the specific backend"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Return the name of this strategy"""
        pass


class OpenAICompatibleStrategy(AIBackendStrategy):
    """Strategy using Ollama's OpenAI-compatible API directly"""

    def __init__(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'  # required but unused
        )

    def generate_response(self, message: str, history: List[Dict[str, str]],
                         system_prompt: str, model: str) -> str:
        """Generate response using OpenAI-compatible API"""
        # Build message list starting with system prompt
        messages = [{"role": "system", "content": system_prompt}]

        # Add history messages (already in the correct format)
        messages.extend(history)

        # Add current user message
        messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error with OpenAI-compatible API: {str(e)}\n\nMake sure Ollama is running and the model '{model}' is available."

    def get_name(self) -> str:
        return "OpenAI-Compatible (Direct Ollama API)"


class LangChainStrategy(AIBackendStrategy):
    """Strategy using LangChain LCEL"""

    def __init__(self):
        self.chains = {}  # Cache chains by model

    def _get_chain(self, model: str, system_prompt: str):
        """Get or create a chain for the given model"""
        cache_key = f"{model}_{hash(system_prompt)}"

        if cache_key not in self.chains:
            # Create prompt template with system message and chat history
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="history", optional=True),
                ("human", "{input}")
            ])

            # Create model
            llm = ChatOllama(model=model, temperature=0.7)

            # Build LCEL chain
            chain = prompt | llm | StrOutputParser()

            self.chains[cache_key] = chain

        return self.chains[cache_key]

    def generate_response(self, message: str, history: List[Dict[str, str]],
                         system_prompt: str, model: str) -> str:
        """Generate response using LangChain LCEL"""
        try:
            chain = self._get_chain(model, system_prompt)

            # Convert history from messages format to LangChain format
            lc_history = []
            for msg in history:
                if msg["role"] == "user":
                    lc_history.append(("human", msg["content"]))
                elif msg["role"] == "assistant":
                    lc_history.append(("ai", msg["content"]))

            # Invoke the chain
            response = chain.invoke({
                "input": message,
                "history": lc_history
            })

            return response
        except Exception as e:
            return f"Error with LangChain: {str(e)}\n\nMake sure Ollama is running and the model '{model}' is available."

    def get_name(self) -> str:
        return "LangChain LCEL"


# ============================================================================
# AI Proxy Agent
# ============================================================================

class AIProxyAgent:
    """
    Proxy agent that routes requests to different AI backends.
    This demonstrates the Proxy pattern where the client (Gradio UI) doesn't
    need to know about the specific implementation details of each backend.
    """

    def __init__(self):
        self.strategies = {
            "openai": OpenAICompatibleStrategy(),
            "langchain": LangChainStrategy()
        }
        self.current_strategy = "openai"

    def set_strategy(self, strategy_name: str):
        """Switch the backend strategy"""
        if strategy_name in self.strategies:
            self.current_strategy = strategy_name
        else:
            raise ValueError(f"Unknown strategy: {strategy_name}")

    def chat(self, message: str, history: List[Dict[str, str]],
             system_prompt: str, model: str) -> str:
        """
        Main chat interface - routes the request to the current strategy.
        This is the proxy method that the frontend calls.
        """
        strategy = self.strategies[self.current_strategy]
        return strategy.generate_response(message, history, system_prompt, model)

    def get_current_strategy_name(self) -> str:
        """Get the name of the current strategy"""
        return self.strategies[self.current_strategy].get_name()


# ============================================================================
# Gradio Interface
# ============================================================================

# Initialize the proxy agent
proxy_agent = AIProxyAgent()

# Available Ollama models
AVAILABLE_MODELS = [
    "llama3.2",
    "mistral",
    "phi",
    "gemma",
    "qwen2",
]

# Default system prompt
DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant. Provide clear, concise, and accurate responses."


def chat_interface(message: str, history: List[Dict[str, str]],
                  system_prompt: str, model: str, backend: str) -> tuple[str, List[Dict[str, str]]]:
    """
    Main chat function that interfaces with the proxy agent.
    This is called by Gradio when the user sends a message.
    """
    if not message.strip():
        return "", history

    # Set the backend strategy
    proxy_agent.set_strategy(backend)

    # Get response from proxy agent
    response = proxy_agent.chat(message, history, system_prompt, model)

    # Update history with new messages in the messages format
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})

    return "", history


def create_gradio_interface():
    """Create and configure the Gradio interface"""

    with gr.Blocks(title="AI Proxy Agent Interface", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # AI Proxy Agent Interface

        This interface demonstrates a **Proxy Pattern** architecture where:
        - The **Frontend** (Gradio UI) provides the user interface
        - The **Proxy Agent** routes requests to different AI backends
        - The **Backend Strategies** handle the actual AI model calls

        You can switch between two backend strategies:
        1. **OpenAI-Compatible**: Direct calls to Ollama's OpenAI-compatible API
        2. **LangChain LCEL**: Uses LangChain Expression Language chains

        Both backends connect to your local Ollama models!
        """)

        with gr.Row():
            with gr.Column(scale=3):
                # Chat interface
                chatbot = gr.Chatbot(
                    label="Chat History",
                    height=500,
                    show_copy_button=True,
                    type='messages'
                )

                msg = gr.Textbox(
                    label="Your Message",
                    placeholder="Type your message here...",
                    lines=2
                )

                with gr.Row():
                    submit_btn = gr.Button("Send", variant="primary")
                    clear_btn = gr.Button("Clear Chat")

            with gr.Column(scale=1):
                gr.Markdown("### Configuration")

                backend = gr.Radio(
                    choices=["openai", "langchain"],
                    value="openai",
                    label="Backend Strategy",
                    info="Choose which backend to use"
                )

                model = gr.Dropdown(
                    choices=AVAILABLE_MODELS,
                    value="llama3.2",
                    label="Model",
                    info="Select Ollama model",
                    allow_custom_value=True
                )

                system_prompt = gr.Textbox(
                    label="System Prompt",
                    value=DEFAULT_SYSTEM_PROMPT,
                    lines=4,
                    info="Customize the AI's behavior"
                )

                gr.Markdown("""
                ### Backend Info

                **OpenAI-Compatible**:
                - Direct API calls to Ollama
                - URL: http://localhost:11434/v1
                - Uses OpenAI Python client

                **LangChain LCEL**:
                - Uses LangChain chains
                - LCEL pipe operator syntax
                - Pattern: prompt | model | parser

                ### Prerequisites

                Make sure Ollama is running:
                ```bash
                ollama serve
                ```

                Pull a model if needed:
                ```bash
                ollama pull llama3.2
                ```
                """)

        # Event handlers
        submit_btn.click(
            fn=chat_interface,
            inputs=[msg, chatbot, system_prompt, model, backend],
            outputs=[msg, chatbot]
        )

        msg.submit(
            fn=chat_interface,
            inputs=[msg, chatbot, system_prompt, model, backend],
            outputs=[msg, chatbot]
        )

        clear_btn.click(
            fn=lambda: ([], ""),
            outputs=[chatbot, msg]
        )

        # Add examples
        gr.Examples(
            examples=[
                ["What is the capital of France?"],
                ["Explain quantum computing in simple terms"],
                ["Write a Python function to calculate factorial"],
                ["What are the main differences between Python and JavaScript?"],
                ["Tell me a short story about a robot learning to paint"]
            ],
            inputs=msg,
            label="Example Prompts"
        )

    return demo


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("AI Proxy Agent Interface")
    print("=" * 70)
    print("\nStarting Gradio interface...")
    print("\nMake sure Ollama is running:")
    print("  $ ollama serve")
    print("\nAvailable models:", ", ".join(AVAILABLE_MODELS))
    print("\nThe interface demonstrates a proxy pattern architecture:")
    print("  Frontend → Proxy Agent → Backend Strategies (OpenAI/LangChain)")
    print("=" * 70)

    demo = create_gradio_interface()
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True
    )
