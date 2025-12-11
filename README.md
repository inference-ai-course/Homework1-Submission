README — Week 1 Homework Submission

MLE in GenAI – Week 1: Local LLMs, Ollama, LangChain, and LCEL
Author: Wei Yang
File: Wei_Yang_submission_week1.ipynb

🔍 Overview

This Week 1 homework demonstrates the setup and use of a local LLM development environment using:

Ollama (local LLM runtime)

llama3 model

LangChain

LCEL (LangChain Expression Language)

OpenAI-compatible API interface

The goal of this assignment is to verify that a complete local LLM pipeline is installed correctly and running without relying on cloud APIs.

🧩 Homework Objectives

The notebook implements the Week 1 requirements:

✔️ 1. Install & Configure Ollama

Installed Ollama on the local machine

Pulled and used the llama3 model

Confirmed the local server is running

✔️ 2. Test OpenAI-compatible Local Endpoint

Demonstrated access to the local model via:

from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

✔️ 3. LangChain & LCEL Integration

Connected the local LLM to LangChain

Demonstrated:

Simple prompt→response pipeline

LCEL chain with declarative composition

Prompt Templates

Model → OutputParser workflows

✔️ 4. End-to-End Notebook Documentation

The notebook includes explanations, code blocks, and output verifying:

LLM responses

Pipeline execution via LCEL

Proper environment setup

📂 Contents of the Notebook
Section	Description
Environment Setup	Python setup, OpenAI client config, Ollama test
Local LLM via OpenAI Interface	Model call using local endpoint
LangChain Integration	PromptTemplates, Chains, LCEL expressions
Testing llama3	Interactive tests to verify functionality
Summary	What was learned and validated
🛠️ How to Run This Notebook
1. Install Ollama

https://ollama.com/download

2. Pull the llama3 model
ollama pull llama3

3. Start Ollama (if not already running)
ollama serve

4. Install Python Dependencies

Your environment needs:

pip install openai langchain langchain-community python-dotenv


(or use your course environment)

5. Open Jupyter and run the notebook
jupyter notebook

✅ Results

Running the notebook successfully demonstrates:

A functioning local LLM development pipeline

Ability to issue prompts via OpenAI-compatible API

Ability to execute LangChain LCEL pipelines

Proper integration of prompt templating + model inference

This verifies that Week 1 tooling is installed and functional, enabling future assignments involving OCR, RAG systems, embeddings, and hybrid search.