# Content Creator Command Center

> Plan, publish, and profit from your content across every platform. Content calendar, analytics tracking, brand deals, income dashboard, and idea bank — built for creators who take their craft seriously.

---

## Quick Start

1. **Import this template** into your Notion workspace
2. **Set up your databases** using the CSV files provided (Content Calendar, Analytics, Brand Deals, Income, Platforms, Ideas)
3. **Customise your Platforms** database with your actual handles and follower counts
4. **Plan your first week** — add 3-5 pieces of content to the Content Calendar
5. **Start tracking** — log your first published content and its analytics

> See the full [Setup Guide](SETUP-GUIDE.md) for detailed instructions including formula configurations.

---

## Creator Dashboard

### Revenue Snapshot

| Metric | This Month | Last Month | YTD |
|---|---|---|---|
| Total Income | $0.00 | $0.00 | $0.00 |
| Sponsorship Revenue | $0.00 | $0.00 | $0.00 |
| Passive Income | $0.00 | $0.00 | $0.00 |
| Brand Deals Pipeline | $0.00 | $0.00 | $0.00 |

### Growth Metrics

| Metric | Current | Last Month | Target |
|---|---|---|---|
| Total Followers (all platforms) | 0 | 0 | — |
| Newsletter Subscribers | 0 | 0 | — |
| YouTube Subscribers | 0 | 0 | — |
| Monthly Content Output | 0 | 0 | — |
| Avg Engagement Rate | 0% | 0% | 5% |

### How to Calculate

- **Engagement Rate** = (Likes + Comments + Shares) / Views x 100
- **Revenue Per 1K Views (RPM)** = (Total Revenue / Total Views) x 1000
- **Content ROI** = Revenue Generated / Hours Spent Creating
- **Pipeline Value** = Sum of all Brand Deals where Status is not Declined or Paid

---

## Content Calendar

> **Database:** Import `databases/content-calendar.csv`

Your single source of truth for everything you're creating, across every platform.

### Content Lifecycle

```
Idea -> Scripting -> Filming -> Editing -> Scheduled -> Published -> Evergreen
```

### Content Calendar Views

- **Board View** — Kanban by Status (drag content through stages)
- **Calendar View** — Monthly calendar by Publish Date
- **By Platform** — Grouped by Platform to see content distribution
- **This Week** — Table filtered to current week's content
- **Pipeline** — Everything not yet Published, sorted by Publish Date

### Content Types

| Type | Best Platform | Typical Production Time |
|---|---|---|
| **Long-form Video** | YouTube | 8-15 hours (script to upload) |
| **Short-form Video** | TikTok, Instagram Reels | 1-3 hours |
| **Carousel** | Instagram, LinkedIn | 2-4 hours |
| **Thread** | Twitter/X, LinkedIn | 30-60 minutes |
| **Newsletter Issue** | Email | 2-4 hours |
| **Article** | Blog, LinkedIn | 3-6 hours |
| **Podcast Episode** | Podcast platforms | 3-5 hours (record + edit) |

### Batching Strategy

Block your week for maximum efficiency:

| Day | Activity |
|---|---|
| **Monday** | Scripting and research |
| **Tuesday** | Filming / recording |
| **Wednesday** | Editing |
| **Thursday** | Scheduling, thumbnails, captions |
| **Friday** | Engagement, community, planning next week |

---

## Analytics Tracker

> **Database:** Import `databases/analytics.csv`

Track performance for every piece of content you publish. Data-driven creators grow faster.

### Performance Ratings

| Rating | Criteria |
|---|---|
| **Viral** | 5x+ your average views/reach. Significant new follower spike |
| **Above Average** | 1.5-5x your typical performance |
| **Average** | Within normal range for that platform |
| **Below Average** | Under 50% of your typical performance |
| **Flop** | Under 20% of typical performance. Analyse why |

### Platform Benchmarks (Adjust to Your Own)

| Platform | Average Views | Good CTR | Good Engagement |
|---|---|---|---|
| YouTube | 5K-15K | 5-10% | 5%+ like ratio |
| TikTok | 10K-50K | 2-4% | 8%+ engagement |
| Instagram | 3K-10K | 3-5% | 3%+ engagement |
| Newsletter | 1K-3K opens | 35-45% open rate | 3%+ click rate |
| LinkedIn | 2K-10K | N/A | 3%+ engagement |

### Analytics Views

