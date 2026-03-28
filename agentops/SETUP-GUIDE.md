# AgentOps Setup Guide

Step-by-step instructions to get AgentOps (AI Agent Operations Hub) running in your Notion workspace. If you can use a spreadsheet and a terminal, you can set this up.

**Estimated setup time:** 30-45 minutes for the full version.

---

## Step 1: Import the Main Template

You have two options:

### Option A: Import the Markdown File (Recommended)

1. Open Notion and navigate to the workspace where you want AgentOps
2. Click the **"..."** menu in the sidebar or use **Import** from the bottom of the sidebar
3. Select **"Import" → "Markdown & CSV"**
4. Choose the `agentops-main.md` file
5. Notion will create a new page with all the content, headings, and structure

### Option B: Copy-Paste

1. Open `agentops-main.md` in any text editor
2. Select all content (Cmd+A / Ctrl+A)
3. In Notion, create a new blank page
4. Paste (Cmd+V / Ctrl+V) — Notion will convert the Markdown to Notion blocks

> **Note:** Option A preserves formatting more reliably. If toggle sections don't import correctly, you can manually create them by typing `/toggle` in Notion.

---

## Step 2: Create the Databases

For each CSV file in the `databases/` folder, you'll create a Notion database.

### How to Create a Database from CSV

1. In your AgentOps page, go to the relevant section (e.g., scroll to "Agent Registry")
2. Type `/database` and select **"Database - Inline"** or **"Database - Full Page"**
3. Name the database (e.g., "Agent Registry")
4. Delete any default columns Notion creates
5. Click the **"..."** menu at the top-right of the database
6. Select **"Merge with CSV"** or go to **Import → CSV**
7. Choose the corresponding CSV file (e.g., `agent-registry.csv`)
8. Notion will create columns matching the CSV headers

### Database Creation Order

