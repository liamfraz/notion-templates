# TikTok & Reels Content Machine

> Your short-form content factory. Plan, film, post, and go viral across TikTok, Instagram Reels, and YouTube Shorts — from one workspace.

---

## Quick Start

1. **Import this template** into your Notion workspace
2. **Set up your databases** using the CSV files provided
3. **Customise your Posting Schedule** with your actual time slots
4. **Stock your Hooks Library** — start with the 10 proven hooks included
5. **Plan your first batch** — add 5-7 videos to the Content Pipeline

> See the full [Setup Guide](SETUP-GUIDE.md) for detailed instructions.

---

## Short-Form Dashboard

### Performance Snapshot

| Metric | This Week | Last Week | This Month |
|---|---|---|---|
| Videos Posted | 0 | 0 | 0 |
| Total Views | 0 | 0 | 0 |
| Avg Completion Rate | 0% | 0% | 0% |
| Total Shares | 0 | 0 | 0 |
| Revenue | $0.00 | $0.00 | $0.00 |

### Platform Breakdown

| Platform | Videos | Views | Avg Completion | Best Performer |
|---|---|---|---|---|
| TikTok | 0 | 0 | 0% | — |
| Instagram Reels | 0 | 0 | 0% | — |
| YouTube Shorts | 0 | 0 | 0% | — |

---

## Content Pipeline

> **Database:** Import `databases/content-pipeline.csv`

Your production line for short-form video. Every video tracked from initial idea through to cross-posted and archived.

### Content Lifecycle

```
Idea -> Scripting -> Filming -> Editing -> Scheduled -> Posted -> Viral -> Archived
```

### Content Pipeline Views

- **Board View** — Kanban by Status (drag videos through production stages)
- **By Platform** — Grouped by Platform to balance content distribution
- **This Week** — Table filtered to current week's Post Dates
- **Filming Queue** — Filtered to Scripting and Filming status (batch your shoots)
- **Viral Hits** — Filtered to Status = Viral (study what worked)

---

## Hooks Library

> **Database:** Import `databases/hooks-library.csv`

Your hook is the first 1-3 seconds. It determines whether someone watches or scrolls. Build a library of proven hooks and reuse what works.

### Hook Types

| Type | What It Does | Example |
|---|---|---|
| **Question** | Creates instant curiosity | "Why is nobody talking about this?" |
| **Bold Claim** | Challenges expectations | "I wasted 3 years doing this wrong" |
| **Controversy** | Provokes a reaction | "This is why you're broke" |
| **Curiosity Gap** | Promises a reveal | "What happens when you do this for 30 days" |
| **Pattern Interrupt** | Breaks the scroll pattern | Visual shock, unexpected movement, loud start |
| **Before-After** | Shows transformation | "Here's what I looked like before and after" |
| **How To** | Promises value | "3 things I wish I knew before starting" |
| **List** | Sets clear expectations | "The top 5 apps you need right now" |

### Hook Writing Framework

**The 3-Second Rule:** Your audience decides in 3 seconds. Every hook must:

1. **Stop the scroll** — visual or audio pattern interrupt
2. **Create a gap** — open a loop the viewer needs closed
3. **Promise value** — imply what they'll gain by watching

**Hook Formula:** `[Emotional trigger] + [Specific detail] + [Implied outcome]`

**Examples:**
- "I made $500 from a 15-second video" (money + specificity + implied method)
- "Stop doing this with your morning routine" (fear + familiarity + better way)
- "Nobody told me this about moving to Australia" (curiosity + location + insider knowledge)

### Hooks Library Views

- **All Hooks** — Table sorted by Performance Rating
- **By Category** — Grouped by hook type
- **Top Performers** — Filtered to Viral and Strong ratings
- **By Niche** — Grouped by Niche for quick selection
- **Unused** — Filtered to Times Used = 0

---

## Hashtag Tracker

> **Database:** Import `databases/hashtag-tracker.csv`

Hashtags are discovery tools. Track which ones drive views, which are declining, and build platform-specific hashtag sets.

### Hashtag Strategy

| Category | Purpose | Example |
|---|---|---|
| **Niche** | Reach your target audience | #productivityhacks, #techtips |
| **Trending** | Ride current waves | #sidehustle2026, #aigenerated |
| **Community** | Tap into active subcultures | #techtok, #learnontiktok, #moneytok |
| **Branded** | Build your own community | #flowtechcreator |
| **Challenge** | Participate in viral challenges | Platform-specific, time-sensitive |

### Hashtag Formula Per Post

| Platform | Recommended Count | Mix |
|---|---|---|
| **TikTok** | 3-5 hashtags | 1 trending + 2 niche + 1 community |
| **Instagram Reels** | 5-10 hashtags | 2 trending + 3 niche + 2 community + 1 branded |
| **YouTube Shorts** | 3-5 hashtags | Focus on search terms. Hashtags matter less here |

### Hashtag Tracker Views

