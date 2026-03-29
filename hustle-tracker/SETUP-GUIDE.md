# Side Hustle Tracker & Revenue Dashboard -- Setup Guide

Get the full dashboard running in your Notion workspace in about 40 minutes.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace sidebar
2. Click **Import** (at the bottom of the sidebar)
3. Select **Markdown** and upload `hustle-tracker-main.md`
4. Notion will create a new page with all the sections

Alternatively, create a new page and paste the markdown content directly.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### Side Hustles Database

1. In Notion, create a new **Full-page database**
2. Name it `Side Hustles`
3. Click the `...` menu at the top right of the database
4. Select **Merge with CSV** and upload `databases/side-hustles.csv`
5. Set column types:
   - Name: `Title`
   - Category: `Select` (options: E-commerce, Freelance, Content Creation, Digital Products, Tutoring, Dropshipping, Real Estate, Crafts/Handmade, Consulting, Print on Demand, Affiliate Marketing, SaaS)
   - Platform: `Select` (options: Etsy, Shopify, Upwork, Fiverr, Substack, Udemy, Airbnb, Amazon KDP, Redbubble, Gumroad, Own Website)
   - Monthly Revenue ($): `Number` (format: Australian Dollar)
   - Monthly Expenses ($): `Number` (format: Australian Dollar)
   - Net Profit ($): `Number` (format: Australian Dollar)
   - Hours/Week: `Number`
   - Status: `Select` (options: Active, Scaling, Paused, Planning)
   - Started: `Date`
   - Revenue Score (1-5): `Number`
   - Growth Score (1-5): `Number`
   - Scalability (1-5): `Number`
   - Passion Score (1-5): `Number`
   - Total Score: `Number`
   - Notes: `Text`

### Monthly Revenue Database

1. Create a new **Full-page database** named `Monthly Revenue`
2. Merge with `databases/monthly-revenue.csv`
3. Set column types:
   - Month: `Date` (set to first of month, e.g. 2026-01-01)
   - Hustle: `Select` (match your Side Hustles names)
   - Revenue ($): `Number` (format: Australian Dollar)
   - Expenses ($): `Number` (format: Australian Dollar)
   - Net Profit ($): `Number` (format: Australian Dollar)
   - Hours Spent: `Number`
   - Hourly Rate ($): `Number` (format: Australian Dollar)
   - Growth vs Prior: `Text`
   - Notes: `Text`

### Expenses Database

1. Create a new **Full-page database** named `Expenses`
2. Merge with `databases/expenses.csv`
3. Set column types:
   - Date: `Date`
   - Description: `Title`
   - Amount ($): `Number` (format: Australian Dollar)
   - Category: `Select` (options: Software, Marketing, Inventory, Shipping, Education, Equipment, Professional Services, Advertising)
   - Hustle: `Select` (match your Side Hustles names, plus "All Hustles")
   - Tax Deductible: `Checkbox`
   - Payment Method: `Select` (options: Credit Card, PayPal, Bank Transfer, Automatic)
   - Receipt: `Text`
   - Notes: `Text`

### Goals Database

1. Create a new **Full-page database** named `Goals`
2. Merge with `databases/goals.csv`
3. Set column types:
   - Goal: `Title`
   - Target: `Text`
   - Current: `Text`
   - Progress (%): `Number` (format: Percent)
   - Status: `Select` (options: On Track, Behind, Achieved, Not Started)
   - Deadline: `Date`
   - Hustle: `Select` (match your Side Hustles names, plus "All Hustles")
   - Priority: `Select` (options: High, Medium, Low)
   - Milestone 1: `Text`
   - Milestone 2: `Text`
   - Milestone 3: `Text`
   - Notes: `Text`

### Time Log Database

1. Create a new **Full-page database** named `Time Log`
2. Merge with `databases/time-log.csv`
3. Set column types:
   - Date: `Date`
   - Hustle: `Select` (match your Side Hustles names)
   - Hours: `Number`
   - Activity Type: `Select` (options: Admin, Creation, Marketing, Client Work, Learning, Strategy)
   - Billable: `Checkbox`
   - Energy Level (1-5): `Number`
   - Notes: `Text`

### Tax Estimates Database

1. Create a new **Full-page database** named `Tax Estimates`
2. Merge with `databases/tax-estimates.csv`
3. Set column types:
   - Quarter: `Title`
   - Gross Income ($): `Number` (format: Australian Dollar)
   - Deductions ($): `Number` (format: Australian Dollar)
   - Taxable Income ($): `Number` (format: Australian Dollar)
   - Estimated Tax ($): `Number` (format: Australian Dollar)
   - Medicare Levy ($): `Number` (format: Australian Dollar)
   - Total Liability ($): `Number` (format: Australian Dollar)
   - Due Date: `Date`
   - Status: `Select` (options: Paid, Upcoming, Overdue)
   - Notes: `Text`

---

## Step 3: Customise Your Side Hustles

This is the most important step. Replace the sample data with your actual hustles.

