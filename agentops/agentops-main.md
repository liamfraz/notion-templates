# AgentOps -- AI Agent & Automation Dashboard

> Track your AI sessions, automation flows, API costs, and prompt library in one workspace. Built for developers who ship with AI.

---

## `// QUICK START`

1. **Import this page** into your Notion workspace
2. **Create databases** from the CSV files in the `/databases` folder (see SETUP-GUIDE.md)
3. **Link databases** to the views below using Notion's linked database feature
4. **Start logging** -- add your first AI session today

**Estimated setup time:** 15 minutes

---

## `// COMMAND CENTER`

Your operational overview. Pin this page to your sidebar.

### Key Metrics (Update Weekly)

| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| AI Sessions | 12 | 9 | Up |
| Total Cost | $24.80 | $18.50 | Up |
| Success Rate | 91% | 85% | Up |
| Active Flows | 6 | 6 | Stable |
| Flow Errors | 2 | 5 | Down |
| Prompts Used | 8 | 6 | Up |

### Quick Actions

- [ ] Log today's AI sessions
- [ ] Check automation flow errors
- [ ] Review weekly API spend vs budget
- [ ] Update prompt library with new patterns
- [ ] Triage tech debt backlog

### Active Alerts

> **Cost Alert:** Anthropic API at 89% of monthly budget ($89.30 / $100.00)
> **Flow Error:** Lead Scoring Pipeline paused -- Clearbit API key expired
> **Tech Debt:** 3 open high-severity items need attention

---

## `// AI SESSIONS`

Log every session with an AI tool. The goal: understand where AI saves you time and where it wastes it.

### How to Log a Session

After each meaningful AI interaction, add a row with:

```
Date | Tool | Task (what you asked for)
Duration | Tokens | Cost | Model
Outcome: Success / Partial / Failed
Quality: 1-5 (would you do it again this way?)
Key Learnings (one sentence -- what did you learn?)
```

### Session Quality Guide

| Rating | Meaning | Action |
|--------|---------|--------|
| 5 | AI nailed it, saved significant time | Save the prompt to library |
| 4 | Good result with minor edits needed | Note what could improve |
| 3 | Usable but required heavy editing | Consider different approach |
| 2 | Mostly rewrote the output | Log what went wrong |
| 1 | Complete waste of time | Avoid this task/tool combo |

### Linked Database: AI Sessions

> *Create a linked database view here pointing to the AI Sessions database*
> Recommended views:
> - **Recent** -- sorted by date descending, last 14 days
> - **By Tool** -- grouped by Tool column
> - **Failed** -- filtered to Outcome = Failed or Partial
> - **Best Hits** -- filtered to Quality >= 4, sorted by date

### Session Insights Template

Copy this at the end of each week:

```
## Week of [DATE]

Sessions: [COUNT]
Total cost: $[AMOUNT]
Avg quality: [SCORE]/5
Top tool: [TOOL] ([COUNT] sessions)

Best session: [DESCRIPTION]
Worst session: [DESCRIPTION]
Pattern noticed: [INSIGHT]
```

---

## `// PROMPT LIBRARY`

Your curated collection of prompts that actually work. Version them, rate them, reuse them.

### Prompt Categories

| Category | Description | Use When |
|----------|-------------|----------|
| System Prompt | Sets agent behavior and rules | Starting a new AI session |
| Task Prompt | Single-task instruction | Asking AI to do one specific thing |
| Chain | Multi-step orchestrated flow | Complex tasks needing phases |
| Template | Fill-in-the-blank structure | Repeatable formats (commits, PRs, docs) |
| Instruction | Behavioral modifier | Adjusting AI behavior mid-session |

### Linked Database: Prompt Library

> *Create a linked database view here pointing to the Prompt Library database*
> Recommended views:
> - **Top Rated** -- filtered to Rating >= 4, sorted by Use Count descending
> - **By Category** -- grouped by Category column
> - **Recently Used** -- sorted by Last Used descending
> - **By Tool** -- grouped by Tool column

### Prompt Versioning Convention

When you improve a prompt, bump the version:

```
1.0 -> 1.1  Minor tweak (wording change, added example)
1.1 -> 1.2  Moderate change (new rule, restructured section)
1.x -> 2.0  Major rewrite (fundamentally different approach)
```

Keep the old version in the Notes field so you can revert if the new version underperforms.

### Creating Good Prompts

```
BAD:  "Write me some tests"
GOOD: "Generate test cases covering: 1) Happy path with typical
       inputs 2) Edge cases (empty arrays, null, boundary values)
       3) Error cases (invalid input, network failures). Use the
       existing test framework. Each test name reads like a sentence."
```

Key principles:
- **Be specific** about format, structure, and constraints
- **Include anti-patterns** ("don't do X") for things AI gets wrong
- **Add verification steps** ("after generating, check that...")
- **Reference the codebase** ("follow the patterns in src/utils/")

---

## `// AUTOMATION REGISTRY`

