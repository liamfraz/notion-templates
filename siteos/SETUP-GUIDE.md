# SiteOS Setup Guide

Step-by-step instructions to get SiteOS running in your Notion workspace. No technical knowledge required — if you can use a spreadsheet, you can set this up.

**Estimated setup time:** 45-60 minutes for the full version.

---

## Step 1: Import the Main Template

You have two options:

### Option A: Import the Markdown File (Recommended)

1. Open Notion and navigate to the workspace where you want SiteOS
2. Click the **"..."** menu in the sidebar or use **Import** from the bottom of the sidebar
3. Select **"Import" → "Markdown & CSV"**
4. Choose the `siteos-main.md` file
5. Notion will create a new page with all the content, headings, and structure

### Option B: Copy-Paste

1. Open `siteos-main.md` in any text editor
2. Select all content (Cmd+A / Ctrl+A)
3. In Notion, create a new blank page
4. Paste (Cmd+V / Ctrl+V) — Notion will convert the Markdown to Notion blocks

> **Note:** Option A preserves formatting more reliably. If toggle sections don't import correctly, you can manually create them by typing `/toggle` in Notion.

---

## Step 2: Create the Databases

For each CSV file in the `databases/` folder, you'll create a Notion database.

### How to Create a Database from CSV

1. In your SiteOS page, go to the relevant section (e.g., scroll to "Project Tracker")
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
2. **Subcontractors** — `databases/subcontractors.csv`
3. **Defects** — `databases/defects.csv`
4. **RFIs** — `databases/rfis.csv`
5. **Variations** — `databases/variations.csv`
6. **Safety Incidents** — `databases/safety-incidents.csv`
7. **Progress Claims** — `databases/progress-claims.csv`
8. **Site Diary** — `databases/site-diary.csv`
9. **Meetings** — `databases/meetings.csv`

### Setting Property Types

After import, Notion may not get every property type right. Go through each database and correct the types:

**Projects:**
| Property | Set Type To |
|----------|------------|
| Contract Value | Number (format as AUD) |
| Status | Select |
| Start Date | Date |
| End Date | Date |
| % Complete | Number (format as Percent) |

**Subcontractors:**
| Property | Set Type To |
|----------|------------|
| Insurance Expiry | Date |
| License Expiry | Date |
| Induction Status | Select |
| Approved | Checkbox |

**Defects:**
| Property | Set Type To |
|----------|------------|
| Category | Select |
| Priority | Select |
| Status | Select |
| Date Reported | Date |
| Date Due | Date |
| Date Closed | Date |
| Photo Link | URL |

**RFIs:**
| Property | Set Type To |
|----------|------------|
| Status | Select |
| Date Submitted | Date |
| Date Required | Date |
| Date Responded | Date |
| Impact on Cost | Select |
| Impact on Time | Select |

**Variations:**
| Property | Set Type To |
|----------|------------|
| Reason | Select |
| Status | Select |
| Cost Impact ($) | Number (format as AUD) |
| Time Impact (Days) | Number |
| Submitted Date | Date |
| Approved Date | Date |

**Safety Incidents:**
| Property | Set Type To |
|----------|------------|
| Type | Select |
| Status | Select |
| Date | Date |

**Progress Claims:**
| Property | Set Type To |
|----------|------------|
| Claim Type | Select |
| Status | Select |
| Amount Claimed ($) | Number (format as AUD) |
| Amount Approved ($) | Number (format as AUD) |
| Retention Held ($) | Number (format as AUD) |
| Net Payment ($) | Number (format as AUD) |
| Date Submitted | Date |
| Date Approved | Date |

**Site Diary:**
| Property | Set Type To |
|----------|------------|
| Date | Date |
| Weather | Select |
| Temperature | Number |

**Meetings:**
| Property | Set Type To |
|----------|------------|
| Meeting Type | Select |
| Date | Date |
| Next Meeting Date | Date |

---

## Step 3: Set Up Database Relations

Relations are what make SiteOS powerful. They connect your data so a single project shows all its defects, RFIs, variations, and everything else.

### How to Create a Relation

1. Open the database you want to add a relation to
2. Click **"+"** to add a new property
3. Select **"Relation"**
4. Choose the database to relate to
5. Name the property clearly

### Relations to Create

| In This Database | Add Relation To | Property Name | Notes |
|-----------------|----------------|---------------|-------|
| Defects | Projects | Project | Replace the existing text "Project" column |
| RFIs | Projects | Project | Replace the existing text "Project" column |
| Variations | Projects | Project | Replace the existing text "Project" column |
| Safety Incidents | Projects | Project | Replace the existing text "Project" column |
| Progress Claims | Projects | Project | Replace the existing text "Project" column |
| Site Diary | Projects | Project | Replace the existing text "Project" column |
| Meetings | Projects | Project | Replace the existing text "Project" column |