- **All Content** — Table sorted by Published Date (descending)
- **Top Performers** — Filtered to Viral and Above Average
- **By Platform** — Grouped by Platform, sorted by Views
- **Revenue Generating** — Filtered where Revenue > $0
- **Flop Review** — Filtered to Below Average and Flop (learn from these)

### After Every Publish, Log

1. Views/reach after 24 hours and after 7 days
2. Engagement metrics (likes, comments, shares)
3. Revenue generated (ad revenue, affiliate clicks)
4. What worked and what didn't (in Notes)
5. Performance Rating

---

## Brand Deals Tracker

> **Database:** Import `databases/brand-deals.csv`

### Deal Pipeline

```
Pitched -> Negotiating -> Contracted -> In Progress -> Delivered -> Paid
```

### Deal Categories

| Category | Description | Typical Fee Range |
|---|---|---|
| **Sponsor** | Dedicated or integrated brand content | $1,000 - $5,000+ |
| **Affiliate** | Commission-based, ongoing revenue | $200 - $1,000/month |
| **Ambassador** | Long-term brand partnership | $1,500 - $5,000/month |
| **One-off** | Single ad read or mention | $300 - $1,500 |

### Pricing Your Content

Base rate formula for YouTube:
```
Fee = (Average Views / 1000) x CPM Rate ($25-$50 for tech niche)
Minimum: $500 for any brand integration
```

### Negotiation Tips

