# Week 1: Introduction to Large Language Models & Prompt Engineering

**Course:** Machine Learning Engineer in the Generative AI Era  
**Week:** 1 of 10  
**Date:** July 21, 2025  
**Topic:** Introduction to LLMs & Prompt Engineering

---

## 📚 Overview

This homework assignment introduces you to Large Language Models (LLMs) and prompt engineering fundamentals. You will learn to interact with LLMs programmatically, master the CO-STAR prompt engineering framework, and begin building your course capstone project: a personalized research agent.

By the end of this assignment, you will have hands-on experience with:
- Making API calls to LLMs using Python
- Structuring effective prompts using the CO-STAR framework
- Generating and parsing structured outputs (JSON/XML)
- Implementing chain-of-thought reasoning
- Understanding model limitations and tradeoffs
- Prototyping your first AI agent

---

## 🎯 Learning Objectives

Upon completion of this assignment, students will be able to:

1. Configure and authenticate with LLM APIs (cloud or local)
2. Construct effective prompts using the CO-STAR framework
3. Generate structured outputs from natural language inputs
4. Implement chain-of-thought prompting techniques
5. Evaluate and document model limitations
6. Design and prototype a basic AI research agent
7. Compare tradeoffs between different LLM deployment options

---

## 🛠️ Setup Options

This assignment supports three deployment paths to accommodate different learning styles, budgets, and technical constraints:

### Path A: Claude API (Cloud)
**Recommended for:** Students prioritizing result quality and course alignment

- **Requirements:** Anthropic API key, internet connection
- **Cost:** ~$0.50-2.00 for this assignment
- **Advantages:** State-of-the-art performance, no local hardware requirements
- **Model:** Claude 3.5 Sonnet or Claude 3.5 Haiku

### Path B: Ollama (Local)
**Recommended for:** Budget-conscious students and those learning deployment

- **Requirements:** 8GB+ RAM, 10-20GB disk space
- **Cost:** $0 (free)
- **Advantages:** Unlimited experimentation, offline capability, privacy
- **Recommended Models:**
  - `llama3.2:3b` - Lightweight, fast
  - `llama3.1:8b` - Better quality
  - `mistral:7b` - Good balance
  - `qwen2.5:7b` - Strong reasoning

### Path C: Hybrid
**Recommended for:** Most students

- Use Ollama for experimentation and iteration
- Use Claude API for final deliverables
- Combines cost efficiency with quality output

---

## 📋 Prerequisites

### Required for All Paths
- Python 3.8 or higher
- VS Code, Cursor IDE, or any IDE with Jupyter notebook support
- Basic Python proficiency (functions, dictionaries, string manipulation)
- 2-3 hours of focused work time

### Path A (Claude API)
- Anthropic API account: https://console.anthropic.com
- Valid API key with available credits
- Stable internet connection

### Path B (Ollama)
- Minimum 8GB RAM (16GB recommended)
- 10-20GB free disk space
- Ollama installed: https://ollama.ai
- Verification commands:
  ```bash
  ollama pull llama3.2:3b
  ollama run llama3.2:3b "Hello, world!"
  ```

