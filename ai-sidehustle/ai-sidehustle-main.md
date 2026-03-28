# AI Side Hustle Tracker

> Track revenue, expenses, tasks, and launches across all your AI-powered side projects. Know your numbers. Scale what works. Kill what doesn't.

---

## `// QUICK START`

1. **Import this page** into your Notion workspace
2. **Create databases** from the CSV files in the `/databases` folder (see SETUP-GUIDE.md)
3. **Link databases** to the views below using Notion's linked database feature
4. **Replace sample data** with your actual projects and numbers
5. **Run your first monthly P&L** at the end of this month

**Estimated setup time:** 15 minutes

---

## `// DASHBOARD`

Your bird's-eye view of every dollar coming in and going out. Pin this page to your sidebar.

### Revenue Snapshot (Update Monthly)

| Metric | This Month | Last Month | Trend |
|--------|-----------|-----------|-------|
| Total Revenue | $9,240 | $8,150 | Up |
| Total Expenses | $1,680 | $1,420 | Up |
| Net Profit | $7,560 | $6,730 | Up |
| Active Projects | 6 | 5 | Up |
| Avg Hourly Rate | $68.50 | $62.30 | Up |
| Best Performer | Automation Services | Automation Services | Stable |

### Quick Actions

- [ ] Update this month's revenue for each project
- [ ] Log any new expenses
- [ ] Review task board -- clear blockers
- [ ] Check launch checklist for upcoming launches
- [ ] Run monthly P&L calculation

### Alerts

> **Revenue Alert:** Prompt Pack Store sales dropped 18% -- consider a new bundle or promotion
> **Expense Alert:** Marketing spend up 40% this month -- check ROI on Facebook Ads
> **Launch Alert:** AI Course launch checklist 60% complete -- on track for April deadline

---

## `// PROJECTS`

Every AI-powered side project in one place. The goal: know exactly what each project earns, what it costs, and whether it's worth your time.

### Project Status Guide

| Status | Meaning | Action |
|--------|---------|--------|
| Active | Running and generating revenue | Maintain and optimise |
| Scaling | Actively investing to grow | Track growth rate weekly |
| Paused | Temporarily stopped | Review monthly -- restart or kill |
| Planning | Not yet launched | Use Launch Checklist to ship it |
| Completed | Finished or archived | Review for lessons learned |

### Database Properties

| Property | Type | Description |
|----------|------|-------------|
| Project Name | Title | Name of the side project |
| Category | Select | Freelancing, Digital Product, Content, Course, SaaS, Automation |
| Platform | Select | Gumroad, Substack, Upwork, Fiverr, Etsy, Udemy, Own Website |
| Monthly Revenue ($) | Number | Current monthly revenue in AUD |
| Status | Select | Active, Scaling, Paused, Planning, Completed |
| Start Date | Date | When you started the project |
| URL | URL | Link to the project's live page |
| AI Tools Used | Multi-select | Claude, ChatGPT, Midjourney, Runway, n8n, etc. |
| Monthly Hours | Number | Hours per month spent on this project |
| Effective Hourly Rate ($) | Formula | Monthly Revenue / Monthly Hours |
| Growth Rate (%) | Number | Month-over-month revenue growth |
| Notes | Text | Context, plans, observations |

### Linked Database: Projects

> *Create a linked database view here pointing to the Projects database*
> Recommended views:
> - **Revenue by Project** -- table sorted by Monthly Revenue descending
> - **By Status** -- board view grouped by Status column (Kanban)
> - **By Platform** -- grouped by Platform column
> - **Hourly Rate Ranked** -- sorted by Effective Hourly Rate descending
> - **Growth Leaders** -- sorted by Growth Rate descending

### Revenue per Hour Calculator

For each project, your effective hourly rate tells you the truth:

```
Monthly Revenue / Monthly Hours = $/hour

Example: $5,500 / 62 hrs = $88.71/hour
```

Anything below $30/hour is a red flag. Either automate it, outsource it, or kill it.

### The 80/20 Rule for Side Hustles

