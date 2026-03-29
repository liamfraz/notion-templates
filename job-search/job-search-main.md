# Job Search CRM 2026 -- Your Structured Job Hunt Dashboard

> Land your next role faster. Track applications, prep for interviews, research salaries, and manage offers -- all in one workspace. Built for tech professionals navigating the 2026 job market.

---

## `// QUICK START`

1. **Import this page** into your Notion workspace
2. **Create databases** from the CSV files in the `/databases` folder (see SETUP-GUIDE.md)
3. **Link databases** to the views below using Notion's linked database feature
4. **Add your first application** -- the best time to start tracking is now

**Estimated setup time:** 20 minutes

---

## `// MISSION CONTROL`

Your job search at a glance. Pin this page to your sidebar and check it daily.

### Pipeline Snapshot (Update Weekly)

| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Active Applications | 7 | 5 | Up |
| Interviews Scheduled | 3 | 2 | Up |
| Responses Received | 4 | 3 | Up |
| Offers in Hand | 1 | 0 | Up |
| Networking Contacts Made | 3 | 2 | Up |
| Response Rate | 57% | 40% | Up |

### Daily Actions

- [ ] Check email and LinkedIn for recruiter messages
- [ ] Follow up on applications older than 7 days
- [ ] Send one networking message (coffee chat, referral request, check-in)
- [ ] Review and prep for any interviews in the next 48 hours
- [ ] Log any new applications or status changes

### Active Alerts

> **Offer deadline:** SafetyCulture offer expires March 20 -- decision needed in 5 days
> **Interview prep:** Atlassian System Design round on March 8 -- prep materials ready?
> **Follow-up overdue:** Envato application has been ghosted for 6 weeks -- mark as closed

---

## `// APPLICATIONS TRACKER`

Every role you apply to, tracked from first click to final outcome. No more spreadsheet chaos.

### Application Status Guide

| Status | Meaning | Your Action |
|--------|---------|-------------|
| Applied | Application submitted | Wait 5-7 business days, then follow up |
| Screening | Recruiter is reviewing | Respond to any requests within 24 hours |
| Phone Screen | Initial call scheduled | Research company, prepare elevator pitch |
| Technical Interview | Technical round scheduled | Study relevant tech stack, practice problems |
| Onsite | Final round / onsite visit | Deep prep, prepare questions, plan logistics |
| Offer | Offer received | Review comp, negotiate, compare with other offers |
| Rejected | They said no | Ask for feedback, note learnings, move on |
| Withdrawn | You said no | Document why -- helps refine what you want |
| Ghosted | No response after 3+ weeks | Follow up once more, then close and move on |

### Linked Database: Applications

> *Create a linked database view here pointing to the Applications database*
> Recommended views:
> - **Active Pipeline** -- filtered to Status not in (Rejected, Withdrawn, Ghosted), sorted by Applied Date
> - **By Status** -- grouped by Status column (Kanban board view)
> - **Dream Jobs** -- filtered to Priority = Dream Job or Strong Fit
> - **All Applications** -- full table sorted by Applied Date descending

### Application Quality Checklist

Before submitting any application:

```
- [ ] Resume tailored to this specific role (not generic)
- [ ] Cover letter addresses their specific needs (if required)
- [ ] Researched the company's recent news and product updates
- [ ] Identified at least one internal contact to reach out to
- [ ] Salary range is within your acceptable band
- [ ] You can genuinely see yourself in this role for 2+ years
```

### Response Rate Tracker

Track your response rates to improve your approach:

```
## Week of [DATE]

Applications sent: [COUNT]
Responses received: [COUNT]
Response rate: [PERCENT]%

Top source this week: [SOURCE]
Weakest source: [SOURCE]

Resume version used: [VERSION]
Any patterns in rejections? [NOTES]
```

---

## `// INTERVIEW TRACKER`

Prep is everything. Track every round, every interviewer, every follow-up.

### Interview Round Guide

