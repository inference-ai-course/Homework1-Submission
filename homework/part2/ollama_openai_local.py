"""
ollama_openai_local.py

Description:
    This script demonstrates how to use the OpenAI Python SDK to interact with a local Ollama server.
    It sends a chat completion request to the server and prints the response.

Usage:
    python ollama_openai_local.py

Dependencies:
    - openai

Author: Christine Zhao
Version: 1.0.0
Created: 2025-10-25
"""

from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama3.2', # required, but unused
)

response = client.chat.completions.create(
  model="llama3.2",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)