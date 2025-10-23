from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama 
from langchain.schema import AIMessage, HumanMessage  
import gradio as gr

def predict(message, history):
    history_langchain_format = []
    for msg in history:
        if msg['role'] == "user":
            history_langchain_format.append(HumanMessage(content=msg['content']))
        elif msg['role'] == "assistant":
            history_langchain_format.append(AIMessage(content=msg['content']))
    history_langchain_format.append(HumanMessage(content=message))

    prompt = PromptTemplate.from_template(
        message
    )

    model = ChatOllama(model = "llama2")  

    chain = (
        { message: RunnablePassthrough()}  # Accept user input
        | prompt                          # Transform it into a prompt message
        | model                           # Call the model
        | StrOutputParser()               # Parse the output as a string
    )
    gpt_response = model.invoke(history_langchain_format)
    return gpt_response.content

countryList = ["USA", "Canada", "Germany", "France", "Italy", "Spain", "China", "Japan", "India", "Australia"]

demo = gr.ChatInterface(
    predict,
    type="messages"
)

demo.launch()