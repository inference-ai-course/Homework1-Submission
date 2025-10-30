# Class 1 Project: Prompt Engineering and Structured Outputs

This project guides you through advanced prompt engineering techniques, focusing on summarization, prompt frameworks, and structured output formats for LLMs.

## Project Tasks

### 1. Interact with ChatGPT
- **Goal:** Summarize a motivational passage in 5 short bullet points, using simple language for a high school student.
- **Example Passage:**
  > Life isn’t just about the big milestones—it’s built on the quiet victories we often overlook. Waking up early, choosing kindness, finishing a task you’ve been avoiding—these are the small wins that shape our momentum. They remind us that progress isn’t always loud. It’s steady, subtle, and deeply personal. Celebrate them. Stack them. Let them carry you forward.

### 2. CO-STAR Rewrite
- **Goal:** Rephrase your prompt using the [CO-STAR](https://promptingguide.ai/techniques/costar) framework:
  - **Context:** What is the background or situation?
  - **Objective:** What do you want the model to do?
  - **Style:** How should the response be written?
  - **Tone:** What emotional feel should the response have?
  - **Audience:** Who is the response for?
  - **Response format:** What should the output look like?

#### Example CO-STAR Breakdown
- **Context:** You are given a short motivational passage about how small, everyday actions contribute to progress in life.
- **Objective:** Summarize the main ideas in exactly five bullet points, keeping the meaning accurate and easy to understand.
- **Style:** Use plain, everyday language. Keep each bullet short and clear. Avoid complex words or long sentences.
- **Tone:** Positive, encouraging, and relatable.
- **Audience:** High school students.
- **Response format:** Five concise bullet points, each capturing one key idea. No extra commentary or analysis.

### 3. Structured Output (JSON)
- **Goal:** Learn to request outputs in JSON format for clarity and downstream use.
- **Example:**
```json
{
  "Context": "You are given a short motivational passage about how small, everyday actions contribute to progress in life.",
  "Objective": "Summarize the main ideas of the passage in exactly five bullet points, keeping the meaning accurate and easy to understand.",
  "Style": "Use plain, everyday language. Keep each bullet short and clear. Avoid complex words or long sentences.",
  "Tone": "Positive, encouraging, and relatable — something that feels friendly and motivating.",
  "Audience": "High school students who may not have advanced vocabulary but can connect with simple, real-life examples.",
  "ResponseFormat": "Five concise bullet points, each capturing one key idea from the passage. No extra commentary or analysis."
}
```

### 4. XML Output & Nesting
- **Goal:** Practice rewriting your prompt for XML output, including nested XML for more complex outputs or logic.
- **Example:**
```xml
<Prompt name="SummarizeSmallWins_CO-STAR" version="1.0">
  <Context>
    <Description>You are given a short motivational passage about how small, everyday actions build progress in life.</Description>
  </Context>
  <Objective>
    <Goal>Summarize the passage into exactly five bullet points capturing the main ideas.</Goal>
  </Objective>
  <Style>
    <Vocabulary level="plain">Use everyday words.</Vocabulary>
    <Sentences length="short">Keep each bullet brief and clear.</Sentences>
    <Avoid>
      <Item>Complex words</Item>
      <Item>Long sentences</Item>
    </Avoid>
  </Style>
  <Tone>
    <Primary>Positive</Primary>
    <Secondary>Encouraging</Secondary>
    <Tertiary>Relatable</Tertiary>
  </Tone>
  <Audience>
    <Group>High school students</Group>
    <Assumptions>May not know advanced vocabulary but connect with simple, real-life examples.</Assumptions>
  </Audience>
  <ResponseFormat>
    <Type>bulleted-list</Type>
    <Length exactItems="5"/>
    <ItemRules>
      <Rule>One key idea per bullet.</Rule>
      <Rule>No extra commentary or analysis.</Rule>
    </ItemRules>
    <OutputSchema>
      <BulletedList count="5">
        <Bullet index="1">{idea_1}</Bullet>
        <Bullet index="2">{idea_2}</Bullet>
        <Bullet index="3">{idea_3}</Bullet>
        <Bullet index="4">{idea_4}</Bullet>
        <Bullet index="5">{idea_5}</Bullet>
      </BulletedList>
    </OutputSchema>
    <Validation>
      <Check id="count" condition="BulletedList/Bullet count == 5" onFail="revise"/>
      <Check id="simplicity" condition="vocabulary == plain AND sentences == short" onFail="simplify"/>
      <Check id="no_extras" condition="no extra commentary" onFail="remove_extras"/>
    </Validation>
  </ResponseFormat>
  <Input>
    <Passage placeholder="{text_to_summarize}"/>
  </Input>
  <Instructions>
    Produce only the BulletedList defined in OutputSchema, replacing placeholders with the five key ideas from the passage.
  </Instructions>
</Prompt>
```

---

## Learning Outcomes
- Practice prompt engineering for summarization and clarity
- Apply the CO-STAR framework to structure prompts
- Request and interpret structured outputs in JSON and XML
- Understand how to specify output schemas and validation rules for LLMs

Work through each section in the notebook and use the examples as templates for your own prompts and outputs.
