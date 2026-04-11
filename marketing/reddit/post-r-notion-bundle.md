# r/Notion Post — Freelancer OS Bundle

**Subreddit:** r/Notion
**Title:** I spent 3 months building a freelancer dashboard — here's the full breakdown + free template

---

## Post Body

Over the last few months I've been iterating on a Notion system for running freelance work end-to-end. Not a "productivity system" — a proper operational stack covering clients, projects, and money.

Here's the exact structure, because I find database schema more useful than screenshots when evaluating a template:

---

### Part 1: Client & Business Management

**Client CRM (8 fields)**
Client Name | Status (Active/Warm/Dormant/At Risk) | Health Score (formula) | Last Contact Date | Open Items (rollup) | Relationship Tier | Revenue YTD (rollup from invoices) | Next Action

Health Score formula: weighted combination of days-since-contact + open items count + engagement tier. Surfaces as Green / Yellow / Red in board view.

**Lead Pipeline (9 fields)**
Company | Contact | Stage (Cold → Warm → Proposal → Negotiating → Won/Lost) | Deal Value | Probability % | Weighted Value (formula: Deal Value × Probability) | Next Action | Due Date | Days Since Last Move (formula)

Leads stagnant for 14+ days get a flag in filtered views.

**Invoice Register (7 fields)**
Invoice # | Client (relation) | Amount | Status (Draft/Sent/Overdue/Paid) | Issue Date | Due Date | Days Overdue (formula, only shows when status = Overdue)

**Time Tracker (6 fields)**
Client (relation) | Project (relation) | Date | Hours | Hourly Rate | Billable Amount (formula)

---

### Part 2: Project Management

**Projects (10 fields)**
Project Name | Client (relation) | Status | Health (RAG formula) | Budget | Actual Cost | Timeline | % Complete | Open Risks (rollup) | Open Decisions (rollup)

**Risk Register (8 fields)**
Risk | Project (relation) | Probability (1-5) | Impact (1-5) | Risk Score (formula: P×I) | Mitigation | Owner | Status

**Decision Log (7 fields)**
Decision | Project (relation) | Made By | Date | Stakeholders (relation) | Affected Tasks (relation) | Rationale

**Weekly Review (dashboard page, not a database)**
Filtered views that auto-populate: tasks due this week, tasks overdue, risks with score ≥12, decisions pending >7 days, invoices overdue. Open it Friday morning, triage in 15 minutes.

---

### Part 3: Financial Tracking

**Income Streams (7 fields)**
Stream Name | Type (Client Work / Product / Retainer / Other) | Monthly Revenue | Monthly Expenses | Net Profit (formula) | Effort Hours | Effective Rate (formula: Net Profit / Hours)

This is the view that tells you which work is actually worth doing.

**Expense Tracker (6 fields)**
Item | Category | Amount | Date | Tax Deductible (checkbox) | Notes

**Financial Goals (5 fields)**
Goal | Target | Current (rollup or manual) | Progress % (formula) | Quarter

---

### What I learned building this

- The health score formula was the hardest part. Went through 4 iterations before it surfaced the right clients at the right time
- Decision log is underrated. Clients will relitigate decisions if you don't have a paper trail — having it linked to stakeholders and tasks has saved multiple conversations
- The weekly review page (not a database — just filtered views) is where the system actually gets used. If your dashboard is too complex, you skip it

Free template (Lite version of all three parts) is in the first comment. Full version also there.

---

## Comment (post separately — do NOT include in post body)

**Free Lite version** — includes Client CRM, Invoice Register, Basic Project Tracker, and Income Streams. Import and use immediately: https://gumroad.com/l/freelancer-os-notion-bundle (click "I want this" — the Lite version download is included at no cost)

**Full Freelancer OS** ($49 AUD, or $29 with code **LAUNCH40** for 48 hours) — everything above plus the full PM system, risk register, decision log, brand deals pipeline, quarterly review, SOW template, negotiation playbook, and sample data across all 23 databases.

Happy to answer questions about any of the formula setups — the health score and risk scoring formulas get asked about most.

---

## Posting notes

- Post Sunday 8–10am AEST (r/Notion peaks Sunday)
- Add flair: "Template" or "Showcase"
- The database schema format works extremely well on r/Notion — the community likes seeing the actual structure, not just "here's a pretty template"
- r/Notion requires no affiliate/tracking links — standard Gumroad URL is fine
- If asked about Formula 2.0 syntax: yes, formulas use F2.0 and are included in the template with documentation comments
- Engage anyone who asks "how do you connect the time tracker to the invoice register?" — this is the most common technical question and worth a detailed reply (it drives purchases)
- Don't oversell in comments. Technical answers only. Let the schema do the convincing
