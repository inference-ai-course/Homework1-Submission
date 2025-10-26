# project_guidelines.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a homework submission repository for an LLM and AI agents course. The main work is contained in a Jupyter notebook focusing on:
- Model Context Protocol (MCP) with Claude for browser automation
- Running local LLMs using Ollama
- Building LLM chains with LangChain
- Optional: Building web interfaces with Gradio

## Development Environment

### Python Environment
- Python 3.11 is used for this project
- A virtual environment is located in `./venv/`
- Activate the environment: `source venv/bin/activate`

### Installing Dependencies
There is no requirements.txt file in this repository. The main dependencies used in the notebook include:
- `openai` (for OpenAI-compatible API calls to Ollama)
- `langchain-community` and `langchain-core` (for building LLM chains)
- Standard Jupyter notebook packages (ipykernel, ipython)

If you need to install LangChain for the homework tasks:
```bash
source venv/bin/activate
pip install langchain-community langchain-core langchain-ollama
```

For Gradio (advanced task):
```bash
pip install gradio
```

### Jupyter Notebook
Run the main homework notebook:
```bash
source venv/bin/activate
jupyter notebook "Class 1 Homework.ipynb"
```

Or use VSCode/Cursor's built-in Jupyter support to open the notebook directly.

## Project Structure

- `Class 1 Homework.ipynb` - Main homework notebook with all assignment tasks
- `homework/` - Empty directory (likely for additional homework files)
- `lecture_code/` - Empty directory (likely for lecture example code)
- `lecture_slides/` - Empty directory (likely for course slides)
- `venv/` - Python virtual environment (gitignored)

## Homework Tasks Overview

### Part 1: MCP (Model Context Protocol)
Uses Claude with MCP servers for browser automation tasks including:
- Brave Search, GitHub, Puppeteer, Filesystem, Sequential Thinking, and Notion integrations
- Requires Cline extension and MCP configuration

### Part 2: Ollama Local LLMs
- Install Ollama locally: https://ollama.ai/
- Run local models: `ollama run llama3.2`
- Ollama serves an OpenAI-compatible API at `http://localhost:11434/v1/`
- Test with curl or Python's OpenAI library pointing to the local endpoint

### Part 3: LangChain + Ollama
- Use LangChain Expression Language (LCEL) to build chains
- Connect LangChain to local Ollama models
- Example pattern: `prompt | model | parser` using the pipe operator

### Advanced Task (Optional)
Build a Gradio web UI to demonstrate Ollama and LangChain integration.

## Key Architecture Notes

### Ollama as Local OpenAI Server
When using Ollama with the OpenAI Python client, the architecture is:
- Ollama runs locally on port 11434
- It exposes an OpenAI-compatible API endpoint
- Set `base_url='http://localhost:11434/v1'` in OpenAI client
- The `api_key` parameter is required but unused (can be set to 'ollama')

### LangChain LCEL Pattern
LCEL uses the pipe operator `|` to chain components:
```python
chain = (
    {"input_key": RunnablePassthrough()}
    | prompt_template
    | model
    | output_parser
)
result = chain.invoke("user input")
```

This creates a data flow pipeline where each component's output becomes the next component's input.

## Working with the Notebook

When executing code cells that call local services (Ollama), ensure:
1. Ollama is running: `ollama serve` (usually runs automatically)
2. The desired model is downloaded: `ollama pull llama3.2`
3. The venv is activated and packages are installed

When testing OpenAI-compatible endpoints with Ollama, remember the base URL is local, not the official OpenAI API.
