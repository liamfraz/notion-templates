# YouTube Command Center -- Setup Guide

Follow these steps to get your workspace running. Allow 45-60 minutes for initial setup.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace.
2. Create a new page called **"YouTube Command Center"** (or whatever you prefer).
3. Click the **"..."** menu in the top-right, then **Import** > **Markdown**.
4. Select `youtube-calendar-main.md`.
5. The full template structure will import as your main hub page.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### 2.1 Import Each CSV

1. Inside your YouTube Command Center page, create a new sub-page for the database (e.g., "Videos").
2. On the sub-page, click **"..."** > **Import** > **CSV**.
3. Select the CSV file. Notion will create a table with all columns and sample data.
4. Repeat for all 6 databases:
   - `videos.csv` -- Videos
   - `analytics.csv` -- Analytics Tracker
   - `thumbnails.csv` -- Thumbnail Tracker
   - `playlists.csv` -- Playlists
   - `revenue.csv` -- Revenue Tracker
   - `ideas.csv` -- Idea Pipeline

### 2.2 Set Column Types

After import, update column types for accurate filtering and formulas:

**Videos:**
| Column | Type |
|---|---|
| Title | Title |
| Status | Select (Idea / Scripting / Filming / Editing / Thumbnail / Scheduled / Published / Evergreen) |
| Category | Select (Tutorial / Review / Vlog / Listicle / Commentary / Behind the Scenes / Collaboration / Shorts) |
| Publish Date | Date |
| Target Length | Text |
| Thumbnail Status | Select (Not Started / Designing / A-B Testing / Final) |
| SEO Score | Select (High / Medium / Low) |
| Sponsor | Text |
| Notes | Text |

**Analytics:**
| Column | Type |
|---|---|
| Video Title | Title |
| Views | Number |
| Watch Hours | Number |
| Avg View Duration | Text |
| CTR (%) | Number (percent format) |
| Impressions | Number |
| Likes | Number |
| Comments | Number |
| Subscribers Gained | Number |
| Revenue ($) | Number (AUD currency format) |
| Published Date | Date |
| Performance Rating | Select (Viral / Above Average / Average / Below Average / Flop) |

**Thumbnails:**
| Column | Type |
|---|---|
| Video Title | Title |
| Version | Select (A / B / C / Final) |
| Style | Select (Face + Text / Graphic / Screenshot / Reaction / Comparison / Before-After) |
| CTR (%) | Number (percent format) |
| Impressions | Number |
| Status | Select (Testing / Winner / Retired) |
| Notes | Text |

**Playlists:**
| Column | Type |
|---|---|
| Playlist Name | Title |
| Videos Count | Number |
| Total Views | Number |
| Category | Text |
| Status | Select (Active / Growing / Archived) |
| Strategy | Select (Evergreen / Series / Seasonal / Topical) |
| Last Updated | Date |
| Notes | Text |

**Revenue:**
| Column | Type |
|---|---|
| Month | Date |
| Source | Select (AdSense / Memberships / Super Chats / Merch Shelf / Affiliate / Sponsorship) |
| Amount ($) | Number (AUD currency format) |
| Type | Select (Passive / Active / Recurring) |
| Notes | Text |

**Ideas:**
| Column | Type |
|---|---|
| Title | Title |
| Category | Select (Tutorial / Review / Vlog / Listicle / Commentary / Behind the Scenes / Collaboration / Shorts) |
| Priority | Select (Hot / Medium / Low / Someday) |
| SEO Potential | Select (High / Medium / Low) |
| Competition | Select (High / Medium / Low) |
| Search Volume | Select (High / Medium / Low) |
| Target Audience | Text |
| Notes | Text |

---

## Step 3: Set Up Relations

Relations link your databases together for powerful cross-referencing.

### 3.1 Create These Relations

1. **Analytics -> Videos**
   - In the Analytics database, add a "Relation" column linked to Videos.
   - Match records by Video Title.

2. **Thumbnails -> Videos**
   - In the Thumbnails database, add a "Relation" column linked to Videos.
   - Match records by Video Title.