| Round | What to Expect | Prep Time |
|-------|---------------|-----------|
| Phone Screen | 30 min with recruiter, culture fit, salary expectations | 1 hour |
| Technical 1 | Coding problems, system knowledge, or take-home | 4-8 hours |
| Technical 2 | Deeper dive, architecture, or pair programming | 4-6 hours |
| System Design | Large-scale design problem, whiteboarding | 6-10 hours |
| Behavioral | STAR stories, leadership principles, conflict resolution | 2-3 hours |
| Culture Fit | Team dynamics, work style, values alignment | 1-2 hours |
| Hiring Manager | Role specifics, team vision, growth trajectory | 2-3 hours |
| Final | Executive or cross-functional, usually conversational | 1-2 hours |

### Linked Database: Interviews

> *Create a linked database view here pointing to the Interviews database*
> Recommended views:
> - **Upcoming** -- filtered to Status = Scheduled, sorted by Date ascending
> - **By Company** -- grouped by Company column
> - **Results** -- showing Outcome column, sorted by Date descending
> - **Prep Needed** -- filtered to Status = Scheduled AND Date within 7 days

### Interview Prep Framework

Copy this for each upcoming interview:

```
## Interview Prep: [COMPANY] -- [ROUND]

### Company Research
- [ ] Recent product launches or pivots
- [ ] Engineering blog posts (last 6 months)
- [ ] Glassdoor interview reviews for this role
- [ ] Company values and how they apply to engineering
- [ ] Recent funding, layoffs, or leadership changes

### Technical Prep
- [ ] Review their tech stack (from Companies database)
- [ ] Practice 3 relevant coding problems
- [ ] Prepare 2 system design scenarios
- [ ] Review my recent projects for relevant examples

### Questions to Ask
1. [Technical question about their architecture]
2. [Team question about collaboration and growth]
3. [Product question about roadmap and priorities]

### STAR Stories Ready
- Challenge overcome: [STORY]
- Technical leadership: [STORY]
- Conflict resolution: [STORY]
- Failure and learning: [STORY]

### Logistics
- Date/time: [DATETIME]
- Platform: [Zoom/Google Meet/In-person]
- Interviewer: [NAME, ROLE]
- Dress code: [NOTES]
```

### Post-Interview Checklist

```
Within 1 hour:
- [ ] Send thank-you email to interviewer(s)
- [ ] Log interview details in the database
- [ ] Rate your own performance (honest 1-5)
- [ ] Note any questions you struggled with

Within 24 hours:
- [ ] Update application status
- [ ] Add any new contacts to Contacts database
- [ ] Review and improve prep notes for next round
```

---

## `// CONTACTS & NETWORKING`

Your network is your net worth in a job search. Track every meaningful connection.

### Relationship Types

| Type | How to Engage | Follow-up Frequency |
|------|--------------|-------------------|
| Recruiter | Be responsive, professional, direct about what you want | When they reach out |
| Hiring Manager | Research their work, ask thoughtful questions | After each interview round |
| Referral | Thank them, keep them updated on progress | Every 2 weeks during process |
| Mentor | Ask specific questions, share progress, respect their time | Monthly |
| Former Colleague | Catch up genuinely, mention you're looking, ask for intros | Every 2-3 weeks |
| Alumni | Lead with shared connection, be specific about asks | As needed |

### Linked Database: Contacts

> *Create a linked database view here pointing to the Contacts database*
> Recommended views:
> - **Active Contacts** -- filtered to Status = Active or Follow Up
> - **By Company** -- grouped by Company column
> - **Needs Follow-up** -- filtered to Last Contact older than 14 days AND Status != Cold
> - **By Relationship** -- grouped by Relationship type

### Networking Message Templates

**Reaching Out to a Connection for a Referral:**
```
Hi [NAME],

Hope you're doing well. I noticed [COMPANY] has an opening for
[ROLE] and I'm really interested in the team's work on [SPECIFIC
PROJECT/PRODUCT].

Given your experience there, would you be open to a quick chat
about what the team is like? And if it seems like a fit, I'd be
grateful for a referral.

Happy to work around your schedule. Thanks either way.

[YOUR NAME]
```