- **Active Hashtags** — Filtered to Status = Active, sorted by Avg Views
- **By Platform** — Grouped by Platform
- **Declining** — Filtered to Declining and Retired (stop using these)
- **Testing** — Filtered to Status = Testing (monitor performance)

---

## Sounds & Trends Tracker

> **Database:** Import `databases/sounds-trends.csv`

Trending sounds can 10x your reach. Track what's hot, what's peaked, and what's evergreen.

### Sound Lifecycle

```
Spotted -> Trending -> Peak -> Declining -> Dead OR Evergreen
```

### When to Use Each Status

| Status | Action |
|---|---|
| **Trending** | Jump on immediately. Film within 24-48 hours |
| **Peak** | Still viable but window is closing. Post within 1 week |
| **Declining** | Too late for trend-riding. Skip unless content is exceptional |
| **Evergreen** | Always safe to use. Background music, lo-fi beats, utility sounds |

### Sound Strategy by Platform

| Platform | Sound Impact | Best Practice |
|---|---|---|
| **TikTok** | Critical — trending sounds boost discovery significantly | Use trending sounds within 48 hours of spotting |
| **Instagram Reels** | Moderate — algorithm considers sound but less weight | Evergreen and lo-fi beats work well. Less pressure to trend-chase |
| **YouTube Shorts** | Low — original audio and voiceover perform best | Focus on original content. Background music secondary |

### Sounds & Trends Views

- **Currently Trending** — Filtered to Trending and Peak status
- **Evergreen Library** — Filtered to Evergreen status
- **By Platform** — Grouped by Platform
- **Recently Spotted** — Sorted by First Spotted date, descending

---

## Analytics

> **Database:** Import `databases/analytics.csv`

Track platform-specific metrics that matter for short-form: completion rate, shares, saves, and revenue.

### Performance Ratings

| Rating | Criteria |
|---|---|
| **Viral** | 5x+ your average views. Significant follower spike. High share rate |
| **Above Average** | 1.5-5x your typical performance |
| **Average** | Within normal range for that platform |
| **Below Average** | Under 50% of typical performance |
| **Flop** | Under 20% of typical. Analyse completion rate and hook |

### The Metrics That Actually Matter

| Metric | Why It Matters | Target |
|---|---|---|
| **Completion Rate** | The algorithm's #1 signal. Higher = more distribution | 70%+ for TikTok, 60%+ for Reels, 50%+ for Shorts |
| **Shares** | Shares signal "worth sharing" to the algorithm | 2%+ share rate |
| **Saves** | Saves indicate rewatch value | 3%+ save rate |
| **Comments** | Engagement depth. Reply to every one in first hour | Aim for conversation, not just count |
| **Watch Time** | Total minutes watched, not just views | Drives long-term algorithmic favour |

### Analytics Views

- **All Videos** — Table sorted by Posted Date (descending)
- **Top Performers** — Filtered to Viral and Above Average
- **By Platform** — Grouped by Platform, sorted by Views
- **Completion Rate Leaderboard** — Sorted by Completion Rate descending
- **Revenue Generating** — Filtered where Revenue > 0
- **Flop Review** — Filtered to Flop and Below Average (learn from these)

---

## Posting Schedule

> **Database:** Import `databases/posting-schedule.csv`

Consistency beats virality. Build a posting schedule that matches your capacity and your audience's active hours.

### Optimal Posting Times (2026 Data)

| Platform | Best Times (AEST) | Peak Days |
|---|---|---|
| **TikTok** | 7:00-8:00, 12:00-13:00, 19:00-21:00 | Tuesday, Thursday, Saturday |
| **Instagram Reels** | 7:00-9:00, 17:00-19:00 | Monday, Wednesday, Friday |
| **YouTube Shorts** | 12:00-14:00, 18:00-20:00 | Tuesday, Thursday, Saturday |

### Posting Schedule Views

- **Weekly Grid** — Table grouped by Day
- **By Platform** — Grouped by Platform
- **Active Schedule** — Filtered to Scheduled status
- **Performance Review** — Sorted by Performance Rating

---

## Trending Content Strategy

### How to Ride a Trend

1. **Spot it early** — You have 24-72 hours from first sighting to peak
2. **Add your niche angle** — Don't just copy; apply the trend to your topic
3. **Film fast** — Speed beats production quality for trends
4. **Post on TikTok first** — Trends start here. Cross-post 24-48 hours later
5. **Use the exact trending sound** — Don't substitute with a similar one

### Evergreen vs Trending Content Mix

| Content Type | % of Output | Purpose |
|---|---|---|
| **Evergreen** | 60% | Consistent baseline views, searchable, long-term value |
| **Trending** | 30% | Spikes in reach, new audience discovery |
| **Experimental** | 10% | Testing new formats, hooks, and niches |

---

## Algorithm Tips

### TikTok Algorithm (2026)

- **Completion rate is king** — Keep videos under 30s until you hit 70%+ completion consistently
- **First 2 hours matter** — Reply to every comment immediately after posting
- **Repost strategy** — Flops can be reposted 2-3 weeks later with a new hook
- **Niche down** — Algorithm rewards topic consistency. Don't switch niches every video

