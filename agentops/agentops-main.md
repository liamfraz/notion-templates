# AgentOps -- AI Agent Operations Hub

> Your entire agent fleet in one workspace. Built by a developer who runs AI agents in production daily — not a template designer who read an "AI Trends 2026" blog post.

---

## Quick Start

1. **Duplicate** this template to your Notion workspace
2. **Follow** the Setup Guide (included separately) to import databases from CSV
3. **Configure** relations between databases (Agent Registry is the hub)
4. **Delete** the sample data and start logging your own agents, tasks, and costs

> **Why AgentOps exists:** You're running agents across Anthropic, OpenAI, Google, and open-source providers. Your costs live in five different dashboards. Your prompts are scattered across repos, chat histories, and sticky notes. Your error logs are terminal output you scrolled past yesterday. AgentOps puts it all in one place — with the relationships between them intact. One agent links to its tasks, its execution logs, its prompts, and its costs. No more hunting.

---

## `// COMMAND CENTER`

The Command Center is your daily operational view. Set it up with linked database views (instructions in the Setup Guide) to see everything at a glance.

### Daily Spend Dashboard

| View | What It Shows | Database |
|------|--------------|----------|
| Today's Spend | Total cost across all agents for today, grouped by provider | Cost Tracker / Execution Logs |
| Cost Trend (7 days) | Daily spend over the past week, sorted by date | Cost Tracker |
| Budget Status | Providers approaching or exceeding monthly budget | Cost Tracker |

### Agent Performance Dashboard

| View | What It Shows | Database |
|------|--------------|----------|
| Agent Health | All agents with status, success rate, and avg duration | Agent Registry |
| Top Performers | Agents sorted by success rate descending, filtered to Active | Agent Registry |
| Task Throughput | Tasks completed today vs. queued, grouped by agent | Task Queue |

### Error Rates Dashboard

| View | What It Shows | Database |
|------|--------------|----------|
| Recent Failures | Execution logs with Status = Error, last 24 hours | Execution Logs |
| Error by Agent | Grouped count of errors per agent this week | Execution Logs |
| Error by Type | Grouped count by Error Type (rate limit, timeout, auth, hallucination) | Execution Logs |

### Quick Actions

- Queue New Task
- Register New Agent
- Log Execution
- Save Prompt
- Record Monthly Spend

> **Tip:** Pin the Command Center to your sidebar. Open it first thing in the morning to check overnight agent runs, catch any failures, and see where your spend landed.

---

## `// AGENT REGISTRY`

Your fleet inventory. Every AI agent you operate, catalogued and tracked.

### Context

The Agent Registry is the central hub of AgentOps. Every other database relates back to an agent. When you register an agent, you're creating a single source of truth for its provider, model, cost profile, and operational status. When something breaks, you start here.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Agent Name | Title | Descriptive name for the agent (e.g., "Code Review Bot", "Data Extraction Pipeline") |
| Provider | Select | Anthropic / OpenAI / Google / Meta / Mistral / Azure / Local |
| Model | Text | Specific model version (e.g., claude-opus-4-20250514, gpt-4o-2024-11-20) |
| Cost Per Run ($) | Number (currency) | Average cost per execution in AUD |
| Status | Select | Active / Paused / Deprecated / Testing / Error |
| Category | Select | Code Generation / Data Extraction / Analysis / Content / Testing / Automation / Research |
| Tasks Completed | Number | Total tasks completed lifetime |
| Success Rate (%) | Number (percent) | Percentage of tasks completed without error |
| Avg Duration (sec) | Number | Average execution time in seconds |
| Last Run | Date | Timestamp of most recent execution |
| API Key Ref | Text | Reference to where the API key is stored (NOT the key itself) |
| Notes | Text | Configuration details, quirks, known limitations |

### Linked Databases (Relations)

Each agent automatically links to:
- **Task Queue** — tasks assigned to this agent
- **Execution Logs** — run history for this agent
- **Prompt Library** — prompts used by this agent
- **Cost Tracker** — monthly spend attributed to this agent

### Recommended Views