1. Open the **Side Hustles** database
2. Delete all sample rows
3. Add your real side hustles:
   - Be honest about monthly revenue (use last month's actual number)
   - Track effort accurately (set a timer for one week if you're not sure)
   - Set the right status -- don't mark something "Active" if you haven't worked on it in 3 weeks
   - Score each hustle honestly using the 5-dimension Scoring System (1-5 for Revenue, Growth, Scalability, Time Efficiency, and Passion)
   - Calculate Total Score by adding all five dimensions

If you only have 1-2 hustles, that's fine. The template scales. You'll add more as you grow.

---

## Step 4: Set Up Monthly Revenue Tracking

The Monthly Revenue database is where the real insights live.

### First Month Setup

1. Add one row per hustle for the current month
2. Fill in revenue, expenses, and hours spent
3. Net Profit is calculated: Revenue minus Expenses
4. Hourly Rate is calculated: Net Profit / Hours Spent
5. The Growth vs Prior column will be "New" for your first month

### Monthly Routine (20 minutes, 1st of each month)

```
1. Open each platform dashboard and note final revenue
2. Add rows to Monthly Revenue for each active hustle
3. Calculate net profit and hourly rate for each
4. Note the growth percentage vs prior month
5. Log any missing expenses
6. Update Goals progress
```

### Setting a Calendar Reminder

Block 20 minutes on the 1st of each month. Title it "Side Hustle Monthly Update" and link to your Notion template page.

---

## Step 5: Configure Tax Calculator

1. Read the Tax Calculator section in the main template
2. Open the **Tax Estimates** database
3. Replace sample figures with your actual quarterly estimates:
   - Start with your actual Q1 income and deductions
   - Project Q2-Q4 based on your growth trajectory
4. Adjust the worked example in the main template to reflect your situation:
   - Update your day job salary (or remove if full-time side hustler)
   - Update your side hustle income estimates
   - Recalculate using the Australian tax brackets
5. Set quarterly calendar reminders to update estimates and set aside tax money

**Important:** The tax calculator provides estimates only. Consult your accountant for actual tax returns.

---

## Step 6: Set Up Database Relations

Notion relations link databases together for more powerful tracking.

### Side Hustles <-> Monthly Revenue
1. Open the Monthly Revenue database
2. Add a new `Relation` property pointing to `Side Hustles`
3. Name it "Hustle Link"
4. This lets you click through from a monthly entry to see the full hustle details

### Side Hustles <-> Expenses
1. Open the Expenses database
2. Add a new `Relation` property pointing to `Side Hustles`
3. Name it "Hustle Link"
4. See all expenses tied to a specific hustle

### Side Hustles <-> Goals
1. Open the Goals database
2. Add a new `Relation` property pointing to `Side Hustles`
3. Name it "Related Hustle"
4. Connect goals to the hustles they're driving

### Side Hustles <-> Time Log
1. Open the Time Log database
2. Add a new `Relation` property pointing to `Side Hustles`
3. Name it "Hustle Link"
4. Track time entries against specific hustles

### Relation Map

```
Side Hustles (central hub)
  |-- Monthly Revenue (track earnings over time)
  |-- Expenses (what it costs to run)
  |-- Goals (where you're headed)
  |-- Time Log (hours invested)

Tax Estimates (standalone -- updated quarterly from totals)
```

---

## Step 7: Create Linked Database Views

1. Go back to the main Side Hustle Tracker page
2. In each section that says "Create a linked database view here", type `/linked` and select **Create linked view of database**
3. Point each linked view to the appropriate database
4. Set up the recommended views listed in each section (filters, sorts, grouping)

### Recommended Dashboard Layout

For the Revenue Dashboard section at the top:
- Create a **Gallery view** of Side Hustles showing Name, Net Profit, Status, and Total Score
- Create a **List view** of Goals filtered to Status != Achieved, sorted by Priority
- Create a **Calendar view** of Tax Estimates showing Due Dates

For the Time Tracker section:
- Create a **Board view** of Time Log grouped by Activity Type
- Create a **Table view** grouped by Hustle showing sum of Hours

---

## Tips

- **Start with Side Hustles and Monthly Revenue.** These two databases give you 80% of the value. Add the others as you settle in.
- **Be brutally honest with numbers.** This template is for you, not for showing off on social media. Accurate data leads to better decisions.
- **Score your hustles quarterly.** The Hustle Scoring System is most powerful when you re-score every 3 months and compare trends.
- **Set aside tax money immediately.** Every time you receive hustle income, transfer your estimated tax percentage to a separate savings account. Do not spend it.
- **Track time for one week.** If you don't know how many hours each hustle takes, set a timer for one week. The numbers might surprise you.
- **Kill underperformers.** If a hustle has been below $25/hour for 3 months and isn't growing, pause it and redirect that time to your top earners.
- **Use the Quarterly Review.** The 45-minute quarterly checklist is where the big decisions happen. Don't skip it.

---

*Questions? Feature requests? Reach out on X or open an issue on GitHub.*
