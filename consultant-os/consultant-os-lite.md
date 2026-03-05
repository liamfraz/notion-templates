# Technical Consultant OS — Lite

> Track your clients, log your time, and manage invoices. The essentials for freelance technical consultants.

---

## Quick Start

1. Import this page into Notion
2. Create three databases from the CSVs: Clients, Time Entries, Invoices
3. Link them with relations (Clients <-> Time Entries, Clients <-> Invoices)
4. Start logging your time and tracking your invoices

> Want the full version? **Technical Consultant OS** ($49) adds: Lead Pipeline, Project Tracker, SOW Templates, Rate Card Manager, Knowledge Base, Skills Matrix, Monthly Review Templates, and Business Dashboard. [Get it here →](#)

---

## Client CRM

Track every client relationship in one place.

### Database: Clients

Import `clients-lite.csv` or create a table with these columns:

| Column | Type |
|---|---|
| Company Name | Title |
| Contact Person | Text |
| Email | Email |
| Phone | Phone |
| Engagement Status | Select: Active / Past / Prospect |
| Health Score | Select: Green / Amber / Red |
| Total Revenue ($) | Number |
| Last Contact | Date |
| Notes | Text |

### Client Health Scoring

| Score | Criteria |
|---|---|
| **Green** | Active work, regular contact, invoices paid on time |
| **Amber** | No contact in 14-30 days, outstanding invoices, or delays |
| **Red** | No contact in 30+ days, overdue invoices, or at risk of churn |

**Tip:** Review client health scores weekly. Set a recurring reminder.

---

## Time Tracker

Log every hour. Bill accurately. Know your utilisation rate.

### Database: Time Entries

Create a table with these columns:

| Column | Type |
|---|---|
| Date | Date |
| Client | Relation (to Clients) |
| Description | Text |
| Hours | Number |
| Rate ($) | Number |
| Billable Amount ($) | Formula: `if(prop("Billable") == "Yes", prop("Hours") * prop("Rate"), 0)` |
| Billable | Select: Yes / No |
| Category | Select: Development / Consulting / Meeting / Admin / Travel |

### Logging Guidelines

- Log time **daily** — don't batch at end of week
- Minimum increment: 15 minutes
- Always link to a Client
- Write clear descriptions (clients may see these on invoices)
- Mark each entry as Billable or Non-Billable

### Key Metrics

```
Utilisation Rate = Billable Hours / Available Hours x 100
Target: 75% (30 billable hours out of 40)

Effective Rate = Total Billable Amount / Total Hours (incl. non-billable)
```

### Recommended Views

- **This Week** — Table filtered to current week, sorted by date
- **By Client** — Table grouped by Client
- **Calendar** — Calendar view by Date

---

## Invoice Register

Track what you've billed and what's outstanding.

### Database: Invoices

Create a table with these columns:

| Column | Type |
|---|---|
| Invoice Number | Title (format: INV-YYYY-NNN) |
| Client | Relation (to Clients) |
| Amount ($) | Number |
| Tax ($) | Number |
| Total ($) | Number |
| Date Issued | Date |
| Date Due | Date |
| Date Paid | Date |
| Status | Select: Draft / Sent / Overdue / Paid / Cancelled |
| Notes | Text |

### Invoice Formula: Days Until Due

```
if(prop("Status") == "Paid", 0, dateBetween(prop("Date Due"), now(), "days"))
```

### Payment Terms

| Term | Use When |
|---|---|
| **Due on Receipt** | Small amounts, one-off work |
| **Net 14** | Default for most clients |
| **Net 30** | Enterprise / larger organisations |

### Overdue Process

1. **Day 1 past due** — Friendly email reminder
2. **Day 7** — Phone call + email
3. **Day 14** — Formal notice, consider pausing work
4. **Day 30** — Final notice, escalate

### Recommended Views

- **All Invoices** — Table sorted by Date Issued (descending)
- **By Status** — Board view grouped by Status
- **Overdue** — Table filtered to Status = "Overdue"

---

## Setting Up Relations

Link your three databases for powerful filtering:

1. **Time Entries -> Clients** — See all time logged for each client
2. **Invoices -> Clients** — See all invoices for each client

### Rollups on Client Records

- **Total Hours** — Rollup from Time Entries, "Hours" column, Sum
- **Total Invoiced** — Rollup from Invoices, "Amount" column, Sum

---

## Weekly Checklist

- [ ] Review time entries for accuracy and completeness
- [ ] Send any pending invoices
- [ ] Chase overdue invoices (check "Overdue" view)
- [ ] Update client health scores
- [ ] Log any unbilled time

---

## Upgrade to Full Version

The Lite version covers the basics. When you're ready to grow, **Technical Consultant OS** ($49) adds:

- **Lead Pipeline** — Track prospects from first contact to signed deal
- **Project Tracker** — Milestones, deliverables, risks, and budget tracking
- **Rate Card Manager** — Manage hourly, daily, and fixed rates by service
- **SOW Templates** — Professional Statement of Work templates ready to customise
- **Knowledge Base** — Reusable code snippets, checklists, and documentation
- **Skills Matrix** — Track certifications, proficiency, and learning goals
- **Business Dashboard** — Revenue, utilisation, and pipeline at a glance
- **Monthly Review Template** — Structured business health review

[Get the full Technical Consultant OS →](#)

---

*Built for technical consultants who'd rather build systems than manage spreadsheets.*