- Always counter the first offer (it's rarely the final budget)
- Ask for usage rights fees if they want to run your content as ads
- Get payment terms in writing before creating content
- Net 30 is standard; push for Net 15 or 50% upfront for new brands
- Track everything — your deal history sets your future rates

### Brand Deals Views

- **Pipeline** — Board view by Status
- **This Month** — Table filtered to current month deadlines
- **By Payment** — Grouped by Payment Status (spot overdue payments)
- **Revenue** — Table sorted by Fee, descending

---

## Income Tracker

> **Database:** Import `databases/income.csv`

### Income Categories

| Source | Type | Scalability |
|---|---|---|
| **Ad Revenue** | Passive | Scales with views |
| **Sponsorships** | Active | Scales with audience size and niche |
| **Affiliate** | Passive | Scales with content library |
| **Digital Products** | Passive | Scales infinitely after creation |
| **Coaching** | Active | Limited by your time |
| **Memberships** | Recurring | Scales with community size |
| **Donations** | Passive | Unpredictable, don't rely on this |

### Income Views

- **Monthly Summary** — Grouped by Month, summing Amount
- **By Source** — Grouped by Source to see revenue mix
- **Passive vs Active** — Grouped by Type
- **By Platform** — See which platforms generate the most revenue

### Revenue Health Targets

| Milestone | Monthly Revenue | What It Means |
|---|---|---|
| **Hobby** | $0 - $500 | Side project, learning phase |
| **Side Hustle** | $500 - $2,000 | Covers tools and reinvestment |
| **Part-Time** | $2,000 - $5,000 | Meaningful supplementary income |
| **Full-Time** | $5,000 - $15,000 | Can replace a salary |
| **Business** | $15,000+ | Building a team and scaling |

### Key Formula

```
Revenue Diversification Score = 1 - (Largest Source / Total Revenue)
Target: 0.5+ (no single source > 50% of income)
```

---

## Platform Manager

> **Database:** Import `databases/platforms.csv`

### Platform Strategy

| Priority | Meaning | Time Allocation |
|---|---|---|
| **Primary** | Main growth and revenue channels | 60% of effort |
| **Secondary** | Supporting channels, repurpose content | 30% of effort |
| **Experimental** | Testing new platforms, low commitment | 10% of effort |

### Platform Status

| Status | Action |
|---|---|
| **Active** | Posting consistently, meeting frequency targets |
| **Growing** | Actively investing in growth, may exceed normal posting |
| **Paused** | Intentionally not posting (burnout prevention, strategy shift) |
| **New** | Just started, building initial content library |

### Cross-Platform Repurposing

```
YouTube Long-form (primary)
  ├── TikTok Clips (cut key moments)
  ├── Instagram Carousel (key takeaways)
  ├── Twitter Thread (main points)
  ├── Newsletter (deep dive + link)
  ├── LinkedIn Article (professional angle)
  └── Blog Post (SEO-optimised written version)
```

### Platform Views

- **All Platforms** — Table sorted by Priority
- **Active Only** — Filtered to Active and Growing
- **Growth Dashboard** — Sorted by Monthly Growth (descending)

---

## Idea Bank

> **Database:** Import `databases/ideas.csv`

Never lose a content idea again. Capture everything, prioritise ruthlessly, create strategically.

### Idea Priorities

| Priority | Meaning | Action |
|---|---|---|
| **Hot** | High potential, timely, or audience-requested | Create this week |
| **Medium** | Good idea, no urgency | Schedule within 2 weeks |
| **Low** | Worth doing eventually | Backlog |
| **Someday** | Maybe, maybe not | Review monthly |

### Idea Sources

- **Audience Request** — Comments, DMs, poll responses. Highest conversion
- **Trending** — Current events, viral topics. Time-sensitive
- **Evergreen** — Always relevant. Build a library of these
- **Collaboration** — Joint content with other creators. Audience crossover
- **Personal** — Your own experiences and stories. Authentic content

### Idea Scoring (Quick Gut Check)

Before moving an idea to production, score it:

| Factor | Question |
|---|---|
| **Audience demand** | Did someone ask for this? |
| **Monetisation** | Can this generate revenue (ads, affiliate, sponsor)? |
| **Repurposability** | Can I turn this into 3+ pieces across platforms? |
| **Effort** | How many hours to produce? |
| **Timeliness** | Is this relevant right now? |

If it scores 3+ "yes" answers, move it to Ready to Create.

### Idea Bank Views

- **All Ideas** — Table sorted by Priority
- **Hot Ideas** — Filtered to Priority = Hot
- **By Platform** — Grouped by Platform
- **Ready to Create** — Filtered to Status = Ready to Create
- **By Source** — Grouped by Source to see where your best ideas come from

---

## Monthly Creator Review

Run this review on the **last day of each month**. Block 90 minutes.

### Review Checklist

- [ ] Calculate total income vs target — update Income Tracker
- [ ] Review analytics for all published content — identify top 3 and bottom 3
- [ ] Update follower counts across all platforms
- [ ] Review brand deal pipeline — chase overdue payments, follow up on pitches
- [ ] Score content performance — what formats/topics performed best?
- [ ] Clean up Idea Bank — archive stale ideas, promote hot ones
- [ ] Review platform strategy — is time allocation matching results?
- [ ] Calculate engagement rates across platforms
- [ ] Set content goals for next month (titles, publish dates, platforms)
- [ ] Update Content Calendar with next month's planned content

### Monthly Reflection Questions

1. What was my best-performing piece of content and why?
2. Which platform gave the best ROI for time invested?
3. Am I diversified enough across income sources?
4. What did my audience ask for that I haven't created yet?
5. Am I on track for my quarterly growth goals?

---

## Appendix: Suggested Notion Setup

### Database Relations Map

```
Content Calendar (1) ----< (many) Analytics (via Content Title)
Brand Deals (many) ----< (many) Platforms (via Platform)
Income (many) ----< (many) Platforms (via Platform)
Ideas (many) ----< (many) Platforms (via Platform)
Content Calendar (many) ----< (many) Platforms (via Platform)
```

### Recommended Views

| Database | View 1 | View 2 | View 3 |
|---|---|---|---|
| Content Calendar | Board (by Status) | Calendar (by Publish Date) | Table (by Platform) |
| Analytics | Table (all, by date) | Table (top performers) | Table (by Platform) |
| Brand Deals | Board (by Status) | Table (by deadline) | Table (by Payment Status) |
| Income | Table (by Month) | Table (by Source) | Table (by Platform) |
| Platforms | Table (all) | Table (active only) | Gallery (cards) |
| Ideas | Board (by Priority) | Table (by Platform) | Table (ready to create) |

### Useful Formulas (Notion Formula 2.0)

**Engagement Rate (Analytics):**
```
round((prop("Likes") + prop("Comments") + prop("Shares")) / prop("Views") * 100 * 100) / 100
```

**Revenue Per 1K Views (Analytics):**
```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

**Days Until Deadline (Brand Deals):**
```
if(prop("Status") == "Paid" or prop("Status") == "Declined", 0, dateBetween(prop("Deadline"), now(), "days"))
```

**Monthly Income Total (Dashboard — manual or via rollup):**
```
Sum of prop("Amount") where prop("Month") = current month
```

---

*Built for creators who'd rather make content than manage spreadsheets.*