1. **Table View** — All agents with key metrics visible. Sort by Status then Success Rate.
2. **Board View** — Group by Status. See Active vs. Paused vs. Deprecated at a glance.
3. **Board View (Provider)** — Group by Provider. See your fleet distribution across Anthropic, OpenAI, etc.
4. **Gallery View** — Agent cards showing Provider, Success Rate, and Cost Per Run. Visual fleet overview.
5. **Filtered View** — "Needs Attention" — Status is Error OR Success Rate < 80%.

### Usage Template

When registering a new agent, fill in:
- Agent Name (be specific — "Invoice Parser v2" not "Parser")
- Provider and Model (include version string)
- Category
- Status: set to Testing initially
- Notes: document the agent's purpose, input/output format, and any dependencies

> **Fleet management reality:** You will end up with more agents than you think. The Code Review Bot you built in February, the three variations of your Data Extraction Pipeline, the "quick test" agent you forgot to deprecate. The Registry keeps you honest. Review it monthly, deprecate what's dead, and update success rates from your execution logs.

---

## `// TASK QUEUE`

The work pipeline. Every task assigned to an agent, tracked from creation to completion or failure.

### Context

The Task Queue is where you assign work to your agents and track execution outcomes. Think of it as a job queue with observability. Every task has a lifecycle: Created -> Queued -> Running -> Completed/Failed. When a task fails, the error message and retry count tell you what happened and how many times the system tried.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Task ID | Title | Unique identifier (e.g., TSK-2026-0142) |
| Task Name | Text | Human-readable description of the task |
| Agent | Relation | Links to Agent Registry |
| Priority | Select | Critical / High / Medium / Low |
| Status | Select | Queued / Running / Completed / Failed / Cancelled / Retrying |
| Created | Date | When the task was created |
| Started | Date | When execution began |
| Completed | Date | When execution finished (success or failure) |
| Input Tokens | Number | Tokens sent to the model |
| Output Tokens | Number | Tokens received from the model |
| Cost ($) | Number (currency) | Total cost of this task execution in AUD |
| Error Message | Text | Error details if the task failed |
| Retry Count | Number | Number of retry attempts |

### Recommended Views

1. **Board View** — Group by Status. Your task pipeline. Drag tasks through stages.
2. **Table View** — Filter by Agent, sort by Priority then Created date.
3. **Filtered View** — "Active" — Status is Queued or Running. What's happening right now.
4. **Filtered View** — "Failed" — Status is Failed. Your error investigation queue.
5. **Calendar View** — Tasks by Created date. See workload distribution over time.

### Usage Template

When queueing a new task:
- Task ID: follow your naming convention (TSK-YYYY-NNNN)
- Task Name: be specific ("Extract invoice line items from PDF batch #47" not "Process invoices")
- Agent: select from the registry
- Priority: Critical = blocking production, High = needed today, Medium = this week, Low = when available
- Status: set to Queued

> **Debugging failed tasks:** When a task fails, check three things in order: (1) the Error Message on the task, (2) the Execution Log for that run, (3) the Agent Registry to see if the agent's overall success rate has dropped. Pattern: if one task fails, it's probably the input. If many tasks fail on the same agent, it's probably the agent or the API.

---

## `// EXECUTION LOGS`

The audit trail. Every agent run recorded with full context for debugging and analysis.

### Context

Execution Logs are your black box recorder. When an agent runs a task, the log captures timing, token usage, cost, model version, and any errors. This is where you go when something breaks. It's also where you go when something works and you want to understand why — was it the prompt version, the model, or the input quality?

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Log ID | Title | Unique identifier (e.g., LOG-2026-03-28-0001) |
| Agent | Relation | Links to Agent Registry |
| Task | Relation | Links to Task Queue |
| Timestamp | Date | When the execution started |
| Duration (sec) | Number | Total execution time in seconds |
| Status | Select | Success / Error / Timeout / Rate Limited / Partial |
| Input Tokens | Number | Tokens sent to the model |
| Output Tokens | Number | Tokens received from the model |
| Cost ($) | Number (currency) | Cost of this execution in AUD |
| Model | Text | Exact model version used |
| Error Type | Select | None / Rate Limit / Timeout / Auth Failure / Context Length / Hallucination / API Error / Unknown |
| Stack Trace | Text | Error details and stack trace for failed executions |
| Session ID | Text | Session identifier for grouping related executions |