### Instagram Reels Algorithm (2026)

- **Saves > Likes** — Reels algorithm weighs saves heavily. Create rewatchable content
- **Share to Stories** — Sharing your Reel to Stories gives a secondary distribution boost
- **Hashtags still matter** — 5-10 relevant hashtags, mix niche and trending

### YouTube Shorts Algorithm (2026)

- **Custom thumbnails** — Outperform auto-generated even on Shorts
- **Longer Shorts win** — 45-58 seconds outperforms sub-30 second content
- **Subscribe prompts** — Shorts are subscriber acquisition machines. Always include a CTA
- **Original audio preferred** — YouTube favours voiceover content over lip-sync

---

## Cross-Posting Workflow

### The 3-Platform Pipeline

```
TikTok (film + post first)
  ├── Instagram Reels (remove watermark, repost 24-48 hours later)
  └── YouTube Shorts (adjust duration if needed, post 48-72 hours later)
```

### Cross-Posting Rules

1. **Never post with another platform's watermark** — Download clean or use SnapTik/SaveTik
2. **Adjust captions per platform** — TikTok is casual, Reels is polished, Shorts is searchable
3. **Stagger posting** — Same day posting across platforms cannibalises views
4. **Platform-native content wins** — 70% cross-posted, 30% platform-specific
5. **Aspect ratio** — All short-form is 9:16 vertical. No exceptions

### Caption Style by Platform

- **TikTok** — Short, punchy, end with a question. 3-5 hashtags
- **Instagram Reels** — Slightly longer, include CTA ("Save this"), 5-10 hashtags in block
- **YouTube Shorts** — SEO-focused, keyword-rich title, 3-5 hashtags

---

## Monthly Review

Run this review on the **last day of each month**. Block 60 minutes.

### Review Checklist

- [ ] Calculate total views and revenue across all platforms
- [ ] Identify top 3 performing videos — what hooks and formats worked?
- [ ] Identify bottom 3 performers — what went wrong?
- [ ] Update follower counts across all 3 platforms
- [ ] Review Hooks Library — promote winners, archive losers
- [ ] Clean up Hashtag Tracker — retire declining hashtags, add new discoveries
- [ ] Update Sounds & Trends — move peaked sounds to Declining or Evergreen
- [ ] Review Posting Schedule — are your time slots still optimal?
- [ ] Check cross-posting ratio — are you balanced across platforms?
- [ ] Set content goals for next month (video count, niche focus, experiments)

### Monthly Reflection Questions

1. Which platform drove the most growth this month and why?
2. What was my best hook and can I write 5 variations of it?
3. Am I over-indexing on trends at the expense of evergreen content?
4. What content did my audience share the most? (Shares = virality signal)
5. Is my posting frequency sustainable? Adjust if needed

---

## Database Relations Map

```
Content Pipeline (1) ----< (many) Analytics (via Video Title)
Content Pipeline (many) ----< (many) Hooks Library (via Hook Type)
Content Pipeline (many) ----< (many) Sounds & Trends (via Sound)
Content Pipeline (many) ----< (many) Hashtag Tracker (via hashtags used)
Posting Schedule (many) ----< (many) Content Pipeline (via scheduled content)
```

### Recommended Views Summary

| Database | View 1 | View 2 | View 3 |
|---|---|---|---|
| Content Pipeline | Board (by Status) | Table (by Platform) | Table (Filming Queue) |
| Hooks Library | Table (by Rating) | Board (by Category) | Table (Top Performers) |
| Hashtag Tracker | Table (Active) | Table (by Platform) | Table (Declining) |
| Sounds & Trends | Table (Trending) | Table (Evergreen) | Table (by Platform) |
| Analytics | Table (by Date) | Table (Top Performers) | Table (by Platform) |
| Posting Schedule | Table (by Day) | Table (by Platform) | Table (Active) |

---

## Useful Formulas (Notion Formula 2.0)

**Engagement Rate (Analytics):**
```
round((prop("Likes") + prop("Comments") + prop("Shares") + prop("Saves")) / prop("Views") * 100 * 100) / 100
```

**Share Rate (Analytics):**
```
if(prop("Views") > 0, round(prop("Shares") / prop("Views") * 100 * 100) / 100, 0)
```

**Save Rate (Analytics):**
```
if(prop("Views") > 0, round(prop("Saves") / prop("Views") * 100 * 100) / 100, 0)
```

**Revenue Per 1K Views (Analytics):**
```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

**Hashtag Effectiveness (Hashtag Tracker):**
```
if(prop("Posts Using") > 0, round(prop("Avg Views When Used") / prop("Posts Using")), 0)
```

**Hook Success Score (Hooks Library):**
```
if(prop("Times Used") > 0, round(prop("Avg Completion Rate") * prop("Times Used") / 10), 0)
```

---

*Built for creators who'd rather go viral than go in circles.*
