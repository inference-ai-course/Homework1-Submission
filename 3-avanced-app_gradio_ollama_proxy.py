"""
Gradio + LangChain + Ollama: Proxy AI-Agent with Optional Translation
--------------------------------------------------------------------
- Chat UI on top of local Ollama via LangChain's ChatOllama.
- Optional translation pipeline (auto-detect input -> English -> back to chosen language).
- Keeps chat history in the Gradio session.

Run:
    python app_gradio_ollama_proxy.py

Requirements:
    pip install -U gradio langchain langchain-core langchain-community langchain-ollama
    # optional:
    pip install deep-translator langdetect
"""

from typing import List, Dict
import os
import gradio as gr

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Prefer the official package; fall back to community import if needed.
try:
    from langchain_ollama import ChatOllama
except ImportError:
    from langchain_community.chat_models import ChatOllama

# ---- Optional translation dependencies (fail gracefully if missing) ----
LANGDETECT_AVAILABLE = False
DEEP_TRANSLATOR_AVAILABLE = False
try:
    from langdetect import detect
    LANGDETECT_AVAILABLE = True
except Exception:
    pass

try:
    from deep_translator import GoogleTranslator
    DEEP_TRANSLATOR_AVAILABLE = True
except Exception:
    pass


def detect_lang(text: str) -> str:
    """Detect language code using langdetect if available, else fallback to 'en'."""
    if LANGDETECT_AVAILABLE:
        try:
            return detect(text)
        except Exception:
            return "en"
    return "en"


def translate(text: str, source: str, target: str) -> str:
    """Translate with deep-translator if available; otherwise return text unchanged."""
    if not text:
        return text
    if not DEEP_TRANSLATOR_AVAILABLE:
        return text
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception:
        return text


# -------------------- Chain (LCEL) --------------------
def build_chain(model_name: str, base_url: str, temperature: float):
    llm = ChatOllama(
        model=model_name,
        base_url=base_url,
        temperature=temperature,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_prompt}"),
            ("human", "{user_input}"),
        ]
    )
    chain = (
        {
            "system_prompt": RunnablePassthrough(),
            "user_input": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


# -------------------- Gradio Callbacks --------------------
def submit_message(
    user_message: str,
    chat_history: List[Dict[str, str]],   # list of {"role","content"}
    model_name: str,
    base_url: str,
    temperature: float,
    system_prompt: str,
    enable_translation: bool,
    output_lang_choice: str,
):
    """
    Handles a single user turn:
      - (optional) translate user -> English
      - run chain
      - (optional) translate model output -> chosen language
    """
    user_message = (user_message or "").strip()
    if not user_message:
        # return unchanged history, clear textbox, and keep state as-is
        return chat_history, gr.update(value=""), chat_history

    # Build chain per the current settings
    chain = build_chain(model_name=model_name, base_url=base_url, temperature=temperature)

    # Determine languages
    detected = detect_lang(user_message) if enable_translation else "en"
    input_for_llm = user_message

    # Translate INTO English for the model if enabled
    if enable_translation:
        input_for_llm = translate(user_message, source="auto", target="en")

    # Invoke the model
    try:
        model_output = chain.invoke(
            {
                "system_prompt": (system_prompt or "You are a helpful assistant.").strip(),
                "user_input": input_for_llm,
            }
        )
    except Exception as e:
        model_output = f"[Error calling model: {e}]"

    # Translate BACK to chosen output language if enabled
    final_output = model_output
    if enable_translation:
        target_lang = detected if output_lang_choice == "auto" else (output_lang_choice or detected or "en")
        final_output = translate(model_output, source="auto", target=target_lang)

    # ---- append as messages (NOT tuples) ----
    new_history = list(chat_history or [])
    new_history.append({"role": "user", "content": user_message})
    new_history.append({"role": "assistant", "content": final_output})

    # Update Chatbot, clear textbox, and persist state
    return new_history, gr.update(value=""), new_history


def clear_chat():
    # reset chatbot view, clear textbox, and reset state
    return [], "", []


# -------------------- Gradio UI --------------------
def make_ui():
    with gr.Blocks(title="Ollama Proxy Agent (LangChain + Gradio)", theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🧩 Ollama Proxy AI-Agent (LangChain + Gradio)
            - Choose an **Ollama** model and talk to it from your browser.
            - Optional **translation pipeline** (auto-detect → English → your language).
            """
        )

        with gr.Row():
            with gr.Column(scale=2):
                chat = gr.Chatbot(height=460, type="messages", label="Conversation")
                msg = gr.Textbox(placeholder="Type your message here…", lines=3)
                with gr.Row():
                    send_btn = gr.Button("Send", variant="primary")
                    clear_btn = gr.Button("Clear")

            with gr.Column(scale=1):
                gr.Markdown("### Model & Server")
                model_name = gr.Dropdown(
                    choices=["llama2", "llama3", "mistral", "phi3", "qwen2"],
                    value="llama2",
                    label="Ollama Model",
                )
                base_url = gr.Textbox(
                    value=os.environ.get("OLLAMA_HOST_HTTP", "http://127.0.0.1:11434"),
                    label="Ollama Base URL",
                )
                temperature = gr.Slider(0.0, 1.5, value=0.2, step=0.05, label="Temperature")

                gr.Markdown("### System Prompt")
                system_prompt = gr.Textbox(
                    value="You are a helpful assistant for Hotel Spa Excelsior marketing and general tasks. Be concise.",
                    lines=4,
                    label="System Prompt",
                )

                gr.Markdown("### Translation (Optional)")
                enable_translation = gr.Checkbox(
                    value=True,
                    label="Enable translation pipeline (auto-detect input → English → output language)",
                )
                output_lang_choice = gr.Dropdown(
                    label="Output language",
                    choices=["auto", "en", "fr", "de", "es", "it", "pt", "zh-cn", "zh-tw", "ja", "ko", "ar", "hi"],
                    value="auto",
                )

        # Store messages as list[dict]: [{"role": "...", "content": "..."}]
        state = gr.State([])

        # Bind events (update chat, clear textbox, and persist state)
        send_btn.click(
            submit_message,
            inputs=[msg, state, model_name, base_url, temperature, system_prompt, enable_translation, output_lang_choice],
            outputs=[chat, msg, state],
        )
        msg.submit(
            submit_message,
            inputs=[msg, state, model_name, base_url, temperature, system_prompt, enable_translation, output_lang_choice],
            outputs=[chat, msg, state],
        )
        clear_btn.click(fn=clear_chat, outputs=[chat, msg, state])

        gr.Markdown(
            """
            **Notes**
            - Make sure your Ollama server is running, and the selected model is pulled.
            - For translation features, install: `pip install deep-translator langdetect`
            - If translation packages are missing, the app still works but will not translate.
            """
        )

    return demo


if __name__ == "__main__":
    ui = make_ui()
    ui.queue().launch()
