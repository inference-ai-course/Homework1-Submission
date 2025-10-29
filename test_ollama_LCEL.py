import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama  # New import

# 1. Define the prompt
prompt = PromptTemplate.from_template(
    "What is the capital of {topic}?"
)

# 2. Define the model (model parameter must be a string)
model = ChatOllama(model="llama2")  # Using Ollama

# 3. Chain components using LCEL
chain = (
    {"topic": RunnablePassthrough()}  # Accept user input
    | prompt                          # Convert into a model-readable prompt
    | model                           # Call the model
    | StrOutputParser()               # Parse output as a string
)

# 4. Execute
result = chain.invoke("Germany")
print("User prompt: 'What is the capital of Germany?'")
print("Model answer:", result)
