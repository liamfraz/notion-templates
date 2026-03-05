# Technical Consultant OS — Setup Guide

Follow these steps to get your workspace running. Allow 30-60 minutes for initial setup.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace.
2. Create a new page called **"Consultant OS"** (or whatever you prefer).
3. Click the **"..."** menu in the top-right, then **Import** > **Markdown**.
4. Select `consultant-os-main.md`.
5. The full template structure will import as your main hub page.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### 2.1 Import Each CSV

1. Inside your Consultant OS page, create a new sub-page for the database (e.g., "Clients Database").
2. On the sub-page, click **"..."** > **Import** > **CSV**.
3. Select the CSV file. Notion will create a table with all columns and sample data.
4. Repeat for all 8 databases:
   - `clients.csv` — Client CRM
   - `leads.csv` — Lead Pipeline
   - `projects.csv` — Project Tracker
   - `time-entries.csv` — Time Tracker
   - `invoices.csv` — Invoice Register
   - `rate-card.csv` — Rate Card Manager
   - `knowledge-base.csv` — Knowledge Base
   - `skills.csv` — Skills Matrix

### 2.2 Set Column Types

After import, update column types for accurate filtering and formulas:

**Clients:**
| Column | Type |
|---|---|
| Total Revenue ($) | Number (AUD format) |
| First Engaged | Date |
| Last Contact | Date |
| Engagement Status | Select (Active / Past / Prospect) |
| Health Score | Select (Green / Amber / Red) |

**Leads:**
| Column | Type |
|---|---|
| Estimated Value ($) | Number (AUD format) |
| Probability (%) | Number (percent format) |
| Expected Close Date | Date |
| Stage | Select (New Lead / Qualified / Proposal Sent / Negotiation / Won / Lost) |
| Source | Select (Referral / LinkedIn / Website / Cold Outreach / Repeat) |
| Created Date | Date |

**Projects:**
| Column | Type |
|---|---|
| Budget ($) | Number (AUD format) |
| Invoiced ($) | Number (AUD format) |
| Rate ($) | Number (AUD format) |
| Estimated Hours | Number |
| Actual Hours | Number |
| Start Date | Date |
| End Date | Date |
| Status | Select (Scoping / Active / On Hold / Complete / Cancelled) |
| Rate Type | Select (Hourly / Daily / Fixed) |
| Service Type | Select |

**Time Entries:**
| Column | Type |
|---|---|
| Date | Date |
| Hours | Number |
| Rate ($) | Number (AUD format) |
| Billable Amount ($) | Number (AUD format) |
| Billable | Checkbox or Select (Yes / No) |
| Category | Select (Development / Consulting / Meeting / Admin / Travel) |

**Invoices:**
| Column | Type |
|---|---|
| Amount ($) | Number (AUD format) |
| Tax ($) | Number (AUD format) |
| Total ($) | Number (AUD format) |
| Date Issued | Date |
| Date Due | Date |
| Date Paid | Date |
| Status | Select (Draft / Sent / Overdue / Paid / Cancelled) |

**Rate Card:**
| Column | Type |
|---|---|
| Standard Rate ($) | Number (AUD format) |
| Discounted Rate ($) | Number (AUD format) |
| Premium Rate ($) | Number (AUD format) |
| Rate Type | Select (Hourly / Daily / Fixed) |

**Knowledge Base:**
| Column | Type |
|---|---|
| Last Updated | Date |
| Use Count | Number |
| Category | Select (Template / Code Snippet / Checklist / Guide / Reference) |

**Skills:**
| Column | Type |
|---|---|
| Certification Expiry | Date |
| Last Used | Date |
| Proficiency | Select (Beginner / Intermediate / Advanced / Expert) |
| Category | Select (Technical / Business / Soft Skill) |
| Priority | Select (High / Medium / Low) |

---

## Step 3: Set Up Relations

Relations link your databases together, enabling powerful filtering and rollups.

### 3.1 Create These Relations

1. **Projects -> Clients**
   - In the Projects database, add a "Relation" column.
   - Link to the Clients database.
   - This creates a two-way relation (Projects appear on Client records too).

2. **Time Entries -> Projects**
   - In Time Entries, add a Relation column linked to Projects.

3. **Time Entries -> Clients**
   - In Time Entries, add a Relation column linked to Clients.

4. **Invoices -> Projects**
   - In Invoices, add a Relation column linked to Projects.

5. **Invoices -> Clients**
   - In Invoices, add a Relation column linked to Clients.

