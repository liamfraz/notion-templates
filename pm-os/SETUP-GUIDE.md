# PM OS Setup Guide

Step-by-step instructions to get PM OS (Project Manager Personal OS) running in your Notion workspace. No technical knowledge required — if you can use a spreadsheet, you can set this up.

**Estimated setup time:** 30-45 minutes for the full version.

---

## Step 1: Import the Main Template

You have two options:

### Option A: Import the Markdown File (Recommended)

1. Open Notion and navigate to the workspace where you want PM OS
2. Click the **"..."** menu in the sidebar or use **Import** from the bottom of the sidebar
3. Select **"Import" → "Markdown & CSV"**
4. Choose the `pm-os-main.md` file
5. Notion will create a new page with all the content, headings, and structure

### Option B: Copy-Paste

1. Open `pm-os-main.md` in any text editor
2. Select all content (Cmd+A / Ctrl+A)
3. In Notion, create a new blank page
4. Paste (Cmd+V / Ctrl+V) — Notion will convert the Markdown to Notion blocks

> **Note:** Option A preserves formatting more reliably. If toggle sections don't import correctly, you can manually create them by typing `/toggle` in Notion.

---

## Step 2: Create the Databases

For each CSV file in the `databases/` folder, you'll create a Notion database.

### How to Create a Database from CSV

1. In your PM OS page, go to the relevant section (e.g., scroll to "Project Tracker")
2. Type `/database` and select **"Database - Inline"** or **"Database - Full Page"**
3. Name the database (e.g., "Projects")
4. Delete any default columns Notion creates
5. Click the **"..."** menu at the top-right of the database
6. Select **"Merge with CSV"** or go to **Import → CSV**
7. Choose the corresponding CSV file (e.g., `projects.csv`)
8. Notion will create columns matching the CSV headers

### Database Creation Order

