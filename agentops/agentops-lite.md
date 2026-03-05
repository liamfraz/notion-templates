# AgentOps Lite -- AI Session & Prompt Tracker

> A free starter template for tracking your AI sessions and building a prompt library. Want the full dashboard with automation tracking, cost analytics, code review checklists, and tech debt management? Upgrade to AgentOps Pro.

---

## `// AI SESSION LOG`

Track every meaningful AI interaction. Understand what works and what doesn't.

### How to Use

After each AI session, add a row to the table below with:
- What tool you used (Claude Code, ChatGPT, Copilot, etc.)
- What you asked it to do
- How long it took
- Whether it worked (Success / Partial / Failed)
- Quality rating from 1-5
- One sentence on what you learned

### Session Log

| Date | Tool | Task | Duration | Outcome | Quality | Learnings |
|------|------|------|----------|---------|---------|-----------|
| 2026-03-01 | Claude Code | Refactored database query layer | 45 min | Success | 5 | Providing the schema as context made all the difference |
| 2026-03-02 | ChatGPT | Generated email templates | 15 min | Partial | 3 | Too generic on first pass -- needed specific examples |
| 2026-03-03 | Claude Code | Built API error handling | 30 min | Success | 4 | The prompt from my library saved 10 min of back-and-forth |

> **Tip:** Convert this table to a Notion database for filtering and sorting. Select the table, then click "Turn into database."

### Quality Rating Guide

```
5 = AI nailed it, significant time saved
4 = Good result, minor edits only
3 = Usable but needed heavy editing
2 = Mostly had to rewrite the output
1 = Complete waste of time
```

---

## `// PROMPT LIBRARY`

Save prompts that work. Stop rewriting the same instructions every session.

### Your Prompts

| Name | Category | Tool | Rating | Use Count |
|------|----------|------|--------|-----------|
| Code Review Agent | System Prompt | Claude Code | 5 | 42 |
| Test Generator | Task Prompt | Claude Code | 4 | 28 |
| Expression Builder | Task Prompt | ChatGPT | 4 | 19 |

> **Tip:** Store the full prompt text in the page body of each row when you convert to a database.

### Starter Prompts

Here are 3 high-quality prompts to get you started:

**1. Code Review Agent** (System Prompt)
```
Review this code for: 1) Security issues (hardcoded secrets, injection)
2) Logic errors and edge cases 3) Performance problems (N+1 queries)
4) API hallucinations -- verify every import actually exists
5) Missing error handling. List each issue with severity and fix.
```

**2. Test Case Generator** (Task Prompt)
```
Generate test cases covering: 1) Happy path with typical inputs
2) Edge cases (empty arrays, null, boundary values) 3) Error cases
(invalid input, network failures). Use the existing test framework.
Each test name should read like a sentence.
```

**3. Documentation Writer** (Task Prompt)
```
Write docs for this code: 1) One-line summary 2) A "Why" section
explaining the design decision 3) Usage examples with realistic data
4) Document edge cases and error states 5) Under 100 lines.
Write like you're explaining to a smart colleague.
```

---

## `// BASIC COST TRACKER`

Keep a running tally of what you're spending on AI tools.

| Month | Anthropic | OpenAI | Google | Other | Total | Budget |
|-------|-----------|--------|--------|-------|-------|--------|
| Jan 2026 | $96.50 | $7.85 | $8.40 | $0 | $112.75 | $150.00 |
| Feb 2026 | $89.30 | $7.20 | $12.60 | $0 | $109.10 | $150.00 |
| Mar 2026 | -- | -- | -- | -- | -- | $150.00 |

### Budget Rules (Keep It Simple)

1. Set a monthly total budget before the month starts
2. Check at mid-month -- are you on track?
3. If over 75% at mid-month, slow down on expensive models
4. Use cheaper models (Gemini Flash, Haiku) for simple tasks

---

## `// WHAT'S IN THE FULL VERSION?`

AgentOps Pro includes everything above plus:

- **Command Center** -- dashboard with key metrics and alerts
- **Automation Registry** -- track Power Automate, n8n, Zapier, and Make flows
- **Detailed API Cost Analytics** -- per-provider, per-model cost tracking with budget alerts
- **Code Review Checklist** -- 20-item QA checklist specifically for AI-generated code
- **Tech Debt Log** -- track and triage technical debt from AI-generated code
- **Tool Registry** -- catalog your entire stack (MCP servers, CLIs, APIs, libraries)
- **Monthly Ops Report Template** -- structured monthly review format
- **7 pre-built CSV databases** with realistic sample data
- **Database relations** -- linked views connecting sessions to prompts, flows to costs
- **Setup guide** with step-by-step database configuration

[Get AgentOps Pro ->](YOUR_GUMROAD_LINK_HERE)

---

*Built for developers who ship with AI.*
