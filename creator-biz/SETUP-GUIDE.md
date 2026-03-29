# Creator Business OS — Setup Guide

Follow these steps to get your workspace running. Allow 60-90 minutes for initial setup.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace.
2. Create a new page called **"Creator Business OS"** (or whatever you prefer).
3. Click the **"..."** menu in the top-right, then **Import** > **Markdown**.
4. Select `creator-biz-main.md`.
5. The full template structure will import as your main hub page.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### 2.1 Import Each CSV

1. Inside your Creator Business OS page, create a new sub-page for the database (e.g., "Income Streams").
2. On the sub-page, click **"..."** > **Import** > **CSV**.
3. Select the CSV file. Notion will create a table with all columns and sample data.
4. Repeat for all 7 databases:
   - `income-streams.csv` — Income Streams
   - `brand-deals.csv` — Brand Deals Pipeline
   - `expenses.csv` — Expense Tracker
   - `sponsors-crm.csv` — Sponsors CRM
   - `invoices.csv` — Invoice Tracker
   - `goals.csv` — Financial Goals
   - `products.csv` — Digital Products

### 2.2 Set Column Types

After import, update column types for accurate filtering and formulas:

**Income Streams:**
| Column | Type |
|---|---|
| Stream Name | Title |
| Type | Select (Ad Revenue / Sponsorship / Affiliate / Digital Products / Coaching / Memberships / Merch / Licensing) |
| Platform | Text |
| Monthly Revenue ($) | Number (currency format) |
| Monthly Expenses ($) | Number (currency format) |
| Net Profit ($) | Number (currency format) |
| Status | Select (Active / Growing / Paused / New / Declining) |
| Effort (hrs/week) | Number |
| Started | Date |
| Notes | Text |

**Brand Deals:**
| Column | Type |
|---|---|
| Brand | Title |
| Status | Select (Lead / Pitched / Negotiating / Contracted / In Progress / Delivered / Invoiced / Paid / Declined) |
| Platform | Text |
| Deal Value ($) | Number (currency format) |
| Deliverables | Text |
| Deadline | Date |
| Contact Name | Text |
| Contact Email | Email |
| Payment Terms | Text |
| Category | Select (Sponsor / Affiliate / Ambassador / UGC / Licensing) |
| Notes | Text |

**Expenses:**
| Column | Type |
|---|---|
| Expense | Title |
| Category | Select (Software / Equipment / Contractors / Advertising / Education / Travel / Office / Insurance / Accounting) |
| Amount ($) | Number (currency format) |
| Frequency | Select (Monthly / Annual / One-off / Quarterly) |
| Tax Deductible | Checkbox |
| Vendor | Text |
| Date | Date |
| Notes | Text |

**Sponsors CRM:**
| Column | Type |
|---|---|
| Company | Title |
| Contact Name | Text |
| Contact Email | Email |
| Relationship Stage | Select (Cold / Warm / Hot / Active Partner / Past Partner) |
| Last Contact | Date |
| Deal History ($) | Number (currency format) |
| Platform Fit | Select (YouTube / TikTok / Instagram / Newsletter / Podcast / Multiple) |
| Industry | Select (Tech / Finance / Lifestyle / Health / SaaS / E-commerce / Education) |
| Notes | Text |

**Invoices:**
| Column | Type |
|---|---|
| Invoice Number | Title |
| Client | Text |
| Amount ($) | Number (currency format) |
| Status | Select (Draft / Sent / Paid / Overdue / Cancelled) |
| Issue Date | Date |
| Due Date | Date |
| Paid Date | Date |
| Payment Method | Select (Bank Transfer / PayPal / Stripe / Other) |
| Category | Select (Sponsorship / Freelance / Product / Licensing) |
| Notes | Text |

**Goals:**
| Column | Type |
|---|---|
| Goal | Title |
| Category | Select (Revenue / Growth / Product / Brand Deals / Savings / Investment) |
| Target ($) | Number (currency format) |
| Current ($) | Number (currency format) |
| Status | Select (On Track / Behind / Ahead / Completed / Not Started) |
| Deadline | Date |
| Priority | Select (High / Medium / Low) |
| Quarter | Select (Q1 2026 / Q2 2026 / Q3 2026 / Q4 2026) |
| Notes | Text |

**Products:**
| Column | Type |
|---|---|
| Product Name | Title |
| Type | Select (Template / Course / E-book / Preset Pack / Membership / Workshop / Printable) |
| Platform | Select (Gumroad / Teachable / Etsy / Shopify / Own Site / Stan Store) |
| Price ($) | Number (currency format) |
| Units Sold | Number |
| Revenue ($) | Number (currency format) |
| Status | Select (Active / Draft / Archived / Coming Soon) |
| Launch Date | Date |
| Notes | Text |

---

## Step 3: Set Up Relations

Relations link your databases together for powerful cross-referencing.

### 3.1 Create These Relations

1. **Brand Deals -> Sponsors CRM**
   - In the Brand Deals database, add a "Relation" column linked to Sponsors CRM.
   - Match each deal to its company record.

2. **Brand Deals -> Invoices**
   - In the Brand Deals database, add a "Relation" column linked to Invoices.
   - Link each deal to its corresponding invoice.

3. **Products -> Income Streams**
   - In the Products database, add a "Relation" column linked to Income Streams.
   - Link products to their revenue stream (e.g., "Notion Template Shop").

