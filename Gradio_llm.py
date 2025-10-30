import gradio as gr
from langchain_ollama import ChatOllama  

# Initialize Llama2 model
model = ChatOllama(model="llama2:latest")

# Chat function with streaming and multi-turn support
def chat_fn(message, history):
    history = history or []  # Initialize history
    history.append({"role": "user", "content": message})

    reply_text = ""
    for chunk in model.stream(message):
        try:
            reply_text += chunk.content  # For AIMessageChunk
        except AttributeError:
            reply_text += str(chunk)     # Fallback for other types
        # Yield current conversation including partial AI reply
        yield history + [{"role": "assistant", "content": reply_text}], history

    # Append final AI response to history
    history.append({"role": "assistant", "content": reply_text})
    return history, history

# Gradio interface
with gr.Blocks() as demo:
    state = gr.State([])  # Keep full chat history
    chatbot = gr.Chatbot(type="messages", label="Llama2 Chat")
    msg_input = gr.Textbox(placeholder="请输入问题...")

    # Submit event
    msg_input.submit(chat_fn, inputs=[msg_input, state], outputs=[chatbot, state])

demo.launch()
