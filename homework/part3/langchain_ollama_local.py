"""
langchain_ollama_local.py

Description:
    This script demonstrates how to use LangChain's LCEL (LangChain Expression Language) to interact with a local Ollama server.
    It sets up a simple prompt-response chain using LangChain components and prints the model's answer.

Usage:
    python langchain_ollama_local.py

Dependencies:
    - langchain-community
    - langchain-core
    - langchain-ollama

Author: Christine Zhao
Version: 1.0.0
Created: 2025-10-25
"""

# Example: Using LCEL to reproduce a "Basic Prompting" scenario
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
#from langchain_community.chat_models import ChatOllama # deprecated in LangChain v0.3.1 and will be removed in v1.0.0
from langchain_ollama import ChatOllama

# 2. Define the prompt
prompt = PromptTemplate.from_template(
    "What is the capital of {topic}?"
)

# 3. Define the model
model = ChatOllama(model = "llama3.2")  # Using Ollama 

# 4. Chain the components together using LCEL
chain = (
    # LCEL syntax: use the pipe operator | to connect each step
    {"topic": RunnablePassthrough()}  # Accept user input
    | prompt                          # Transform it into a prompt message
    | model                           # Call the model
    | StrOutputParser()               # Parse the output as a string
)

# 5. Execute
result = chain.invoke("Germany")
print("User prompt: 'What is the capital of Germany?'")
print("Model answer:", result)
