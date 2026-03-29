# Content Creator Command Center — Setup Guide

Follow these steps to get your workspace running. Allow 45-60 minutes for initial setup.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace.
2. Create a new page called **"Creator Command Center"** (or whatever you prefer).
3. Click the **"..."** menu in the top-right, then **Import** > **Markdown**.
4. Select `creator-os-main.md`.
5. The full template structure will import as your main hub page.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### 2.1 Import Each CSV

1. Inside your Creator Command Center page, create a new sub-page for the database (e.g., "Content Calendar").
2. On the sub-page, click **"..."** > **Import** > **CSV**.
3. Select the CSV file. Notion will create a table with all columns and sample data.
4. Repeat for all 6 databases:
   - `content-calendar.csv` — Content Calendar
   - `analytics.csv` — Analytics Tracker
   - `brand-deals.csv` — Brand Deals Pipeline
   - `income.csv` — Income Tracker
   - `platforms.csv` — Platform Manager
   - `ideas.csv` — Idea Bank

### 2.2 Set Column Types

After import, update column types for accurate filtering and formulas:

**Content Calendar:**
| Column | Type |
|---|---|
| Title | Title |
| Platform | Select (YouTube / TikTok / Instagram / Twitter/X / LinkedIn / Newsletter / Blog / Podcast) |
| Content Type | Select (Long-form Video / Short-form Video / Reel / Thread / Article / Newsletter Issue / Carousel / Podcast Episode) |
| Status | Select (Idea / Scripting / Filming / Editing / Scheduled / Published / Evergreen) |
| Publish Date | Date |
| Topic | Select (AI Tools Review / Productivity Tips / Behind the Scenes / Tutorial / Hot Take / Collaboration / Q&A) |
| Category | Text |
| Engagement Goal | Text |
| Notes | Text |

**Analytics:**
| Column | Type |
|---|---|
| Content Title | Title |
| Platform | Select (same options as Content Calendar) |
| Views | Number |
| Likes | Number |
| Comments | Number |
| Shares | Number |
| Click-Through Rate (%) | Number (percent format) |
| Revenue ($) | Number (AUD format) |
| Published Date | Date |
| Performance Rating | Select (Viral / Above Average / Average / Below Average / Flop) |

**Brand Deals:**
| Column | Type |
|---|---|
| Brand | Title |
| Status | Select (Pitched / Negotiating / Contracted / In Progress / Delivered / Paid / Declined) |
| Platform | Select (same options) |
| Fee ($) | Number (AUD format) |
| Deliverables | Text |
| Deadline | Date |
| Contact | Text |
| Payment Status | Select (Pending / Invoiced / Paid / Overdue) |
| Category | Select (Sponsor / Affiliate / Ambassador / One-off) |

**Income:**
| Column | Type |
|---|---|
| Month | Date |
| Source | Select (Ad Revenue / Sponsorships / Affiliate / Digital Products / Coaching / Memberships / Donations) |
| Amount ($) | Number (AUD format) |
| Type | Select (Passive / Active / Recurring) |
| Platform | Text |
| Notes | Text |

**Platforms:**
| Column | Type |
|---|---|
| Platform | Title |
| Handle | Text |
| Followers | Number |
| Monthly Growth | Number |
| Content Frequency | Text |
| Primary Format | Text |
| Status | Select (Active / Growing / Paused / New) |
| Priority | Select (Primary / Secondary / Experimental) |

**Ideas:**
| Column | Type |
|---|---|
| Idea | Title |
| Platform | Select (same options) |
| Category | Text |
| Priority | Select (Hot / Medium / Low / Someday) |
| Status | Select (Backlog / Researching / Ready to Create / In Production / Published) |
| Source | Select (Audience Request / Trending / Evergreen / Collaboration / Personal) |
| Potential | Select (High / Medium / Low) |
| Notes | Text |

---

## Step 3: Set Up Relations

Relations link your databases together for powerful cross-referencing.

### 3.1 Create These Relations

1. **Analytics -> Content Calendar**
   - In the Analytics database, add a "Relation" column linked to Content Calendar.
   - Match records by Content Title.

