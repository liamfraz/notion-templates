# Side Hustle Tracker & Revenue Dashboard

> Track every side hustle, every dollar, every hour. Know your numbers. Grow what works. Cut what doesn't. Built for anyone running multiple income streams.

---

## `// QUICK START`

1. **Import this page** into your Notion workspace
2. **Create databases** from the CSV files in the `/databases` folder (see SETUP-GUIDE.md)
3. **Replace sample data** with your actual side hustles, revenue, and expenses
4. **Set your first quarterly review** -- block 45 minutes at the end of each quarter

**Estimated setup time:** 40 minutes

---

## `// REVENUE DASHBOARD`

Your bird's-eye view of every dollar coming in and going out. Pin this page to your sidebar.

### Revenue Snapshot (Update Monthly)

| Metric | Value |
|--------|-------|
| Total Revenue | $12,840/mo |
| Total Expenses | $2,460/mo |
| Net Profit | $10,380/mo |
| Active Hustles | 9 |
| Best Performer | Freelance Copywriting ($3,200/mo) |
| Avg Monthly Growth | +11% |
| Estimated Tax Liability | $2,890/qtr |

### Quick Actions

- [ ] Update this month's revenue for each hustle
- [ ] Log any new expenses
- [ ] Check hourly rate per hustle -- flag anything below $35/hr
- [ ] Review goals progress and update milestones
- [ ] Run the Hustle Scoring System for any new or changed hustles
- [ ] Estimate next quarter's tax liability

### Alerts

> **Goal Alert:** Etsy shop revenue stalled for 2 months -- consider new product line or SEO refresh
> **Revenue Alert:** Dropshipping margins thinning -- supplier costs up 8%, review pricing
> **Tax Alert:** Approaching $75K annual revenue -- review GST registration requirements
> **Time Alert:** Private tutoring hourly rate dropped below $40 -- reassess scheduling

---

## `// SIDE HUSTLES`

Every income stream in one place. The goal: know exactly where your money comes from, how much effort each hustle takes, and which ones deserve more of your time.

### Hustle Scoring System

Rate each hustle from 1-5 on these five dimensions. Total score out of 25 tells you where to focus.

| Dimension | What It Measures | 1 (Low) | 5 (High) |
|-----------|-----------------|---------|----------|
| Revenue Score | Current monthly earnings | Under $200 | Over $3,000 |
| Growth Score | Month-over-month trajectory | Declining | Growing 20%+ |
| Time Efficiency | Effective hourly rate | Under $20/hr | Over $80/hr |
| Scalability | Can it grow without more hours? | Fully manual | Fully passive |
| Passion Score | How much you enjoy the work | Dread it | Love it |

**How to interpret:**

```
20-25: Star Performer -- double down, this is your future
15-19: Solid Earner -- maintain and look for efficiency gains
10-14: Average -- needs improvement or a clear growth plan
5-9:   Underperformer -- set a 90-day deadline to improve or kill it
```

### Linked Database: Side Hustles

> *Create a linked database view here pointing to the Side Hustles database*
> Recommended views:
> - **All Active** -- filtered to Status = Active or Scaling, sorted by Net Profit descending
> - **By Category** -- grouped by Category column (E-commerce, Freelance, Content Creation, etc.)
> - **Hustle Score Ranked** -- sorted by Total Score descending
> - **Revenue per Hour** -- sorted by effective hourly rate descending (calculated: Net Profit / (Hours/Week x 4.3))
> - **Scalability Focus** -- filtered to Scalability >= 4, sorted by Growth Score descending

### The Three Questions for Every Hustle

```
Before adding any new hustle to the tracker, answer these:

1. Can this earn $1,000/month within 6 months?
   If no, it's a hobby -- track it separately.

2. Can this scale without proportionally more hours?
   If no, you're building a second job, not a side hustle.

3. Does this leverage a skill or asset you already have?
   If no, the learning curve will eat your first 3-6 months of profit.

Two "no" answers = don't start it.
Three "no" answers = definitely don't start it.
```

---

## `// MONTHLY REVENUE`