4. **Income Streams -> Brand Deals** (optional)
   - Link sponsorship income streams to their specific deals for drill-down.

### 3.2 After Linking, Update Existing Records

Go through the sample data and link records using the new relation columns. For example, link the "Canva" brand deal to the "Canva" record in Sponsors CRM, and link it to invoice INV-2026-003.

---

## Step 4: Configure Formulas

Add these formula columns to automate calculations.

### Income Streams — Profit Margin %

```
if(prop("Monthly Revenue ($)") > 0, round((prop("Monthly Revenue ($)") - prop("Monthly Expenses ($)")) / prop("Monthly Revenue ($)") * 100 * 100) / 100, 0)
```

### Income Streams — Revenue Per Hour

```
if(prop("Effort (hrs/week)") > 0, round(prop("Net Profit ($)") / (prop("Effort (hrs/week)") * 4.33) * 100) / 100, 0)
```

### Invoices — Days Until Due

```
if(prop("Status") == "Paid" or prop("Status") == "Cancelled", 0, dateBetween(prop("Due Date"), now(), "days"))
```

### Invoices — Overdue Flag

```
if(prop("Status") == "Sent" and now() > prop("Due Date"), "OVERDUE", "")
```

### Goals — Progress %

```
if(prop("Target ($)") > 0, round(prop("Current ($)") / prop("Target ($)") * 100 * 100) / 100, 0)
```

### Products — Calculated Revenue (verification)

```
prop("Price ($)") * prop("Units Sold")
```

### Brand Deals — Days Until Deadline

```
if(prop("Status") == "Paid" or prop("Status") == "Declined", 0, dateBetween(prop("Deadline"), now(), "days"))
```

---

## Step 5: Set Up Rollups

Rollups aggregate data from related databases.

### On Sponsors CRM Records (after Brand Deals relation)

1. **Total Deal Value** — Rollup from Brand Deals relation, "Deal Value ($)" column, Sum
2. **Number of Deals** — Rollup from Brand Deals relation, Count

### On Income Streams Records (after Products relation)

1. **Product Count** — Rollup from Products relation, Count
2. **Product Revenue** — Rollup from Products relation, "Revenue ($)" column, Sum

### On Brand Deals Records (after Invoices relation)

1. **Invoice Status** — Rollup from Invoices relation, "Status" column, Show original
2. **Amount Invoiced** — Rollup from Invoices relation, "Amount ($)" column, Sum

---

## Step 6: Create Views

Set up multiple views for each database. The main template page lists recommended views for each database.

**Quick wins:**

- **Income Streams** — Table sorted by Net Profit descending
- **Brand Deals** — Board view grouped by Status (Kanban pipeline)
- **Expenses** — Table grouped by Category
- **Sponsors CRM** — Table sorted by Last Contact ascending (follow up on oldest first)
- **Invoices** — Table filtered to Sent and Overdue (outstanding money)
- **Goals** — Board view grouped by Priority
- **Products** — Table sorted by Revenue descending

**Power views:**

- **Income Streams: Effort vs Profit** — Table showing only Stream Name, Effort, Net Profit, and Profit Margin
- **Brand Deals: Follow-up** — Filtered to deals not in Paid/Declined status, sorted by Deadline
- **Expenses: Tax Time** — Filtered to Tax Deductible = Yes, grouped by Category
- **Invoices: Cash Flow** — Filtered to Sent status, sorted by Due Date
- **Goals: This Quarter** — Filtered to current quarter, sorted by Priority

---

## Step 7: Replace Sample Data

1. Review all sample data to understand the structure and relationships.
2. Start with **Income Streams** — add your actual revenue sources.
3. Then **Expenses** — add your real business costs from the last 3 months.
4. Add your **Goals** for the current and next quarter.
5. If you have brand deals, populate the **Brand Deals** and **Sponsors CRM** databases.
6. Set up **Products** if you sell digital products.
7. Create invoice records for any **outstanding invoices**.
8. Delete sample entries once you are comfortable with the structure.

**Tip:** Keep a few sample entries as reference while you are getting started. Delete them once you have added your own data.

---

## Troubleshooting

**CSV won't import correctly**
- Open the CSV in a text editor and verify commas are not inside unquoted fields.
- Notion sometimes struggles with multi-line values. If a "Notes" field has commas, ensure it is wrapped in double quotes.

**Relations not linking properly**
- Make sure the value in the relation column exactly matches a record name in the target database.
- Notion relations are case-sensitive.

**Formulas returning errors**
- Check that column names in your formulas exactly match your database column names (including spaces and capitalisation).
- Notion Formula 2.0 uses `prop("Column Name")` syntax.
- Currency columns must be set to Number type, not Text.

**Numbers displaying incorrectly**
- Click the column header, choose "Number format", and select the right format (Number, Percent, or Currency).
- Import sets all number columns to plain Number by default — change to Currency (AUD) where needed.

**Tax Deductible showing as text instead of checkbox**
- After CSV import, Tax Deductible will be a Text column with "Yes"/"No" values.
- Change the column type to Checkbox. Notion will convert "Yes" to checked and "No" to unchecked.

**Rollups showing zero**
- Rollups only work after you have linked records using relation columns.
- Make sure you have actually connected records in Step 3.2 before expecting rollup values.

---

*Setup complete. Start by adding your real income streams and expenses, then run your first Monthly Finance Checklist.*