3. **Ideas -> Videos** (optional)
   - Link ideas to the video they become when moved to production.

4. **Revenue -> Videos** (optional)
   - Link sponsorship revenue entries to their specific video.

### 3.2 After Linking, Update Existing Records

Go through the sample data and link records using the new relation columns. For example, link the "How I Edit YouTube Videos in 2026" analytics entry to its Videos entry.

---

## Step 4: Configure Formulas

Add these formula columns to automate calculations.

### Analytics -- Engagement Rate

```
round((prop("Likes") + prop("Comments")) / prop("Views") * 100 * 100) / 100
```

### Analytics -- Revenue Per 1K Views (RPM)

```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

### Analytics -- Subscriber Conversion Rate

```
if(prop("Views") > 0, round(prop("Subscribers Gained") / prop("Views") * 100 * 100) / 100, 0)
```

### Analytics -- CTR Performance Flag

```
if(prop("CTR") >= 8, "Excellent", if(prop("CTR") >= 5, "Good", if(prop("CTR") >= 3, "Average", "Needs Work")))
```

### Videos -- Days Since Published

```
dateBetween(now(), prop("Publish Date"), "days")
```

---

## Step 5: Set Up Rollups

Rollups aggregate data from related databases.

### On Video Records (if linked to Analytics)

1. **Total Views** -- Rollup from Analytics relation, "Views" column, Sum
2. **Total Revenue** -- Rollup from Analytics relation, "Revenue" column, Sum
3. **Best CTR** -- Rollup from Thumbnails relation, "CTR" column, Max

### On Playlist Records (if linked to Videos)

1. **Total Watch Hours** -- Rollup from Videos relation via Analytics, "Watch Hours" column, Sum

### On Revenue (Monthly Dashboard)

1. **Monthly Total** -- Group by Month, Sum of Amount (use a Table view grouped by Month)

---

## Step 6: Create Views

Set up multiple views for each database (the main template page lists recommended views).

**Quick wins:**

- **Videos** -- Board view grouped by Status (drag videos through production stages)
- **Videos** -- Calendar view by Publish Date
- **Analytics** -- Table filtered to Viral and Above Average (learn from wins)
- **Analytics** -- Table sorted by CTR descending (find best thumbnails)
- **Thumbnails** -- Grouped by Video Title (see all versions side by side)
- **Thumbnails** -- Filtered to Status = Testing (active A/B tests)
- **Playlists** -- Table sorted by Total Views descending
- **Revenue** -- Table grouped by Month
- **Revenue** -- Table grouped by Source
- **Ideas** -- Board view grouped by Priority (Hot / Medium / Low / Someday)
- **Ideas** -- Filtered to SEO Potential = High

---

## Step 7: Replace Sample Data

1. Review all sample data to understand the structure and relationships.
2. Delete sample entries and add your own real channel data.
3. Start with the Videos database -- plan your next 2-3 uploads.
4. Add analytics for your most recent published videos.
5. Log your current month's revenue by source.
6. Populate playlists with your actual playlist names and video counts.

**Tip:** Keep a few sample entries as reference while you're getting started. Delete them once you're comfortable with the structure.

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
- For the CTR Performance Flag formula, make sure your CTR column stores a plain number (e.g., 7.8), not a percentage (0.078).

**Numbers displaying incorrectly**
- Click the column header, choose "Number format", and select the right format (Number, Percent, or Currency).
- For Revenue columns, select "Australian Dollar" or "Number" depending on your preference.

**Thumbnail CTR not updating**
- YouTube Studio updates CTR data with a delay. Wait 24-48 hours after uploading a new thumbnail before recording CTR.
- Ensure you have at least 10,000 impressions per thumbnail version before comparing results.

**Avg View Duration showing as text**
- AVD is stored as text (e.g., "9:34") for readability. If you need to calculate with it, create a separate "AVD Minutes" number column and convert manually.

---

*Setup complete. Start by adding your next 3 planned videos to the Videos database.*