Track revenue, expenses, and profit for each hustle every month. This is where you spot trends, catch declining streams early, and celebrate wins.

### How to Track

```
On the 1st of each month (or last day of prior month):
1. Open each platform dashboard and note final revenue
2. Add one row per hustle to the Monthly Revenue database
3. Fill in revenue, expenses, hours spent
4. Hourly Rate is auto-calculated: Net Profit / Hours Spent
5. Note the Growth vs Prior column -- flag anything declining 2+ months in a row
```

### Linked Database: Monthly Revenue

> *Create a linked database view here pointing to the Monthly Revenue database*
> Recommended views:
> - **Current Month** -- filtered to current month, sorted by Revenue descending
> - **By Hustle** -- grouped by Hustle column
> - **Trend View** -- sorted by Month, showing Revenue and Net Profit columns
> - **Hourly Rate Ranked** -- sorted by Hourly Rate descending
> - **Growth Tracker** -- filtered to show only declining hustles (Growth vs Prior contains "-")

### Monthly Review Template

Copy this at the end of each month:

```
## [MONTH YEAR] Revenue Review

### Summary
Total Revenue: $[AMOUNT]
Total Expenses: $[AMOUNT]
Net Profit: $[AMOUNT]
Total Hours: [COUNT]
Blended Hourly Rate: $[AMOUNT]

### Top Performer
Hustle: [NAME]
Revenue: $[AMOUNT]
Hourly Rate: $[AMOUNT]
Why: [EXPLANATION]

### Underperformer
Hustle: [NAME]
Revenue: $[AMOUNT]
Hourly Rate: $[AMOUNT]
Action: [SCALE / PIVOT / KILL]

### Time-Value Check
Highest $/hour: [NAME] at $[AMOUNT]/hr
Lowest $/hour: [NAME] at $[AMOUNT]/hr
Should I reallocate hours from lowest to highest? [YES/NO/WHY]

### Key Decisions
- [What to double down on]
- [What to cut or pause]
- [New hustles to explore]
- [Expenses to reduce]
```

---

## `// EXPENSES`

Track every business expense for tax time and profit calculations. Log them as they happen -- not at tax time.

### Linked Database: Expenses

> *Create a linked database view here pointing to the Expenses database*
> Recommended views:
> - **Recent** -- sorted by Date descending
> - **By Category** -- grouped by Category (Software, Marketing, Inventory, etc.)
> - **By Hustle** -- grouped by Hustle column
> - **Tax Deductible** -- filtered to Tax Deductible = Yes
> - **Monthly Total** -- sorted by Date, showing sum of Amount
> - **Big Expenses** -- filtered to Amount > $200, sorted by Amount descending

### Tax Deduction Categories (Australia)

```
Commonly deductible for side hustle businesses:

OPERATIONAL
- Software subscriptions (Shopify, Canva, accounting tools)
- Marketing and advertising spend (Facebook Ads, Google Ads)
- Inventory and stock purchases
- Shipping and postage costs
- Platform fees (Etsy, eBay, Gumroad percentages)

PROFESSIONAL
- Outsourcing and contractor payments
- Accounting and bookkeeping fees
- Business insurance
- Professional development (courses, books, conferences)
- ABN registration and business licences

EQUIPMENT
- Computer hardware (laptop, monitor, keyboard)
- Camera and lighting equipment
- Office furniture (percentage of business use)
- Phone (percentage of business use)

HOME OFFICE
- Percentage of rent/mortgage (dedicated office space)
- Percentage of electricity, internet, phone
- Home office occupancy expenses (council rates, insurance)

Keep ALL receipts. Digital copies are fine -- the ATO accepts photos and scans.
Talk to your accountant about the $20K instant asset write-off threshold.
```

### Expense Logging Habit

```
Log expenses as they happen -- not at tax time.

Weekly check (Friday afternoon, 10 minutes):
1. Check bank statement and credit card for business charges
2. Add any missing expenses to the database
3. Photograph/scan receipts and note the file name
4. Tag the hustle it belongs to
5. Mark whether it's tax deductible

Monthly check (end of month, 5 minutes):
1. Verify all recurring subscriptions are logged
2. Check for any forgotten one-off purchases
3. Ensure receipt column is filled for every entry
```

