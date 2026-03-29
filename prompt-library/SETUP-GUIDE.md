# AI Prompt Library & Workflow Manager -- Setup Guide

Get the full prompt library running in your Notion workspace in about 30 minutes.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace sidebar
2. Click **Import** (at the bottom of the sidebar)
3. Select **Markdown** and upload `prompt-library-main.md`
4. Notion will create a new page with all the sections

Alternatively, create a new page and paste the markdown content directly.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### Prompts Database

1. In Notion, create a new **Full-page database**
2. Name it `Prompts`
3. Click the `...` menu at the top right of the database
4. Select **Merge with CSV** and upload `databases/prompts.csv`
5. Set column types:
   - Name: `Title`
   - Category: `Select` (options: Writing, Coding, Marketing, Analysis, Research, Creative, Business, Productivity)
   - Model: `Select` (options: Claude, ChatGPT, Gemini, Any)
   - Prompt Text: `Text`
   - Rating: `Number` (format: Number, 1-5)
   - Use Count: `Number`
   - Output Format: `Select` (options: Markdown, Text, Code, Table, JSON)
   - Tags: `Text`
   - Last Used: `Date`
   - Version: `Number` (format: Number with one decimal)
   - Notes: `Text`

### Workflows Database

1. Create a new **Full-page database** named `Workflows`
2. Merge with `databases/workflows.csv`
3. Set column types:
   - Name: `Title`
   - Description: `Text`
   - Steps: `Number`
   - Category: `Select` (options: Writing, Coding, Marketing, Analysis, Business, Research)
   - Prompts Used: `Text`
   - Avg Time (min): `Number`
   - Success Rate: `Text`
   - Status: `Select` (options: Active, Draft, Retired)
   - Last Run: `Date`
   - Tags: `Text`
   - Notes: `Text`

### Collections Database

1. Create a new **Full-page database** named `Collections`
2. Merge with `databases/collections.csv`
3. Set column types:
   - Name: `Title`
   - Description: `Text`
   - Prompt Count: `Number`
   - Category: `Select` (options: Writing, Coding, Marketing, Analysis, Business, Research, Productivity)
   - Use Case: `Text`
   - Created: `Date`
   - Last Updated: `Date`
   - Rating: `Number` (format: Number, 1-5)
   - Tags: `Text`

### Usage Log Database

1. Create a new **Full-page database** named `Usage Log`
2. Merge with `databases/usage-log.csv`
3. Set column types:
   - Date: `Date`
   - Prompt: `Text`
   - Model Used: `Select` (options: Claude, ChatGPT, Gemini)
   - Rating Given: `Number` (format: Number, 1-5)
   - Output Quality: `Select` (options: Excellent, Good, Acceptable, Poor, Useless)
   - Time Saved (min): `Number`
   - Category: `Select` (options: Writing, Coding, Marketing, Analysis, Research, Creative, Business, Productivity)
   - Notes: `Text`

---

## Step 3: Add Your Own Prompts

This is the most important step. The sample prompts are genuinely useful, but your library only becomes powerful when it reflects your actual work.

1. Open the **Prompts** database
2. Keep any sample prompts that are relevant to your work
3. Add your own prompts:
   - Start with prompts you already use regularly (check your ChatGPT/Claude history)
   - Use the CRAFT method from the template to structure them properly
   - Rate honestly -- a 3-star prompt is better than pretending everything is a 5
   - Set the Model field based on where you've actually tested it

If you only have 5-10 prompts to start, that's fine. The library grows naturally as you work. Aim to add 2-3 prompts per week.

---

## Step 4: Set Up Workflows

Workflows are where the real time savings happen.

### Building Your First Workflow

1. Open the **Workflows** database
2. Review the 12 sample workflows -- keep any that match your work
3. To create a new workflow:
   - Pick a task you do at least weekly
   - Break it into 2-5 steps
   - Find or create a prompt for each step
   - Test the chain with real input
   - Record the workflow with an honest success rate

### Workflow Tips

```
Start with 2-3 workflows maximum. Master them before adding more.
A workflow that saves 30 minutes per week = 26 hours per year.
Track success rate honestly -- below 70% means the workflow needs rework.
```

---

## Step 5: Configure Database Relations

Notion relations link databases together for more powerful tracking.

### Prompts <-> Workflows

1. Open the Workflows database
2. Add a new `Relation` property pointing to `Prompts`
3. Name it "Prompts in Workflow"
4. For each workflow, link to the specific prompts it uses
5. This replaces the text-based "Prompts Used" field with clickable links

### Prompts <-> Collections

1. Open the Collections database
2. Add a new `Relation` property pointing to `Prompts`
3. Name it "Included Prompts"
4. Link each collection to its member prompts
5. This lets you see which prompts belong to which collections

### Prompts <-> Usage Log

1. Open the Usage Log database
2. Add a new `Relation` property pointing to `Prompts`
3. Name it "Prompt Used"
4. Link each log entry to the specific prompt
5. This lets you see usage history directly from the prompt page

### Relation Map

```
Prompts (central hub)
  |-- Workflows (which workflows use this prompt)
  |-- Collections (which collections include this prompt)
  |-- Usage Log (every time this prompt was used)

Workflows (standalone -- linked to Prompts via relation)
Collections (standalone -- linked to Prompts via relation)
Usage Log (standalone -- linked to Prompts via relation)
```

---

## Step 6: Create Linked Database Views

1. Go back to the main AI Prompt Library & Workflow Manager page
2. In each section that says "Create a linked database view here", type `/linked` and select **Create linked view of database**
3. Point each linked view to the appropriate database
4. Set up the recommended views listed in each section (filters, sorts, grouping)

### Recommended Dashboard Layout

For the Dashboard section at the top:
- Create a **Gallery view** of Prompts showing Name, Category, Rating, and Use Count
- Create a **Board view** of Workflows grouped by Status
- Create a **Calendar view** of Usage Log to see daily prompt activity

### Key Views to Set Up First

For the Prompts section:
- **By Category** (grouped by Category) -- your most-used view
- **Top Rated** (filtered to Rating >= 4, sorted by Use Count) -- your best prompts
- **Needs Review** (filtered to Rating <= 3) -- prompts to fix or archive

For the Workflows section:
- **Active** (filtered to Status = Active) -- your running workflows
- **By Success Rate** (sorted descending) -- see what's working

---

## Tips

- **Start with Prompts and Usage Log.** These two databases give you 80% of the value. Add Workflows and Collections as you settle in.
- **Use the CRAFT method.** Every prompt in your library should have Context, Role, Action, Format, and Tone. It takes 60 seconds longer to write and saves 20 minutes of back-and-forth.
- **Rate every output.** The rating system only works if you use it. Spend 5 seconds after each prompt to rate 1-5.
- **Version your prompts.** When you improve a prompt, bump the version number. Don't overwrite -- iterate.
- **Review monthly.** Block 15 minutes on the last day of each month. Archive stale prompts, fix low-rated ones, and fill category gaps.
- **Log usage as it happens.** Don't batch-log at the end of the week. You'll forget the details that make the data useful.

---

*Questions? Feature requests? Reach out on X or open an issue on GitHub.*