Create them in this order (because of the relations you'll set up in Step 3):

1. **Agent Registry** — `databases/agent-registry.csv` (create this first — everything links to it)
2. **Task Queue** — `databases/task-queue.csv`
3. **Execution Logs** — `databases/execution-logs.csv`
4. **Prompt Library** — `databases/prompt-library.csv`
5. **Cost Tracker** — `databases/cost-tracker.csv`

### Setting Property Types

After import, Notion may not get every property type right. Go through each database and correct the types:

**Agent Registry:**
| Property | Set Type To |
|----------|------------|
| Cost Per Run ($) | Number (format as currency) |
| Status | Select |
| Category | Select |
| Tasks Completed | Number |
| Success Rate (%) | Number (format as Percent) |
| Avg Duration (sec) | Number |
| Last Run | Date |

**Task Queue:**
| Property | Set Type To |
|----------|------------|
| Priority | Select |
| Status | Select |
| Created | Date |
| Started | Date |
| Completed | Date |
| Input Tokens | Number |
| Output Tokens | Number |
| Cost ($) | Number (format as currency) |
| Retry Count | Number |

**Execution Logs:**
| Property | Set Type To |
|----------|------------|
| Timestamp | Date |
| Duration (sec) | Number |
| Status | Select |
| Input Tokens | Number |
| Output Tokens | Number |
| Cost ($) | Number (format as currency) |
| Error Type | Select |

**Prompt Library:**
| Property | Set Type To |
|----------|------------|
| Category | Select |
| Success Rate (%) | Number (format as Percent) |
| Use Count | Number |
| Last Used | Date |
| Tags | Multi-select |

**Cost Tracker:**
| Property | Set Type To |
|----------|------------|
| Provider | Select |
| API Calls | Number |
| Input Tokens | Number |
| Output Tokens | Number |
| Cost ($) | Number (format as currency) |
| Budget ($) | Number (format as currency) |
| % of Budget | Number (format as Percent) |

---

## Step 3: Set Up Database Relations

Relations are what make AgentOps powerful. They connect your data so a single agent page shows all its tasks, execution logs, prompts, and costs in one place.

### How to Create a Relation

1. Open the database you want to add a relation to
2. Click **"+"** to add a new property
3. Select **"Relation"**
4. Choose the database to relate to
5. Name the property clearly

### Relations to Create

| In This Database | Add Relation To | Property Name | Notes |
|-----------------|----------------|---------------|-------|
| Task Queue | Agent Registry | Agent | Replace the existing text "Agent" column |
| Execution Logs | Agent Registry | Agent | Replace the existing text "Agent" column |
| Execution Logs | Task Queue | Task | Replace the existing text "Task" column |
| Prompt Library | Agent Registry | Agent | Replace the existing text "Agent" column |
| Cost Tracker | Agent Registry | Agent | Replace the existing text "Agent" column |

**For each relation above:**
1. Delete the original text-based column (it was imported from CSV as plain text)
2. Create a new Relation property with the name listed above
3. Link it to the target database
4. Go through each row and select the correct entry from the relation picker

> **Tip:** When you create a relation, Notion asks if you want to show it in the related database too. Always say **Yes**. This means your Agent Registry will automatically show a "Tasks" column listing all related tasks, an "Execution Logs" column, etc. — giving you a complete agent overview from a single row.

---

## Step 4: Set Up Dashboard Views

The Command Center section of your main AgentOps page should contain **linked database views** — not copies of the databases, but filtered views of them.

### How to Create a Linked Database View

1. Navigate to the Command Center section of your AgentOps page
2. Type `/linked` and select **"Linked view of database"**
3. Choose the source database (e.g., Execution Logs)
4. Configure the view

### Dashboard Views to Create

**1. Daily Spend Dashboard**

*Today's Spend:*
- Source: Execution Logs
- View type: Table
- Filter: Timestamp is today
- Sort: Cost ($) descending
- Properties visible: Agent, Task, Cost ($), Input Tokens, Output Tokens, Model

*Budget Status:*
- Source: Cost Tracker
- View type: Table
- Filter: Month is current month
- Sort: % of Budget descending
- Properties visible: Provider, Agent, Cost ($), Budget ($), % of Budget

**2. Agent Performance Dashboard**

*Agent Health:*
- Source: Agent Registry
- View type: Table
- Filter: Status is Active
- Sort: Success Rate (%) descending
- Properties visible: Agent Name, Provider, Model, Tasks Completed, Success Rate (%), Avg Duration

*Task Throughput:*
- Source: Task Queue
- View type: Board
- Group by: Status
- Filter: Created is this week
- Sort: Priority (Critical first)

**3. Error Rates Dashboard**

*Recent Failures:*
- Source: Execution Logs
- View type: Table
- Filter: Status is not "Success" AND Timestamp is within last 7 days
- Sort: Timestamp descending
- Properties visible: Agent, Task, Status, Error Type, Cost ($), Stack Trace

*Errors by Type:*
- Source: Execution Logs
- View type: Board
- Group by: Error Type
- Filter: Status is not "Success" AND Timestamp is within last 30 days

---

## Step 5: Customise for Your Workflow

### Replace Sample Data

The CSV files include sample data from fictional agent operations. Delete these rows and start entering your own data. The sample data is there to show you the format and level of detail expected in each field.

### Add Your Agents

Start by registering your actual agents in the Agent Registry:
- List every AI agent, bot, or pipeline you currently run
- Include the model version string from your API configuration
- Set realistic cost-per-run estimates from your provider dashboards
- Mark agents as Active, Testing, or Deprecated based on current state

### Customise Select Options

The Select properties (Status, Priority, Category, Error Type, etc.) may need additional options for your workflow:
- Click on any Select property → "Edit property" → add/remove options
- Add provider names if you use providers not in the default list
- Add error types specific to your stack (e.g., "Embedding Failure", "Vector DB Timeout")
- Add categories that match your agent taxonomy

### Set Up Notion Automations

Go to the **"..."** menu on each database → **"Automations"**:

1. **Task failure alert:** When Task Queue Status changes to "Failed" → Send notification with the task name
2. **Budget warning:** When Cost Tracker % of Budget exceeds 80% → Send notification
3. **New task defaults:** When a new Task Queue entry is created → Set Status to "Queued" and Created to today
4. **Error escalation:** When Execution Log Status is "Error" → Send notification to investigate

---

## Step 6: Optional — Automate Log Entries

For developers who want to automate data entry from their agent pipelines:

### Notion API Approach

1. Create a Notion integration at https://www.notion.so/my-integrations
2. Share your AgentOps databases with the integration
3. Use the Notion API to POST new entries to Execution Logs and Task Queue databases
4. Store the database IDs and integration token as environment variables (never hardcode)

### n8n / Make Webhook Approach

1. Create a webhook trigger in n8n or Make
2. Have your agent pipeline send a POST request on task completion
3. Map the webhook payload to Notion database properties
4. The flow creates a new Execution Log entry automatically

### Simple Logging Script

```python
# Minimal example — add to your agent pipeline's completion handler
import os
import requests

def log_execution(agent_name, task_id, duration, status, cost, tokens_in, tokens_out):
    requests.post(
        "https://api.notion.com/v1/pages",
        headers={
            "Authorization": f"Bearer {os.environ['NOTION_TOKEN']}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        },
        json={
            "parent": {"database_id": os.environ["EXECUTION_LOGS_DB_ID"]},
            "properties": {
                "Log ID": {"title": [{"text": {"content": f"LOG-{task_id}"}}]},
                "Duration (sec)": {"number": duration},
                "Status": {"select": {"name": status}},
                "Cost ($)": {"number": cost},
                "Input Tokens": {"number": tokens_in},
                "Output Tokens": {"number": tokens_out}
            }
        }
    )
```

---

## Troubleshooting

### CSV Import Issues

**Problem:** Columns don't align after import
**Fix:** Open the CSV in a text editor and check for commas within data fields. All fields containing commas should be wrapped in double quotes.

**Problem:** Dates import as text
**Fix:** After import, change the property type to Date. Notion should auto-parse most date formats (YYYY-MM-DD works best). If not, re-enter dates manually.

**Problem:** Numbers import as text
**Fix:** Change the property type to Number. For currency fields, select Number → format as currency.

### Relation Issues

**Problem:** Can't find the agent in the relation picker
**Fix:** Make sure the agent exists in the Agent Registry first. Relations only show existing entries.

**Problem:** Existing text data doesn't auto-link to relations
**Fix:** This is expected. When you replace a text column with a relation column, you need to manually select the related item for each row. For sample data this is only a few entries.

### Performance

**Problem:** Pages loading slowly
**Fix:** If you have 500+ entries in Execution Logs, use filtered views instead of showing all entries. Archive logs older than 90 days to a separate database or export to CSV.

---

## Need Help?

If you get stuck during setup:
- Re-read the relevant section of this guide
- Check Notion's official docs at notion.so/help
- Reach out via the email on your purchase receipt

The hardest part is the initial setup. Once it's running, AgentOps keeps your agents, costs, and operations in one place so nothing falls through the cracks.
