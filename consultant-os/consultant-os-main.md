# Technical Consultant OS

> Run your consulting business from one workspace. Client pipeline, project delivery, time tracking, and knowledge base — designed for technical professionals.

---

## Quick Start

1. **Import this template** into your Notion workspace
2. **Set up your databases** using the CSV files provided (Clients, Leads, Projects, Time Entries, Invoices, Rate Card, Knowledge Base, Skills)
3. **Link your databases** with relations: Clients <-> Projects <-> Time Entries <-> Invoices
4. **Configure your Rate Card** with your actual rates
5. **Start logging** — add your first client, create a project, and track your time

> See the full [Setup Guide](SETUP-GUIDE.md) for detailed instructions including formula configurations.

---

## Business Dashboard

### Revenue Snapshot

| Metric | This Month | This Quarter | YTD |
|---|---|---|---|
| Revenue (Invoiced) | $0.00 | $0.00 | $0.00 |
| Revenue (Collected) | $0.00 | $0.00 | $0.00 |
| Outstanding Invoices | $0.00 | $0.00 | $0.00 |
| Pipeline Value | $0.00 | $0.00 | $0.00 |

### Key Metrics

| Metric | Current | Target | Status |
|---|---|---|---|
| Active Projects | 0 | — | — |
| Utilisation Rate | 0% | 75% | — |
| Avg Days to Payment | 0 | 14 | — |
| Lead Conversion Rate | 0% | 30% | — |
| Monthly Recurring Revenue | $0.00 | — | — |

### How to Calculate

- **Utilisation Rate** = (Billable Hours / Available Hours) x 100. Available hours = working days in month x 8.
- **Pipeline Value** = Sum of (Estimated Value x Probability %) for all active leads.
- **Avg Days to Payment** = Average of (Date Paid - Date Issued) for paid invoices this period.

---

## Client CRM

> **Database:** Import `databases/clients.csv`

Track every client relationship in one place. Each client record links to their projects, time entries, and invoices.

### Client Health Scoring

| Score | Criteria |
|---|---|
| **Green** | Active engagement, regular contact (< 14 days), invoices paid on time |
| **Amber** | No contact in 14-30 days, outstanding invoices, or project delays |
| **Red** | No contact in 30+ days, overdue invoices, escalated issues, or at risk of churn |

### Client View Filters

- **Active Clients** — Engagement Status = "Active"
- **Needs Attention** — Health Score = "Amber" or "Red"
- **Prospects** — Engagement Status = "Prospect"
- **Past Clients** — Engagement Status = "Past" (review quarterly for re-engagement)

### Suggested Relations

- Client -> Projects (one-to-many)
- Client -> Invoices (one-to-many)
- Client -> Time Entries (one-to-many)
- Client -> Leads (one-to-one)

---

## Lead Pipeline

> **Database:** Import `databases/leads.csv`

### Pipeline Stages

```
New Lead -> Qualified -> Proposal Sent -> Negotiation -> Won / Lost
```

| Stage | Actions | Typical Duration |
|---|---|---|
| **New Lead** | Initial contact, understand requirements | 1-3 days |
| **Qualified** | Discovery call, confirm budget/timeline/fit | 3-7 days |
| **Proposal Sent** | Send SOW or proposal document | 7-14 days |
| **Negotiation** | Scope/rate adjustments, contract review | 7-21 days |
| **Won** | Sign contract, onboard, create project | — |
| **Lost** | Record reason, follow up in 3 months | — |

### Pipeline Metrics

- **Weighted Pipeline** = Sum of (Estimated Value x Probability) for all open leads
- **Conversion Rate** = Won / (Won + Lost) over trailing 90 days
- **Average Deal Size** = Total Won Value / Number of Won Deals
- **Average Sales Cycle** = Average days from New Lead to Won

### Lead Sources to Track

- Referral (highest conversion — nurture your network)
- LinkedIn (inbound and outbound)
- Website / Blog / SEO
- Cold Outreach
- Repeat Client (easiest to close)

---

## Project Tracker

> **Database:** Import `databases/projects.csv`

### Project Lifecycle

```
Scoping -> Active -> [On Hold] -> Complete / Cancelled
```

### Project Views