Every automated workflow, across every platform, in one place.

### Status Definitions

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| Active | Running in production | Monitor errors |
| Paused | Intentionally stopped | Document why in Notes |
| Error | Broken, needs fix | Fix within 24 hours |
| Development | Being built or tested | Track in tech debt if stalled |

### Linked Database: Automation Flows

> *Create a linked database view here pointing to the Automation Flows database*
> Recommended views:
> - **All Active** -- filtered to Status = Active, sorted by Last Run
> - **Needs Attention** -- filtered to Status = Error OR Success Rate < 90%
> - **By Platform** -- grouped by Platform column
> - **Run Stats** -- table view showing Run Count, Error Count, Success Rate

### Flow Health Check (Monthly)

Run through every active flow monthly:

```
- [ ] Last run within expected schedule?
- [ ] Success rate above 95%?
- [ ] Error count trending down?
- [ ] API keys and credentials still valid?
- [ ] Monitoring/alerting configured?
- [ ] Owner still on the team?
- [ ] Documentation up to date?
```

### When a Flow Breaks

```
1. Check error logs for the specific failure
2. Determine: transient (retry) or systemic (fix)?
3. If systemic: set status to Error, create tech debt item
4. Fix and test with sample data before reactivating
5. Update the flow's Notes with what broke and why
6. If >3rd failure this month: consider architecture change
```

---

## `// API COST TRACKER`

Know exactly what your AI tools cost. No surprises at the end of the month.

### Linked Database: API Costs

> *Create a linked database view here pointing to the API Costs database*
> Recommended views:
> - **Current Month** -- filtered to current month
> - **By Provider** -- grouped by Provider, summing Cost column
> - **Budget Status** -- showing % of Budget, sorted descending
> - **Trend (6 Months)** -- chart view of Cost by Month by Provider

### Budget Rules

```
1. Set a monthly budget per provider BEFORE the month starts
2. Alert at 75% of budget -- review what's driving spend
3. Alert at 90% of budget -- pause non-essential usage
4. Never exceed 120% without explicit decision to raise budget
5. Review and adjust budgets quarterly based on actual usage
```

### Cost Optimization Tactics

| Tactic | Savings | Effort |
|--------|---------|--------|
| Use smaller models for simple tasks | 40-60% | Low |
| Cache common API responses | 20-30% | Medium |
| Batch similar requests | 10-20% | Low |
| Set max token limits on responses | 15-25% | Low |
| Use Gemini Flash for long-context tasks | 50-70% | Low |
| Review and cancel unused API subscriptions | Variable | Low |

### Monthly Cost Report Template

```
## [MONTH YEAR] API Cost Report

### Summary
Total spend: $[AMOUNT]
Budget: $[AMOUNT]
Over/Under: $[AMOUNT] ([PERCENT]%)

### By Provider
- Anthropic: $[AMOUNT] ([PERCENT]% of budget)
- OpenAI: $[AMOUNT] ([PERCENT]% of budget)
- Google: $[AMOUNT] ([PERCENT]% of budget)

### Notable Changes
- [What changed vs last month]
- [Any new tools or increased usage]

### Next Month Adjustments
- [Budget changes]
- [Tool changes]
```

---

## `// CODE REVIEW CHECKLIST`

QA checklist specifically designed for AI-generated code. Print it, pin it, use it every time.

### Linked Database: Code Review Checklist

> *Create a linked database view here pointing to the Code Review Checklist database*
> Recommended views:
> - **By Severity** -- grouped by Severity (Critical first)
> - **AI-Specific** -- filtered to AI-Specific = Yes
> - **By Category** -- grouped by Category

### The 5-Minute AI Code Review

When you're short on time, at minimum check these:

```
CRITICAL (never skip):
[ ] No hardcoded secrets or API keys
[ ] AI didn't hallucinate non-existent APIs or imports
[ ] All external calls have error handling
[ ] No SQL injection or XSS vectors

IMPORTANT (check when possible):
[ ] Tests exist and test behavior, not implementation
[ ] No unnecessary abstraction layers
[ ] TypeScript types are specific (no 'any' abuse)
[ ] No N+1 query patterns
```

### Post-Review Action

After reviewing AI-generated code:
1. If issues found: fix them before committing
2. Log the issue type in your session notes (helps improve prompts)
3. If the same issue keeps appearing: update your system prompt
4. If it's a novel hallucination: add it to this checklist

---

## `// TECH DEBT LOG`

Track the mess so you can clean it up systematically.

### Linked Database: Tech Debt

> *Create a linked database view here pointing to the Tech Debt database*
> Recommended views:
> - **Open Items** -- filtered to Status != Resolved, sorted by Severity
> - **AI-Generated** -- filtered to Source = AI-Generated
> - **Ready to Fix** -- filtered to Estimated Effort <= 2 hours AND Status = Open

### Severity Guide

