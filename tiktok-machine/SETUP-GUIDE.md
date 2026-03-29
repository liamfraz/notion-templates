# TikTok & Reels Content Machine — Setup Guide

Follow these steps to get your workspace running. Allow 30-45 minutes for initial setup.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace.
2. Create a new page called **"Content Machine"** (or whatever you prefer).
3. Click the **"..."** menu in the top-right, then **Import** > **Markdown**.
4. Select `tiktok-machine-main.md`.
5. The full template structure will import as your main hub page.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### 2.1 Import Each CSV

1. Inside your Content Machine page, create a new sub-page for the database (e.g., "Content Pipeline").
2. On the sub-page, click **"..."** > **Import** > **CSV**.
3. Select the CSV file. Notion will create a table with all columns and sample data.
4. Repeat for all 6 databases:
   - `content-pipeline.csv` — Content Pipeline
   - `hooks-library.csv` — Hooks Library
   - `hashtag-tracker.csv` — Hashtag Tracker
   - `sounds-trends.csv` — Sounds & Trends
   - `analytics.csv` — Analytics
   - `posting-schedule.csv` — Posting Schedule

### 2.2 Set Column Types

After import, update column types for accurate filtering and formulas:

**Content Pipeline:**
| Column | Type |
|---|---|
| Title | Title |
| Platform | Select (TikTok / Instagram Reels / YouTube Shorts / All) |
| Status | Select (Idea / Scripting / Filming / Editing / Scheduled / Posted / Viral / Archived) |
| Category | Select (Tutorial / Trend / Story Time / POV / Get Ready With Me / Day in Life / Reaction / Educational / Comedy) |
| Hook Type | Select (Question / Bold Claim / Controversy / Curiosity Gap / Pattern Interrupt / Before-After) |
| Post Date | Date |
| Duration (seconds) | Number |
| Sound | Text |
| Notes | Text |

**Hooks Library:**
| Column | Type |
|---|---|
| Hook Text | Title |
| Category | Select (Question / Bold Claim / Controversy / Curiosity Gap / Pattern Interrupt / Before-After / How To / List) |
| Niche | Select (Productivity / Tech / Lifestyle / Business / Finance / Fitness / Food / Travel) |
| Times Used | Number |
| Avg Completion Rate (%) | Number (percent format) |
| Performance Rating | Select (Viral / Strong / Average / Weak) |
| Notes | Text |

**Hashtag Tracker:**
| Column | Type |
|---|---|
| Hashtag | Title |
| Category | Select (Niche / Trending / Community / Branded / Challenge) |
| Platform | Select (TikTok / Instagram / YouTube Shorts / All) |
| Posts Using | Number |
| Avg Views When Used | Number |
| Status | Select (Active / Declining / Retired / Testing) |
| Last Used | Date |
| Notes | Text |

**Sounds & Trends:**
| Column | Type |
|---|---|
| Sound Name | Title |
| Platform | Select (TikTok / Instagram Reels / YouTube Shorts) |
| Status | Select (Trending / Peak / Declining / Evergreen) |
| Category | Select (Music / Voiceover / Original Audio / Remix / Sound Effect) |
| First Spotted | Date |
| Times Used | Number |
| Avg Performance Rating | Select (Viral / Strong / Average / Weak) |
| Content Ideas | Text |
| Notes | Text |

**Analytics:**
| Column | Type |
|---|---|
| Video Title | Title |
| Platform | Select (TikTok / Instagram Reels / YouTube Shorts) |
| Views | Number |
| Completion Rate (%) | Number (percent format) |
| Shares | Number |
| Saves | Number |
| Comments | Number |
| Likes | Number |
| Revenue ($) | Number (AUD currency format) |
| Posted Date | Date |
| Performance Rating | Select (Viral / Above Average / Average / Below Average / Flop) |

**Posting Schedule:**
| Column | Type |
|---|---|
| Day | Title |
| Time Slot | Text |
| Platform | Select (TikTok / Instagram Reels / YouTube Shorts) |
| Content Type | Select (Tutorial / Trend / Story Time / POV / Educational / Comedy) |
| Status | Select (Scheduled / Posted / Skipped) |
| Performance Rating | Select (Viral / Strong / Average / Weak) |
| Notes | Text |

---

## Step 3: Set Up Relations

Relations link your databases together for powerful cross-referencing.

### 3.1 Create These Relations

1. **Analytics -> Content Pipeline**
   - In the Analytics database, add a "Relation" column linked to Content Pipeline.
   - Match records by Video Title.

2. **Content Pipeline -> Hooks Library** (optional)
   - Link videos to the hook they used for performance tracking.