---

## `// TAX CALCULATOR`

Estimate your quarterly and annual tax liability. Plan ahead so tax time isn't a nasty surprise.

> **IMPORTANT DISCLAIMER:** This section provides estimates only. It is NOT tax advice. Tax law is complex and your individual circumstances matter. Always consult a registered tax agent or accountant for your actual tax return. The information below is based on publicly available ATO rates and may change.

### Australian Tax Brackets 2025-26

| Taxable Income | Tax Rate | Tax on This Bracket |
|---------------|----------|-------------------|
| $0 -- $18,200 | 0% | $0 |
| $18,201 -- $45,000 | 16% | Up to $4,288 |
| $45,001 -- $135,000 | 30% | Up to $27,000 |
| $135,001 -- $190,000 | 37% | Up to $20,350 |
| $190,001+ | 45% | No cap |

### Medicare Levy

```
Standard Medicare Levy: 2% of taxable income
Medicare Levy Surcharge: additional 1-1.5% if you earn over $93,000
and don't have private health insurance

Include Medicare Levy in all your tax estimates.
```

### GST Threshold

```
You MUST register for GST if your annual turnover reaches $75,000.

If you're approaching this threshold:
- Track your rolling 12-month revenue carefully
- Register BEFORE you hit $75K, not after
- Once registered, you charge 10% GST on sales and can claim GST credits
  on business purchases
- BAS lodgement is required quarterly or monthly

Tip: If your clients are mostly overseas (e.g., selling digital products
internationally), those sales may be GST-free exports. Talk to your accountant.
```

### Worked Example: Estimating Quarterly Tax

```
SCENARIO: Side hustles earning $12,840/month alongside a day job

Assumptions:
- Day job salary: $85,000/year (tax already withheld by employer)
- Side hustle gross income: $12,840/month = $154,080/year
- Allowable deductions: $29,520/year
- Side hustle taxable income: $124,560/year
- Combined taxable income: $85,000 + $124,560 = $209,560

TAX CALCULATION (on combined income):
  $0 - $18,200:        $0
  $18,201 - $45,000:   $4,288  (16% of $26,800)
  $45,001 - $135,000:  $27,000 (30% of $90,000)
  $135,001 - $190,000: $20,350 (37% of $55,000)
  $190,001 - $209,560: $8,802  (45% of $19,560)
  Total tax:           $60,440
  Medicare Levy (2%):  $4,191
  Grand total:         $64,631

  Minus tax already withheld on salary (approx): $20,797
  Remaining liability: $43,834
  Quarterly instalment: ~$10,959

IMPORTANT: This is a rough estimate. Your accountant will calculate
the exact amount including offsets, rebates, and deductions specific
to your situation.
```

### Quarterly Tax Formula

```
Step 1: Estimate annual side hustle income
        (Monthly revenue x 12)

Step 2: Subtract allowable deductions
        (Business expenses, home office, depreciation)

Step 3: Add to your other taxable income
        (Employment, investments, etc.)

Step 4: Apply tax brackets above

Step 5: Add Medicare Levy (2%)

Step 6: Subtract tax already withheld from employment

Step 7: Divide remaining liability by 4

Step 8: Set aside that amount each quarter in a separate savings account
        DO NOT spend your tax money.
```

### Linked Database: Tax Estimates

> *Create a linked database view here pointing to the Tax Estimates database*
> Recommended views:
> - **Current Year** -- all quarters for 2026
> - **Unpaid** -- filtered to Status != Paid

---

## `// GOALS`

Set targets, track progress, stay accountable. Every goal has milestones so you can see momentum, not just the finish line.

### SMART Goal Template

