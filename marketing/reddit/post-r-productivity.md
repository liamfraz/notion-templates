# r/productivity Post

**Subreddit:** r/productivity
**Title:** The AI agent workflow Notion template that manages my 12 side projects — full breakdown

---

## Post Body

I run 12 active AI-powered projects — content pipelines, automation flows, client tools. For a long time I managed all of it by checking Anthropic's billing dashboard once a month, wincing, and moving on.

Then one of my automation flows silently started failing. I found out three weeks later when a client noticed. I'd been paying for Claude API calls returning errors on every run with zero visibility.

That was enough. Here's the Notion system I built:

---

**Stage 1 — Inbox Capture**

Everything new goes into the Task Queue. New project requirement, new agent to spin up, new prompt to test — it gets logged immediately with its assigned agent, a priority level (P1 emergency → P4 backlog), and an estimated token cost.

Nothing lives in my head or Slack DMs. If it's not in the queue, it doesn't exist.

---

**Stage 2 — AI Triage (Agent Registry)**

Every AI agent I run — Claude extractors, GPT summarisers, Gemini classifiers, n8n flows — catalogued with:
- Provider and model version
- Cost per run (from token usage)
- Success rate (rolled up from Execution Logs)
- Operational status (Active / Degraded / Deprecated)

When a task comes in, I match it to the right agent based on cost and success rate — not gut feel. The data decides.

---

**Stage 3 — Priority Queue**

The Task Queue board view groups tasks by status (Queued → Running → Complete → Failed) and sorts by priority within each column. I can see at a glance: what's waiting, what's running, what broke.

Every completed execution logs its cost automatically via a linked Execution Log entry. Over time the queue builds a picture of where my compute budget actually goes.

---

**Stage 4 — Project Tracker (Cost + Performance)**

Two dashboards close the loop:

*Daily Spend* — rolled up from execution logs, broken down by provider and agent. I set monthly budgets per provider. When usage hits 80% of budget, it shows in orange.

*Agent Performance* — success rates over the past 30 days, per agent. If a rate drops below 85%, something changed — prompt drift, API update, bad input data. I catch it in days, not weeks.

The Prompt Library ties in too — each prompt tracks success rate across all executions, so I know which prompts are reliable vs. which are causing silent failures.

---

It's a Notion template: https://gumroad.com/l/agentops-notion-template — 5 linked databases, cost formulas, and a setup guide. $29 AUD, free Lite version available if you just want the Agent Registry and Prompt Library.

If you're running AI workflows without this kind of tracking, you're flying blind. Happy to answer questions.