### Recommended Views

1. **Table View** — Sort by Timestamp descending. Most recent runs first. This is your default view.
2. **Filtered View** — "Errors Only" — Status is not Success. Your debugging queue.
3. **Board View** — Group by Status. See the ratio of successes to failures at a glance.
4. **Board View (Error Type)** — Group by Error Type. Spot systemic issues (e.g., too many rate limits = you need backoff logic).
5. **Filtered View** — "By Agent" — Filter to a specific agent. See its full execution history.
6. **Filtered View** — "Expensive Runs" — Cost > $0.50. Catch unexpectedly costly executions.

### Usage Template

Logs should ideally be created programmatically (see Setup Guide for Notion API patterns). For manual logging:
- Log ID: follow the convention LOG-YYYY-MM-DD-NNNN
- Link to the Agent and Task
- Record actual token counts from the API response
- Always capture Error Type and Stack Trace for failures — future you will thank present you

> **Log hygiene:** Execution logs grow fast. If you're running 50+ agent tasks per day, you'll have 1500+ log entries per month. Use filtered views aggressively. Archive logs older than 90 days to a separate database or export to CSV monthly. The logs are valuable for trend analysis but deadly for Notion performance if you let them grow unchecked.

---

## `// PROMPT LIBRARY`

Your prompt engineering lab. Every prompt saved, versioned, and tracked for performance.

### Context

Prompts are code. They deserve version control, testing, and performance tracking just like any other code artifact. The Prompt Library stores every prompt used by your agents, tracks which version is live, and records success rates so you know which prompts actually work vs. which ones you assumed work because you tested them once.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | Descriptive name (e.g., "Code Review System Prompt v3") |
| Agent | Relation | Links to Agent Registry (which agent uses this prompt) |
| Category | Select | System Prompt / Task Prompt / Few-Shot Example / Chain-of-Thought / Output Schema / Guard Rail |
| Prompt Text | Text | The full prompt content |
| Version | Text | Version identifier (e.g., v1.0, v2.1) |
| Success Rate (%) | Number (percent) | Percentage of successful executions using this prompt |
| Use Count | Number | How many times this prompt has been used |
| Last Used | Date | Most recent execution using this prompt |
| Tags | Multi-select | retrieval / generation / analysis / code / summarisation / extraction / classification |
| Notes | Text | Change log, known issues, performance observations |

### Recommended Views

1. **Table View** — Sort by Agent then Version. See all prompts organised by agent.
2. **Board View** — Group by Category. See the distribution of prompt types.
3. **Filtered View** — "Top Performers" — Success Rate > 90%, sorted by Use Count descending.
4. **Filtered View** — "Needs Work" — Success Rate < 75%. Prompts that need iteration.
5. **Gallery View** — Prompt cards showing Name, Agent, Version, and Success Rate.

### Usage Template

When saving a new prompt:
- Name: include the agent name and version (e.g., "Invoice Parser System Prompt v2")
- Category: classify accurately — System Prompt vs. Task Prompt matters for debugging
- Prompt Text: paste the full prompt, including any formatting, delimiters, or XML tags
- Version: increment when you change anything. v1.0 -> v1.1 for minor tweaks, v1.0 -> v2.0 for rewrites
- Notes: document what changed and why

> **Prompt versioning discipline:** Never overwrite a prompt. Create a new version. When v3 of your system prompt tanks your success rate, you need v2 to roll back to. The Version field and Notes field together form your prompt changelog. Treat it like git — cheap to create versions, expensive to lose history.

---

## `// COST TRACKER`

Monthly spend across every provider and agent. Your financial control panel.

### Context