### Optional Tools
- **Cursor IDE** (https://cursor.sh) - AI-powered code editor (recommended)
- **Claude Code CLI** - Command-line agentic coding tool
- **Git** for version control
- **Discord** for course community

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
# Clone the course repository
git clone https://github.com/inference-ai-course/Homework1-Submission.git
cd Homework1-Submission
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
   # On macOS/Linux:
   source .venv/bin/activate

   # On Windows:
   venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```
The `requirements.txt` should be set up already, but modify the optional section if needed, and feel free to use OpenAI API if you want. 

### Step 4: Configure API Keys (Path A or C)

```bash
# Copy the example environment file
cp .env.example .env
# Edit .env with your API key
```

⚠️ **Security Note:** The `.env` file is included in `.gitignore` and will never be committed to version control.

### Step 5: Verify Ollama Installation (Path B or C)

```bash
# Check Ollama is installed
ollama --version

# Pull recommended model
ollama pull llama3.2:3b

# Test the model
ollama run llama3.2:3b "Hello, test!"
```

### Step 6: Open the Notebook in Your IDE

#### Option A: VS Code
```bash
# Install Python extension if not already installed
# Open VS Code
code .

# Open homework1.ipynb
# VS Code will prompt to select a kernel - choose your venv
```

#### Option B: Cursor IDE (Recommended)
```bash
# Open Cursor
cursor .

# Open homework1.ipynb
# Select kernel: Python Environments → venv
```


---

## 📁 Repository Structure

```
Homework1-submission/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── notebooks/
│   ├── 00_setup_verification.ipynb       # Quick check everything works
│   ├── 01_environment_setup.ipynb        # Section 1
│   ├── 02_llm_basics.ipynb               # Section 2
│   ├── 03_costar_framework.ipynb         # Section 3
│   ├── 04_structured_outputs.ipynb       # Section 4
│   ├── 05_chain_of_thought.ipynb         # Section 5
│   ├── 06_model_comparison.ipynb         # Section 6
│   ├── 07_mcp_introduction.ipynb         # Section 7
│   └── 08_project_kickoff.ipynb          # Section 8
│
├── src/                                   # Shared utilities
│   ├── __init__.py
│   ├── llm_client.py                     # LLMClient class
│   ├── cost_tracker.py                   # CostTracker class
│   ├── prompt_templates.py               # CO-STAR templates
│   └── utils.py                          # Helper functions
│
├── outputs/                               # Student deliverables
│   ├── project_proposal.md
│   ├── limitations_log.md
│   └── resource_analysis.md
│
└── docs/
    ├── path_a_setup.md
    ├── path_b_setup.md
    └── quick_start_guide.md
```

---

## 📓 Assignment Structure

The homework is organized into 8 sections within the pre-configured Jupyter notebook (`homework1.ipynb`):

### Section 1: Environment Setup & Tool Selection (30 min)
- Choose deployment path (Claude/Ollama/Hybrid)
- Verify installation and configuration
- Test connectivity with simple API call
- **Pre-configured:** Environment checks and validation cells

### Section 2: LLM Basics - First API Call (15 min)
- Understand request/response cycle
- System vs User prompts
- Temperature and generation parameters
- Multi-model compatibility
- **Pre-configured:** Helper functions for API calls

### Section 3: Prompt Engineering with CO-STAR (30 min)
- **C**ontext: Providing background information
- **O**bjective: Defining clear goals
- **S**tyle: Formal vs casual communication
- **T**one: Authoritative vs exploratory
- **A**udience: Target reader consideration
- **R**esponse Format: JSON, XML, plain text
- **Pre-configured:** Interactive exercises with templates

### Section 4: Structured Outputs (25 min)
- JSON formatting and parsing
- XML formatting and parsing
- Schema validation with Pydantic
- Error handling strategies
- **Pre-configured:** Validation schemas and parsing utilities

### Section 5: Chain-of-Thought Prompting (20 min)
- Theoretical foundation
- Implementation techniques
- Comparative analysis (with/without CoT)
- Multi-model reasoning comparison
- **Pre-configured:** Side-by-side comparison cells

### Section 6: Model Comparison & Limitations (25 min)
- Systematic model comparison
- Speed vs quality tradeoffs
- Cost analysis (cloud vs local)
- Hallucination documentation
- **Pre-configured:** Comparison framework and logging templates

### Section 7: Introduction to MCP (25 min)
- Model Context Protocol overview
- Agent architecture concepts
- Tool integration planning
- Future course preview
- **Pre-configured:** Conceptual diagrams and code scaffolding

### Section 8: Project Kickoff (30 min)
- Research agent definition
- Mission statement formulation
- Model selection justification
- Working prototype development
- **Pre-configured:** Project template with guided prompts

---

## 🎮 Working with the Notebook

### Running Cells

The notebook is designed to be run **sequentially from top to bottom**. Each cell builds on previous cells.

```python
# Example: First cell sets up the environment
# DO NOT SKIP THIS CELL
import os
from dotenv import load_dotenv
load_dotenv()

print("✓ Environment loaded successfully")
```

### Path Selection

At the beginning of the notebook, you'll select your path:

```python
# CONFIGURATION: Choose your path
PATH = "A"  # Options: "A" (Claude), "B" (Ollama), "C" (Hybrid)

# The notebook will automatically configure based on your choice
```

### Code Cells vs Markdown Cells

- **Code cells** (gray background): Run these to execute Python code
- **Markdown cells** (white background): Read these for instructions and context
- **TODO cells**: These require you to fill in code or answers

```python
# TODO: Your code here
# Replace this comment with your implementation
```

### Keyboard Shortcuts (in Jupyter)

- `Shift + Enter`: Run current cell and move to next
- `Ctrl/Cmd + Enter`: Run current cell and stay
- `A`: Insert cell above (in command mode)
- `B`: Insert cell below (in command mode)
- `DD`: Delete cell (in command mode)
- `M`: Convert to markdown (in command mode)
- `Y`: Convert to code (in command mode)

### Cursor IDE Features

If using Cursor IDE, you can:
- Use `Cmd/Ctrl + K` to chat with AI about code
- Highlight code and ask AI for explanations
- Use AI to help debug errors
- **Remember:** Understand all AI-generated code before submitting

---

## 📝 Deliverables

### Required Files (in `outputs/` directory)

1. **All 9 completed notebooks** (in `notebooks/`)
   - All code cells executed
   - All TODO sections complete
   - Observations documented

2. **Project Proposal** (`outputs/project_proposal.md`)
   - One-sentence mission statement
   - Agent description (2-3 paragraphs)
   - Model selection justification
   - Success criteria

3. **Limitations Log** (`outputs/limitations_log.md`)
   - Minimum 3-5 documented cases
   - Model name, prompt, expected/actual behavior
   - Hypotheses and improvement ideas

4. **Resource Analysis** (`outputs/resource_analysis.md`)
   - Path selection rationale
   - Cost estimates or hardware notes
   - Deployment strategy

---

## 🎯 Success Criteria

Your submission will be considered complete when:

- ✅ All 9 notebooks completed and executed without errors
- ✅ All TODO sections filled in
- ✅ All 4 deliverable files created in `outputs/`
- ✅ Working agent prototype built
- ✅ Cost tracker shows your API usage
- ✅ Reflections written in markdown cells

---

## 📊 Grading Rubric

| Component | Weight | Criteria |
|-----------|--------|----------|
| Notebook Completion | 30% | All 9 notebooks completed, code runs |
| CO-STAR Implementation | 15% | Demonstrates all 6 components |
| Structured Outputs | 10% | Reliable JSON/XML generation |
| Model Comparison | 10% | Thoughtful analysis |
| Project Proposal | 15% | Clear, feasible, justified |
| Limitations Log | 10% | Insightful observations |
| Documentation | 10% | Clear markdown, reflections |
| **Total** | **100%** | |

### Grading Scale
- **A (90-100%):** Exceptional work with creative extensions
- **B (80-89%):** Complete work meeting all requirements
- **C (70-79%):** Adequate work with minor gaps
- **D (60-69%):** Incomplete work or significant gaps
- **F (<60%):** Substantial missing components

---

## 💰 Cost Estimates

### Claude API (Path A)

| Model | Input Cost | Output Cost | Homework Est. | Project Est. |
|-------|-----------|-------------|---------------|--------------|
| Claude 3.5 Sonnet | $3/1M tokens | $15/1M tokens | $1-2 | $10-20 |
| Claude 3.5 Haiku | $1/1M tokens | $5/1M tokens | $0.50-1 | $3-8 |

### Ollama (Path B)
- **Software Cost:** $0
- **Hardware:** May require RAM upgrade ($50-150 if needed)
- **Electricity:** <$0.05 per session

### Hybrid (Path C)
- **Learning Phase:** $0 (Ollama)
- **Deliverables:** $1-5 (Claude)
- **Total Homework:** $1-5

---

## 🚀 Getting Started

### Quick Start (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/inference-ai-course/Homework1-Submission.git
cd Homework1-Submission

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API key (if using Claude)
cp .env.example .env
# Edit .env with your API key

# 5. Open notebook in your IDE
code .  # VS Code
# or
cursor .  # Cursor IDE
# or
jupyter lab  # Traditional Jupyter

# 6. Open homework1.ipynb and start working!
```

### Detailed Workflow

1. **Choose Your Path** (5 min)
   - Review deployment options
   - Consider budget, hardware, learning goals
   - Document choice in notebook Section 1

2. **Verify Setup** (10 min)
   - Run Section 1 verification cells
   - Confirm API connectivity or Ollama installation
   - Troubleshoot any issues

3. **Complete Core Sections** (90 min)
   - Work through Sections 2-7 sequentially
   - Complete all TODO items
   - Run experiments and document observations

4. **Project Kickoff** (30 min)
   - Complete Section 8
   - Write project proposal
   - Build initial prototype

5. **Documentation** (20 min)
   - Complete limitations log
   - Write resource analysis
   - Review and polish all deliverables

6. **Submit** (5 min)
   - Verify all files in `outputs/` directory
   - Commit and push to your repository
   - Submit according to course instructions

---

## 🔧 Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError: No module named 'anthropic'"
```bash
# Solution: Install dependencies in Terminal
pip install -r requirements.txt
```

#### Issue: "API key not found"
```bash
# Solution: Check .env file, did you created it? 
cat .env  # Should show ANTHROPIC_API_KEY=...

# Reload environment in notebook
from dotenv import load_dotenv
load_dotenv(override=True)
```

#### Issue: Ollama not responding
```bash
# Check if Ollama is running
ollama list

# Restart Ollama
# macOS/Linux: pkill ollama && ollama serve
# Windows: Restart Ollama app
```

#### Issue: Kernel not found in VS Code/Cursor
```bash
# Install ipykernel in your virtual environment
pip install ipykernel

# Register kernel
python -m ipykernel install --user --name=venv
```

#### Issue: Rate limit errors with Claude API
```python
# Add delays between API calls
import time
time.sleep(1)  # Wait 1 second between calls

# Or use exponential backoff (code provided in notebook)
```

### Getting Help

1. **Check notebook comments**: Solutions often in code comments
2. **Review setup guides**: See `docs/` folder for detailed guides
3. **Search Discord**: Your issue may already be solved
4. **Ask in Discord**: Post in #support-and-question channel
5. **Office hours**: Attend Scott's TA office hour (OH) for live troubleshooting (not guarantee, you will have a lot to discuss in the OH)
6. **Email instructor**: For private/urgent matters

---

## 📚 Resources

### Official Documentation
- [Anthropic API Documentation](https://docs.anthropic.com)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Ollama Models Library](https://ollama.ai/library)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### IDE Documentation
- [VS Code Jupyter Extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Cursor IDE Documentation](https://cursor.sh/docs)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)

### Python Libraries
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- [Pydantic](https://docs.pydantic.dev/)
- [Requests](https://requests.readthedocs.io/)

### Community
- Course Discord Server: [Link provided by instructor]
- Course GitHub Repository: [Link provided by instructor]
- Office Hours: [Schedule provided by instructor]

### Recommended Reading
- "Attention Is All You Need" - Transformer paper
- "Chain-of-Thought Prompting Elicits Reasoning" - Wei et al.
- Anthropic's prompt engineering cookbook

---

## ❓ FAQ

### General Questions

**Q: How long should this assignment take?**  
**A:** Plan for 2-3 hours for core notebook completion, plus 1-2 hours for project brainstorming and documentation.

**Q: Can I use a different IDE?**  
**A:** Yes! Any IDE that supports Jupyter notebooks will work. VS Code, Cursor, JupyterLab, and PyCharm are all fine.

**Q: Do I need to use Cursor IDE?**  
**A:** No, it's optional. Any Python IDE works. Cursor is recommended for its AI features but not required.

**Q: Can I work with a partner?**  
**A:** You must write your own code, but discussing concepts and collaborative debugging is encouraged.

**Q: What if I get stuck?**  
**A:** Use Discord community, attend office hours, or consult documentation. Document your debugging process in the notebook.

### Path Selection

**Q: Which path should I choose?**  
**A:** Path A for best results and course alignment, Path B for zero cost and local learning, Path C for balanced approach.

**Q: Can I switch paths mid-assignment?**  
**A:** Yes! Change the `PATH` variable in the notebook and run the setup cells again.

**Q: Will smaller Ollama models work?**  
**A:** Yes, concepts are the same. Results will vary in quality but educational value remains high.

### Technical Issues

**Q: My computer can't run Ollama. What should I do?**  
**A:** Use Path A (Claude API) or explore cloud options like Google Colab with GPU.

**Q: The notebook won't open in my IDE**  
**A:** Ensure Jupyter extension is installed. For VS Code: Install "Jupyter" extension. For Cursor: Built-in support should work.

**Q: How do I know if my setup is correct?**  
**A:** Run the verification cells in Section 1. They'll report success or specific errors.

**Q: I'm getting API authentication errors**  
**A:** Check your `.env` file has correct key, reload environment, verify key is active in console.anthropic.com

### Cost Management

**Q: How can I minimize API costs?**  
**A:** Use Haiku for testing, implement caching, add delays, use shorter prompts during development, or use Ollama for experimentation.

**Q: What if I run out of credits?**  
**A:** Switch to Ollama (Path B) for remaining work, or contact instructor about alternative arrangements.

**Q: Can I use the free tier of Claude?**  
**A:** You'll need an API key with credits. Free tier chat.claude.com doesn't provide API access.

---

## 🎁 Bonus Challenges (Optional)

For students seeking additional depth and extra credit (up to 10%):

### 1. Multi-Model Ensemble (5% extra credit)
Implement a system that:
- Queries 3+ different models with the same prompt
- Compares responses using automated metrics
- Implements voting/consensus mechanism
- Documents which model types excel at which tasks

### 2. Cost Optimizer (3% extra credit)
Build an automatic model selector that:
- Analyzes task complexity
- Estimates token usage
- Selects cheapest suitable model
- Tracks cost savings over naive approach

### 3. Cursor IDE Deep Dive (2% extra credit)
Complete the entire assignment in Cursor and document:
- How AI-assist helped or hindered
- Specific prompts used with Cursor AI
- Comparison with traditional coding
- Best practices discovered

### 4. MCP Server Implementation (5% extra credit)
Preview of Week 10:
- Set up a basic MCP server
- Implement file system tool
- Connect to Claude Desktop
- Document setup process for classmates

### 5. Comprehensive Benchmark Suite (5% extra credit)
Create systematic measurements:
- Speed tests across models
- Quality assessments (automated + manual)
- Cost per quality point analysis
- Interactive visualization of results

### 6. Helping others (1% extra credit for each response, up to 5%)
Post question or answer in Discord `support-and-questions` channel

**Submission:** 
- Add bonus work to `outputs/bonus_challenges.md` with code in separate notebook section.
- Post the screenshort of discord discussion to `outputs/bonus_challenges.md`.

---

## 📅 Timeline & Deadlines

### Recommended Schedule

| Day | Tasks | Time |
|-----|-------|------|
| **Day 1** | Setup complete, Section 1 | 30 min |
| **Day 2** | Sections 2-3 complete | 1 hour |
| **Day 3** | Sections 4-5 complete | 1 hour |
| **Day 4** | Section 6 complete, start limitations log | 45 min |
| **Day 5** | Section 7 complete | 30 min |
| **Day 6** | Section 8 + project proposal | 1 hour |
| **Day 7** | Review, polish, submit | 30 min |

### Important Dates
- **Assignment Release:** After each course
- **Office Hours:** Wed. 7-8pm (CT)
- **Submission Deadline:** Sunday 11:59pm
- **Late Submission Deadline:** Tuesday night (with penalty)

### Late Policy
- Up to 24 hours late (Monday): -10%
- Up to 48 hours late (Tuesday): -25%
- Beyond 48 hours: Contact instructor

---

## 🤝 Collaboration Policy

### Permitted
- Discussing concepts and approaches
- Helping each other debug setup issues
- Sharing resources and documentation
- Collaborating on understanding course material
- Pair programming for learning (but submit individual code)

### Not Permitted
- Copying code from other students
- Submitting someone else's work as your own
- Sharing complete solutions before deadline
- Using assignment solutions from previous years
- Having someone else write your code

### AI Tools Policy
- You **may** use AI assistants (Claude, GPT, Cursor AI, etc.) to help learn concepts
- You **must** understand and be able to explain all submitted code
- You **must** document AI assistance in comments when used significantly
- You **should** experiment with prompting the AI effectively (it's part of learning!)

**Example acceptable AI use:**
```python
# Used Claude to help debug this API call error
# Original error was "401 Unauthorized"
# Claude suggested checking .env file format
# I learned that the key needed to be on one line
```

---

## 📧 Support

### Support Channels (in order of preference)

1. **Notebook Comments:** Check inline comments and markdown cells first
2. **Setup Guides:** Review `docs/` folder for detailed setup instructions
3. **Discord - Search:** Your question may already be answered
4. **Discord - Ask:** Post in `#support-and-discussions` channel
   - Include error messages and screenshots
   - Mention your path (A/B/C) and IDE
   - Share relevant code snippets
5. **Office Hours:** Attend for live help with complex issues
6. **Email Instructor:** For private or urgent matters only

### Reporting Issues

Found a bug in course materials or the pre-configured notebook?

**Submit a GitHub issue with:**
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Error messages and screenshots
- Your environment (OS, Python version, path, IDE)

**Format:** markdown

**Problem:** Section 3 code cell raises KeyError

**Steps to Reproduce:**
1. Run cells in order through Section 3
2. Cell 42 raises error

**Error Message:**
```
KeyError: 'response'
```

**Environment:**
- OS: macOS 14.1
- Python: 3.11.5
- Path: A (Claude API)
- IDE: VS Code


---

## 🏆 Learning Outcomes Alignment

This assignment directly supports the following course-level learning outcomes:

- **LO1:** Understand fundamental concepts of Large Language Models
  - *Assessment:* Section 2, model comparison in Section 6
  
- **LO2:** Apply prompt engineering best practices
  - *Assessment:* CO-STAR implementation in Section 3
  
- **LO3:** Evaluate tradeoffs in AI system design
  - *Assessment:* Resource analysis, limitations log
  
- **LO4:** Build functional AI applications
  - *Assessment:* Working prototype in Section 8
  
- **LO5:** Document and communicate technical decisions
  - *Assessment:* Project proposal, all markdown documentation

---

## 📄 License

Course materials © 2025 inferenceAI. Licensed for educational use only.

**Students may:**
- Use materials for completing course assignments
- Reference materials for personal learning
- Share concepts learned (not solutions) with others

**Students may not:**
- Redistribute course materials publicly
- Use materials for commercial purposes
- Share solutions publicly before deadline

---

## 🙏 Acknowledgments

- **Anthropic** for Claude API and comprehensive documentation
- **Ollama Team** for democratizing local LLM deployment
- **Course TAs** for testing materials and providing feedback
- **Previous Cohorts** for suggestions and improvements
- **Open Source Community** for tools and libraries

Special thanks to contributors who helped refine this assignment.

---

## 📌 Version History

- **v1.1** (July 21, 2025) - Updated for IDE-based workflow with pre-configured notebook
- **v1.0** (July 14, 2025) - Initial release

### Changelog
See `CHANGELOG.md` for detailed version history and updates.

---

## 🎬 Next Steps

**After completing this assignment:**

1. ✅ Submit all deliverables in `outputs/` directory
2. ✅ Share your project idea in Discord `#project-ideas` channel
3. 📖 Read Week 2 materials on "LLM Architecture & Training Lifecycle"
4. 🔬 Continue experimenting with your agent prototype
5. 💬 Provide feedback on this assignment (optional survey link)

---

**Ready to start? Open `notebook` folder in your preferred IDE and begin!** 

*Questions? Check FAQ above or ask in Discord #support-discussions* 