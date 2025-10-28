# Homework 1 Submission

This homework helped me understand how to design and ochestrate ai agents using real world tools. 
This homework uses modular command pipeline style, basically chaining components together to achieve a specific workflow.

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