AI APIs charge per token. Tokens add up. The Cost Tracker aggregates your spend by month, provider, and agent so you can set budgets, track burn rate, and catch overruns before they become invoice surprises. This is the database your CFO (or your bank account) will thank you for.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Month | Title | Month and year (e.g., "2026-03") |
| Provider | Select | Anthropic / OpenAI / Google / Meta / Mistral / Azure / Local |
| Agent | Relation | Links to Agent Registry |
| API Calls | Number | Total number of API calls for this period |
| Input Tokens | Number | Total input tokens consumed |
| Output Tokens | Number | Total output tokens generated |
| Cost ($) | Number (currency) | Total spend in AUD for this period |
| Budget ($) | Number (currency) | Monthly budget allocation in AUD |
| % of Budget | Number (percent) | Cost / Budget as a percentage |
| Model | Text | Primary model used |
| Notes | Text | Context on spend (e.g., "spike due to batch reprocessing of Q1 invoices") |

### Recommended Views

1. **Table View** — Sort by Month descending, then Provider. Current month's spend at the top.
2. **Board View** — Group by Provider. See spend distribution across providers.
3. **Filtered View** — "Over Budget" — % of Budget > 90%. Catch overruns early.
4. **Filtered View** — "Current Month" — Month is this month. Your live spend view.
5. **Chart View** — If using Notion charts, plot Cost by Month to see spend trends.

### Usage Template

At the start of each month:
- Create one row per provider per agent (or per provider if you want a simpler view)
- Set the Budget based on your allocation
- Update Cost, API Calls, and Token counts weekly or as available from provider dashboards

At month end:
- Verify totals against provider invoices
- Add Notes explaining any anomalies
- Use the data to adjust next month's budgets

> **Cost discipline:** The biggest cost surprise in AI ops is not a single expensive call — it's a cheap call running 10,000 times because someone forgot to add a dedup check. Track API Calls alongside Cost. If your API call count doubled but your task count didn't, something is retrying silently.

---

## `// DATABASE RELATIONSHIPS MAP`

Here is how all databases connect:

```
                    AGENT REGISTRY (Central Hub)
                           |
          +--------+-------+-------+--------+
          |        |               |        |
      Task Queue  Execution    Prompt    Cost
                   Logs       Library   Tracker
          |        |
          +--------+
          (Task links to its Execution Logs)
```

**Key Relations:**
- Every database links back to **Agent Registry** (many-to-one)
- **Task Queue** entries generate **Execution Logs** when they run
- **Prompt Library** entries link to the **Agent** that uses them
- **Cost Tracker** aggregates spend per **Agent** per month
- **Execution Logs** link to both the **Agent** and the specific **Task**

---

## `// FORMULAS & AUTOMATIONS`

### Useful Notion Formulas

**Cost Per 1K Tokens (Execution Logs):**
```
if(prop("Input Tokens") + prop("Output Tokens") > 0, round(prop("Cost ($)") / ((prop("Input Tokens") + prop("Output Tokens")) / 1000) * 100) / 100, 0)
```

**Budget Remaining (Cost Tracker):**
```
prop("Budget ($)") - prop("Cost ($)")
```

**Budget Alert (Cost Tracker):**
```
if(prop("% of Budget") >= 100, "OVER BUDGET", if(prop("% of Budget") >= 80, "WARNING", "OK"))
```

**Error Rate (Agent Registry — calculated from Execution Logs rollup):**
```
if(prop("Tasks Completed") > 0, round((1 - prop("Success Rate (%)") / 100) * 100), 0)
```

**Task Duration (Task Queue):**
```
if(and(prop("Started") != empty, prop("Completed") != empty), dateBetween(prop("Completed"), prop("Started"), "minutes"), 0)
```

### Recommended Automations (Notion Automations)

1. **When** a Task Status changes to "Failed" → **Send notification** with the Error Message
2. **When** Cost Tracker % of Budget exceeds 80% → **Send notification** to review spend
3. **When** a new Task is created → **Set** Status to "Queued" and Created to today
4. **When** Agent Status changes to "Error" → **Send notification** to investigate
5. **When** an Execution Log is created with Status "Rate Limited" → **Send notification** to check rate limit configuration

---

## `// TEMPLATES WITHIN DATABASES`

### New Agent Registration Template
Pre-filled template for new agents:
- Status: Testing
- Cost Per Run: 0 (update after first runs)
- Success Rate: 0% (calculated after first 10 runs)
- Prompt in Notes: "Document this agent's purpose, input format, output format, dependencies, and any rate limits."