Create them in this order (because of the relations you'll set up in Step 3):

1. **Projects** — `databases/projects.csv` (create this first — everything links to it)
2. **Stakeholders** — `databases/stakeholders.csv`
3. **Tasks** — `databases/tasks.csv`
4. **Goals** — `databases/goals.csv`
5. **Weekly Reviews** — `databases/weekly-reviews.csv`
6. **Meeting Notes** — `databases/meeting-notes.csv`
7. **Risks** — `databases/risks.csv`
8. **Decisions** — `databases/decisions.csv`

### Setting Property Types

After import, Notion may not get every property type right. Go through each database and correct the types:

**Projects:**
| Property | Set Type To |
|----------|------------|
| Budget | Number (format as currency) |
| Status | Select |
| Start Date | Date |
| End Date | Date |
| Priority | Select |
| % Complete | Number (format as Percent) |
| Health | Select |

**Stakeholders:**
| Property | Set Type To |
|----------|------------|
| Role | Select |
| Influence Level | Select |
| Interest Level | Select |
| Engagement Strategy | Select |
| Last Contact Date | Date |

**Tasks:**
| Property | Set Type To |
|----------|------------|
| Status | Select |
| Priority | Select |
| Due Date | Date |
| Estimated Hours | Number |
| Actual Hours | Number |
| Tags | Multi-select |

**Goals:**
| Property | Set Type To |
|----------|------------|
| Time Frame | Select |
| Status | Select |
| Target Date | Date |
| % Complete | Number (format as Percent) |
| Priority | Select |

**Weekly Reviews:**
| Property | Set Type To |
|----------|------------|
| Week Starting | Date |
| Energy Level | Select |
| Productivity Rating | Number |
| Goals Met | Checkbox |

**Meeting Notes:**
| Property | Set Type To |
|----------|------------|
| Date | Date |
| Meeting Type | Select |
| Follow-up Date | Date |

**Risks:**
| Property | Set Type To |
|----------|------------|
| Likelihood | Select |
| Impact | Select |
| Risk Score | Number |
| Status | Select |
| Date Identified | Date |
| Date Resolved | Date |
| Category | Select |

**Decisions:**
| Property | Set Type To |
|----------|------------|
| Date | Date |
| Status | Select |
| Impact Level | Select |
| Review Date | Date |

---

## Step 3: Set Up Database Relations

Relations are what make PM OS powerful. They connect your data so a single project shows all its tasks, risks, decisions, and everything else in one place.

### How to Create a Relation

1. Open the database you want to add a relation to
2. Click **"+"** to add a new property
3. Select **"Relation"**
4. Choose the database to relate to
5. Name the property clearly

### Relations to Create

| In This Database | Add Relation To | Property Name | Notes |
|-----------------|----------------|---------------|-------|
| Tasks | Projects | Project | Replace the existing text "Project" column |
| Meeting Notes | Projects | Project | Replace the existing text "Project" column |
| Risks | Projects | Project | Replace the existing text "Project" column |
| Decisions | Projects | Project | Replace the existing text "Project" column |
| Weekly Reviews | Projects | Projects Reviewed | Links reviews to the projects discussed that week |
| Stakeholders | Projects | Related Projects | Replace the existing text "Project" column |

**For each relation above:**
1. Delete the original text-based "Project" column (it was imported from CSV as plain text)
2. Create a new Relation property called "Project" (or the name listed above)
3. Link it to the Projects database
4. Go through each row and select the correct project from the relation picker

> **Tip:** When you create a relation, Notion asks if you want to show it in the related database too. Always say **Yes**. This means your Projects database will automatically show a "Tasks" column listing all related tasks, a "Risks" column, etc. — giving you a complete project overview from a single row.

---

## Step 4: Set Up Dashboard Views

The Dashboard section of your main PM OS page should contain **linked database views** — not copies of the databases, but filtered views of them.

### How to Create a Linked Database View

1. Navigate to the Dashboard section of your PM OS page
2. Type `/linked` and select **"Linked view of database"**
3. Choose the source database (e.g., Tasks)
4. Configure the view:

### Dashboard Views to Create

**1. This Week's Tasks**
- Source: Tasks
- View type: Table
- Filter: Due Date is this week AND Status is not "Done"
- Sort: Due Date ascending

**2. Active Projects Board**
- Source: Projects
- View type: Board
- Group by: Status
- Filter: Status is not "Complete"

**3. Upcoming Meetings**
- Source: Meeting Notes
- View type: Table
- Filter: Date is within the next 7 days
- Sort: Date ascending

**4. Goal Progress**
- Source: Goals
- View type: Table
- Filter: Time Frame is current quarter
- Sort: % Complete descending

**5. Open Risks**
- Source: Risks
- View type: Table
- Filter: Status is "Open" or "Mitigating"
- Sort: Risk Score descending

**6. Recent Decisions**
- Source: Decisions
- View type: Table
- Filter: Date is within the last 30 days
- Sort: Date descending

---

## Step 5: Customise for Your Workflow

### Replace Sample Data

The CSV files include sample data from fictional projects. Delete these rows and start entering your own data. The sample data is there to show you the format and level of detail expected in each field.

### Add Your Details

At the top of the PM OS page, replace the intro text with:
- Your name and role
- Your current project portfolio summary
- Key stakeholder contact details or links

### Customise Select Options

The Select properties (Status, Priority, Category, etc.) may need additional options for your workflow:
- Click on any Select property → "Edit property" → add/remove options
- Add meeting types that match your recurring cadence (e.g., "Sprint Review", "Steering Committee", "1:1")
- Add risk categories relevant to your domain (e.g., "Technical", "Resource", "Budget", "Compliance")
- Add goal time frames if you track beyond quarterly (e.g., "Annual", "Half-Year")

### Set Up Notion Automations

Go to the **"..."** menu on each database → **"Automations"**:

1. **Auto-date on task completion:** When Task Status changes to "Done" → Set a completion timestamp
2. **Overdue task notifications:** When Task Due Date is reached and Status is not "Done" → Send notification
3. **Risk escalation alerts:** When Risk Score exceeds your threshold → Send notification
4. **Weekly review reminder:** Every Friday afternoon → Send reminder to complete your Weekly Review

---

## Step 6: Build the Habit

### Rollout Strategy

**Week 1: Capture Everything**
- Set up the full system following this guide
- Enter your current project data, active tasks, and known risks
- Use it yourself for one full week to work out the kinks

**Week 2: Daily Task Management**
- Start each morning by reviewing your "This Week's Tasks" dashboard view
- Log meeting notes directly in PM OS during or immediately after meetings
- Close out completed tasks daily — don't let them pile up

**Week 3: Weekly Review Rhythm**
- Complete your first Weekly Review on Friday
- Review goal progress and adjust priorities for the following week
- Update risk statuses and project health indicators

**Week 4: Full Integration**
- PM OS is now your single source of truth for all project work
- Run stakeholder updates and status reports directly from your dashboard views
- Log all decisions in the Decisions database so you have a clear audit trail
- Refine your dashboard layout based on what you find yourself checking most

### Tips for Adoption

1. **Start with tasks and projects.** Get comfortable with the core workflow before adding risks, goals, and decisions.
2. **Make it the single source of truth.** If someone asks about a project status, point them to PM OS. Don't maintain a parallel spreadsheet.
3. **Use the mobile app.** Install Notion on your phone for quick task capture and meeting notes on the go.
4. **Review your dashboard daily.** A dashboard only works if you look at it. Make it your morning start page.
5. **Keep your Weekly Reviews honest.** The value compounds over time — after a few months, you'll have a clear record of what worked, what didn't, and how your priorities evolved.

---

## Troubleshooting

### CSV Import Issues

**Problem:** Columns don't align after import
**Fix:** Open the CSV in a text editor and check for commas within data fields. All fields containing commas should be wrapped in double quotes.

**Problem:** Dates import as text
**Fix:** After import, change the property type to Date. Notion should auto-parse most date formats. If not, you may need to re-enter dates manually.

### Relation Issues

**Problem:** Can't find the project in the relation picker
**Fix:** Make sure the project exists in the Projects database first. Relations only show existing entries.

**Problem:** Existing text data doesn't auto-link to relations
**Fix:** This is expected. When you replace a text column with a relation column, you need to manually select the related item for each row. For the sample data, this is only a few entries. For your real data, do it as you enter new records.

### Performance

**Problem:** Pages loading slowly
**Fix:** If you have 500+ entries in a database, use filtered views instead of showing all entries. Notion handles large databases well, but rendering all rows at once can be slow.

---

## Need Help?

If you get stuck during setup:
- Re-read the relevant section of this guide
- Check Notion's official docs at notion.so/help
- Reach out via the email on your purchase receipt

You've got this. The hardest part is the initial setup — once it's running, PM OS keeps your projects, decisions, and priorities in one place so nothing falls through the cracks.