```
Most people spread too thin. Focus on the projects that:
1. Generate the highest $/hour
2. Have the strongest growth rate
3. Build compounding assets (courses, templates, SaaS)
4. Require the least active time (passive income)

Kill or pause everything else. 3-4 focused projects beat 8 scattered ones.
```

---

## `// INCOME LOG`

Record every dollar that comes in. Track by project, source, and payment method. This is your single source of truth for revenue.

### How to Log Income

Every time you receive a payment, add a row:

```
Date | Project | Amount | Source (platform or client name)
Payment Method | Notes | Tax Withheld | Net Amount
```

Log payments as they hit your account, not when invoiced. This keeps your P&L accurate.

### Database Properties

| Property | Type | Description |
|----------|------|-------------|
| Date | Date | When you received the payment |
| Project | Relation | Links to Projects database |
| Amount ($) | Number | Gross amount received in AUD |
| Source | Text | Gumroad, Stripe, client name, etc. |
| Payment Method | Select | PayPal, Stripe, Bank Transfer, Gumroad, Direct Deposit |
| Notes | Text | Invoice number, client details, context |
| Tax Withheld ($) | Number | Any tax withheld at source |
| Net Amount ($) | Formula | Amount minus Tax Withheld |

### Linked Database: Income Log

> *Create a linked database view here pointing to the Income Log database*
> Recommended views:
> - **Recent** -- sorted by Date descending, last 30 days
> - **By Project** -- grouped by Project column, summing Amount
> - **Monthly Totals** -- grouped by month, summing Amount and Net Amount
> - **By Source** -- grouped by Source column

### Tax Tracking Notes (Australia)

```
If you're earning side hustle income in Australia:
- You MUST declare all income in your tax return (even small amounts)
- Register for an ABN if you're operating as a sole trader
- If turnover exceeds $75K, you must register for GST
- Track tax withheld per payment for your BAS
- Keep all records for 5 years (ATO requirement)

This is not tax advice. Talk to your accountant.
```

---

## `// EXPENSE TRACKER`

Track every business expense. Know what each project costs to run. Be ready for BAS time.

### How to Log Expenses

Log expenses as they happen -- not at tax time. Set a weekly reminder (Friday afternoon):

```
1. Check bank statement for business charges
2. Add any missing expenses to the database
3. Mark tax-deductible items
4. Attach receipt file names
5. Tag the project it belongs to
```

### Database Properties

| Property | Type | Description |
|----------|------|-------------|
| Date | Date | When the expense occurred |
| Category | Select | Software, Marketing, Education, Hardware, Outsourcing, Hosting, Office, Other |
| Description | Title | What you bought or paid for |
| Amount ($) | Number | Amount in AUD |
| Project | Relation | Links to Projects database |
| Tax Deductible | Checkbox | Whether this is a claimable business expense |
| Receipt | Text | File name or link to stored receipt |
| Vendor | Text | Who you paid |
| Payment Method | Select | Credit Card, PayPal, Bank Transfer, Direct Debit |
| Notes | Text | Additional context |

### Linked Database: Expense Tracker

> *Create a linked database view here pointing to the Expenses database*
> Recommended views:
> - **Recent** -- sorted by Date descending
> - **By Category** -- grouped by Category, summing Amount
> - **By Project** -- grouped by Project column, summing Amount
> - **Tax Deductible** -- filtered to Tax Deductible = Yes
> - **Monthly Total** -- grouped by month, summing Amount

### Tax Deduction Categories (Australia)

```
Commonly deductible for AI side hustles:
- Software subscriptions (AI tools, hosting, design tools)
- Marketing and advertising spend
- Education and training (courses, bootcamps, conferences)
- Hardware (laptop, tablet, monitor -- percentage of business use)
- Home office expenses (percentage of rent/mortgage, utilities)
- Outsourcing and contractor payments
- Domain names and hosting
- Professional services (accountant, legal)

Keep ALL receipts. The ATO can audit you for up to 4 years.
Talk to your accountant about the $20K instant asset write-off threshold.
```

---

## `// TASK BOARD`

Kanban-style task management tied to your projects. Stop juggling five to-do apps. Everything lives here.