**Following Up After an Interview:**
```
Hi [NAME],

Thanks for taking the time to chat today. I really enjoyed
learning about [SPECIFIC TOPIC DISCUSSED] and how the team
approaches [CHALLENGE MENTIONED].

Our conversation reinforced my excitement about this role,
particularly [SPECIFIC ASPECT]. I'd love to contribute to
[TEAM GOAL DISCUSSED].

Looking forward to the next steps.

Best,
[YOUR NAME]
```

**Re-engaging a Cold Contact:**
```
Hi [NAME],

It's been a while -- hope things are going well at [COMPANY].

I wanted to share that I've been [BRIEF UPDATE ON YOUR SEARCH
OR A RECENT ACHIEVEMENT]. Would love to catch up over coffee
if you have 15 minutes sometime.

No pressure either way. Cheers.

[YOUR NAME]
```

---

## `// SALARY RESEARCH`

Know your worth before you negotiate. Data beats gut feeling.

### Linked Database: Salary Research

> *Create a linked database view here pointing to the Salary Research database*
> Recommended views:
> - **By Level** -- grouped by Level column
> - **By Company** -- sorted by Total Comp descending
> - **Highest Comp** -- sorted by Total Comp descending, top 10
> - **Recently Verified** -- sorted by Date Verified descending

### 2026 AU Tech Salary Benchmarks

| Level | Base Salary Range | Total Comp Range | Years Experience |
|-------|------------------|-----------------|-----------------|
| Junior | $80K - $110K | $85K - $120K | 0-2 years |
| Mid | $120K - $160K | $130K - $180K | 3-5 years |
| Senior | $160K - $220K | $180K - $280K | 5-8 years |
| Staff | $200K - $280K | $250K - $380K | 8-12 years |
| Principal | $250K - $320K | $300K - $450K | 12+ years |
| Engineering Manager | $200K - $260K | $230K - $340K | 8+ years |

*Sources: Levels.fyi, Glassdoor, Blind, Hays Salary Guide 2026. Ranges are for Sydney/Melbourne.*

### Salary Research Checklist

Before any negotiation:

```
- [ ] Collected 3+ data points from different sources
- [ ] Verified data is from 2025 or 2026 (older data is stale)
- [ ] Accounted for location differences (Sydney vs Melbourne vs Remote)
- [ ] Understand total comp breakdown (base + equity + bonus + super)
- [ ] Know the company's typical equity structure (RSU, options, phantom)
- [ ] Identified your walk-away number (minimum acceptable)
- [ ] Identified your target number (what you'd be happy with)
- [ ] Identified your stretch number (best case scenario)
```

### Understanding AU Tech Compensation

```
TOTAL COMP = Base Salary + Superannuation + Equity + Bonus + Benefits

Key AU-specific considerations:
- Super is currently 11.5% (2026) -- some companies pay above minimum
- Equity varies wildly: RSUs (public), options (startup), or nothing
- Sign-on bonuses are becoming more common in AU tech
- "Package" often means base + super only -- always ask for breakdown
- WFH stipends ($1-3K/yr) are now standard at most tech companies
- Learning budgets ($2-5K/yr) are a real differentiator
```

---

## `// OFFERS & NEGOTIATION`

When offers come in, compare them properly. Don't leave money on the table.

### Linked Database: Offers

> *Create a linked database view here pointing to the Offers database*
> Recommended views:
> - **Active Offers** -- filtered to Status = Pending or Negotiating
> - **Comparison** -- table showing all comp columns side by side
> - **Timeline** -- sorted by Deadline ascending

### Offer Comparison Framework

When comparing multiple offers, score each on these dimensions:

