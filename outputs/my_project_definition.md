# My Research Agent Project
**Created:** 2026-03-31 17:06:26


# MY RESEARCH AGENT PROJECT

## 1. PROJECT TITLE
Quality & Safety Regression Harness

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
- Functional: The system can run a full evaluation set end-to-end without manual intervention except setup.
- Structured: The evaluator returns valid structured results for at least 90% of test cases.
- Useful: The report clearly shows which candidate outputs improved, worsened, or failed.
- Quality: The scoring dimensions are understandable and consistent enough to support decision-making.
- Demo-able: I can show the complete workflow in about 5 minutes.
- Practical: The project is useful for testing prompt or model changes in a realistic AI workflow.

## 7. SCOPE
IN SCOPE:
- A small evaluation dataset of around 20-30 test cases
- Baseline vs candidate comparison
- Structured scoring across key dimensions
- Regression detection logic
- Final markdown or CSV report
- English and French test coverage in at least a basic form

OUT OF SCOPE:
- Fine-tuning any model
- Full enterprise Proprietary LLM models integration
- Advanced dashboard or database backend
- Large-scale benchmark datasets
- Automated retraining or optimization loops
- Full production web app
- Human annotation platform

## 8. DATA SOURCES
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
- LLM:
  - open-source LLMs(Llama,Qwen, DeepSeek etc) for generation and/or comparison
  - optionally Chatgpt/Claude/Gemini API later for evaluation or comparison
- Python: pandas, matplotlib (optional)
- JSON, Markdown and CSV
- Possibly:
  - Hugging Face transformers or API wrappers
  - simple local file-based test dataset

## 10. TIMELINE
Week 1:
- Finalize project definition
- Design evaluation dimensions and scoring rubric
- Create initial test dataset
- Build simple baseline vs candidate execution flow

Week 2-3:
- Implement structured evaluator prompts
- Save outputs and scores in JSON/CSV
- Add regression comparison logic
- Generate first working report

Week 4 (Insight I):
- Demo: show a small end-to-end evaluation on a baseline and candidate setup
- Get feedback on scope, scoring quality, and usefulness

Week 5-6:
- Improve prompt quality and scoring consistency
- Add better bilingual and safety test coverage
- Refine report format and summary logic

Week 7 (Insight II):
- Finalize scope
- Decide which optional features to keep or drop

Week 8-10:
- Polish implementation
- Test reliability on more cases
- Improve documentation
- Prepare final demo and explanation

## 11. RISKS & MITIGATION
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



---

## AI Feedback

Overall, your project definition looks comprehensive and well-thought-out. Here are some constructive feedback and suggestions:

1. Scope: The scope you've outlined for 2-3 weeks might be overly ambitious. Some of the stretch goals you've listed, such as adding a proprietary LLM models adapter or a dashboard/web UI, could potentially require more time and resources to implement correctly.

Consider breaking down your project into smaller tasks and focusing on delivering a solid core functionality first. You can always revisit and add more features later in future iterations.

2. Challenges: Some potential challenges you might encounter include:
* Ensuring the consistency of your testing dataset and scoring rubric.
* Handling edge cases or unusual test prompts that may not fit well within your scoring dimensions.
* Managing the trade-offs between model performance, computational resources, and evaluation time.

Plan for these challenges by including contingencies in your timeline and being prepared to adapt your approach as needed.

3. Suggestions:
* Consider adding more testing to ensure that your code is robust and reliable. You might want to include unit tests, integration tests, and maybe even some end-to-end tests.
* Think about how you can make your project more flexible and adaptable. This could involve designing your architecture to be modular or using techniques like feature toggles or A/B testing.
* Keep in mind that your project is not just about implementing a specific set of features but also about delivering value to the user. Consider how you can ensure that your project meets their needs and provides a good user experience.

4. Prioritization:
One thing I would suggest prioritizing is ensuring that your scoring dimensions are clear, concise, and well-defined. This will help maintain consistency across tests and reduce the risk of subjectivity or bias in your evaluation.

Additionally, make sure to test your project thoroughly to ensure it meets your goals and requirements. A good rule of thumb is to prioritize testing when you're not sure if something works as expected.

Overall, your project definition looks solid, and with careful planning, execution, and iteration, you can create a high-quality project that meets your goals.