### Task Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| Backlog | Captured but not started | Review weekly -- promote or delete |
| To Do | Committed for this week/sprint | Start working on it |
| In Progress | Actively working on it | Finish before starting new tasks |
| Blocked | Waiting on something external | Document the blocker in Notes |
| Done | Completed | Celebrate, then archive monthly |

### Database Properties

| Property | Type | Description |
|----------|------|-------------|
| Task Name | Title | What needs to be done |
| Project | Relation | Links to Projects database |
| Priority | Select | High, Medium, Low |
| Status | Select | Backlog, To Do, In Progress, Blocked, Done |
| Due Date | Date | When it needs to be finished |
| Estimated Hours | Number | How long you think it will take |
| Actual Hours | Number | How long it actually took (fill in when done) |
| Category | Select | Build, Marketing, Admin, Content, Design, Research |
| Notes | Text | Context, blockers, links |

### Linked Database: Task Board

> *Create a linked database view here pointing to the Task Board database*
> Recommended views:
> - **Kanban** -- board view grouped by Status (this is your daily driver)
> - **My Week** -- filtered to Status = To Do or In Progress, sorted by Priority
> - **By Project** -- grouped by Project column
> - **Overdue** -- filtered to Due Date < Today AND Status != Done
> - **Time Tracking** -- table showing Estimated vs Actual Hours

### Task Prioritisation

```
PRIORITY MATRIX

High Impact + Low Effort  = DO FIRST  (quick wins)
High Impact + High Effort = SCHEDULE   (big bets)
Low Impact  + Low Effort  = BATCH      (do them all at once)
Low Impact  + High Effort = DROP       (time traps)
```

### Weekly Task Review (10 minutes, Sunday evening)

```
- [ ] Move completed tasks to Done
- [ ] Clear anything sitting in Backlog for 3+ weeks (delete or commit)
- [ ] Pull top-priority items into To Do for the week
- [ ] Check for overdue tasks -- reschedule or drop
- [ ] Ensure each active project has at least one task in flight
```

---

## `// LAUNCH CHECKLIST`

A repeatable checklist for launching new AI side projects. Copy this for each new launch.

### Launch Phases

| Phase | Description | Typical Duration |
|-------|-------------|-----------------|
| Research | Validate the idea before building | 1-2 weeks |
| Build | Create the product or service | 2-4 weeks |
| Pre-Launch | Set up marketing and distribution | 1 week |
| Launch | Go live and promote | 1-3 days |
| Post-Launch | Iterate based on feedback | Ongoing |

### Database Properties

| Property | Type | Description |
|----------|------|-------------|
| Item | Title | The checklist item |
| Phase | Select | Research, Build, Pre-Launch, Launch, Post-Launch |
| Project | Relation | Links to Projects database |
| Status | Select | Not Started, In Progress, Done, Skipped |
| Due Date | Date | Target completion date |
| Owner | Text | Who's responsible (you, contractor, etc.) |
| Dependencies | Text | What needs to happen first |
| Notes | Text | Links, context, decisions |

### Linked Database: Launch Checklist

> *Create a linked database view here pointing to the Launch Checklist database*
> Recommended views:
> - **By Phase** -- grouped by Phase column (Research -> Build -> Pre-Launch -> Launch -> Post-Launch)
> - **Active Launch** -- filtered to a specific Project, sorted by Phase then Due Date
> - **Incomplete** -- filtered to Status != Done AND Status != Skipped
> - **Timeline** -- sorted by Due Date ascending

### Launch Checklist Template

Copy this for every new project launch:

```
RESEARCH PHASE
- [ ] Validate demand (search volume, Reddit threads, competitor analysis)
- [ ] Identify target audience and their specific pain point
- [ ] Check competitor pricing and positioning
- [ ] Estimate time to MVP and decide go/no-go

BUILD PHASE
- [ ] Define MVP scope (what's the minimum viable version?)
- [ ] Build the core product or service
- [ ] Create sample content or demo
- [ ] Test with 2-3 people from your target audience
- [ ] Iterate based on feedback

PRE-LAUNCH PHASE
- [ ] Write sales page copy
- [ ] Create thumbnail and preview images
- [ ] Set up payment processing (Gumroad, Stripe, etc.)
- [ ] Prepare launch announcement (email, social, communities)
- [ ] Set pricing (with launch discount)

LAUNCH PHASE
- [ ] Publish the product
- [ ] Send launch announcement to email list
- [ ] Post in 3-5 relevant communities
- [ ] Share on social media
- [ ] Monitor for issues and respond to questions

POST-LAUNCH PHASE
- [ ] Collect first 5 pieces of customer feedback
- [ ] Fix any critical issues within 24 hours
- [ ] Add to Projects database with revenue tracking
- [ ] Plan first iteration based on feedback
- [ ] Set up recurring promotion schedule
```