```
## Offer Comparison: [DATE]

                    | Company A | Company B | Company C
--------------------|-----------|-----------|----------
Base Salary         | $         | $         | $
Total Comp (Year 1) | $         | $         | $
Total Comp (Year 4) | $         | $         | $
PTO Days            |           |           |
Remote Flexibility  | /5        | /5        | /5
Growth Opportunity  | /5        | /5        | /5
Team Quality        | /5        | /5        | /5
Tech Stack Fit      | /5        | /5        | /5
Work-Life Balance   | /5        | /5        | /5
Company Trajectory  | /5        | /5        | /5
Commute/Location    | /5        | /5        | /5
TOTAL SCORE         | /45       | /45       | /45
```

### Negotiation Playbook

```
GOLDEN RULES:
1. Never accept on the spot -- always ask for time to consider
2. Negotiate base salary FIRST, then equity, then sign-on
3. Be specific: "$185K" not "something in the mid-180s"
4. Use competing offers as leverage (but never bluff)
5. Be genuinely enthusiastic -- negotiation is collaborative, not adversarial

SCRIPT: Asking for More
"Thank you for the offer -- I'm genuinely excited about this role.
After reviewing the package and comparing with market data, I was
hoping we could discuss the base salary. Based on my research and
the value I'd bring from [SPECIFIC EXPERIENCE], I was targeting
[$TARGET]. Is there flexibility there?"

SCRIPT: Leveraging Another Offer
"I want to be transparent -- I have another offer at [$AMOUNT] from
[COMPANY]. I prefer your team and the role, but the gap in
compensation is significant. Is there room to close that gap?"

SCRIPT: Negotiating Non-Salary Items
"I understand the base salary is firm. Could we explore other
areas? Specifically, I'd value [additional PTO / sign-on bonus /
learning budget / equity refresh / flexible schedule]."
```

### Accepting an Offer

```
Before accepting:
- [ ] Written offer letter received (not just verbal)
- [ ] All comp components clearly documented
- [ ] Start date confirmed and reasonable
- [ ] Notice period at current job accounted for
- [ ] Benefits start date confirmed
- [ ] Any contingencies (background check, references) understood
- [ ] Compared with all other active offers
- [ ] Gut check: would you be excited to start Monday?

After accepting:
- [ ] Withdraw from all other active processes (be gracious)
- [ ] Notify your network contacts who helped
- [ ] Update LinkedIn (after start date, not before)
- [ ] Send a genuine thank-you to everyone who helped
```

---

## `// COMPANY RESEARCH`

Know where you're applying before you apply. Quality over quantity.

### Linked Database: Companies

> *Create a linked database view here pointing to the Companies database*
> Recommended views:
> - **Target Companies** -- filtered to Priority = Target, sorted by Glassdoor Score
> - **By Industry** -- grouped by Industry column
> - **Active Processes** -- filtered to Status in (Applied, Interviewing, Offer)
> - **Research Needed** -- filtered to Culture Rating = Unknown

### Company Research Template

Copy this for each target company:

```
## [COMPANY NAME] Research

### Basics
- Industry: [INDUSTRY]
- Size: [EMPLOYEES]
- Founded: [YEAR]
- HQ: [LOCATION]
- Funding/Revenue: [DETAILS]

### Engineering Culture
- Tech stack: [FROM DATABASE]
- Engineering blog: [URL]
- Open source contributions: [YES/NO, DETAILS]
- Interview process: [FROM GLASSDOOR]
- Typical interview length: [WEEKS]

### Recent News (Last 6 Months)
- [NEWS ITEM 1]
- [NEWS ITEM 2]
- [NEWS ITEM 3]

### Red Flags to Watch
- [ ] Glassdoor reviews trending down?
- [ ] Recent layoffs or restructuring?
- [ ] High turnover in engineering leadership?
- [ ] Negative sentiment on Blind or HackerNews?
- [ ] Unclear business model or funding concerns?

### My Fit Assessment
Why I want to work here: [REASONS]
Concerns: [CONCERNS]
Priority: [TARGET / INTERESTED / MAYBE / BACKUP]
```

---

## `// WEEKLY JOB SEARCH REVIEW`

Spend 30 minutes every Sunday reviewing your search. Consistency beats intensity.

### Weekly Review Template

Copy this each week:

