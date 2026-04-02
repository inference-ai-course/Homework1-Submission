
# PROJECT DEFINITION TEMPLATE

## 1. PROJECT TITLE
Quality & Safety Regression Harness for LLM Applications

## 2. THE PROBLEM
A system may silently become less accurate, less safe, less consistent in formatting, or weaker in bilingual English/French behavior. Manual checking is slow, subjective, and difficult to repeat. 
I want a practical way to evaluate and compare LLM behavior so I can detect regressions before deploying or trusting a new version.

## 3. YOUR SOLUTION
My agent will act as a regression evaluation harness for LLM systems.

It will:
1. load a set of predefined evaluation test cases
2. run them against a baseline configuration and a candidate configuration
3. collect the outputs in a structured format
4. score them on dimensions such as instruction following, structure, safety, and bilingual consistency
5. compare results and flag regressions
6. generate a final summary report showing where the candidate improved or got worse

## 4. USER WORKFLOW
- User inputs: a test case dataset, a baseline setup, and a candidate setup
- Agent does:
  - send each test prompt to both versions
  - capture outputs
  - score outputs with a structured rubric
  - compare scores across versions
  - identify regressions and major failures
- User receives:
  - a per-test comparison table
  - a regression summary
  - a final report highlighting the most important quality and safety changes
For the first version, the user will likely run this from a notebook or Python script rather than a full UI.

## 5. COMPONENTS
Which techniques from the course will you use?

☑ CO-STAR prompting - I will use CO-STAR to design consistent evaluator prompts so the scoring instructions are clear, repeatable, and targeted.
☑ Structured outputs (JSON/XML) - I will require the evaluator to return structured fields such as  test_id, pass/fail, quality score, safety score, bilingual score, reason, and regression_flag.
☑ Chain-of-thought - I will use reasoning-based evaluation prompts so the model can judge outputs step by step before returning the final structured result.
☑ Model selection - I may use one model for generation and another for evaluation, or compare different model sizes/cost levels for the same task.
☐ MCP/Tool use - Not required for version 1. If time allows, I may add file or dataset loading tools later.
☑ Multi-step workflow - The project has the following pipeline: load tests → run baseline → run candidate → score outputs → compare results → generate report.
☑ Other: Reporting and analysis - I will generate a markdown and/or CSV regression report for easy review.

## 6. SUCCESS CRITERIA
How will you know if your project succeeded?

- Functional: The system can run a full evaluation set end-to-end without manual intervention except setup.
- Structured: The evaluator returns valid structured results for at least 90% of test cases.
- Useful: The report clearly shows which candidate outputs improved, worsened, or failed.
- Quality: The scoring dimensions are understandable and consistent enough to support decision-making.
- Demo-able: I can show the complete workflow in about 5 minutes.
- Practical: The project is useful for testing prompt or model changes in a realistic AI workflow.


## 7. SCOPE
What's IN scope and OUT of scope?

IN SCOPE (Must have):
- A small evaluation dataset of around 20-30 test cases
- Baseline vs candidate comparison
- Structured scoring across key dimensions
- Regression detection logic
- Final markdown or CSV report
- English and French test coverage in at least a basic form

OUT OF SCOPE (Nice to have, but not now):
- Fine-tuning any model
- Full enterprise Proprietary LLM models integration
- Advanced dashboard or database backend
- Large-scale benchmark datasets
- Automated retraining or optimization loops
- Full production web app
- Human annotation platform

## 8. DATA SOURCES
What data will your agent work with?

The project will work mainly with a custom evaluation dataset that I create.
The dataset will include:
- prompt-following tasks
- structured extraction tasks
- safety-sensitive prompts
- English test cases
- French test cases
- a few bilingual consistency checks
If needed, I may also include a small number of synthetic or manually written examples to expand the test set.

## 9. TECH STACK
What tools/libraries will you use?

- LLM:
  - open-source LLMs(Llama,Qwen, DeepSeek etc) for generation and/or comparison
  - optionally Chatgpt/Claude/Gemini API later for evaluation or comparison
- Python: pandas, matplotlib (optional)
- JSON, Markdown and CSV
- Possibly:
  - Hugging Face transformers or API wrappers
  - simple local file-based test dataset

## 10. TIMELINE
What's your week-by-week plan?

Week 1 (This week):
- Finalize project definition
- Design evaluation dimensions and scoring rubric
- Create initial test dataset
- Build simple baseline vs candidate execution flow

Week 2-3:
- Implement structured evaluator prompts
- Save outputs and scores in JSON/CSV
- Add regression comparison logic
- Generate first working report

Week 4 (Project Insight I):
- Demo: show a small end-to-end evaluation on a baseline and candidate setup
- Get feedback on scope, scoring quality, and usefulness

Week 5-6:
- Improve prompt quality and scoring consistency
- Add better bilingual and safety test coverage
- Refine report format and summary logic

Week 7 (Project Insight II):
- Finalize scope
- Decide which optional features to keep or drop

Week 8-10:
- Polish implementation
- Test reliability on more cases
- Improve documentation
- Prepare final demo and explanation

Week 10 (Final Presentation):
- Demo the complete regression harness
- Show one example where the system catches a meaningful regression

## 11. RISKS & MITIGATION
What could go wrong?

Risk 1: The evaluator model may be inconsistent or subjective.
Mitigation: Keep the rubric simple, use structured outputs, and test the same cases repeatedly to check stability.

Risk 2: The project becomes too large if I try to support too many models or features.
Mitigation: Limit version 1 to one baseline, one candidate, and a small dataset.

Risk 3: Bilingual evaluation may be harder than expected.
Mitigation: Start with a small English/French subset and use only a few clearly defined bilingual checks.

Risk 4: Open-source models may be harder to configure than expected.
Mitigation: Keep the architecture model-agnostic so I can swap models later without redesigning the project.


## 12. STRETCH GOALS
What would you add if you had more time?
- Add cost and latency tracking
- Add support for user-uploaded test datasets
- Add a Proprietary LLM models compatible adapter for API-based testing
- Add severity ranking for regressions
- Add pairwise side-by-side judging
- Support more evaluation dimensions
- Add prompt version tracking over time
- Add a simple dashboard or web UI