---

## `// MONTHLY P&L`

Your profit and loss summary. Update this at the end of each month to see the real numbers.

### Monthly P&L Template

Copy this at the end of each month and fill in actuals:

```
## [MONTH YEAR] Profit & Loss

### Revenue by Project
| Project | Revenue ($) | % of Total |
|---------|------------|------------|
| [Project 1] | [AMOUNT] | [%] |
| [Project 2] | [AMOUNT] | [%] |
| [Project 3] | [AMOUNT] | [%] |
| **TOTAL REVENUE** | **[AMOUNT]** | **100%** |

### Expenses by Category
| Category | Amount ($) | % of Revenue |
|----------|-----------|-------------|
| Software & Tools | [AMOUNT] | [%] |
| Marketing | [AMOUNT] | [%] |
| Outsourcing | [AMOUNT] | [%] |
| Education | [AMOUNT] | [%] |
| Other | [AMOUNT] | [%] |
| **TOTAL EXPENSES** | **[AMOUNT]** | **[%]** |

### Summary
- **Net Profit:** $[AMOUNT]
- **Profit Margin:** [%]
- **Effective Hourly Rate:** $[AMOUNT]
- **Total Hours Worked:** [COUNT]

### Key Decisions
- Top performer: [PROJECT] -- action: [SCALE / MAINTAIN]
- Underperformer: [PROJECT] -- action: [FIX / PAUSE / KILL]
- New opportunity: [DESCRIPTION]
- Expense to cut: [DESCRIPTION]
```

### P&L Health Indicators

```
GREEN (healthy):
  Profit margin above 70%
  Revenue growing month-over-month
  Expenses under 30% of revenue
  At least one project with passive income

YELLOW (watch):
  Profit margin 50-70%
  Revenue flat for 2+ months
  Expenses between 30-50% of revenue
  All income requires active work

RED (fix now):
  Profit margin below 50%
  Revenue declining
  Expenses above 50% of revenue
  Burning out from too many projects
```

---

## `// RESOURCES`

### Useful Links

- [Gumroad Creator Dashboard](https://gumroad.com/dashboard) -- digital product sales
- [Substack Dashboard](https://substack.com/dashboard) -- newsletter analytics
- [Udemy Instructor Dashboard](https://www.udemy.com/instructor/) -- course revenue
- [Etsy Shop Manager](https://www.etsy.com/your/shops/me/dashboard) -- marketplace sales
- [Upwork Reports](https://www.upwork.com/reports/) -- freelance earnings
- [ATO Business Portal](https://www.ato.gov.au/business/) -- Australian tax obligations
- [ABN Lookup](https://abr.business.gov.au/) -- verify your ABN registration

### Notion Shortcuts for Fast Data Entry

```
Notion shortcuts that speed up logging:
  Cmd/Ctrl + N         New page (quick entry)
  /database inline     Create inline database view
  /template            Create a reusable template button
  /board               Create a board view (Kanban)
  @today               Insert today's date
  /callout             Insert callout for alerts
```

### Side Hustle Health Indicators

```
GREEN (healthy):
  Revenue growing month-over-month
  Hourly rate above $50
  Expenses under 30% of revenue
  At least one passive income project

YELLOW (watch):
  Revenue flat for 2+ months
  Hourly rate between $30-$50
  Expenses between 30-50% of revenue
  All income requires active work

RED (fix now):
  Revenue declining
  Hourly rate below $30
  Expenses above 50% of revenue
  Burning out from too many projects
```

---

*Built for solopreneurs who are done guessing and ready to run their AI side hustles like a real business.*
*Version 1.0 | Last updated: March 2026*