### New Task Template
Pre-filled template for new tasks:
- Status: Queued
- Priority: Medium (change as needed)
- Created: Today
- Retry Count: 0
- Prompt in Task Name: "Be specific. Include the data source, expected output, and any constraints."

### Execution Log Template
Pre-filled template:
- Status: Success (change if error)
- Error Type: None (change if error)
- Prompt in Stack Trace: "Paste the full error output. Include the API response body if available."

### Monthly Cost Entry Template
Pre-filled template:
- Month: Current month
- Budget: $0 (set your allocation)
- Prompt in Notes: "Record any context for spend anomalies — batch jobs, retries, model upgrades, testing spikes."

---

## `// OPERATIONAL PLAYBOOKS`

<details>
<summary><strong>When an agent starts failing</strong></summary>

1. Check the **Execution Logs** filtered to that agent, sorted by Timestamp descending
2. Identify the Error Type — is it Rate Limit, Timeout, Auth, or something else?
3. Check the **Task Queue** for failed tasks — is it one task or many?
4. If many tasks fail: check the **Agent Registry** for the agent's API Key Ref and verify the key is still valid
5. If one task fails repeatedly: check the input data and the **Prompt Library** for recent prompt changes
6. Update the Agent Status to "Error" until resolved
7. Document the root cause in the Execution Log's Stack Trace field

</details>

<details>
<summary><strong>Monthly cost review process</strong></summary>

1. Open the **Cost Tracker** filtered to the current month
2. Compare actual spend vs. budget for each provider
3. Check which agents drove the most cost — sort by Cost descending
4. Review API Call counts — high call counts with low task counts indicate retries or loops
5. Check token ratios — if Output Tokens >> Input Tokens, your agents might be over-generating
6. Adjust next month's budgets based on actuals
7. Archive completed month's execution logs to CSV

</details>

<details>
<summary><strong>Prompt iteration workflow</strong></summary>

1. Identify the prompt to improve (Success Rate < target in **Prompt Library**)
2. Create a new version (v1.0 → v1.1) — never overwrite the existing version
3. Run 10 test tasks with the new prompt version
4. Check Execution Logs for the test tasks — compare Success Rate, Duration, and Cost
5. If improved: update the agent to use the new version and mark the old version in Notes
6. If worse: keep the old version active and document what you tried in the new version's Notes
7. Update the Prompt Library entry with new Success Rate and Use Count

</details>

<details>
<summary><strong>Onboarding a new agent</strong></summary>

1. Register the agent in the **Agent Registry** with Status: Testing
2. Create the agent's system prompt in the **Prompt Library** as v1.0
3. Queue 5-10 test tasks in the **Task Queue** with diverse inputs
4. Review **Execution Logs** for the test runs — check success rate, duration, cost, and output quality
5. If success rate > 80% across test tasks: change Status to Active
6. Set up a monthly row in **Cost Tracker** with the budget allocation
7. Document the agent's operational parameters in the Registry Notes field

</details>

---

## `// RESOURCES`

### Notion API Integration (Advanced)

If you want to automate log entries, you can POST execution data to Notion via the API. Basic pattern:

```python
# Example: Log an execution via Notion API
import os
import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = "your-execution-logs-database-id"

requests.post(
    "https://api.notion.com/v1/pages",
    headers={
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    },
    json={
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Log ID": {"title": [{"text": {"content": "LOG-2026-03-28-0042"}}]},
            "Duration (sec)": {"number": 12.4},
            "Status": {"select": {"name": "Success"}},
            "Cost ($)": {"number": 0.08}
        }
    }
)
```

### External Tools That Pair Well

- **Langfuse** — open-source observability for LLM apps (use for detailed tracing, use AgentOps for the business view)
- **Notion API** — automate log entries from your agent pipelines
- **n8n / Make** — build webhook flows that create Notion database entries on agent completion
- **Grafana** — if you want time-series dashboards, export Cost Tracker data for visualisation

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 2026 | Initial release |

---

> **Built by a developer who runs agents in production.** AgentOps was designed from real operational pain — not from a product requirements doc. Every database, every property, every view exists because I needed it when debugging a failing agent at midnight or explaining a cost spike to myself on invoice day. If something doesn't work for your workflow, reach out and I'll fix it.