```
Before adding a goal, run it through this filter:

Specific:    What exactly will you achieve? (Not "make more money")
Measurable:  What number will you track? (e.g., $5,000/mo revenue)
Achievable:  Is it realistic given your current trajectory?
Relevant:    Does it align with your bigger picture?
Time-bound:  What's the deadline?

BAD:  "Grow my Etsy shop"
GOOD: "Reach $2,000/month Etsy revenue by 30 September 2026"
```

### Progress Tracking Framework

```
For each goal, define 3 milestones:

Milestone 1 (25%): The first meaningful step. Proves the concept.
Milestone 2 (50%): Halfway point. Momentum is real.
Milestone 3 (75%): Almost there. Final push territory.
Goal (100%):       Done. Celebrate. Set the next one.

Update progress weekly. If a goal hasn't moved in 3 weeks,
it's either too vague or you've silently deprioritised it.
Either sharpen it or remove it -- zombie goals drain energy.
```

### Linked Database: Goals

> *Create a linked database view here pointing to the Goals database*
> Recommended views:
> - **Active Goals** -- filtered to Status != Achieved, sorted by Priority
> - **By Hustle** -- grouped by Hustle column
> - **Behind Schedule** -- filtered to Status = Behind
> - **Achieved** -- filtered to Status = Achieved (celebrate wins)
> - **Progress Board** -- board view grouped by Status (Not Started -> On Track -> Behind -> Achieved)

---

## `// TIME TRACKER`

Understand your true hourly rate per hustle. Time is your most limited resource -- spend it where the returns are highest.

### Time-Value Analysis Framework

```
For each hustle, calculate:

Effective Hourly Rate = Monthly Net Profit / Monthly Hours

Then categorise:

PREMIUM TIME ($80+/hr):
  This is where you should spend MORE hours.
  Automate everything around it. Protect this time fiercely.

GOOD TIME ($50-$80/hr):
  Solid return. Look for ways to increase rate:
  - Raise prices
  - Reduce admin time
  - Systematise repeatable tasks

ACCEPTABLE TIME ($30-$50/hr):
  Worth doing if it's growing or if you enjoy it.
  Set a 6-month improvement target.

POOR TIME (Under $30/hr):
  Red flag. Either:
  - You're still in the learning/building phase (acceptable for 3 months)
  - The hustle is fundamentally low-value (kill it)
  - You're doing too much admin (automate or outsource)
```

### When to Quit a Hustle: Decision Tree

```
Ask these questions in order:

1. Has it earned less than $500/month for 3+ consecutive months?
   YES → Go to Q2
   NO  → Keep going, it's still viable

2. Is the trend improving, flat, or declining?
   IMPROVING → Give it 3 more months with specific targets
   FLAT      → Go to Q3
   DECLINING → Go to Q4

3. Is your hourly rate above $30/hr?
   YES → It's stable but small. Keep if you enjoy it, otherwise reallocate time.
   NO  → Go to Q4

4. Do you have a specific, actionable plan to fix it?
   YES → Implement the plan. Review in 60 days. If no improvement, kill it.
   NO  → Kill it. Reallocate those hours to your highest-scoring hustle.

"Killing" doesn't mean deleting everything. It means:
- Stop spending active hours on it
- Let passive income trickle if applicable
- Archive the knowledge for potential future use
- Free up those hours for better opportunities
```

### Linked Database: Time Log

> *Create a linked database view here pointing to the Time Log database*
> Recommended views:
> - **This Week** -- filtered to current week, sorted by Date descending
> - **By Hustle** -- grouped by Hustle, showing sum of Hours
> - **By Activity Type** -- grouped by Activity Type
> - **Billable Only** -- filtered to Billable = Yes
> - **Energy Tracker** -- sorted by Energy Level, helps identify when you do your best work

### Weekly Time Audit (10 minutes, Sunday evening)

```
1. Review this week's time entries
2. Calculate hours per hustle
3. Flag any hustle where you spent 5+ hours with under $30/hr return
4. Plan next week: allocate hours intentionally, starting with highest-value hustles
5. Block time in your calendar for your top 2 hustles FIRST
```

---

## `// QUARTERLY REVIEW`

Block 45 minutes at the end of each quarter. This is your deep-dive session where you make the big decisions.

