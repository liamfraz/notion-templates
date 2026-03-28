# AI Side Hustle Tracker -- Setup Guide

Get the full dashboard running in your Notion workspace in about 15 minutes.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace sidebar
2. Click **Import** (at the bottom of the sidebar)
3. Select **Markdown** and upload `ai-sidehustle-main.md`
4. Notion will create a new page with all the sections

Alternatively, create a new page and paste the markdown content directly.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### Projects Database

1. In Notion, create a new **Full-page database**
2. Name it `Projects`
3. Click the `...` menu at the top right of the database
4. Select **Merge with CSV** and upload `databases/projects.csv`
5. Set column types:
   - Project Name: `Title`
   - Category: `Select` (options: Freelancing, Digital Product, Content, Course, SaaS, Automation)
   - Platform: `Select` (options: Gumroad, Substack, Upwork, Fiverr, Etsy, Udemy, Own Website, Amazon KDP)
   - Monthly Revenue ($): `Number` (format: Australian Dollar)
   - Status: `Select` (options: Active, Scaling, Paused, Planning, Completed)
   - Start Date: `Date`
   - URL: `URL`
   - AI Tools Used: `Multi-select` (options: Claude, ChatGPT, Midjourney, Runway, n8n, Cursor, Canva, ElevenLabs)
   - Monthly Hours: `Number`
   - Effective Hourly Rate ($): `Number` (format: Australian Dollar) -- or use a Formula: `prop("Monthly Revenue ($)") / prop("Monthly Hours")`
   - Growth Rate (%): `Number` (format: Percent)
   - Notes: `Text`

### Income Log Database

1. Create a new **Full-page database** named `Income Log`
2. Merge with `databases/income-log.csv`
3. Set column types:
   - Date: `Date`
   - Project: `Text` (convert to Relation after all databases are created)
   - Amount ($): `Number` (format: Australian Dollar)
   - Source: `Text`
   - Payment Method: `Select` (options: PayPal, Stripe, Bank Transfer, Gumroad, Direct Deposit)
   - Notes: `Text`
   - Tax Withheld ($): `Number` (format: Australian Dollar)
   - Net Amount ($): `Number` (format: Australian Dollar) -- or use a Formula: `prop("Amount ($)") - prop("Tax Withheld ($)")`

### Expenses Database

1. Create a new **Full-page database** named `Expenses`
2. Merge with `databases/expenses.csv`
3. Set column types:
   - Date: `Date`
   - Category: `Select` (options: Software, Marketing, Education, Hardware, Outsourcing, Hosting, Office, Other)
   - Description: `Title`
   - Amount ($): `Number` (format: Australian Dollar)
   - Project: `Text` (convert to Relation after all databases are created)
   - Tax Deductible: `Checkbox`
   - Receipt: `Text`
   - Vendor: `Text`
   - Payment Method: `Select` (options: Credit Card, PayPal, Bank Transfer, Direct Debit)
   - Notes: `Text`

### Task Board Database

1. Create a new **Full-page database** named `Task Board`
2. Merge with `databases/task-board.csv`
3. Set column types:
   - Task Name: `Title`
   - Project: `Text` (convert to Relation after all databases are created)
   - Priority: `Select` (options: High, Medium, Low)
   - Status: `Select` (options: Backlog, To Do, In Progress, Blocked, Done)
   - Due Date: `Date`
   - Estimated Hours: `Number`
   - Actual Hours: `Number`
   - Category: `Select` (options: Build, Marketing, Admin, Content, Design, Research)
   - Notes: `Text`

### Launch Checklist Database

1. Create a new **Full-page database** named `Launch Checklist`
2. Merge with `databases/launch-checklist.csv`
3. Set column types:
   - Item: `Title`
   - Phase: `Select` (options: Research, Build, Pre-Launch, Launch, Post-Launch)
   - Project: `Text` (convert to Relation after all databases are created)
   - Status: `Select` (options: Not Started, In Progress, Done, Skipped)
   - Due Date: `Date`
   - Owner: `Text`
   - Dependencies: `Text`
   - Notes: `Text`

---

## Step 3: Set Up Relations

Now link the databases together. This is what makes the system powerful.

### Projects <-> Income Log
1. Open the **Income Log** database
2. Change the `Project` column from Text to `Relation`
3. Point it to the `Projects` database
4. This lets you see all income entries for a specific project

### Projects <-> Expenses
1. Open the **Expenses** database
2. Change the `Project` column from Text to `Relation`
3. Point it to the `Projects` database
4. Track spending per project

### Projects <-> Task Board
1. Open the **Task Board** database
2. Change the `Project` column from Text to `Relation`
3. Point it to the `Projects` database
4. See all tasks tied to each project

### Projects <-> Launch Checklist
1. Open the **Launch Checklist** database
2. Change the `Project` column from Text to `Relation`
3. Point it to the `Projects` database
4. Track launch progress per project

### Relation Map

```
Projects (central hub)
  |-- Income Log (revenue per project)
  |-- Expenses (costs per project)
  |-- Task Board (work per project)
  |-- Launch Checklist (launch progress per project)
```

---

## Step 4: Configure Views

Go back to the main AI Side Hustle Tracker page and set up linked database views.

### For Each Section

1. In each section that says "Create a linked database view here", type `/linked` and select **Create linked view of database**
2. Point each linked view to the appropriate database
3. Set up the recommended views listed in each section

### Key Views to Set Up First

**Revenue by Project (Projects database)**
- Table view sorted by Monthly Revenue descending
- Shows: Project Name, Platform, Monthly Revenue, Monthly Hours, Effective Hourly Rate, Status

**Active Tasks Kanban (Task Board database)**
- Board view grouped by Status
- Shows: Task Name, Project, Priority, Due Date
- Filter: Status != Done

**Monthly P&L (Income Log + Expenses)**
- Create two linked views side by side
- Income Log: grouped by Project, summing Amount
- Expenses: grouped by Category, summing Amount

---

## Step 5: Replace Sample Data

1. Open each database and delete the sample rows
2. Add your real projects, income, expenses, and tasks
3. Be honest with your numbers -- accurate data leads to better decisions
4. Start with Projects and Income Log first (they give you 80% of the value)

### If You Only Have 1-2 Projects

That's fine. The template scales. Add projects as you grow. The important thing is to start tracking from day one.

---

## Tips

- **Start with Projects and Income Log.** These two databases give you 80% of the value. Add the others as you settle in.
- **Log income as it arrives.** Don't batch it at month-end. Real-time data means real-time decisions.
- **Use the Launch Checklist for every new project.** Duplicate the template rows and customise for each launch.
- **Review weekly, decide monthly.** Quick 10-minute task review on Sundays, full P&L review at month-end.
- **Kill underperformers.** If a project has been under $30/hour for 3 months and isn't growing, pause it and redirect that time.

---

*Questions? Feature requests? Reach out on X or open an issue on GitHub.*
