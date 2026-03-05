# AgentOps Setup Guide

Get the full dashboard running in your Notion workspace in about 15 minutes.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace sidebar
2. Click **Import** (at the bottom of the sidebar)
3. Select **Markdown** and upload `agentops-main.md`
4. Notion will create a new page with all the sections

Alternatively, create a new page and paste the markdown content directly.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### AI Sessions Database

1. In Notion, create a new **Full-page database**
2. Name it `AI Sessions`
3. Click the `...` menu at the top right of the database
4. Select **Merge with CSV** and upload `databases/ai-sessions.csv`
5. Set column types:
   - Date: `Date`
   - Tool: `Select` (options: Claude Code, ChatGPT, GitHub Copilot, Gemini, Other)
   - Task: `Title`
   - Duration (min): `Number`
   - Tokens Used: `Number` (format: number with commas)
   - Cost ($): `Number` (format: US Dollar)
   - Model: `Select`
   - Outcome: `Select` (options: Success, Partial, Failed)
   - Quality (1-5): `Number`
   - Key Learnings: `Text`
   - Files Modified: `Text`
   - Session ID: `Text`

### Prompt Library Database

1. Create a new **Full-page database** named `Prompt Library`
2. Merge with `databases/prompt-library.csv`
3. Set column types:
   - Name: `Title`
   - Category: `Select` (options: System Prompt, Task Prompt, Chain, Template, Instruction)
   - Tool: `Select`
   - Prompt Text: `Text`
   - Version: `Number` (format: 1 decimal)
   - Rating (1-5): `Number`
   - Use Count: `Number`
   - Last Used: `Date`
   - Tags: `Multi-select`
   - Notes: `Text`

### Automation Flows Database

1. Create a new **Full-page database** named `Automation Flows`
2. Merge with `databases/automation-flows.csv`
3. Set column types:
   - Flow Name: `Title`
   - Platform: `Select` (options: Power Automate, n8n, Zapier, Make, Custom)
   - Status: `Select` (options: Active, Paused, Error, Development)
   - Trigger Type: `Text`
   - Last Run: `Date` (include time)
   - Success Rate (%): `Number` (format: percent)
   - Run Count: `Number`
   - Error Count: `Number`
   - Category: `Select` (options: Business, Personal, Integration, Monitoring)
   - Owner: `Person` (or Text if using solo)
   - Description: `Text`
   - Last Modified: `Date`

### API Costs Database

1. Create a new **Full-page database** named `API Costs`
2. Merge with `databases/api-costs.csv`
3. Set column types:
   - Month: `Date` (set to first of month)
   - Provider: `Select` (options: Anthropic, OpenAI, Google, Azure, Other)
   - API Calls: `Number`
   - Tokens (Input): `Number` (format: number with commas)
   - Tokens (Output): `Number` (format: number with commas)
   - Cost ($): `Number` (format: US Dollar)
   - Model: `Select`
   - Budget ($): `Number` (format: US Dollar)
   - % of Budget: `Number` (format: percent)
   - Notes: `Text`

### Code Review Checklist Database

1. Create a new **Full-page database** named `Code Review Checklist`
2. Merge with `databases/code-review-checklist.csv`
3. Set column types:
   - Check Item: `Title`
   - Category: `Select` (options: Security, Logic, Performance, Style, Testing)
   - Severity: `Select` (options: Critical, Important, Nice-to-Have)
   - AI-Specific (Yes/No): `Checkbox`
   - Description: `Text`

### Tech Debt Database

1. Create a new **Full-page database** named `Tech Debt`
2. Merge with `databases/tech-debt.csv`
3. Set column types:
   - ID: `Text`
   - Title: `Title`
   - Source: `Select` (options: AI-Generated, Manual, Refactor-Needed)
   - Severity: `Select` (options: High, Medium, Low)
   - File/Module: `Text`
   - Description: `Text`
   - Estimated Effort: `Text`
   - Status: `Select` (options: Open, In Progress, Resolved)
   - Created Date: `Date`
   - Resolved Date: `Date`

### Tool Registry Database

