# Creator Business OS

> Run your creator career like a real business. Track every dollar in, every dollar out, every deal in the pipeline, and every product on your shelf — so you can stop guessing and start growing.

---

## Quick Start

1. **Import this template** into your Notion workspace
2. **Set up your databases** using the 7 CSV files provided (Income Streams, Brand Deals, Expenses, Sponsors CRM, Invoices, Goals, Products)
3. **Connect your relations** — link Brand Deals to Sponsors CRM, Invoices to Brand Deals, and Products to Income Streams
4. **Replace sample data** with your actual numbers — start with Income Streams and Expenses
5. **Run your first Monthly Finance Review** using the checklist below

> See the full [Setup Guide](SETUP-GUIDE.md) for detailed instructions including formula configurations and rollups.

---

## Business Dashboard

### Financial Overview

| Metric | This Month | Last Month | YTD |
|---|---|---|---|
| Total Revenue | $0.00 | $0.00 | $0.00 |
| Total Expenses | $0.00 | $0.00 | $0.00 |
| Net Profit | $0.00 | $0.00 | $0.00 |
| Tax Provisions (25%) | $0.00 | $0.00 | $0.00 |
| Brand Deals Pipeline | $0.00 | $0.00 | $0.00 |

### Cash Flow Snapshot

| Metric | Amount |
|---|---|
| Outstanding Invoices | $0.00 |
| Overdue Invoices | $0.00 |
| Upcoming Expenses (30 days) | $0.00 |
| Available Cash (after tax provision) | $0.00 |

### How to Calculate

- **Net Profit** = Total Revenue - Total Expenses
- **Tax Provision** = Net Profit x 0.25 (adjust for your tax bracket)
- **Profit Margin** = (Net Profit / Total Revenue) x 100
- **Pipeline Value** = Sum of Brand Deals where Status is not Declined or Paid
- **Effective Hourly Rate** = Net Profit / Total Hours Worked

---

## Income Streams

> **Database:** Import `databases/income-streams.csv`

Track every revenue source with profit margins. Know exactly which streams are worth your time and which are costing you money.

### Revenue Stream Lifecycle

```
New -> Active -> Growing -> Optimising -> Scaling -> Declining -> Paused
```

### Recommended Views

- **Dashboard View** — Table sorted by Net Profit descending (see your best performers first)
- **By Type** — Grouped by Type to see revenue diversification
- **Active Streams** — Filtered to Active and Growing statuses
- **Effort vs Profit** — Table with Effort and Net Profit columns visible (find your highest ROI streams)
- **Monthly Trends** — Calendar view for tracking seasonal patterns

### Revenue Diversification Strategy

Healthy creator businesses have revenue distributed across multiple categories. Use the Income Streams database to assess your mix.

**Target Revenue Mix (mature creator):**

| Category | Target % | Why |
|---|---|---|
| Sponsorships | 30-40% | High revenue per deal but time-intensive to maintain |
| Digital Products | 20-30% | Scalable passive income — build once, sell forever |
| Ad Revenue | 15-20% | Baseline income that scales with audience growth |
| Affiliates | 10-15% | Low effort recurring income from genuine recommendations |
| Services (coaching, freelance) | 5-15% | High hourly rate but not scalable — use strategically |
| Memberships | 5-10% | Predictable recurring revenue, builds community moat |

**Warning Signs:** Over 50% from one source = fragile. Over 70% from one platform = platform risk. Zero passive income = trading time for money forever.

---

## Brand Deals Pipeline

> **Database:** Import `databases/brand-deals.csv`

Manage every brand relationship from cold lead to paid invoice. Never forget to follow up, never forget to invoice.

### Deal Flow

```
Lead -> Pitched -> Negotiating -> Contracted -> In Progress -> Delivered -> Invoiced -> Paid
```

### Recommended Views

- **Pipeline Board** — Kanban by Status (drag deals through stages)
- **Active Deals** — Filtered to In Progress and Negotiating
- **Revenue Board** — Grouped by Category with deal values visible
- **Follow-up Required** — Filtered to deals where Last Contact > 7 days ago
- **By Platform** — See which platforms attract the most deals

### Brand Deal Negotiation Playbook

**Know Your Numbers Before You Pitch:**

| Metric | Formula | Example |
|---|---|---|
| CPM (Cost Per Mille) | Deal Value / (Avg Views / 1000) | $3000 / (50K / 1000) = $60 CPM |
| Cost Per Subscriber | Deal Value / Subscribers | $3000 / 25K = $0.12/sub |
| Effective Hourly Rate | Deal Value / Hours Spent | $3000 / 10hrs = $300/hr |

**Negotiation Framework:**