6. **Leads -> Clients** (optional)
   - Link leads to the client record when a lead converts to a client.

### 3.2 After Linking, Update Existing Records

Go through the sample data and link the records using the new relation columns. For example, link the "SharePoint Intranet Automation" project to the "Meridian Property Group" client.

---

## Step 4: Configure Formulas

Add these formula columns to automate calculations.

### Time Entries — Billable Amount (if not using CSV value)

```
if(prop("Billable") == "Yes", prop("Hours") * prop("Rate"), 0)
```

### Projects — Budget Consumed (%)

```
round(prop("Invoiced") / prop("Budget") * 100)
```

### Projects — Hours Remaining

```
prop("Estimated Hours") - prop("Actual Hours")
```

### Invoices — Days Until Due

```
if(prop("Status") == "Paid", 0, dateBetween(prop("Date Due"), now(), "days"))
```

### Invoices — Days Outstanding (for paid invoices)

```
if(empty(prop("Date Paid")), 0, dateBetween(prop("Date Paid"), prop("Date Issued"), "days"))
```

### Leads — Weighted Value

```
prop("Estimated Value") * prop("Probability") / 100
```

---

## Step 5: Set Up Rollups

Rollups aggregate data from related databases.

### On Client Records

1. **Total Invoiced** — Rollup from Invoices relation, "Amount" column, Sum
2. **Total Hours** — Rollup from Time Entries relation, "Hours" column, Sum
3. **Active Projects Count** — Rollup from Projects relation, Count where Status = "Active"

### On Project Records

1. **Total Time Logged** — Rollup from Time Entries relation, "Hours" column, Sum
2. **Total Billed** — Rollup from Invoices relation, "Amount" column, Sum

---

## Step 6: Configure Your Rate Card

1. Open the Rate Card database.
2. Delete or modify the sample entries to match your actual services and rates.
3. Set your standard, discounted, and premium rates in AUD.
4. Reference the rate card when creating new projects and proposals.

---

## Step 7: Create Views

Set up multiple views for each database (the main template page lists recommended views).

**Quick wins:**

- **Leads** — Board view grouped by Stage (drag leads across stages)
- **Projects** — Board view grouped by Status
- **Invoices** — Board view grouped by Status (see overdue at a glance)
- **Time Entries** — Table filtered to "This Week" for quick time logging
- **Clients** — Board view grouped by Health Score

---

## Step 8: Import Your Existing Data

1. Export client data from your current system (spreadsheet, CRM, etc.) as CSV.
2. Match columns to the Consultant OS structure.
3. Import via Notion's CSV import into the relevant database.
4. Link records using the relation columns.

**Tip:** Start with clients and projects first. Time entries can begin fresh from today.

---

## Step 9: Set Up Your Dashboard

The Business Dashboard section on the main page uses manual values by default. To make it dynamic:

1. Create **linked database views** (filtered and sorted) inline on the dashboard page.
2. Use Notion's **database rollups** or **linked views with calculations** to pull live numbers.
3. Alternatively, update the dashboard manually during your monthly review.

**Key metrics to track:**
- Revenue this month (sum of paid invoices this month)
- Active project count (filtered view of Projects where Status = Active)
- Pipeline value (sum of Weighted Value from Leads)
- Utilisation rate (calculate during monthly review)

---

## Step 10: Ongoing Usage

### Daily
- Log time entries at end of each work day
- Update project notes after significant work

### Weekly
- Review time entries for accuracy and completeness
- Check pipeline — update lead stages and probabilities
- Chase any overdue invoices

### Monthly
- Run the Monthly Business Review (use `templates/monthly-review.md`)
- Update client health scores
- Review budget health on active projects
- Update skills matrix if needed

### Quarterly
- Review and update rate card
- Deep pipeline review — close stale leads
- Skills matrix review — set learning goals
- Review knowledge base — archive outdated entries

---

## Troubleshooting

**CSV won't import correctly**
- Open the CSV in a text editor and verify commas are not inside unquoted fields.
- Notion sometimes struggles with multi-line values. If a "Notes" field has commas, ensure it's wrapped in double quotes.

**Relations not linking properly**
- Make sure the value in the relation column exactly matches a record name in the target database.
- Notion relations are case-sensitive.

**Formulas returning errors**
- Check that column names in your formulas exactly match your database column names (including spaces and capitalisation).
- Notion Formula 2.0 uses `prop("Column Name")` syntax.

---

*Setup complete. Start with logging your first time entry and adding your active clients.*