1. Create a new **Full-page database** named `Tool Registry`
2. Merge with `databases/tool-registry.csv`
3. Set column types:
   - Tool Name: `Title`
   - Type: `Select` (options: MCP Server, CLI, API, Library, Extension)
   - Status: `Select` (options: Active, Evaluating, Deprecated)
   - Version: `Text`
   - Config Location: `Text` (use code format)
   - Documentation URL: `URL`
   - Cost: `Select` (options: Free, Paid)
   - Notes: `Text`

---

## Step 3: Set Up Relations

Notion relations link databases together. Set up these connections:

### AI Sessions <-> Tool Registry
1. Open the AI Sessions database
2. Add a new `Relation` property pointing to `Tool Registry`
3. Name it "Tool Details"
4. This lets you click through from a session to see tool documentation and config

### Automation Flows <-> API Costs
1. Open the Automation Flows database
2. Add a new `Relation` property pointing to `API Costs`
3. Name it "Cost Records"
4. Link flows to their monthly cost entries for ROI tracking

### AI Sessions <-> Prompt Library
1. Open the AI Sessions database
2. Add a new `Relation` property pointing to `Prompt Library`
3. Name it "Prompts Used"
4. Track which prompts were used in each session

### Tech Debt <-> AI Sessions
1. Open the Tech Debt database
2. Add a new `Relation` property pointing to `AI Sessions`
3. Name it "Source Session"
4. Link debt items back to the session that created them

---

## Step 4: Configure the Command Center

1. Go back to the main AgentOps page
2. In each section that says "Create a linked database view here", type `/linked` and select **Create linked view of database**
3. Point each linked view to the appropriate database
4. Set up the recommended views listed in each section (filters, sorts, grouping)

### Recommended Dashboard Layout

For the Command Center section at the top:
- Create a **Gallery view** of AI Sessions (last 7 days) showing Task as card title
- Create a **Board view** of Automation Flows grouped by Status
- Create a **List view** of Tech Debt filtered to Status = Open

---

## Step 5: Efficient Session Logging

### Quick-Add Method (Recommended)

Create a **Template button** in the AI Sessions database:

1. Open AI Sessions database
2. Click the dropdown arrow next to "New"
3. Click "New template"
4. Pre-fill:
   - Date: `@today`
   - Tool: (leave empty -- you'll select)
   - Outcome: `Success` (default, change if needed)
   - Quality: `4` (default, adjust after)

This way, logging a session takes about 30 seconds.

### End-of-Day Batch Method

If you prefer not to log in real-time:
1. At end of day, open AI Sessions
2. Think through your AI interactions
3. Batch-add all sessions
4. Review quality scores -- be honest, it's for your own data

### Session ID Convention

Use a consistent format: `ses_` followed by 8 random hex characters.
Generate with: `openssl rand -hex 4 | sed 's/^/ses_/'`

---

## Step 6: Integration Ideas

### Bookmarks Bar

Add these to your browser bookmarks bar for one-click access:
- Your AgentOps Notion page
- Anthropic console usage page
- OpenAI usage dashboard
- Your n8n/Power Automate dashboard

### Notion Web Clipper

Use the Notion Web Clipper extension to quickly save:
- Interesting prompts you find online (clip to Prompt Library)
- Tool documentation pages (clip to Tool Registry notes)

### API Webhook Ideas (Advanced)

If you want to automate data entry:

```
Idea 1: n8n workflow that watches your Anthropic usage API
        and auto-creates API Cost entries at end of month

Idea 2: GitHub Action that logs PR review sessions to a
        webhook, which n8n catches and adds to AI Sessions

Idea 3: Power Automate flow that reads a shared Excel sheet
        (for non-Notion team members) and syncs to Notion
```

These require additional setup but can reduce manual logging significantly.

---

## Tips

- **Start small.** Don't try to fill every database on day one. Start with AI Sessions and Prompt Library.
- **Review weekly.** Spend 10 minutes every Friday reviewing your sessions and costs.
- **Iterate your prompts.** The Prompt Library is most valuable when you actively version and improve prompts based on session outcomes.
- **Clean up monthly.** Archive resolved tech debt, remove deprecated tools, update flow statuses.
- **Be honest with quality scores.** A "3" that helps you improve your prompts is more valuable than a fake "5".

---

*Questions? Feature requests? Open an issue or reach out on X.*
