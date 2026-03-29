# YouTube Command Center

> Your entire YouTube channel — from video ideas to revenue tracking — managed in one Notion workspace. Built exclusively for YouTubers who want to grow with data, not guesswork.

---

## Quick Start

1. **Import this template** into your Notion workspace
2. **Set up your databases** using the 6 CSV files provided (Videos, Analytics, Thumbnails, Playlists, Revenue, Ideas)
3. **Replace sample data** with your channel's real numbers
4. **Plan your next upload** — add your next 3 videos to the Videos database
5. **Start tracking** — log analytics for your most recent published video

> See the full [Setup Guide](SETUP-GUIDE.md) for detailed instructions including formula configurations and database relations.

---

## YouTube Dashboard

### Channel Revenue Snapshot

| Metric | This Month | Last Month | YTD |
|---|---|---|---|
| Total Revenue | $0.00 | $0.00 | $0.00 |
| AdSense Revenue | $0.00 | $0.00 | $0.00 |
| Sponsorship Revenue | $0.00 | $0.00 | $0.00 |
| Affiliate Revenue | $0.00 | $0.00 | $0.00 |
| Membership Revenue | $0.00 | $0.00 | $0.00 |

### Channel Growth Metrics

| Metric | Current | Last Month | Target |
|---|---|---|---|
| Subscribers | 0 | 0 | -- |
| Monthly Views | 0 | 0 | -- |
| Watch Hours (monthly) | 0 | 0 | 4,000 |
| Average CTR | 0% | 0% | 7% |
| Average View Duration | 0:00 | 0:00 | 8:00 |
| Videos Published (this month) | 0 | 0 | -- |

### How to Calculate

- **CTR** = (Clicks / Impressions) x 100
- **RPM** = (Total Revenue / Total Views) x 1000
- **Subscriber Conversion Rate** = (New Subscribers / Views) x 100
- **Engagement Rate** = (Likes + Comments) / Views x 100

---

## Videos

> **Database:** Import `databases/videos.csv`

Your production pipeline for every video on your channel. Track each video from initial idea through to published and evergreen status.

### Video Production Pipeline

```
Idea -> Scripting -> Filming -> Editing -> Thumbnail -> Scheduled -> Published -> Evergreen
```

Each stage has a clear purpose:

| Stage | What Happens | Typical Duration |
|---|---|---|
| **Idea** | Concept captured, rough title drafted | Ongoing |
| **Scripting** | Outline, hook, script, and talking points written | 1-3 days |
| **Filming** | B-roll, A-roll, screen recordings captured | 1-2 days |
| **Editing** | Rough cut, fine cut, colour grade, audio mix | 2-4 days |
| **Thumbnail** | Design, A/B test, select final thumbnail | 1-2 days |
| **Scheduled** | Uploaded, metadata set, publish time locked in | 1 day |
| **Published** | Live on YouTube, promotion period active | -- |
| **Evergreen** | Consistently generating views from search/browse | Ongoing |

### Recommended Views

- **Production Board** -- Board view grouped by Status (drag videos through stages)
- **Upload Calendar** -- Calendar view by Publish Date
- **By Category** -- Table grouped by Category to balance your content mix
- **This Month** -- Table filtered to current month's publish dates
- **Evergreen Library** -- Filtered to Status = Evergreen (your search traffic engine)

---

## Analytics

> **Database:** Import `databases/analytics.csv`

YouTube-specific metrics for every published video. Track what the algorithm rewards and double down.

### Key YouTube Metrics Explained

| Metric | What It Tells You | Good Benchmark |
|---|---|---|
| **Views** | Total video views | Depends on channel size |
| **Watch Hours** | Total hours watched | 4,000 needed for monetisation |
| **Avg View Duration (AVD)** | How long viewers stay | 50%+ of video length |
| **CTR (Click-Through Rate)** | How often impressions become clicks | 5-10% for most niches |
| **Impressions** | How often YouTube shows your thumbnail | Higher = more algorithmic push |
| **Subscribers Gained** | New subs from this video | Track per-video to find growth drivers |

### Performance Ratings

| Rating | Criteria |
|---|---|
| **Viral** | 5x+ your average views. Major subscriber spike. Algorithm pushing hard |
| **Above Average** | 1.5-5x your typical performance. Strong CTR and AVD |
| **Average** | Within your normal range. Solid but not breakout |
| **Below Average** | Under 50% of typical performance. Review thumbnail and title |
| **Flop** | Under 20% of typical. Analyse hook, topic choice, and publish timing |

### Analytics Strategy Tips

**When a video underperforms:** Check CTR first (thumbnail/title problem), then AVD (hook/pacing problem), then impressions (topic/metadata problem).

**When a video overperforms:** Create a follow-up immediately, add it to a relevant playlist, pin a comment linking to related content, and note what worked in the Notes field.

### Recommended Views