**For each relation above:**
1. Delete the original text-based "Project" column (it was imported from CSV as plain text)
2. Create a new Relation property called "Project"
3. Link it to the Projects database
4. Go through each row and select the correct project from the relation picker

> **Tip:** When you create a relation, Notion asks if you want to show it in the related database too. Always say **Yes**. This means your Projects database will automatically show a "Defects" column listing all related defects, an "RFIs" column, etc.

### Optional Relations

| In This Database | Add Relation To | Property Name | Purpose |
|-----------------|----------------|---------------|---------|
| Defects | Subcontractors | Assigned To (Relation) | Link defects to the responsible subbie |
| Progress Claims | Subcontractors | Contractor (Relation) | Link claims to the claiming subbie |

---

## Step 4: Set Up Dashboard Views

The Dashboard section of your main SiteOS page should contain **linked database views** — not copies of the databases, but filtered views of them.

### How to Create a Linked Database View

1. Navigate to the Dashboard section of your SiteOS page
2. Type `/linked` and select **"Linked view of database"**
3. Choose the source database (e.g., Projects)
4. Configure the view:

### Dashboard Views to Create

**1. Active Projects Board**
- Source: Projects
- View type: Board
- Group by: Status
- Filter: Status is not "Complete"

**2. Critical Defects**
- Source: Defects
- View type: Table
- Filter: Priority is "Critical" or "High" AND Status is not "Closed"
- Sort: Date Due ascending

**3. Open RFIs**
- Source: RFIs
- View type: Table
- Filter: Status is "Open"
- Sort: Date Required ascending

**4. Pending Variations**
- Source: Variations
- View type: Table
- Filter: Status is "Draft" or "Submitted" or "Pending"
- Sort: Cost Impact descending

**5. Recent Safety Incidents**
- Source: Safety Incidents
- View type: Table
- Filter: Date is within the last 30 days
- Sort: Date descending

**6. Upcoming Claims**
- Source: Progress Claims
- View type: Table
- Filter: Status is "Draft" or "Submitted" or "Under Review"
- Sort: Date Submitted ascending

**7. This Week's Site Diary**
- Source: Site Diary
- View type: Table
- Filter: Date is within this week
- Sort: Date descending

---

## Step 5: Customise for Your Company

### Replace Sample Data

The CSV files include sample data from fictional projects. Delete these rows and start entering your own data. The sample data is there to show you the format and level of detail expected in each field.

### Add Your Company Details

At the top of the SiteOS page, replace the intro text with:
- Your company name and logo (drag an image block)
- Your active project list
- Key contact numbers (site emergency, project manager, etc.)

### Customise Select Options

The Select properties (Status, Category, Priority, etc.) may need additional options for your workflow:
- Click on any Select property → "Edit property" → add/remove options
- Add trades to the Subcontractor Trade list that match your typical project scope
- Add meeting types if you have recurring meetings not covered (e.g., "PCG Meeting", "Consultant Coordination")

### Set Up Notion Automations

Go to the **"..."** menu on each database → **"Automations"**:

1. **Auto-date on status change:** When Defect Status changes to "Closed" → Set Date Closed to today
2. **Overdue notifications:** When RFI Date Required is reached and Status is still "Open" → Send notification
3. **Insurance expiry alerts:** When Subcontractor Insurance Expiry is within 30 days → Send notification

---

## Step 6: Get Your Team Using It

### Rollout Strategy

**Week 1: Just You**
- Set up the full system following this guide
- Enter your current project data
- Use it yourself for one full week to work out the kinks

**Week 2: Add Your Superintendent**
- Start with Site Diary only — one database, one daily task
- Show them the mobile app and how to create entries from their phone
- Review their entries daily and give feedback on level of detail

**Week 3: Add Defect Tracking**
- Superintendent starts logging defects on site
- You review and assign to subcontractors
- Run defect meetings using the Board View

**Week 4: Full Rollout**
- Add remaining team members
- Introduce RFIs, Variations, and Progress Claims
- Set up weekly reporting rhythm using dashboard views

### Tips for Adoption

1. **Don't mandate everything at once.** Start with 1-2 databases and expand.
2. **Make it the single source of truth.** If someone asks about a defect status, point them to SiteOS. Don't maintain a parallel spreadsheet.
3. **Use the mobile app.** Install Notion on all site phones/tablets. Bookmark the key databases for quick access.
4. **Review together.** Pull up the Dashboard in site meetings. When the team sees their data being used for decisions, they'll take entry more seriously.
5. **Celebrate the wins.** "We found that overdue RFI because it was tracked in SiteOS" — that's your adoption story.

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

You've got this. The hardest part is the initial setup — once it's running, SiteOS saves you hours every week.