- **Board View** — Kanban by Status (Scoping | Active | On Hold | Complete)
- **Timeline View** — Gantt chart by Start Date and End Date
- **By Client** — Grouped by Client name
- **Budget Health** — Sorted by (Budget - Invoiced) ascending to spot overruns

### For Each Active Project, Track

- **Deliverables** — What you're building/delivering, with acceptance criteria
- **Milestones** — Key dates and checkpoints
- **Risks** — What could go wrong, likelihood, mitigation
- **Budget Burn** — Actual Hours x Rate vs Budget, percentage consumed
- **Change Requests** — Scope changes with impact on timeline/budget

### Budget Health Formula

```
Budget Consumed (%) = (Actual Hours x Rate) / Budget x 100

If > 80% and project not near completion -> Flag as at risk
```

---

## SOW / Proposal Templates

> **Template:** See `templates/sow-template.md`

Reusable Statement of Work structures for common engagement types:

| Template | Use When |
|---|---|
| **Fixed-Price SOW** | Clear scope, defined deliverables, predictable timeline |
| **Time & Materials SOW** | Evolving scope, advisory work, ongoing support |
| **Retainer Agreement** | Ongoing monthly commitment, reserved capacity |
| **Training Proposal** | Workshop or training delivery |

### Proposal Workflow

1. Discovery call — understand the problem
2. Draft SOW using template
3. Internal review (does the scope match the budget?)
4. Send to client
5. Negotiate and revise
6. Sign and create project

---

## Rate Card Manager

> **Database:** Import `databases/rate-card.csv`

### Rate Tiers

| Tier | When to Apply |
|---|---|
| **Standard** | Default rate for most engagements |
| **Discounted** | Long-term retainers, high-volume clients, strategic accounts |
| **Premium** | Urgent/after-hours work, niche expertise, short-notice requests |

### Rate Review Cadence

- Review rates **every 6 months**
- Increase by 5-10% annually minimum (keep pace with market)
- New clients always get current rates — never grandfather old rates to new clients
- Existing retainers: raise at renewal with 30 days notice

### Pricing Strategies

- **Hourly** — Best for advisory, support, and variable-scope work
- **Daily** — Best for on-site consulting, workshops, and deep-dive sessions
- **Fixed Price** — Best for well-defined projects with clear deliverables. Always add 20% buffer
- **Retainer** — Best for ongoing relationships. Offer slight discount for commitment

---

## Time Tracker

> **Database:** Import `databases/time-entries.csv`

### Logging Guidelines

- Log time **daily** — don't batch at end of week (you'll forget and under-bill)
- Minimum increment: 15 minutes
- Always link to a Project and Client
- Mark as Billable or Non-Billable
- Write a clear description (clients may see this on invoices)

### Time Categories

| Category | Billable? | Examples |
|---|---|---|
| Development | Yes | Coding, building, configuring |
| Consulting | Yes | Advisory calls, strategy sessions |
| Meeting | Yes/No | Client meetings (yes), internal (no) |
| Admin | No | Invoicing, email, scheduling |
| Travel | Sometimes | Travel to client site (check agreement) |

### Weekly Summary View

Group by Client, then by Project. Sum hours and billable amount. Compare against:
- **Target billable hours**: 30 hrs/week (75% of 40 hrs)
- **Minimum viable**: 20 hrs/week (covers costs)

### Formulas

```
Billable Amount = Hours x Rate (if Billable = Yes, else $0)
Utilisation Rate = Billable Hours / Total Hours Logged x 100
Effective Rate = Total Billable Amount / Total Hours (including non-billable)
```

---

## Invoice Register

> **Database:** Import `databases/invoices.csv`

### Invoice Workflow

```
Draft -> Sent -> [Overdue] -> Paid / Cancelled
```

### Payment Terms

| Term | Use When |
|---|---|
| **Due on Receipt** | Small amounts, one-off work |
| **Net 14** | Default for most clients |
| **Net 30** | Enterprise clients, larger organisations |
| **50/50 Split** | Fixed-price projects (50% upfront, 50% on completion) |
| **Monthly Milestone** | Long projects — invoice at each milestone |

### Overdue Process

