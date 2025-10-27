from openai import OpenAI
import gradio as gr

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key=""
)

def chat(message, info):
    client.chat.completions.create(messages=info, model="llama2")
    return []

def info():
    return [
        {"role": "assistant", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The LA Dodgers won in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

demo = gr.ChatInterface(chat, type="messages")

demo.launch()