3. **Content Pipeline -> Sounds & Trends** (optional)
   - Link videos to the sound used so you can track sound performance.

4. **Content Pipeline -> Hashtag Tracker** (optional)
   - Link videos to hashtags used for hashtag performance analysis.

### 3.2 After Linking, Update Existing Records

Go through the sample data and link records using the new relation columns. For example, link the "Why Your Morning Routine Is Wasting Your Time" analytics entry to its Content Pipeline entry.

---

## Step 4: Configure Formulas

Add these formula columns to automate calculations.

### Analytics — Engagement Rate

```
round((prop("Likes") + prop("Comments") + prop("Shares") + prop("Saves")) / prop("Views") * 100 * 100) / 100
```

### Analytics — Share Rate

```
if(prop("Views") > 0, round(prop("Shares") / prop("Views") * 100 * 100) / 100, 0)
```

### Analytics — Save Rate

```
if(prop("Views") > 0, round(prop("Saves") / prop("Views") * 100 * 100) / 100, 0)
```

### Analytics — Revenue Per 1K Views

```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

### Hooks Library — Success Score

```
if(prop("Times Used") > 0, round(prop("Avg Completion Rate") * prop("Times Used") / 10), 0)
```

### Hashtag Tracker — Views Per Post

```
if(prop("Posts Using") > 0, round(prop("Avg Views When Used") / prop("Posts Using")), 0)
```

---

## Step 5: Create Views

Set up multiple views for each database to surface the right information at the right time.

### Content Pipeline Views

- **Board View** — Kanban grouped by Status. Drag videos through Idea, Scripting, Filming, Editing, Scheduled, Posted, Viral, Archived.
- **By Platform** — Table view grouped by Platform. See content distribution across TikTok, Reels, and Shorts.
- **This Week** — Table filtered to Post Date = this week. Your current publishing queue.
- **Filming Queue** — Table filtered to Status = Scripting or Filming. Batch your shoot days.
- **Viral Hits** — Table filtered to Status = Viral. Study what worked and replicate.

### Hooks Library Views

- **All Hooks** — Table sorted by Performance Rating descending. Best hooks first.
- **By Category** — Table grouped by Category. Browse by hook type.
- **Top Performers** — Table filtered to Performance Rating = Viral or Strong.
- **By Niche** — Table grouped by Niche. Quick selection when creating niche content.
- **Unused** — Table filtered to Times Used = 0. Fresh hooks to test.

### Hashtag Tracker Views

- **Active Hashtags** — Table filtered to Status = Active, sorted by Avg Views When Used descending.
- **By Platform** — Table grouped by Platform. Platform-specific hashtag sets.
- **Declining** — Table filtered to Status = Declining or Retired. Stop using these.
- **Testing** — Table filtered to Status = Testing. Monitor new hashtags.

### Sounds & Trends Views

- **Currently Trending** — Table filtered to Status = Trending or Peak. Act on these now.
- **Evergreen Library** — Table filtered to Status = Evergreen. Safe to use anytime.
- **By Platform** — Table grouped by Platform.
- **Recently Spotted** — Table sorted by First Spotted descending.

### Analytics Views

- **All Videos** — Table sorted by Posted Date descending. Full history.
- **Top Performers** — Table filtered to Performance Rating = Viral or Above Average.
- **By Platform** — Table grouped by Platform, sorted by Views descending.
- **Completion Rate Leaderboard** — Table sorted by Completion Rate descending.
- **Revenue Generating** — Table filtered where Revenue > 0.
- **Flop Review** — Table filtered to Flop or Below Average. Learn from these.

### Posting Schedule Views

- **Weekly Grid** — Table grouped by Day. Your at-a-glance weekly plan.
- **By Platform** — Table grouped by Platform.
- **Active Schedule** — Table filtered to Status = Scheduled.
- **Performance Review** — Table sorted by Performance Rating descending.

---

## Step 6: Replace Sample Data

1. Review all sample data to understand the structure.
2. Delete sample entries and add your own content ideas and posted videos.
3. Start with the Content Pipeline — plan your next 7-10 videos.
4. Add your actual posting schedule time slots.
5. Build your Hooks Library with hooks you've used or want to test.

**Tip:** Keep a few sample entries as reference while you're getting started. Delete them once you're comfortable.

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

**Completion rate showing wrong values**
- Completion rate should be entered as a whole number (e.g., 73 not 0.73). Set the column format to "Percent" only if you enter decimal values.

**Hashtags not matching across databases**
- Ensure hashtag names include the # symbol consistently. Use the same casing across all entries.

---

*Setup complete. Start by planning your next week of short-form content in the Content Pipeline.*