1. **Anchor high** — Start 20-30% above your target rate
2. **Bundle deliverables** — Multi-platform packages for higher total value
3. **Charge for usage rights** — 50-100% extra if they use your content in their ads
4. **Push for recurring** — Quarterly deals provide stability even at 10-15% less per video
5. **Never work for free product** — Product is not payment

**Rate Card Guidelines (by audience size):**

| Audience Size | YouTube Dedicated | Instagram Reel | Newsletter |
|---|---|---|---|
| 10K-50K | $1000-3000 | $300-800 | $200-500 |
| 50K-100K | $3000-6000 | $800-2000 | $500-1200 |
| 100K-500K | $6000-15000 | $2000-5000 | $1200-3000 |

---

## Expenses Tracker

> **Database:** Import `databases/expenses.csv`

Track every business expense with tax categories. Know your burn rate, plan for tax time, and find costs to cut.

### Recommended Views

- **All Expenses** — Table sorted by Date descending
- **By Category** — Grouped by Category to see where money goes
- **Tax Deductible** — Filtered to Tax Deductible = Yes (for tax time)
- **Recurring Costs** — Filtered to Monthly and Annual frequency
- **This Quarter** — Filtered to current quarter for BAS preparation

### Tax & Expense Management

**For Australian Creators:** Register for an ABN at any income level (free at abr.gov.au). GST registration is mandatory at $75K+ annual turnover. Set aside 25-30% of net profit for income tax. Consider 11.5% super contributions — they are tax-deductible.

**For All Creators:**

- Keep a separate business bank account — makes tax time 10x easier
- Set aside tax provisions monthly, not annually
- Track all expenses with receipts from day one
- Review subscriptions quarterly — cancel anything unused for 30+ days
- Categorise expenses as you go — catching up at tax time is painful

---

## Sponsors CRM

> **Database:** Import `databases/sponsors-crm.csv`

Your relationship tracker for every brand contact. Know who to follow up with, who's gone cold, and where your next deal is coming from.

### Relationship Stages

```
Cold -> Warm -> Hot -> Active Partner -> Past Partner
```

### Recommended Views

- **Active Partners** — Filtered to Active Partner status
- **Follow-up Queue** — Sorted by Last Contact ascending (oldest first = most overdue)
- **By Industry** — Grouped by Industry to see your sponsor mix
- **Hot Prospects** — Filtered to Hot and Warm stages
- **Deal History** — Sorted by Deal History descending (your biggest partners first)

### CRM Best Practices

- **Touch base monthly** with active partners, even when there is no deal in progress
- **Update Last Contact** after every email, call, or meeting
- **Log deal values** cumulatively — this shows brands your lifetime value to them
- **Move to Past Partner** only after 6+ months of no activity
- **Never burn bridges** — a "Declined" deal today is a "Warm" lead next quarter

---

## Invoices

> **Database:** Import `databases/invoices.csv`

Track every invoice from draft to paid. Never lose track of money owed to you.

### Invoice Lifecycle

```
Draft -> Sent -> Paid
         └-> Overdue -> Paid / Cancelled
```

### Recommended Views

- **All Invoices** — Table sorted by Issue Date descending
- **Outstanding** — Filtered to Sent and Overdue statuses
- **Overdue** — Filtered to Overdue only (these need immediate action)
- **Paid This Quarter** — Filtered to Paid status in current quarter
- **By Client** — Grouped by Client to see payment history per brand

### Invoice Management Tips

- Send invoices within 24 hours of delivering content
- Always include: your ABN, payment terms, bank details, and a clear description of deliverables
- Set calendar reminders for payment due dates
- Follow up on Day 1 after due date — do not wait. Be polite but firm
- For overdue invoices: email, then call, then escalate to their accounts payable department
- Keep a "payment terms" column in your Brand Deals database so you know when to expect payment

---

## Financial Goals

> **Database:** Import `databases/goals.csv`

Set targets for revenue, growth, savings, and products. Track progress quarterly and adjust.

### Recommended Views

- **Active Goals** — Filtered to exclude Completed status
- **By Quarter** — Grouped by Quarter to see quarterly roadmap
- **Priority Board** — Kanban by Priority
- **Revenue Goals** — Filtered to Revenue category
- **Progress Tracker** — Table with Target, Current, and Status visible

### Goal-Setting Framework

Use OKRs: set a qualitative **Objective** (e.g., "Build a sustainable creator business") then define measurable **Key Results** that go into the Goals database (e.g., "$20K monthly revenue by Q2", "Launch course by Q3", "$50K emergency fund by Q4").

Review goals monthly. Update the "Current" column honestly. If a goal is consistently Behind, adjust the target or change your strategy.

---

## Digital Products

