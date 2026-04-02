# Week 1: LLM Introduction - Homework Reflection

**Student Name:** Kai Yang

**Path Selected:** C

---


## Notebook 02: Task 1 - Custom System Prompt

**Completed:** 2026-03-29 15:47:23

### What I Learned

Creating a custom system prompt can help generate answers that better fit the client’s needs.

### How the System Prompt Affected the Response

The system prompt gives the model guidelines on how questions should be answered, such as role, tone, and output format etc. The answers will be more standardized.

### Real-World Applications
Within a company, the system prompt can be tailored to each department’s needs (customer service might be more empathetic, finance might be more analytic and each team's constraint etc are also different).
For personal use, it can be adapted to different projects, such as travel planning or course learning.

---

## Notebook 02: Task 2 - Temperature Exploration

**Completed:** 2026-03-29 16:37:07

### Temperature 0.0 Analysis

The wording is more concrete ("circuits and wires"), the structure is consitent (two phases of 3~5 words each line), maintains a stable theme (connection).

### Temperature 0.5 Analysis

The wording becomes less concrete and more expressive, the structure is more flexible,there is a better balance between current reality and reflection

### Temperature 1.0 Analysis

The wording is more abstract ("fate"), structure is more randamlised (could have 1 or 2 phases each line), the imagination is more wild.

### Conclusion

**Best temperature for this task:** 1.0

**Reasoning:** I tend toward 1.0 for artwork because it prioritizes creativity over consistency. We might get 100 bad results, but one excellent one makes it all worth it.

### When to Use Each Temperature

- **Temperature 0.0:** factual Q&A, data extraction, work that requires consistency (coding, accounting, legal analysis, technical instructions)
- **Temperature 0.5:** general explanations, summaries, chatbots, emails, resume.
- **Temperature 1.0:** creative writing, brainstorming like project ideas, diverse solutions, creating variations.

---

## Notebook 02: Task 3 - Cost Optimization

**Completed:** 2026-03-29 17:23:11

### Comparison Results

- **Token savings:** 39 tokens (49.4%)
- **Cost savings per request:** $0.000168
- **Projected savings (100 requests):** $0.0168

### Quality Analysis

**Did the verbose version produce a better response?**
Hard to say. The results of the two prompts seem to be different. However, this should mainly be due to the randomness of the model, as it can generate different content for the same prompt as well.

**Was the concise version still clear and complete?**
In general, yes, it might miss the "to be detailed" in the instruction.

### Key Lessons Learned

1. The prompt efficiency is of vital importance: an ill-designed prompt could dramatically increase the cost without bringing improvement.
2. A verbose prompts may be justified when it can provide addtional relevant information on how to response (e.g. "COSTAR"etc) 
3. I should form a good habit: the prompt should provide sufficient relevant information while also remaining concise.

### My Cost Optimization Strategy

Going forward, I will:
- distribute tasks across models and sub-models based on their cost and strengths (for example, use Claude Opus for architecture and planning, then Claude Sonnet or other models for coding based on the plan)
- build good prompt engineering habits (system prompt, COSTAR) to keep prompts informative but concise
- use project guidline files to help the model to better understand the project and save tokens
- apply project management principles (e.g., break large tasks into smaller steps to reduce unnecessary context and save tokens)

---

## Notebook 02: Overall Reflection

**Completed:** 2026-03-29 17:39:29

### 1. What surprised you most about system prompts?

I was surprised by how different the answers could be with different system prompts. It felt as if the model was answering different questions.

### 2. For factual questions, what temperature do you prefer and why?

0.0 factual questions require accuracy. 

### 3. What's your main strategy for keeping API costs low?

Apply good prompting practices, avoid unnecessary input, and especially avoid useless output.

### 4. What's one practical use case where you'd use these techniques?

I would add system prompts to my current projects to improve efficiency and reduce token usage.

### 5. What was your most interesting finding from this notebook?

I did not find anything especially interesting, but I was again impressed by how impactful system prompts could be.

### 6. What will you do differently in future prompting?

I will build better prompting habits by applying principles such as system prompting and frameworks like COSTAR.

---

## Notebook 03: Task 1 - Build Your CO-STAR Prompt

**Completed:** 2026-03-29 19:53:19

### What scenario did you choose?

I choose the educational scenario. I wanted the model to show good and bad pratice of vibe coding

### How did each CO-STAR component help?

**Context:** I specified that this topic is about vibe coding and the model should repond as an expericed professional.

**Objective:** Yes, I asked for a denfinition and two lists.

**Style:** Yes, it was clear and easy to understand.

**Tone:** Yes, I wanted to avoid unnecessary emotional language, which it did.

**Audience:** Yes, it is simple enough for people with little techinical background.

**Response Format:** Yes, the output is what I would like to have.

### Quality of the response

 __4_/5

The overall response was decent and useful. It answered the main question and gave me the kind of structure I asked for.

The response felt a bit too general, maybe I can refine the prompt to ask for more concrete examples and more actionable advice.

### Real-world application

It will be very useful for both this course and my personal projects as I have limited techinical knowledges.

---

## Notebook 03: Task 2 - Component Variation Analysis

**Completed:** 2026-03-29 20:11:27

### Component Varied: style

### Base Configuration
{
  "context": "You are a travel guide writer.",
  "objective": "Describe a day trip to a mountain hiking trail.",
  "style": "descriptive and informative",
  "tone": "enthusiastic",
  "audience": "outdoor enthusiasts",
  "response_format": "2-3 paragraphs"
}

### Variations Tested
{
  "Variation 1": "professional and techinical",
  "Variation 2": "professional and business-oriented",
  "Variation 3": "narrative"
}

### Analysis

**Variation 1 (professional and techinical):**
This version is more structured and detailed, focusing on specifics like elevation, distance, and terrain. 

**Variation 2 (professional and business-oriented):**
This version is more promotional and engaging than Variation 1. It contains appealing language and feel like marketing content.

**Variation 3 (narrative):**
This version is more story-driven. It is engaging and vivid but less informative.

### Key Insight

Style strongly influences how the response feels, even with the content is the same.

### Best Choice

**For this use case, I would choose:** Variation 1

**Because:** 
I would prefer factual information, such as what the activities are and how they are organized, over appealing language or a vivid story.

---

## Notebook 03: Task 3 - Production Template

**Completed:** 2026-03-29 20:57:26

### Template Details

**Name:** Code Review Assistant

**Use Case:** Use this to help me to review the codes

**When to use this template:**
Help me complete this course’s homework and projects, as well as my personal projects and even future professional projects. 

### CO-STAR Components Explained

**Context:** I need the model to play a role with a strong technical background to ensure reliability.

**Objective:** Yes, I asked it to identify issues, risks, and improvements.

**Style:** It makes the feedback easy to follow and act on.

**Tone:** It helps avoid unnecessary emotional fluctuations.

**Audience:** This is mainly for me, as I will be the primary user.

**Response Format:** The output format is easy to read and ensures that no important aspect is missed.

### Test Results

**Quality of output:** __4_/5

**What worked well:**
The objective is clear, and the feedback is structured and easy to follow.

**What could be improved:**
It could include issue prioritization, from major to minor. The output format could also be JSON or Markdown for CLI-to-CLI use. It could additionally include more explanations for beginners.

### Reusability Assessment

**How reusable is this template?** High

**What would need to change for different inputs?**
Audience level, for example beginner vs. experienced programmer.
Level of detail

**Estimated ROI:**
- Time saved per use: 30 minutes
- Frequency of use: 6 times per week
- Total time saved: 3 hours (the real time saved could be much higher, since I might not identify the issue by myself)

### Production Readiness

**Is this ready for real use?** Yes, it will be better with further refinement.

**Next steps to make it production-ready:**
1. Add severity levels (critical, important, minor)
2. Add beginner-friendly explanations
3. Change the output to a md file

### Template Storage

I will save this template:
- [X] In a personal prompt library
- [ ] In team documentation
- [X] In project codebase
- [ ] Other: ___________

---

## Notebook 03: Overall Reflection

**Completed:** 2026-03-29 21:08:10

### 1. How has CO-STAR changed your approach to prompting?

It has made my prompts more structured, and the instructions more accurate and targeted.

### 2. Which component do you find most impactful and why?

Objective. It answers the question of what to do first; then we can define the scope, method, and level of detail.

### 3. When would you skip CO-STAR and use a simpler prompt?

For simple questions, such as converting length measurements.

### 4. How will you use CO-STAR in your work/projects?

I will integrate it into my current workflow to ensure I use it regularly.

### 5. What was your biggest "aha!" moment in this notebook?

I did not have that moment, but I was still surprised by how much the output changed after modifying only one component (style).

### 6. Rate your CO-STAR confidence: _4__/5

I understand the framework and can apply it to real problems, but I still need more practice.

---

## Notebook 04: Task 1 - JSON Extractor

**Completed:** 2026-03-29 22:54:50

### Extraction Quality

**Did it correctly extract all fields?** Yes

All went well.

### Prompt Effectiveness

**How clear was your prompt?** __5_/5

Specify how to handle errors / missing data.

### Real-World Application

**Where would you use this review extractor?**

The product company could use this extractor to collect and organize customer feedback in a structured way.

### Challenges Encountered

The first version of the schema did not fully comply with the ProductReview class.
I solved this by checking both schemas again and making sure they matched exactly.

---

## Notebook 04: Task 2 - Multi-Record Extraction

**Completed:** 2026-03-29 23:43:00

### Multi-Record Extraction

**Number of items in text:** 7

**Number correctly extracted:** 7

**Accuracy:** 7/7=100%

### Challenges with Arrays

The model needs to understand the nested schema and make sure it does not miss any items.

### Data Quality

All fields are correctly identified 

The original prompt didn't enfore resteruant name and vegetarian as well as handing of spciy level. Now they are fixed.

### Scaling Considerations
The model should still be able to handle it, but token limits and cost constraints may become a problem. 
Reliability may also decrease if the input becomes too long.

### Production Readiness
It seems usable if the data is clean. However, it still lacks proper error-handling mechanisms, which could cause problems when the input data is unexpected or inconsistent.
Some error-handling strategies should be added.

---

## Notebook 04: Task 3 - Error Recovery System

**Completed:** 2026-03-30 00:25:11

### Retry System Performance

**Succeeded on attempt:** 2

**What changed between attempts?**
The first prompt just ask to extract.The second specify the format (only valid JSON). The third with an example.

### Error Recovery Strategies

Example-based. Because it is easier for the model to follow it than instructions only. An example can also clarify details that may be missing in the instructions.

### Production Considerations

**Is 3 retries enough?**
In most cases, it should be sufficient. It provides a reasonable balance between reliability and cost.

**What's the cost of retries?**
For Claude Sonnet 4.5
frist run: 10 input tokens * $3 / 1000000 = $ 0.00003 + 25 output tokens *$15 /1000000 = 0.000375 = 0.000405
second run: 17 input tokens * $3 / 1000000 = $ 0.000051 + 25 output tokens *$15 /1000000 = 0.000375 = 0.000426
third run: 71 input tokens * $3 / 1000000 = $ 0.000213 + 25 output tokens *$15 /1000000 = 0.000375 = 0.000588

**When would you give up?**
I would give up when it repeatedly fails, for example by missing required fields or failing to generate valid JSON.

### Alternative Approaches

**Besides retrying, what else could you do?**
1. Apply data-cleaning strategies to make the input cleaner.
2. Use a more structured method for handling the data.
3. Switch to a more capable model or involve human review when needed.1. 

### System Design

**How would you integrate this into a production pipeline?**
I would first use Pydantic to validate the output, then refine the prompt further if validation fails.

---

## Notebook 04: Overall Reflection

**Completed:** 2026-03-30 00:42:32

### 1. What was the hardest part of getting reliable JSON/XML?

The hardest part is guiding the model to map the information into the format we need without adding extra information or missing required fields.

### 2. How confident are you in building production data extractors? (1-5)

**Confidence:** __3_/5

More pratice with real-world data (and problem)

### 3. When would you use JSON vs XML?

In most cases, we use JSON. XML is more common in enterprise systems and legacy APIs..

### 4. What's your strategy for handling extraction failures?

If certain errors are common, I would consider handling them before sending the input to the model. Then I would retry with stricter and stricter prompts and stop after a certain number of attempts.

### 5. How will you use structured outputs in your projects?
Consider this during workflow design to automate the transformation of unstructured data into structured data, which should make downstream processing easier.

### 6. Biggest takeaway from this notebook?
Small prompt changes can significantly improve output reliability. It is not just about prompting, but also about system thinking.

---

## Notebook 05: Task 1 - Multi-Step Problem Solving

**Completed:** 2026-03-30 01:09:12

### Problem Chosen
A parking garage charges $5 for the first hour, $3 for each additional hour,
and has a maximum daily charge of $25. If you park for 9 hours, how much do you pay?

### Without CoT Analysis

**Answer received:** To find out how much you pay, let's break it down:

1. The first hour costs $5.
2. For the remaining...

**Correct?** No

It fails to consider the maximum daily charge.

### With CoT Analysis

**Reasoning shown:** 

Get first hour charge, add extra hours charges, then the total charege, compare it to mmaximum and use the lower of the two.

**Final answer:** 25

**Correct?** Yes

### Comparison

**Which approach was more accurate?** With CoT

**Which was more transparent?** Both

**Which gave you more confidence?** With CoT

### Quality of Reasoning

**Did CoT show all necessary steps?** Yes

All required steps are showing.

**Could you verify each step?** Yes
All steps are correct 2 out of 3 times.

### Key Insight

When CoT helps most? Mutli-step reasonsing

### Real-World Application
The could be applied to all senarios required mutli-step reasoning

---

## Notebook 05: Task 2 - Debug Faulty Reasoning

**Completed:** 2026-03-30 01:23:41

### Did it get the correct answer? ($0.05)

Yes

### Reasoning Quality

Yes
Step 1: Correct: Define Variables T and B
Step 2: Correct: Write Out Equations B + T = 1.10 and T = B + 1.00
Step 3: Correct: Substitute equation (2) into equation (1) we get B + (B + 1.00) = 1.10 then B = 0.05


### If it got it wrong:

**Where did the reasoning fail?**

N/A

**How would you fix the prompt to help it?**

N/A

### If it got it right:

**What made the CoT effective?**

The question is broken down and each step is ensured to be correct.

**Could you simplify the prompt and still get it right?**

Yes, but the same principle applies.

### Key Learning

**What makes a problem "tricky"?**

It tricks the people or the model to get the fast intuitive reponse which is wrong after step-by-step verification.

**How does CoT help with tricky problems?**

It enfore the verification of each step.

### Debugging Strategy

**How would you use CoT to debug LLM reasoning in production?**
I will require the model to show/implement step-by-step reasonsing process to verify/ensure reliability.

---

## Notebook 05: Task 3 - CoT with Different Settings

**Completed:** 2026-03-30 01:51:50

### Temperature Comparison

#### Temperature 0.0 (Deterministic)

**Reasoning quality:** ___2/5

**Final answer:** 30

**Consistency:** No

**Observations:**
The model mistakes the price of set for item; besides it can't get the correct price of the 7th item believing it's free.
Besides, it is not consistent

#### Temperature 0.5 (Balanced)

**Reasoning quality:** __5_/5

**Final answer:** 75

**Different from temp 0.0?** Yes, it is correct.

**Observations:**
I also shows randomness, the result after reunning is wrong.

#### Temperature 1.0 (Creative)

**Reasoning quality:** _3__/5

**Final answer:** 60

**Different from others?** Yes, it gets the first two sets correct but think the 7th item is free.

**Observations:**
The first run's result is logical except for the 7th item 

### Overall Analysis

**Best temperature for CoT reasoning:** 0.5

**Why?**
The balance may make it seem right, but I would still expect 0.0 to have a higher chance of giving the correct result.
None of the three is consistent, so it feels pointless to evaluate them.

**Does CoT work better with lower temperatures?**
Yes, maybe that's the reason why 0.5 got it right (once)

### Trade-offs

**Accuracy vs Creativity:**
The lower the temperature, the more accurate but less creative the model tends to be.

**When might you want higher temperature with CoT?**
For brainstorming tasks that still require logical thinking, for example brainstorming possible strategy changes.

**When should you always use temperature 0.0?**
For tasks that require high accuracy, such as accounting calculations.

### Production Recommendations

**For math/logic problems:** Temperature = _0.0__

**For planning/strategy:** Temperature = __0.5_

**For creative problem-solving:** Temperature = __0.8_

**Reasoning:** 
Lower temperature ensures stable and correct outputs for deterministic tasks, while moderate temperature allows some flexibility for planning without losing coherence. 
Higher temperature is best for creativity and idea generation, where variation is more important than strict correctness.

---

## Notebook 05: Overall Reflection

**Completed:** 2026-03-30 02:11:40

### 1. How has CoT changed your approach to complex problems?

It makes my approach more structured. Instead of asking the question directly, I now break it into several steps.

### 2. When will you use CoT vs regular prompting?

CoT is better for complex, multi-step problems that require reasoning.
Regular prompting is better for simple tasks or factual checks.

### 3. What's your confidence in using CoT? (1-5)

**Confidence:** __3/5

More practice and more problem-solving experience on real-world projects would increase my confidence.

### 4. Most surprising finding about CoT?

With CoT, temperature 0.5 gave the correct answer while 0.0 was wrong.

### 5. How will you use CoT in your projects?
Implement it in workflows that require multi-step reasoning (e.g.architecture-level projects) to reduce the chance of errors.

### 6. CoT limitations you discovered?

The results can still be inconsistent: model may produce different answers after rerunning the same prompt.
Also, if the steps in the prompt are wrong, the output will likely be wrong as well.

### 7. Key takeaway from this notebook?
CoT is a powerful tool for improving reasoning. Using it wisely can help avoid unnecessary setbacks.

---

## Notebook 06: Task 1 - Find Your Perfect Model

**Completed:** 2026-03-30 02:50:59

### Task Description

Generate 3 research questions based on this topic: vibe coding. This is the most relevant for me.

### Model Comparison

For each model, rate the response quality (1-5):

#### Model 1: claude-haiku-4-5-20251001
- **Quality Rating:** _1__/5
- **Speed:** Fast
- **Cost:** $0.001264
- **Strengths:** Speed
- **Weaknesses:** The quality needs improvement, it assumes "vibe coding" is  coding documentation.

#### Model 2: claude-sonnet-4-5-20250929
- **Quality Rating:** __2_/5
- **Speed:** Medium
- **Cost:** $0.003357
- **Strengths:** At least one of the three questions is about AI-assisted coding.
- **Weaknesses:** The other two questions still don't make sense.

#### Model 3: llama3.2:3b
- **Quality Rating:** __1_/5
- **Speed:** Slow
- **Cost:** $0
- **Strengths:** cost
- **Weaknesses:** like Claude Sonnet, it doesn't understand thsi notion.

### Winner for This Task

**Best overall:** claude-sonnet-4-5-20250929

**Why?**
At least it got one relevant question.

### Cost-Quality Tradeoff

**Is the quality difference worth the cost difference?**

For this case, yes. The other models' reponses are pointless.

### Speed Consideration

**Does response time matter for your use case?**

No, it does several seconds to complete and I can wait.

### Decision for Your Project

**Which model will you use for this type of task?**
claude-sonnet-4-5-20250929, it seems to be the one model capable of generating meaningful reponses.

### Scaling Considerations

**If you run this task 1000 times/month:**
- Model A would cost: $1.264
- Model B would cost: $3.357
- Model C would cost: $0

**Still worth it?**
Overall, not really—it feels like a lottery. claude-sonnet-4-5-20250929 seems to have a higher chance of producing meaningful results, but not worthy it.

---

## Notebook 06: Task 2 - Model Selection Strategy

**Completed:** 2026-03-30 03:31:18

### Your Selection Framework
The best performance-to-cost ratio. I prioritize accuracy for important projects and favor low-cost or free models for less critical tasks.

### Key Decision Factors

**Most important factor:** 
Quality

**Why?**
If the output is not good enough, then the time, money, and human effort spent on it are wasted.

### Trade-off Analysis

**Quality vs Cost:**
Use cheaper models for simple or high-volume tasks and reserve expensive models for complex, high-impact tasks.

**Speed vs Quality:**
Speed matters in high-volume scenarios, where lower quality is acceptable. 
For critital tasks, quality is prioritized over speed.

**Local vs API:**
Local models are used for experimentation and cost-sensitive tasks. 
API models shoudl be used when higher accuracy is required.

### Risk Mitigation

**What happens if you choose wrong?**
Too cheap : poor quality, errors, or pointless output
Too expensive : unnecessary cost, less resources for real important projects

**How will you validate your choices?**
Test on sample data, compare outputs across models, after implementing keep monitoring the performance.

### Budget Planning

**Monthly budget allocation:**
- Experimentation: $__0_
- Development: $__30_
- Production: $__30_

**Total:** $__60_/month

**Is this realistic?** Adjusted if needed

### Adaptation Strategy

**How will you adjust as you learn more?**

Keep evaluating model performance and cost, ajust models based on observed metrics.

**What metrics will you track?**

1. Error rate
2. cost per task
3. consistency

### Confidence Level

**How confident are you in this strategy?** __3_/5
More real-world model performance and usage data will allow me to better assess this strategy.

---

## Notebook 06: Task 3 - Budget Optimization

**Completed:** 2026-03-30 04:41:58

### Workflow Design

**Number of steps in your workflow:** 5

**Total LLM calls per workflow run:** 36

### Model Selection Per Step
Step 1: Generate search queries
Model: llama3.2:3b
Why: Simple task, no deep reasoning required, prioritize cost
Estimated calls: 5

Step 2: Extract metadata from papers
Model: llama3.2:3b
Why: Structured extraction, can be handled locally with no cost
Estimated calls: 20

Step 3: Filter relevant papers
Model: claude-haiku-4-5-20251001
Why: Simple relevance filtering, binary/low complexity
Estimated calls: 5

Step 4: Deep analysis of selected papers
Model: claude-opus-4-5-20250929
Why: Complex reasoning, requires good balance of quality and cost
Estimated calls: 5

Step 5: Synthesize findings
Model: claude-sonnet-4-5-20250929
Why: Final output quality is important
Estimated calls: 1


### Cost Calculation

**Total cost per workflow run:** $0.0440

**Cost for 10 runs (development):** $0.44
**Cost for 100 runs (light production):** $4.40
**Cost for 1000 runs (heavy production):** $44

### Quality vs Cost Tradeoffs

**Where did you choose cheaper models?**
Query generation, metadata extraction and filtering
These tasks are simple or non-critical, so cost saving is prioritized

**Where did you splurge on better models?**
Deep analysis and final synthesis. These steps require stronger reasoning ability. 
I deliberately selected the most expensive model (Opus) for deep analysis to evaluate its impact on cost.

**What's at risk if cheaper models fail?**
Incorrect upstream data may cause errors downstream and reduce final output quality

### Optimization Opportunities

**Caching:** Cache metadata extraction results and analysis results for repeated queries

**Batch processing:** Batch metadata extraction and filtering steps to reduce overhead

**Fallback strategy:** Firstly try to improve prompts if still not work, upgrade the models

### Budget Reality Check

**Is this affordable for your use case?** Not Really

**If No, what would you change?**
Change the model of deep analysis back to claude-sonnet-4-5-20250929.

**If Yes, any room for quality upgrades?**
upgrade filtering model to claude-sonnet-4-5-20250929; upgrade final synthesis to Opus is another option but could be too expensive.

### Production Readiness

**Monitoring plan:**
Keep monitoring the error rates, cost per run and consistency.

**Alert thresholds:**
Metrics move beyond thresholds (e.g., cost, error rate) or fall below thresholds (e.g., consistency).

### Biggest Insight
I knew deep analysis required more token but was still suprised by the cost increase when changed its model to Opus.

---

## Notebook 06: Overall Reflection

**Completed:** 2026-03-30 04:53:56

### 1. Which model will you use most often?

I will probably use Claude Sonnet most often because it offers a good balance between quality and cost, I may use it for most development and production tasks.

### 2. Biggest surprise about model differences?

How expensive certain model coulde be.

### 3. How will you balance cost vs quality?

Use cheaper or free models for simple, high-volume tasks, and reserve stronger models for complex or high-impact steps.

### 4. Confidence in model selection? (1-5)

**Confidence:** __3_/5

More hands-on experience with real-world projects would help me better compare models’ performance-to-cost ratios.

### 5. Your model selection strategy in one sentence:

Maximize the overall performance-to-cost ratio while meeting the required quality level.

### 6. How will this impact your project budget?

It should help control my budget by avoiding unnecessary use of expensive models.

### 7. Key takeaway from this notebook?

Model selection should be based on task requirements. The best strategy is a practical balance of quality, cost and speed.

---

## Notebook 07: Task 1 - Design Your Research Agent Tools

**Completed:** 2026-03-30 05:56:39

### Tool Design

**Total tools designed:** 5

**Categories:**
- Search/Discovery: 1 tool
- Data Processing: _2 tools
- Analysis: 1 tool
- Output Generation: 1 tool

### Tool Complexity

**Simplest tool:** search_arxiv
It's mainly a common search by key words.

**Most complex tool:** analyze_paper
iI requires deeper reasoning to understand the meaning and make comparaison.

### Existing vs Custom

**Tools that exist (can use off-the-shelf):** 
search_arxiv, extract_paper_metadata, filter_relevant_papers

**Tools you'd need to build custom:**
analyze_paper, synthesize_findings

### Implementation Priority

**Must-have (Priority 1):**
1. search_arxiv
2. extract_paper_metadata

**Nice-to-have (Priority 2):**
1. filter_relevant_papers
2. analyze_paper

**Future enhancement (Priority 3):**
1. synthesize_findings

### Dependencies

**Do your tools depend on each other?**
Yes, each one depends on the one prior

**What's the sequence of tool calls?**
search_arxiv → extract_paper_metadata → filter_relevant_papers → analyze_paper → synthesize_findings → generate_research_questions.

### Data Flow

**What data flows between tools?**
list of papers => metadata extraction => filtered metadata extraction => analysis output  => summary

**Any bottlenecks?**
Deep analysis as it requires high reasoning ability to understand, analysis and compare the insights. 

### Error Handling

**What could go wrong with each tool?**
search_arxiv: irrelevant or missing results
extract_paper_metadata: missing fields, wrong field mapping
filter_relevant_papers: wrong selection
analyze_paper: misunderstanding, wrong reasoning, hallucination 
synthesize_findings: overgeneralization, loss of important details

**How would you handle failures?**
 Improve prompts, apply schema validation, use CoT when needed, make small test to select fit models.

### Real-World Readiness

**Could you actually build these tools?** Yes with help of LLMs

**What skills/resources would you need?**
Prompt design, structured output validation, chain of thought, testing skills for model selection and  AI coding assistance etc.

**Timeline to implement:**
Tool 1: search_arxiv — 4 to 6 hours
Tool 2: extract_paper_metadata — 1 day
Tool 3: filter_relevant_papers — 1 day
Tool 4: analyze_paper — 2 to 3 days
Tool 5: synthesize_findings — 1 to 2 day

### Biggest Insight

Designing tools for agents means breaking the workflow into small functions with clear inputs and outputs. 
It requires good process design, attention to detail, and continuous effort.

---

## Notebook 07: Task 2 - Tool Calling Strategy

**Completed:** 2026-03-30 06:45:01

### Strategy Design

**How many tool calls did your scenario require?** 7

**Could it be done with fewer?** Yes, combien metadata extraction and filtering. 

**What's the maximum tool calls you'd allow?** 10
This allows enough steps to maintain accuracy without creating unnecessary cost.

### Decision Logic

**How does your agent choose which tool to use?**
It uses the user’s request and the output of the previous step

**Is it rule-based or LLM-driven?**
It is rule-based

**Advantages of your approach:**
1. Clear and logical workflow
2. Easier to debug and control costs

**Disadvantages:**
1. Less flexible for unusual requests
2. May require more manual design upfront

### Error Resilience

**Most likely point of failure:** Deep analysis

**How would you make it robust?**
Use retries, validation, fallback prompts or upgrade the model if the budget allows

**Should the agent retry failed calls?** Yes
Only for temporary errors.

### Efficiency

**Any redundant tool calls in your flow?**
Separate metadata extraction and filtering may be partly redundant.

**How could you optimize?**
Batch metadata extraction, combine filtering with metadata scoring, and cache repeated searches.

**Caching strategy:**
Yes. Cache search results and extracted metadata for a short period.

### User Experience

**Should users see tool calls happening?** No

**How would you show progress?**
Show short progress updates such as “Searching papers,” “Filtering top results,” and “Analyzing papers.”

**What if tools are slow?**
Provide progress messages

### Production Concerns

**Rate limits:**
Use batching, retries with backoff, and queue requests if limits are reached.

**Costs:**
Yes, the extra tool calls are worth it when they improve quality and structure.

**Monitoring:**
Track tool failure rate, cost per workflow, retry rate, and output quality.

### Biggest Challenge

Ensure that the tools complete their tasks with high quality while keeping the workflow efficient and robust.

### Key Insight

Agent systems work best when each tool has a clear role, well-defined inputs and outputs, and explicit stopping conditions.

---

## Notebook 07: Task 3 - MCP vs Alternatives

**Completed:** 2026-03-30 07:41:48

### Approach Selection

**Primary approach:** Function Calling + RAG

**Why this choice?**
Function calling offers a better balance: it is more structured and reliable than prompt engineering, while being easier to implement than MCP. 
RAG can also be added to retrieve data more efficiently and accurately.

### Context Matters

**For rapid prototyping, I'd use:** Prompt Engineering + RAG
**For production deployment, I'd use:** Function Calling + RAG
**For academic research, I'd use:** RAG
**For personal projects, I'd use:** Prompt Engineering / Function Calling

Different contexts have different needs. Prototyping favors speed and low setup cost. 
Production prioritizes reliability and maintainability.
Academic research often reqires retrieval and synthesis accuracy.
Personal projects depend on scope, time constraints etc.

### MCP Specifically

**Will you use MCP in your project?** Possible, more for demonstration purpose.

**If Yes:**
- Which MCP servers? 
    arXiv search server
    PDF/document reader server
    file system server
    web search server
    table or spreadsheet output server
- Custom servers needed? Yes. A custom server may be needed for paper-specific workflows
- Timeline to implement: basic setup: 2 weeks.

**If No:**
- Why not? MCP requires more setup effort and has a steeper learning curve, which may be too much for this project
- What instead? Function Calling + RAG

### Ecosystem Consideration

**How important is reusability?**
Not very important. It will matter more if the project is expanded.

**How important is standardization?**
Important, but not the top priority. For now, getting a working and reliable system is more important.

### Learning Curve

**How comfortable are you with your chosen approach?** __3_/5

**What do you need to learn?**
    Better function calling design
    RAG pipeline design and evaluation
    Error handling and monitoring in production
    How MCP works for future migration

**Learning resources:**
    Hands-on experimentation in personal projects
    Official documentation
    This course's support (TA, Discord)
    Example agent workflows and open-source projects


### Future-Proofing

**Will your choice scale as your project grows?**
Yes, 

**What might force you to change approaches?**
If the project grows into multiple tools, then MCP may become worth adopting.

### Biggest Insight

**Most important factor in choosing an approach:**
The balance between setup complexity and practical value.

**Biggest surprise:**
There are so many points to consider when selecting an approach.

### Action Items

**Next steps to implement your chosen approach:**
1. Define the core function-calling for the agent
2. Build a simple RAG for paper retrieval
3. Test the process on real research queries

---

## Notebook 07: Overall Reflection

**Completed:** 2026-03-30 07:57:40

### 1. How has MCP changed your view of what LLMs can do?

MCP enables LLMs to integrate into more actionable workflows. It shows that LLMs can do much more than just chatting.

### 2. Will you use MCP in your research agent?

Not at the beginning. I would start with function calling because it is easier to implement and control. 
If the project grows, or if I feel I should practice it, I would consider adding MCP later.

### 3. Most exciting MCP capability?

The most interesting part is the possibility itself. I do not know yet what kinds of use cases will be developed, and that is what makes it the most exciting.

### 4. Biggest concern about agentic systems?

Safety. Without rigorous controls, an agent could go rogue and cause serious damage.

### 5. Confidence in building MCP tools? (1-5)

**Confidence:** __2_/5

More hands-on practice with MCP setup, SDK usage, and real tool implementation would increase my confidence.

### 6. MCP vs Function Calling - which will you use?

I would use function calling first. It offers a better balance for my current needs because it is more structured than prompt engineering and easier to implement than MCP. 
MCP is attractive for future scalability and reusability, but function calling is the more practical start.

### 7. Key takeaway from this notebook?

The main takeaway is that tool use is what makes LLM systems much more practical, and different approaches fit different stages of a project. 
MCP is powerful for standardized and reusable systems.

---

## Notebook 08: Task 1 - Project Definition

**Completed:** 2026-03-31 17:06:52

### Project Clarity

**How clear is your project vision?** _4__/5

The overall idea is clear: build a regression harness that compares a baseline and a candidate LLM setup, scores the outputs, and flags quality or safety regressions.
What is still a bit fuzzy is the exact evaluation rubric, how strict the scoring should be, and how much bilingual checking I should include in the first version.

### Scope Assessment

**Is your scope realistic?** Yes

The scope is realistic if I keep it small and focused.

**What's the MVP (minimum viable product)?**

The absolute minimum is:
- a small test dataset of around 15-20 cases
- one baseline and one candidate setup
- one evaluator prompt
- structured evaluation output in JSON
- a simple report showing which cases improved, regressed, or failed

### Confidence Level

**How confident are you that you can build this?** __3_/5
I am moderately confident because the project has a clear workflow and can be broken into small steps. It also matches what we learned in the course, such as prompting, structured outputs, and multi-step workflows.
I am still uncertain because I do not have much hands-on AI engineering experience yet, and evaluator consistency may be harder to implement well than it looks at first.

### Skills Gap

**What skills do you need to learn?**
1. How to design a good evaluation rubric and structured evaluator prompt
2. How to organize the Python workflow for loading test cases, saving outputs, and generating reports

**How will you learn them?**
I will learn them by building the project step by step, reusing course patterns from the notebooks, testing small pieces first, 
and improving them through debugging and iteration instead of trying to design everything perfectly from the start.

### Feedback Integration

**What was the most valuable feedback?**

The most valuable feedback was to narrow the project into a clear MVP instead of trying to support too many models, features, or integrations at the beginning.

**What will you change based on feedback?**

I will keep version 1 simple:
- one baseline vs one candidate
- small test dataset
- a few evaluation dimensions only
- notebook or script interface instead of a full app

### Excitement Level

**How excited are you about this project?** __4_/5

What excites me most is that the project could help address real-world problems that affect businesses on a broad scale.
I can also It can show practical skills useful for jobs.

**If excitement is low, should you change the project?**

My excitement is not low, so I do not think I should change the project. 
The project fits my main job-hunting objective: it is practical, portfolio-friendly, and relevant to real business needs

### Next Steps

**What are your immediate next steps?**
1. Define the evaluation dimensions and scoring rubric
2. Create the first small test dataset
3. Build a simple baseline vs candidate comparison flow

**What will you accomplish this week?**

This week I will finish the project definition, create an initial set of test cases, 
and build a first working prototype that can run a few cases end to end and produce a simple regression report.

---

## Notebook 08: Task 2 - Architecture Design

**Completed:** 2026-03-31 17:07:44

### Architecture Clarity

**Can you explain your architecture to someone else?** Yes

I can explain the high-level flow: load test cases, run baseline output, run candidate output, evaluate both with a rubric, then generate a regression report.

### Complexity Assessment

**Is your architecture too complex?** No

For version 1, it is acceptable as long as I keep the scope small and do not add too many optional features.

**Is it too simple?** No

It is simple enough for a first version, but still complete enough to demonstrate a real workflow. 
What may still be missing is stronger retry/resume logic and more detailed evaluator validation, but those can be improved later.

### Component Dependencies

**Which component is most critical?**

The evaluator component is the most critical because the whole project depends on the quality of the scoring and comparison. 
If the evaluator is weak or inconsistent, the regression results will not be trustworthy.

**Which component is riskiest?**

The evaluator component is also the riskiest because structured judging is harder than it looks. 
The model may be inconsistent, too lenient, too strict, or return invalid JSON.

### LLM Usage

**Total LLM calls per workflow run:** _61__

This assumes about 20 test cases:
- 20 baseline generation calls
- 20 candidate generation calls
- 20 evaluation calls
- 1 final summary call

**Is this reasonable?** Yes

For a small MVP, this is reasonable. The cost and latency should still be manageable because the dataset is small and the project is for demonstration, not large-scale production.

**Could you reduce calls without losing quality?**

Yes. I could reduce calls by:
- using fewer test cases during debugging
- skipping the final summary LLM call and generating the summary with Python rules
- combining evaluation dimensions into one structured evaluator call instead of multiple evaluator calls

### Tool Selection

**Which tools/APIs are you most uncertain about?**

I am most uncertain about:
- which open-source LLM to use for stable output
- how reliable structured JSON output will be
- whether I should use a separate evaluator model or the same model family
- possible setup difficulty if I later add Claude API compatibility

**Do you have backups if a tool fails?**

Yes. My fallback strategy is:
- keep the system model-agnostic
- start with a very simple local or notebook-based workflow
- save raw outputs even if evaluation fails
- use Python-based comparison and summary logic if the LLM evaluator is unreliable
- reduce scope instead of adding more tools

### Code Organization

**How will you organize your code?**

I will organize the code into small modules:
- input handler
- generator
- evaluator
- comparator
- report generator
- config and utility files

I will also keep:
- a data folder for test cases and rubric
- a prompts folder for evaluator and summary prompts
- an outputs folder for raw outputs and reports

**Is it testable?**

Yes. I can test each component separately:
- input handler: check schema validation
- generator: verify outputs are saved correctly
- evaluator: verify JSON parsing and field extraction
- comparator: verify regression logic
- report generator: verify final markdown/CSV output

### Architecture Feedback

**Most valuable insight from the review:**

The most valuable insight was that I should design the project as a clear pipeline and keep version 1 small. 
The architecture does not need to be fancy; it needs to be reliable and understandable.

**What will you change?**

I will make these improvements:
- keep only one baseline and one candidate in version 1
- keep the dataset small
- avoid adding UI or advanced tools now
- make sure intermediate results are saved so I can resume after failures
- keep the evaluator rubric simple and structured

### Implementation Confidence

**How confident are you in implementing this?** __3_/5

I am moderately confident because the architecture is clear and modular. My confidence would increase if I build a very small end-to-end prototype first and confirm that the evaluator can return stable structured outputs.

### Biggest Architecture Challenge

The hardest part is making the evaluator reliable enough to produce useful regression judgments.

I will tackle it by:
- starting with a small and simple rubric
- using structured JSON output
- testing repeated cases to check consistency
- saving raw outputs for manual review
- simplifying the scoring if the first version is too unstable

---

## Notebook 08: Task 3 - First Prototype

**Completed:** 2026-03-31 17:08:20

### Prototype Component

**Which component did you prototype?**

I prototyped the regression evaluator / comparison logic. It compares a baseline output and a candidate output for the same test case, scores both responses, and flags whether the candidate is a regression.

**Why did you choose this component?**

I chose this component because it is the core of my project. If the evaluation logic does not work, the rest of the regression harness will not be useful. It is also the riskiest part, so it made sense to test it early.

### Implementation Experience

**How long did it take?** _3__ hours with help of Chatgpt

**Was it harder or easier than expected?**

It was difficult. It was harder than expected to design a prompt that was strict, consistent, and easy to parse.

**What was the hardest part?**

The hardest part was making the evaluator return reliable structured output while also judging multiple dimensions clearly.

### Testing Results

**Does your prototype work?** Yes

**Test results:**
- Input: one French instruction-following test case with a baseline output and a weaker candidate output
- Expected output: the evaluator should prefer the baseline and flag the candidate as a regression
- Actual output: the evaluator scored both responses, preferred the baseline, and returned a regression flag
- Success? Yes

### Code Quality

**Rate your code quality:** __3_/5

**What would you improve?**
1. Add stronger JSON validation and retry logic
2. Move the prompt and test case schema into reusable helper functions

### Lessons Learned

**What did you learn from building this?**

I learned that the core idea is feasible, but evaluator quality depends a lot on prompt design and output formatting. 
Even a simple prototype already shows how this project can detect quality regressions in a structured way.

**What will you do differently for the next component?**

For the next component, I will make the inputs more structured from the start and separate the logic into smaller helper functions instead of keeping everything in one cell.

### Prompt Engineering

**Did your prompt work well?** Yes

**Iterations needed:** _2

**What made the final prompt effective?**

The final prompt worked because it clearly defined the role, the scoring dimensions, and the exact JSON schema. 
Being specific about the output format made the result easier to parse and review.

### Model Performance

**Which model did you use?** claude-sonnet-4-5-20250929

**Was it the right choice?** Yes

It was a good choice for a first prototype because it followed instructions well and handled structured evaluation reasonably well. 
Later, I may compare it with a cheaper or open-source model.

### Integration Path

**How will this component fit into the full agent?**

This component will become the evaluation engine inside the full regression harness. 
After baseline and candidate responses are generated, this evaluator will score them and produce the regression judgment.

**What needs to happen before/after this component?**

Before this component:
- load test cases
- generate baseline output
- generate candidate output

After this component:
- aggregate results across many test cases
- create a markdown/CSV report
- highlight the most severe regressions

### Next Component

**What component will you build next?**

Next I will build the test case loader and results saver so I can run this evaluation logic on multiple cases instead of just one example.

**Estimated effort:** _4__ hours

### Confidence Boost

**How has building this prototype changed your confidence?**

Before: ___2/5
After: __3_/5

Building this prototype made the project feel more real and manageable. I now have proof that the most important component can work in a simple version.


### Biggest Win

**What are you most proud of in this prototype?**

I am most proud that I turned the project idea into a working proof of concept instead of staying at the planning stage.

### Reality Check

**Is your overall project still realistic?** Yes

**Any scope changes needed?**

Yes, I should keep version 1 smaller than I first imagined. 
I should focus on a small test set, one baseline, one candidate, and a simple structured report before adding more features.

---

## Notebook 08: Overall Course Reflection

**Completed:** 2026-03-31 17:45:00

### 1. Course Journey

**How has your understanding of LLMs changed?**

I have somewhat conflicting takeaways from this week. The knowledge I learned was more practical than I expected, and it seems relatively easy to apply to real-world projects (though it is harder to master). 
On the other hand, the actual implementation process was much more difficult. I would not have succeeded without the help of vibe coding, and I still struggled with it. I need to work harder on the fundamentals of system design, project design, and programming to catch up.

**Most valuable notebook:** N/A / All

For me, there is no single “most valuable” notebook. It is more like a toolbox: a screwdriver may be used more often than a hammer, or vice versa, 
but the most important thing is knowing how to complete the whole project—understanding what the problem is, which tool or tools should be used in each situation, and how they should be used together.

### 2. Skills Gained

**Rate your confidence (1-5):**
- Prompt engineering: __4_/5
- Structured outputs: __4_/5
- Chain-of-thought: _3__/5
- Model selection: __3_/5
- Tool use/MCP: _2__/5
- Building agents: __3_/5

### 3. Project Readiness

**How ready do you feel to build your project?** _3__/5

My readiness would increase if I get more hands-on practice connecting the pieces together in Python.

**Biggest strength you bring:**

My biggest strength is that I am strongly focused on practical value. 
I want to build something that solves a real business problem and can also become a portfolio project for job searching.

**Biggest weakness to work on:**

My main challenge is my lack of relevant background. The issue is not programming itself, but that I do not yet have a clear sense of how to choose, plan, and implement a project, so I have had to rely on LLMs for guidance.
It also takes me longer to digest what we have learned so far.

### 4. Learning Style

**What learning approach worked best?**
- Building things
- Getting feedback

The most effective approach for me is learning by doing, then correcting mistakes with feedback. 
Reading helps, but I understand much better when I try something concrete and then see what is right, wrong, and missing.

### 5. Community

**How will you use the course community?**

I will use the community to ask questions, get feedback when I am stuck.

### 6. Time Management

**Realistic weekly time commitment:** _40__ hours

**When will you work on the project?**

I will focus on this course full-time outside of job application and interview preparation.

### 7. Motivation

**What motivates you to complete this project?**

I want to build practical AI skills and a portfolio project that helps me move into AI-related work as quickly as possible.

**How will you stay motivated?**

I will stay motivated by keeping the project small, visible, and practical.I will focus on one working step at a time and treat each working component as progress.

### 8. Success Definition

**What would make this project a success for YOU?**

This project will be a success for me if:
- it works end to end on a small test set
- it clearly demonstrates useful AI engineering skills
- I can explain it confidently in an interview
- it is good enough to include in my portfolio or GitHub

### 9. After the Course

**How will you use these skills beyond the course?**

I want to use these skills to build more practical AI projects, improve my employability for junior AI roles.

### 10. Final Thoughts

**Most important lesson from Week 1:**

The learning curve is much steeper than I anticipated. 
I have tried hard, but I still often feel like I am falling behind because it takes me much longer than expected to make progress.

**Message to your future self finishing the project:**
Just keep going. Break the objective into small steps and focus on one at a time. Eventually, you will get there.

---