```
## Week of [DATE]

### Numbers
- Applications sent: [COUNT]
- Responses received: [COUNT]
- Interviews completed: [COUNT]
- Networking contacts made: [COUNT]
- Offers received: [COUNT]

### Wins
1. [WIN]
2. [WIN]

### Setbacks
1. [SETBACK]
2. [SETBACK]

### What Worked
- [TACTIC THAT GOT RESULTS]

### What Didn't Work
- [TACTIC TO STOP OR ADJUST]

### Next Week Focus
- [ ] [PRIORITY 1]
- [ ] [PRIORITY 2]
- [ ] [PRIORITY 3]

### Energy Check (1-5)
Motivation: [SCORE]
Confidence: [SCORE]
Burnout risk: [SCORE]

If any score is below 3, take a day off from the search.
It's a marathon, not a sprint.
```

---

## `// INTERVIEW PREP CHECKLIST`

### Technical Interview Prep

```
DATA STRUCTURES & ALGORITHMS (if applicable to role)
- [ ] Arrays and strings (sliding window, two pointers)
- [ ] Hash maps and sets
- [ ] Trees and graphs (BFS, DFS)
- [ ] Dynamic programming basics
- [ ] System design fundamentals

SYSTEM DESIGN (Senior+ roles)
- [ ] Load balancers, caching, CDNs
- [ ] Database choices (SQL vs NoSQL, when to use each)
- [ ] Message queues (Kafka, SQS, RabbitMQ)
- [ ] Microservices vs monolith trade-offs
- [ ] Scalability patterns (horizontal scaling, sharding)
- [ ] Observability (logging, monitoring, alerting)

BEHAVIORAL (All roles)
- [ ] 5 STAR stories prepared and practiced
- [ ] "Tell me about yourself" (90-second pitch ready)
- [ ] "Why this company?" (researched and genuine answer)
- [ ] "Why are you leaving?" (positive framing, no badmouthing)
- [ ] "Where do you see yourself in 3 years?" (aligned with role)
- [ ] Salary expectations answer prepared

PRACTICAL
- [ ] Test your camera, mic, and internet (day before)
- [ ] Have a backup device or phone hotspot ready
- [ ] Quiet room with good lighting booked
- [ ] Water bottle, notepad, and pen on desk
- [ ] IDE or whiteboard tool open and ready
```

---

## `// RESOURCES`

### Useful Bookmarks

- [Levels.fyi AU](https://www.levels.fyi/t/software-engineer/locations/australia) -- salary data for AU tech
- [Glassdoor AU](https://www.glassdoor.com.au/) -- company reviews and interview experiences
- [Blind](https://www.teamblind.com/) -- anonymous tech worker discussions
- [Hays Salary Guide](https://www.hays.com.au/salary-guide) -- AU market salary benchmarks
- [Seek](https://www.seek.com.au/) -- AU job board
- [LinkedIn Jobs](https://www.linkedin.com/jobs/) -- networking and applications
- [Indeed AU](https://au.indeed.com/) -- job aggregator

### Job Search Mental Health

```
Remember:
- Rejection is information, not a verdict on your worth
- The market is tough in 2026 -- it's not just you
- One good offer is all you need
- Taking breaks makes you MORE effective, not less
- Comparison with others' timelines is poison
- Your interview skills improve with every round, even failed ones
- Networking feels uncomfortable but it's the #1 source of good roles

If you're feeling stuck:
1. Talk to someone (friend, mentor, partner)
2. Take a full day off from the search
3. Do something that reminds you of your competence
4. Review your wins list -- you've done hard things before
```

---

> **Want the full Job Search CRM with salary research, offer tracking, and negotiation tools?**
> Get the complete template for just **$19 AUD** -- less than one hour of your future salary.
> *Includes 6 databases, interview prep frameworks, negotiation scripts, and weekly review templates.*

---

*Built for the 2026 tech job market. Because your next role deserves a system, not a scattered spreadsheet.*
*Version 1.0 | Last updated: March 2026*