> **Database:** Import `databases/products.csv`

Track every digital product you sell. Revenue, units, platforms, and launch status.

### Recommended Views

- **Active Products** — Filtered to Active status
- **Revenue Leaderboard** — Table sorted by Revenue descending
- **By Platform** — Grouped by Platform
- **Launch Pipeline** — Filtered to Coming Soon and Draft statuses
- **Product Mix** — Grouped by Type to see product diversification

### Product Strategy

**The Product Ladder:**

```
Free Lead Magnet ($0) -> Entry Product ($9-19) -> Core Product ($29-49) -> Premium Product ($99-199) -> High-Ticket ($500+)
```

Every product should lead to the next one. Your free content attracts an audience, your free lead magnet captures emails, your entry product converts browsers to buyers, and your core products generate sustainable revenue.

**Pricing Tips:**
- Price based on value delivered, not hours spent
- Use odd pricing ($29, $49, $149) — it outperforms round numbers
- Bundle products for 20-30% discount to increase average order value

---

## Quarterly Business Review

Block 2 hours every quarter. Do not skip this.

### Revenue
- [ ] Total revenue vs target
- [ ] Which streams grew, which declined?
- [ ] Any stream below minimum viable revenue? Pause or kill it

### Expenses
- [ ] Total expenses vs last quarter
- [ ] Cancel unused subscriptions
- [ ] Tax provisions — have you set aside enough?

### Brand Deals
- [ ] Deals closed vs target
- [ ] Pipeline health — enough leads for next quarter?
- [ ] Rate card — should you increase your rates?

### Products & Goals
- [ ] Product revenue by SKU — retire or update underperformers
- [ ] Update all goal progress honestly
- [ ] Set new goals for next quarter

---

## Monthly Finance Checklist

Run this on the 1st of every month. Takes 30-45 minutes.

- [ ] Log all income received last month into Income Streams
- [ ] Update product sales numbers in Products database
- [ ] Log all business expenses and categorise them
- [ ] Send outstanding draft invoices and follow up on overdue ones
- [ ] Transfer tax provision (25% of net profit) to savings account
- [ ] Save receipts for all deductible expenses
- [ ] Update brand deal pipeline statuses
- [ ] Follow up on pitches older than 7 days
- [ ] Send outreach to 3 new potential sponsors
- [ ] Update Business Dashboard with current month numbers

---

## Database Relations Map

Connect your databases for powerful cross-referencing:

```
Brand Deals ──── relates to ──── Sponsors CRM
    │                                  │
    │                                  │
    ├── relates to ──── Invoices       │
    │                                  │
Income Streams ── relates to ── Products
    │
    │
Goals ─── references ─── all databases (manual tracking)
    │
    │
Expenses ── standalone (no required relations)
```

### Key Relations to Set Up

1. **Brand Deals -> Sponsors CRM** — Link each deal to the company contact record
2. **Brand Deals -> Invoices** — Link each deal to its invoice for payment tracking
3. **Products -> Income Streams** — Link each product to its revenue stream
4. **Income Streams -> Brand Deals** — Link sponsorship income to specific deals

---

## Useful Formulas

### Net Profit (Income Streams)
```
prop("Monthly Revenue ($)") - prop("Monthly Expenses ($)")
```

### Profit Margin % (Income Streams)
```
if(prop("Monthly Revenue ($)") > 0, round((prop("Monthly Revenue ($)") - prop("Monthly Expenses ($)")) / prop("Monthly Revenue ($)") * 100 * 100) / 100, 0)
```

### Revenue Per Hour (Income Streams)
```
if(prop("Effort (hrs/week)") > 0, round(prop("Net Profit ($)") / (prop("Effort (hrs/week)") * 4.33) * 100) / 100, 0)
```

### Days Until Due (Invoices)
```
if(prop("Status") == "Paid" or prop("Status") == "Cancelled", 0, dateBetween(prop("Due Date"), now(), "days"))
```

### Invoice Overdue Flag (Invoices)
```
if(prop("Status") == "Sent" and now() > prop("Due Date"), "OVERDUE", "")
```

### Goal Progress % (Goals)
```
if(prop("Target ($)") > 0, round(prop("Current ($)") / prop("Target ($)") * 100 * 100) / 100, 0)
```

### Product Conversion Revenue (Products)
```
prop("Price ($)") * prop("Units Sold")
```

### Deal ROI vs Effort (Brand Deals — add Effort Hours column)
```
if(prop("Effort Hours") > 0, round(prop("Deal Value ($)") / prop("Effort Hours") * 100) / 100, 0)
```

---

*Your creator career is a business. Treat it like one. Update your numbers, review your performance, and make decisions based on data — not vibes.*
