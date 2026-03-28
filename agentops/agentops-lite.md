# AgentOps Lite -- AI Agent Operations Essentials

> A free starter template for developers running AI agents. Track your agents, version your prompts, and monitor basic costs in one workspace.

> **Want the full version?** AgentOps (the complete package) includes Task Queue, Execution Logs, 3 operational dashboards, full database relations, Notion formulas, automation recipes, and operational playbooks. [Get AgentOps →]

---

## Quick Start

1. Duplicate this page to your Notion workspace
2. Delete the sample data and start entering your own agents
3. Create the three databases below from the included CSV files (or build them manually)

---

## Agent Registry

Your fleet inventory. Every AI agent catalogued with its provider, model, and operational status.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Agent Name | Title | Descriptive name for the agent |
| Provider | Select | Anthropic / OpenAI / Google / Meta / Mistral / Azure / Local |
| Model | Text | Specific model version (e.g., claude-opus-4-20250514) |
| Cost Per Run ($) | Number (currency) | Average cost per execution in AUD |
| Status | Select | Active / Paused / Deprecated / Testing / Error |
| Category | Select | Code Generation / Data Extraction / Analysis / Content / Testing / Automation / Research |
| Tasks Completed | Number | Total tasks completed lifetime |
| Success Rate (%) | Number (percent) | Percentage of tasks completed without error |
| Notes | Text | Configuration details, quirks, known limitations |

### Sample Data

| Agent Name | Provider | Model | Cost Per Run ($) | Status | Success Rate (%) |
|-----------|----------|-------|-----------------|--------|-----------------|
| Code Review Bot | Anthropic | claude-opus-4-20250514 | $0.12 | Active | 94% |
| Data Extraction Pipeline | OpenAI | gpt-4o-2024-11-20 | $0.08 | Active | 91% |
| Research Summariser | Google | gemini-2.5-pro | $0.05 | Active | 88% |

### Recommended Views

- **Table View** — All agents with key metrics visible. Sort by Status.
- **Board View** — Group by Status. See Active vs. Paused vs. Deprecated at a glance.

---

## Prompt Library

Save, version, and track performance of your agent prompts.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | Descriptive name including version |
| Agent | Text | Which agent uses this prompt |
| Category | Select | System Prompt / Task Prompt / Few-Shot Example / Chain-of-Thought / Output Schema / Guard Rail |
| Prompt Text | Text | The full prompt content |
| Version | Text | Version identifier (e.g., v1.0, v2.1) |
| Success Rate (%) | Number (percent) | Success rate when using this prompt |
| Use Count | Number | Times this prompt has been used |
| Last Used | Date | Most recent execution using this prompt |
| Notes | Text | Change log and observations |

### Sample Data

| Name | Agent | Category | Version | Success Rate (%) |
|------|-------|----------|---------|-----------------|
| Code Review System Prompt v3 | Code Review Bot | System Prompt | v3.0 | 94% |
| Invoice Data Extraction v2 | Data Extraction Pipeline | Task Prompt | v2.1 | 91% |
| Research Summary Template v1 | Research Summariser | System Prompt | v1.2 | 88% |

### Recommended Views

- **Table View** — Sort by Agent then Version.
- **Board View** — Group by Category.

---

## Cost Tracker (Basic)

Monthly spend overview by provider.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Month | Title | Month and year (e.g., "2026-03") |
| Provider | Select | Anthropic / OpenAI / Google / Meta / Mistral / Azure / Local |
| API Calls | Number | Total API calls for the period |
| Cost ($) | Number (currency) | Total spend in AUD |
| Budget ($) | Number (currency) | Monthly budget allocation in AUD |
| Notes | Text | Context on spend patterns |

### Sample Data

| Month | Provider | API Calls | Cost ($) | Budget ($) |
|-------|----------|-----------|----------|------------|
| 2026-03 | Anthropic | 3420 | $187.50 | $200.00 |
| 2026-03 | OpenAI | 2180 | $124.30 | $150.00 |
| 2026-03 | Google | 1560 | $62.40 | $80.00 |

### Recommended Views

- **Table View** — Sort by Month descending, then Provider.
- **Filtered View** — Current month only.

> **Monthly habit:** At the end of each month, verify your Cost Tracker totals against your provider invoices. Five minutes of reconciliation prevents billing surprises.

---

## Setting Up Relations

To connect your databases:

1. In the **Prompt Library** database, add a **Relation** property pointing to **Agent Registry**
2. For each prompt, select the relevant agent

This means when you open an agent page, you'll see all its prompts linked automatically.

---

## What You're Missing (Full AgentOps)

AgentOps Lite covers the essentials. The full AgentOps template adds:

| Feature | Why It Matters |
|---------|---------------|
| Task Queue | Track every task assigned to agents with priority, status, token counts, cost, and error handling |
| Execution Logs | Full audit trail of every agent run — timestamps, duration, token usage, cost, error types, and stack traces |
| Daily Spend Dashboard | See today's spend across all agents and providers in one view |
| Agent Performance Dashboard | Agent health, success rates, throughput, and top performers at a glance |
| Error Rates Dashboard | Recent failures grouped by agent and error type — spot systemic issues fast |
| Full Database Relations | Complete relationship map connecting all 5 databases with cross-references |
| Detailed Cost Tracker | Per-agent, per-model cost breakdowns with budget alerts and % of budget tracking |
| Notion Formulas | Cost per 1K tokens, budget alerts, error rate calculations, task duration formulas |
| Automation Recipes | Failure alerts, budget warnings, status change notifications, error escalation |
| Operational Playbooks | Step-by-step guides for agent failures, monthly cost reviews, prompt iteration, and agent onboarding |
| Notion API Integration | Code examples for automating log entries from your agent pipelines |

[Get the full AgentOps template →]

---

> **Built by a developer who runs agents in production.** Every field in this template exists because it solved a real operational problem. AgentOps Lite gives you the foundation — the full version gives you the visibility.
