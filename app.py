import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="5"
)

def chat(message, history):
    client.chat.completions.create(messages=history, model="llama2")
    return []

def history():
    return [
        {"role": "assistant", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The LA Dodgers won in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]


demo = gr.ChatInterface(chat, type="messages")

demo.launch()