### Quarterly Review Checklist

```
REVENUE ANALYSIS (10 min)
- [ ] Update all Monthly Revenue entries for the quarter
- [ ] Calculate total revenue, expenses, and net profit for Q[X]
- [ ] Compare to previous quarter -- what grew, what shrank?
- [ ] Identify your top 3 earners and bottom 3 earners
- [ ] Calculate blended hourly rate across all hustles

EXPENSE AUDIT (10 min)
- [ ] Review every recurring subscription -- cancel unused ones
- [ ] Check total expenses as a percentage of revenue (target: under 20%)
- [ ] Identify the 3 largest expenses -- are they justified?
- [ ] Ensure all receipts are saved for tax deductions
- [ ] Check for any forgotten or uncategorised expenses

TAX PREPARATION (10 min)
- [ ] Update the Tax Estimates database with actual Q[X] figures
- [ ] Compare estimated tax to actual earnings -- adjust next quarter
- [ ] Set aside quarterly tax instalment in savings account
- [ ] Check if approaching GST threshold ($75K annual)
- [ ] Note any large deductions for accountant

GOAL SETTING (10 min)
- [ ] Review all active goals -- mark achieved ones
- [ ] Update progress percentages and milestones
- [ ] Set 2-3 new goals for next quarter
- [ ] Identify the single most impactful goal for Q[X+1]
- [ ] Remove or archive any zombie goals

HUSTLE SCORING REVIEW (5 min)
- [ ] Re-score all active hustles using the Scoring System
- [ ] Any hustle below 10 points for 2 consecutive quarters? Kill it.
- [ ] Any hustle above 20 points? Allocate more time to it.
- [ ] Any new hustles to add to the tracker?
- [ ] Update the Revenue Dashboard snapshot table
```

---

## `// RESOURCES`

### Useful Links

- [ATO Business Portal](https://www.ato.gov.au/business/) -- Australian tax obligations
- [Register for an ABN](https://www.abr.gov.au/) -- Australian Business Number
- [business.gov.au](https://www.business.gov.au/) -- Australian government business resources
- [ATO Instant Asset Write-Off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business) -- equipment deductions
- [Xero](https://www.xero.com/au/) -- accounting software (popular in Australia)
- [MYOB](https://www.myob.com/au) -- Australian accounting software
- [Rounded](https://www.rounded.com.au/) -- invoicing and expense tracking for freelancers
- [Gumroad Creator Dashboard](https://gumroad.com/dashboard) -- digital product sales
- [Etsy Shop Manager](https://www.etsy.com/your/shops/me/dashboard) -- e-commerce sales
- [Shopify Admin](https://admin.shopify.com/) -- dropshipping and e-commerce
- [Substack Dashboard](https://substack.com/dashboard) -- newsletter analytics
- [Udemy Instructor Dashboard](https://www.udemy.com/instructor/) -- course revenue
- [Upwork Reports](https://www.upwork.com/reports/) -- freelance earnings
- [Fiverr Analytics](https://www.fiverr.com/seller_dashboard/analytics) -- gig earnings

### Side Hustle Health Indicators

```
GREEN (healthy):
  Revenue growing month-over-month
  Hourly rate above $50 across all hustles
  Expenses under 20% of revenue
  At least one passive/scalable income stream
  Tax money set aside quarterly
  Hustle scores mostly 15+ out of 25

YELLOW (watch):
  Revenue flat for 2+ months on any hustle
  Hourly rate between $30-$50 on any hustle
  Expenses between 20-30% of revenue
  All income requires active hours
  Tax estimates haven't been updated this quarter
  Any hustle score between 10-14

RED (fix now):
  Revenue declining on 2+ hustles
  Any hourly rate below $25
  Expenses above 30% of revenue
  Burning out from too many hustles (more than 6 active)
  No tax money set aside
  Any hustle score below 10 for 2+ quarters
  Approaching GST threshold without being registered
```

---

*Built for the multi-hustle era. Track it, optimise it, scale what works, cut what doesn't.*
*Version 1.0 | Last updated: March 2026*