- **All Videos** -- Table sorted by Published Date (descending)
- **Top Performers** -- Filtered to Viral and Above Average
- **Revenue Leaders** -- Sorted by Revenue descending
- **Flop Review** -- Filtered to Below Average and Flop (learn from these)
- **CTR Tracker** -- Sorted by CTR descending to find your best thumbnails

---

## Thumbnails

> **Database:** Import `databases/thumbnails.csv`

Track thumbnail versions and A/B test results. Your thumbnail is the single biggest factor in CTR.

### A/B Testing Workflow

```
Design Version A -> Design Version B -> Upload A (test 48hrs) -> Swap to B (test 48hrs) -> Compare CTR -> Set Winner as Final
```

### Thumbnail Styles

| Style | Best For | Typical CTR Impact |
|---|---|---|
| **Face + Text** | Tutorials, commentary, vlogs | High -- emotional connection |
| **Graphic** | Listicles, evergreen, how-to | Medium -- clean and searchable |
| **Screenshot** | Software tutorials, screen recordings | Medium -- shows what viewer gets |
| **Reaction** | Reviews, commentary, reactions | High -- curiosity gap |
| **Comparison** | Versus videos, tool reviews | High -- clear value proposition |
| **Before-After** | Transformations, results-based content | High -- visual proof |

### Thumbnail Strategy Tips

- Always test at least 2 versions for videos you expect to perform well
- Give each version minimum 48 hours and 10,000+ impressions before judging
- Face thumbnails almost always outperform no-face thumbnails
- Use no more than 4-5 words of text on any thumbnail
- Check thumbnails at mobile size (most viewers browse on phones)
- Track which styles consistently win for your niche

### Recommended Views

- **By Video** -- Grouped by Video Title to see all versions side by side
- **Winners Only** -- Filtered to Status = Winner
- **Currently Testing** -- Filtered to Status = Testing
- **By Style** -- Grouped by Style to identify your best-performing thumbnail approach

---

## Playlists

> **Database:** Import `databases/playlists.csv`

Playlists drive session watch time, which is one of YouTube's strongest ranking signals.

### Playlist Strategies

| Strategy | Purpose | Example |
|---|---|---|
| **Evergreen** | Always relevant, drives search traffic year-round | "YouTube Growth Masterclass" |
| **Series** | Sequential content, builds binge behaviour | "Creator Vlogs" |
| **Seasonal** | Time-sensitive compilations, updated annually | "2026 Best Of" |
| **Topical** | Grouped by theme for browse/search discovery | "AI Tools for Creators" |

### Playlist Optimisation Tips

- Order videos intentionally -- put your best-performing video first
- Use keyword-rich playlist titles (they rank in YouTube search)
- Write playlist descriptions with target keywords
- Aim for 5-10 videos per playlist (enough for a viewing session)
- Link playlists in video descriptions and end screens
- Create a "Start Here" playlist for new subscribers

### Recommended Views

- **All Playlists** -- Table sorted by Total Views descending
- **Active Playlists** -- Filtered to Status = Active or Growing
- **By Strategy** -- Grouped by Strategy type
- **Needs Attention** -- Filtered to Videos Count < 5 (playlists that need more content)

---

## Revenue

> **Database:** Import `databases/revenue.csv`

Track every dollar your channel generates, broken down by source.

### YouTube Revenue Sources

| Source | Type | How It Works |
|---|---|---|
| **AdSense** | Passive | YouTube ad revenue. Scales with views and CPM |
| **Memberships** | Recurring | Channel members pay monthly for perks |
| **Super Chats** | Active | Live stream donations. Scales with live audience size |
| **Merch Shelf** | Passive | YouTube-integrated merchandise sales |
| **Affiliate** | Passive | Commission from product links in descriptions |
| **Sponsorship** | Active | Brand integrations and dedicated sponsor segments |

### Revenue Health Targets (YouTube-Specific)

| Milestone | Monthly Revenue | Typical Channel Size |
|---|---|---|
| **Pre-Monetisation** | $0 | Under 1K subs / 4K watch hours |
| **Early Monetisation** | $50 - $500 | 1K - 10K subscribers |
| **Growing** | $500 - $2,000 | 10K - 50K subscribers |
| **Established** | $2,000 - $10,000 | 50K - 250K subscribers |
| **Full-Time** | $10,000+ | 250K+ subscribers |

### Revenue Diversification

Target: No single source should exceed 50% of total monthly revenue. A healthy mix spreads across AdSense (35%), sponsorships (25%), affiliates (20%), memberships (10%), and other sources (10%).

### Recommended Views

- **Monthly Summary** -- Grouped by Month, summing Amount
- **By Source** -- Grouped by Source to see revenue mix
- **Passive vs Active** -- Grouped by Type
- **Sponsorship Deals** -- Filtered to Source = Sponsorship

---

## Ideas

> **Database:** Import `databases/ideas.csv`