1. **Day 1 past due** — Friendly email reminder
2. **Day 7** — Phone call + email, reattach invoice
3. **Day 14** — Formal notice, pause non-critical work
4. **Day 30** — Final notice, escalate, consider pausing all work
5. **Day 60+** — Engage debt collection or write off

### Invoice Numbering Convention

```
INV-YYYY-NNN
Example: INV-2026-001, INV-2026-002, ...
```

---

## Knowledge Base

> **Database:** Import `databases/knowledge-base.csv`

### Categories

| Category | Purpose |
|---|---|
| **Template** | Reusable document structures (SOWs, proposals, reports) |
| **Code Snippet** | Tested, reusable code for common problems |
| **Checklist** | Step-by-step procedures for repeatable tasks |
| **Guide** | How-to documentation for complex processes |
| **Reference** | Quick-lookup information (API endpoints, config values) |

### Knowledge Base Best Practices

- Update entries after every project (capture what you learned)
- Track **Use Count** to identify your most valuable assets
- Tag entries by technology and client type for easy filtering
- Review quarterly — archive outdated entries, update stale ones
- Every deliverable you create is a potential template for the next project

---

## Skills Matrix

> **Database:** Import `databases/skills.csv`

### Proficiency Levels

| Level | Definition |
|---|---|
| **Beginner** | Foundational knowledge, need guidance for real work |
| **Intermediate** | Can deliver independently on standard tasks |
| **Advanced** | Can handle complex scenarios, mentor others |
| **Expert** | Go-to authority, can architect solutions, speak/write on topic |

### Skills Review Process

1. Review matrix **quarterly**
2. Identify gaps between current skills and market demand
3. Set 1-2 learning goals per quarter
4. Track certifications and renewal dates
5. Update proficiency after completing relevant projects

### Skill Categories

- **Technical** — Languages, platforms, tools, frameworks
- **Business** — Sales, negotiation, project management, finance
- **Soft Skills** — Communication, leadership, stakeholder management

---

## Monthly Business Review

> **Template:** See `templates/monthly-review.md`

Run this review on the **first business day of each month**. Block 2 hours.

### Review Checklist

- [ ] Calculate revenue (invoiced and collected) vs target
- [ ] Review all outstanding invoices — chase overdue
- [ ] Score client health for all active clients
- [ ] Review pipeline — update probabilities, close stale leads
- [ ] Calculate utilisation rate
- [ ] Review budget health on all active projects
- [ ] Identify top 3 wins and top 3 lessons
- [ ] Set goals and priorities for next month
- [ ] Update rate card if needed
- [ ] Review skills matrix — any new certifications or learning completed?

---

## Appendix: Suggested Notion Setup

### Database Relations Map

```
Clients (1) ----< (many) Projects
Clients (1) ----< (many) Leads
Clients (1) ----< (many) Invoices
Projects (1) ----< (many) Time Entries
Projects (1) ----< (many) Invoices
Rate Card (1) ----< (many) Projects (via Service Type)
```

### Recommended Views

| Database | View 1 | View 2 | View 3 |
|---|---|---|---|
| Clients | Table (all) | Board (by Health) | Gallery (active only) |
| Leads | Board (by Stage) | Table (by Expected Close) | Calendar |
| Projects | Board (by Status) | Timeline (Gantt) | Table (by Client) |
| Time Entries | Table (this week) | Table (by Client) | Calendar |
| Invoices | Table (all) | Board (by Status) | Table (overdue only) |
| Knowledge Base | Table (all) | Gallery (by Category) | Table (most used) |
| Skills | Table (all) | Board (by Proficiency) | Table (expiring certs) |

### Useful Formulas (Notion Formula 2.0)

**Billable Amount (Time Entries):**
```
if(prop("Billable") == "Yes", prop("Hours") * prop("Rate"), 0)
```

**Budget Remaining (Projects):**
```
prop("Budget") - prop("Invoiced")
```

**Days Until Due (Invoices):**
```
if(prop("Status") == "Paid", 0, dateBetween(prop("Date Due"), now(), "days"))
```

**Weighted Value (Leads):**
```
prop("Estimated Value") * prop("Probability") / 100
```

**Utilisation Rate (Dashboard — manual or via rollup):**
```
(Billable Hours This Month / (Working Days * 8)) * 100
```

---

*Built for technical consultants who'd rather build systems than manage spreadsheets.*
