# Homework 1 Submission

This homework helped me understand how to design and ochestrate ai agents using real world tools. 
This homework uses modular command pipeline style, basically chaining components together to achieve a specific workflow.

## Homework Structure

This submission is divided into two parts, each in its own Jupyter Notebook.

| Part     | Description                                                                                                                   | File Location                                                 |
| :------- | :---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| **Part 1** | Demonstrates orchestrating various AI agent tools for tasks like web search, GitHub interaction, and file system manipulation. | [`src/main.ipynb`](./src/main.ipynb)                         |
| **Part 2** | Shows how to interact with a local Ollama instance using Python, both via an OpenAI-compatible endpoint and the native `ollama` library. | [`src/part-2-ollama.ipynb`](./src/part-2-ollama.ipynb) |

## Installation

To run this project, you will need to set up a Conda environment. Follow these steps:

1.  **Create the Conda environment:**
    ```bash
    conda create --name homework1 python=3.9
    ```

2.  **Activate the environment:**
    ```bash
    conda activate homework1
    ```

3.  **Install the required dependencies:**
    ```bash
    # This project uses Jupyter Notebook. If you don't have it installed, you can install it with:
    pip install notebook
    ```

## Tasks Overview

This project demonstrates the use of various tools orchestrated by an AI agent to perform a series of tasks. The tasks are documented in the `src/main.ipynb` Jupyter Notebook and are summarized below:

- **Task 1: Brave Search:** Uses the Brave Search tool to find the latest AI paper publication platforms.
- **Task 2: GitHub:** Connects to a GitHub account to list the 5 most recent commits from a repository.
- **Task 3: Puppeteer:** Navigates to a website and captures a full-page screenshot.
- **Task 4: File System:** Creates a folder and a file with specific content on the local filesystem.
- **Task 5: Sequential Thinking:** Generates a step-by-step plan for preparing for a technical interview.
- **Task 6: Notion:** Creates a new page in Notion to document the completed tasks.

### Advanced Task: Workflow Automation

An advanced task demonstrates a complete workflow by chaining multiple tools together:
1.  **Puppeteer:** Visits the US Visa News website.
2.  **Puppeteer:** Scrapes the textual content from the page.
3.  **File System:** Saves the scraped content locally.
4.  **Notion:** Pushes the content to a Notion page.
5.  **Summarization:** Generates a concise summary of the news and includes it in both the local file and the Notion entry.