Your video idea pipeline with built-in SEO scoring to prioritise what to create next.

### SEO Scoring Framework

Before committing to a video idea, evaluate three factors: **SEO Potential** (is there search intent?), **Competition** (how many quality videos already exist?), and **Search Volume** (are enough people searching?). The best opportunities combine High SEO Potential + Low/Medium Competition + High Search Volume.

### Idea Priorities

| Priority | Meaning | Action |
|---|---|---|
| **Hot** | High potential, timely, or audience-requested | Script this week |
| **Medium** | Strong idea, no urgency | Schedule within 2-3 weeks |
| **Low** | Worth doing eventually | Backlog -- revisit monthly |
| **Someday** | Maybe, maybe not | Review quarterly, might archive |

### Recommended Views

- **All Ideas** -- Table sorted by Priority
- **Hot Ideas** -- Filtered to Priority = Hot
- **By Category** -- Grouped by Category to balance content mix
- **High SEO Potential** -- Filtered to SEO Potential = High
- **Quick Wins** -- Filtered to High SEO Potential + Low Competition

---

## YouTube Algorithm Tips

### What the Algorithm Rewards

| Signal | Weight | How to Optimise |
|---|---|---|
| **Click-Through Rate** | Very High | Strong thumbnails and titles. A/B test everything |
| **Average View Duration** | Very High | Strong hooks, good pacing, pattern interrupts |
| **Session Watch Time** | High | Playlists, end screens, series content |
| **Engagement** | Medium | Ask for comments, create discussion points |
| **Upload Consistency** | Medium | Regular schedule trains the algorithm and your audience |
| **Subscriber Activity** | Medium | Notification bell reminders, community posts |

### The First 48 Hours

The first 48 hours after publishing determine your video's trajectory:
1. **Hour 0-2:** Subscriber push. YouTube shows the video to your subscribers first
2. **Hour 2-24:** If CTR and AVD are strong, YouTube expands to Browse and Suggested
3. **Hour 24-48:** Algorithm decides whether to push or suppress. High AVD keeps momentum
4. **Day 3+:** If performance is strong, the video enters broader recommendation pools

### Optimisation Levers

- **Low CTR, High AVD:** Thumbnail/title problem. Great content, bad packaging. Swap thumbnail
- **High CTR, Low AVD:** Clickbait risk. Deliver on the promise faster. Fix the hook
- **Low CTR, Low AVD:** Topic or execution issue. Learn and move on
- **High CTR, High AVD:** Winner. Create more content like this immediately

---

## Monthly Channel Review

Run this review on the **last day of each month**. Block 60-90 minutes.

### Review Checklist

- [ ] Update Revenue database with all income received this month
- [ ] Log analytics for all videos published this month (after 7+ days of data)
- [ ] Review top 3 and bottom 3 videos by views -- what patterns emerge?
- [ ] Check CTR across all recent videos -- any thumbnails worth swapping?
- [ ] Review Avg View Duration -- are viewers dropping off at the same point?
- [ ] Update playlist video counts and total views
- [ ] Calculate total subscriber growth for the month
- [ ] Review revenue diversification -- is any source > 50%?
- [ ] Clean up Ideas database -- archive stale ideas, promote hot ones
- [ ] Plan next month's upload schedule (titles, categories, publish dates)
- [ ] Set one specific growth goal for next month

### Monthly Reflection Questions

1. Which video drove the most subscribers and why?
2. What thumbnail style had the highest average CTR?
3. Is my content mix balanced across categories?
4. Am I publishing consistently enough for the algorithm?
5. What did my audience ask for in comments that I haven't created yet?

---

## Database Relations Map

```
Videos (1) --------< (many) Analytics (via Video Title)
Videos (1) --------< (many) Thumbnails (via Video Title)
Videos (many) -----< (many) Playlists (via playlist assignment)
Ideas (1) ---------< (1) Videos (idea becomes a video)
Revenue (many) ----< (1) Videos (sponsorship linked to specific video)
```

---

## Useful Formulas (Notion Formula 2.0)

### Engagement Rate (Analytics)

```
round((prop("Likes") + prop("Comments")) / prop("Views") * 100 * 100) / 100
```

### Revenue Per 1K Views — RPM (Analytics)

```
if(prop("Views") > 0, round(prop("Revenue") / prop("Views") * 1000 * 100) / 100, 0)
```

### Subscriber Conversion Rate (Analytics)

```
if(prop("Views") > 0, round(prop("Subscribers Gained") / prop("Views") * 100 * 100) / 100, 0)
```

### CTR Performance Flag (Analytics)

```
if(prop("CTR") >= 8, "Excellent", if(prop("CTR") >= 5, "Good", if(prop("CTR") >= 3, "Average", "Needs Work")))
```

### Days Since Published (Videos)

```
dateBetween(now(), prop("Publish Date"), "days")
```

---

*Built for YouTubers who'd rather make videos than manage spreadsheets.*
