from typing import Iterable
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

def get_completion(messages: Iterable[ChatCompletionMessageParam], model: str = "llama3"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Who won the world series in 2020?"},
  {"role": "assistant", "content": "The LA Dodgers won in 2020."},
  {"role": "user", "content": "Where was it played?"}
]

response = get_completion(messages)
print(response)