| Severity | Definition | Fix Timeline |
|----------|-----------|--------------|
| High | Will cause bugs, security issues, or outages | This sprint |
| Medium | Slows development or degrades code quality | This month |
| Low | Cosmetic or minor improvement opportunity | When convenient |

### AI-Specific Debt Patterns

Watch for these recurring patterns in AI-generated code:

```
1. COPY-PASTE PROLIFERATION
   AI generates similar code in separate sessions, creating duplicates.
   Fix: Extract shared logic into utilities after every 3rd session.

2. ABSTRACTION ASTRONAUTICS
   AI creates deep class hierarchies where a function would suffice.
   Fix: Apply the "could this be a function?" test before accepting.

3. STALE DEPENDENCY REFERENCES
   AI suggests packages based on training data, not current versions.
   Fix: Always check package.json after AI adds dependencies.

4. OPTIMISTIC ERROR HANDLING
   AI generates happy-path code and bolts on generic catch blocks.
   Fix: Require specific error types and meaningful recovery in prompts.

5. TEST THEATER
   AI writes tests that pass but don't actually verify behavior.
   Fix: Review test assertions -- if they only check "no error thrown", rewrite.
```

---

## `// TOOL REGISTRY`

Catalog of every MCP server, CLI tool, API, and integration in your stack.

### Linked Database: Tool Registry

> *Create a linked database view here pointing to the Tool Registry database*
> Recommended views:
> - **Active Tools** -- filtered to Status = Active
> - **By Type** -- grouped by Type column
> - **Evaluating** -- filtered to Status = Evaluating
> - **Cost Overview** -- showing Cost column, grouped by Type

### Tool Evaluation Template

Before adding a new tool to your stack:

```
## Tool: [NAME]

### What it does
[One paragraph]

### Why I need it
[Specific problem it solves]

### Alternatives considered
- [Alt 1]: [Why not]
- [Alt 2]: [Why not]

### Integration plan
- [ ] Install and configure
- [ ] Test with sample workflow
- [ ] Add to tool registry
- [ ] Document config location
- [ ] Set up monitoring/alerting

### Cost analysis
Setup time: [HOURS]
Monthly cost: $[AMOUNT]
Expected time saved: [HOURS/MONTH]
ROI breakeven: [MONTHS]
```

---

## `// MONTHLY OPS REPORT`

Template for your monthly review. Copy this section at the start of each month and fill it in.

```
# AgentOps Report -- [MONTH YEAR]

## Summary
Total AI sessions: [COUNT]
Total automation runs: [COUNT]
Total API cost: $[AMOUNT]
Overall success rate: [PERCENT]%

## AI Tool Performance

### Best Performing Tool
- Tool: [NAME]
- Sessions: [COUNT]
- Avg Quality: [SCORE]/5
- Why: [EXPLANATION]

### Worst Performing Tool
- Tool: [NAME]
- Sessions: [COUNT]
- Avg Quality: [SCORE]/5
- Why: [EXPLANATION]

## Cost Analysis
- Total spend: $[AMOUNT]
- vs Last month: [+/-]$[AMOUNT] ([PERCENT]%)
- vs Budget: [OVER/UNDER] by $[AMOUNT]
- Cost per successful session: $[AMOUNT]

## Automation Health
- Active flows: [COUNT]
- Total runs: [COUNT]
- Flows with errors: [COUNT]
- New flows deployed: [COUNT]

## Top Prompts (by use count)
1. [PROMPT NAME] -- used [COUNT] times
2. [PROMPT NAME] -- used [COUNT] times
3. [PROMPT NAME] -- used [COUNT] times

## Tech Debt Status
- Items opened: [COUNT]
- Items resolved: [COUNT]
- Total open: [COUNT]
- Highest priority: [ITEM TITLE]

## Lessons Learned
1. [LESSON]
2. [LESSON]
3. [LESSON]

## Next Month Goals
- [ ] [GOAL]
- [ ] [GOAL]
- [ ] [GOAL]
```

---

## `// RESOURCES`

### Useful Bookmarks

- [Anthropic API Console](https://console.anthropic.com/) -- check usage and billing
- [OpenAI Usage Dashboard](https://platform.openai.com/usage) -- API usage tracking
- [Google AI Studio](https://aistudio.google.com/) -- Gemini usage and testing
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) -- official documentation
- [MCP Server Directory](https://github.com/modelcontextprotocol/servers) -- available MCP servers
- [n8n Workflow Templates](https://n8n.io/workflows/) -- automation inspiration

### Keyboard Shortcuts for Fast Logging

```
Notion shortcuts that speed up data entry:
  Cmd/Ctrl + N         New page (use for quick session log)
  /database inline     Create inline database view
  /template            Create a reusable template button
  Cmd/Ctrl + Shift + L Toggle dark mode (developer preference)
  /code                Insert code block
  /callout             Insert callout for alerts
```

---

*Built by a developer who got tired of not knowing where $200/month in AI costs was going.*
*Version 1.0 | Last updated: March 2026*