2. **Content Calendar -> Platforms** (optional)
   - Link content entries to their platform record for rollups.

3. **Brand Deals -> Platforms** (optional)
   - Link brand deals to the platform they're for.

4. **Ideas -> Content Calendar** (optional)
   - Link ideas to the content they become when moved to production.

### 3.2 After Linking, Update Existing Records

Go through the sample data and link records using the new relation columns. For example, link the "5 AI Tools That Replaced My VA" analytics entry to its Content Calendar entry.

---

## Step 4: Configure Formulas

Add these formula columns to automate calculations.

### Analytics — Engagement Rate

```
round((prop("Likes") + prop("Comments") + prop("Shares")) / prop("Views") * 100 * 100) / 100
```

### Analytics — Revenue Per 1K Views (RPM)

```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

### Brand Deals — Days Until Deadline

```
if(prop("Status") == "Paid" or prop("Status") == "Declined", 0, dateBetween(prop("Deadline"), now(), "days"))
```

### Platforms — Growth Rate (%)

```
if(prop("Followers") > 0, round(prop("Monthly Growth") / prop("Followers") * 100 * 100) / 100, 0)
```

---

## Step 5: Set Up Rollups

Rollups aggregate data from related databases.

### On Platform Records (if using relations)

1. **Total Content** — Rollup from Content Calendar relation, Count
2. **Total Revenue** — Rollup from Income relation, "Amount" column, Sum

### On Content Calendar Records (if linked to Analytics)

1. **Total Views** — Rollup from Analytics relation, "Views" column, Sum
2. **Total Revenue** — Rollup from Analytics relation, "Revenue" column, Sum

---

## Step 6: Customise Your Platforms

1. Open the Platforms database.
2. Replace the sample handles and follower counts with your actual data.
3. Set the correct Priority and Status for each platform.
4. Remove any platforms you don't use.

---

## Step 7: Create Views

Set up multiple views for each database (the main template page lists recommended views).

**Quick wins:**

- **Content Calendar** — Board view grouped by Status (drag content through stages)
- **Content Calendar** — Calendar view by Publish Date
- **Analytics** — Table filtered to Viral and Above Average (learn from wins)
- **Brand Deals** — Board view grouped by Status
- **Income** — Table grouped by Month
- **Ideas** — Board view grouped by Priority (Hot / Medium / Low / Someday)

---

## Step 8: Replace Sample Data

1. Review all sample data to understand the structure.
2. Delete sample entries and add your own real content.
3. Start with the Content Calendar — plan your next 2 weeks.
4. Add your actual brand deals and income data.

**Tip:** Keep a few sample entries as reference while you're getting started. Delete them once you're comfortable.

---

## Step 9: Set Up Your Dashboard

The Creator Dashboard section on the main page uses manual values by default. To make it dynamic:

1. Create **linked database views** (filtered and sorted) inline on the dashboard page.
2. Use Notion's **database rollups** to pull live numbers.
3. Alternatively, update the dashboard manually during your monthly review.

**Key metrics to track:**
- Total income this month (sum of Income entries for current month)
- Content output (count of Published content this month)
- Follower growth (compare Platforms database month over month)
- Brand deal pipeline value (sum of Fees where Status is not Paid/Declined)

---

## Step 10: Ongoing Usage

### Daily
- Update Content Calendar status as you work through stages
- Capture new ideas in the Idea Bank immediately

### Weekly
- Review Content Calendar — is this week's content on track?
- Log analytics for published content (after 7 days)
- Update follower counts in Platforms database
- Engage with audience and note trending topics

### Monthly
- Run the Monthly Creator Review (block 90 minutes)
- Update income tracker with all revenue received
- Review brand deal pipeline — follow up on pitches
- Clean up Idea Bank — archive stale ideas, promote hot ones
- Update Platform Manager with current follower counts

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

**Numbers displaying incorrectly**
- Click the column header, choose "Number format", and select the right format (Number, Percent, or Currency).

---

*Setup complete. Start by planning your next week of content in the Content Calendar.*
