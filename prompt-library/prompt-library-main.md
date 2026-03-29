# AI Prompt Library & Workflow Manager

> Organise, rate, and chain your AI prompts into repeatable workflows. Stop rewriting the same prompts. Start building a system.

---

## `// QUICK START`

1. **Import this page** into your Notion workspace
2. **Create databases** from the CSV files in the `/databases` folder (see SETUP-GUIDE.md)
3. **Add your best prompts** -- start with the ones you use every week
4. **Build your first workflow** -- chain 2-3 prompts together for a task you repeat often

**Estimated setup time:** 30 minutes

---

## `// DASHBOARD`

Your command centre for prompt performance and usage patterns. Pin this page to your sidebar.

### Prompt of the Day

> Pick one prompt from your library each morning and use it deliberately. Track the result. Over time, your "Prompt of the Day" rotation will surface your best performers and push you to use prompts you've forgotten about.

**How to use:** Each morning, open your Prompts database sorted by "Last Used" (oldest first). Pick the top result. Use it. Rate the output. Move on.

### Usage Snapshot (Update Weekly)

| Metric | Value |
|--------|-------|
| Total Prompts | 50 |
| Categories | 8 |
| Avg Rating | 4.2 |
| Most Used Model | Claude |
| Workflows Created | 12 |
| This Week's Uses | 34 |

### Quick Actions

- [ ] Add a new prompt you used today
- [ ] Rate your last 3 prompt outputs
- [ ] Update usage counts for the week
- [ ] Review any prompts rated below 3 stars
- [ ] Check if any workflow needs updating
- [ ] Archive prompts you haven't used in 60 days

### Alerts

> **Quality Alert:** 4 prompts rated below 3 stars -- review and rewrite or archive them
> **Usage Alert:** "Market Research Sprint" workflow hasn't been run in 6 weeks -- still relevant?
> **Version Alert:** 3 prompts still on v1.0 after 20+ uses -- time to refine them

---

## `// PROMPT DATABASE`

The core of your system. Every prompt you use, categorised, rated, and versioned.

### How the Database Works

Each prompt has these fields:

| Field | Purpose |
|-------|---------|
| Name | Short, descriptive title (e.g. "Blog Post Outline Generator") |
| Category | What type of work this prompt supports |
| Model | Which AI model it works best with (Claude, ChatGPT, Gemini, Any) |
| Prompt Text | The full prompt -- variables in [BRACKETS] for easy customisation |
| Rating | 1-5 stars based on output quality |
| Use Count | How many times you've used it |
| Output Format | What the AI returns (list, essay, table, code, JSON, etc.) |
| Tags | Freeform tags for quick filtering |
| Last Used | Date stamp -- helps you find stale prompts |
| Version | Track improvements (start at 1.0, bump when you refine) |
| Notes | What works, what doesn't, edge cases |

### Category Guide

| Category | What Goes Here | Examples |
|----------|---------------|----------|
| Writing | Blog posts, emails, newsletters, copy | "Write a 1500-word blog post on [TOPIC]" |
| Coding | Code generation, review, debugging, docs | "Review this function for edge cases" |
| Marketing | SEO, ads, audience research, strategy | "Generate 10 SEO title variations for [KEYWORD]" |
| Analysis | Data interpretation, reports, trends | "Analyse this CSV and summarise the top 3 trends" |
| Research | Literature review, competitive intel | "Summarise the latest developments in [FIELD]" |
| Creative | Brainstorming, naming, storytelling | "Generate 20 product name ideas for [DESCRIPTION]" |
| Business | Proposals, strategy, OKRs, meetings | "Draft a project proposal for [CLIENT] covering [SCOPE]" |
| Productivity | Task management, planning, decisions | "Break this project into tasks with time estimates" |

### Model Compatibility Guide

| Model | Best For | Watch Out For |
|-------|----------|---------------|
| Claude | Long-form writing, analysis, coding, nuanced instructions | Context window limits on older versions |
| ChatGPT | General tasks, creative writing, quick iterations | Can be verbose, sometimes ignores constraints |
| Gemini | Research, multimodal tasks, Google ecosystem integration | Newer -- less community prompt knowledge |
| Any | Simple prompts that work across all models | Test on your primary model first |

### Linked Database: Prompts

> *Create a linked database view here pointing to the Prompts database*
> Recommended views:
> - **All Prompts** -- sorted by Rating descending, then Use Count descending
> - **By Category** -- grouped by Category column
> - **Top Rated** -- filtered to Rating >= 4, sorted by Use Count descending
> - **Needs Review** -- filtered to Rating <= 3 or Last Used older than 60 days
> - **By Model** -- grouped by Model column
> - **Recently Used** -- sorted by Last Used descending

### Prompt Naming Convention

```
Use consistent names so you can find prompts fast:

[Category] - [Action] - [Specificity]

Examples:
  Writing - Blog Outline - SEO Optimised
  Coding - Code Review - Python Functions
  Marketing - Ad Copy - Facebook Carousel
  Analysis - Data Summary - CSV to Insights
```

---

## `// WORKFLOWS`

Chain prompts together into repeatable multi-step processes. A workflow takes a task from start to finish using 2-5 prompts in sequence.

### Why Workflows Matter

```
Single prompts solve single problems.
Workflows solve entire processes.

Instead of:
  1. Write a prompt to research a topic
  2. Remember what you asked
  3. Write another prompt to draft content
  4. Forget to edit it properly

Build a workflow:
  Research Prompt -> Draft Prompt -> Edit Prompt -> Format Prompt
  Run it the same way every time. Get consistent results.
```

### Workflow Types

| Type | What It Does | Steps | Time Saved |
|------|-------------|-------|------------|
| Content Pipeline | Research -> Draft -> Edit -> Publish prep | 4 | 2-3 hours per piece |
| Code Review | Scan -> Identify issues -> Suggest fixes -> Write tests | 4 | 1-2 hours per review |
| Market Research | Define scope -> Gather data -> Analyse -> Report | 4 | 3-5 hours per report |
| Data Analysis | Clean data -> Analyse -> Visualise -> Summarise | 4 | 2-4 hours per dataset |

### Linked Database: Workflows

> *Create a linked database view here pointing to the Workflows database*
> Recommended views:
> - **All Workflows** -- sorted by Last Run descending
> - **By Category** -- grouped by Category column
> - **Active** -- filtered to Status = Active
> - **By Success Rate** -- sorted by Success Rate descending
> - **Quick Wins** -- filtered to Avg Time < 30, sorted by Success Rate descending

### Building a New Workflow

```
Step 1: Identify a task you do repeatedly (at least weekly)
Step 2: Break it into 2-5 discrete steps
Step 3: Find or create a prompt for each step
Step 4: Test the chain end-to-end with real input
Step 5: Record the workflow in your database
Step 6: Run it 3 times and refine based on results

The output of each prompt should feed naturally into the next.
If you're manually reformatting between steps, your prompts need work.
```

---

## `// COLLECTIONS`

Curated sets of prompts grouped by use case. Think of them as prompt playlists -- grab a collection when you need a complete toolkit for a specific job.

### Pre-Built Collections

**Weekly Newsletter Writer**
Everything you need to produce a newsletter from blank page to send-ready. Includes: topic research, outline generation, draft writing, subject line variations, and CTA optimisation. 6 prompts, designed to work in sequence.

**Code Ship Cycle**
From feature request to merged PR. Includes: requirements breakdown, code generation, test writing, code review, documentation, and PR description. 7 prompts covering the full development loop.

**Product Launch Kit**
Launch day sorted. Includes: positioning statement, landing page copy, email announcement, social media posts, FAQ generation, and press release draft. 8 prompts for a complete launch package.

**Client Onboarding**
New client? Run this collection. Includes: welcome email, project scope document, timeline generator, kickoff meeting agenda, and weekly update template. 5 prompts for professional onboarding.

### Linked Database: Collections

> *Create a linked database view here pointing to the Collections database*
> Recommended views:
> - **All Collections** -- sorted by Rating descending
> - **By Category** -- grouped by Category column
> - **Most Used** -- sorted by Prompt Count descending (higher count = more comprehensive)
> - **Recently Updated** -- sorted by Last Updated descending

### Creating Your Own Collection

```
1. Pick a recurring task or project type
2. List every prompt you'd need from start to finish
3. Order them logically (what comes first?)
4. Test the full collection on a real project
5. Add it to the Collections database
6. Share with your team if applicable

Good collections have 4-8 prompts. Under 4 is just a workflow.
Over 8 means you should probably split into two collections.
```

---

## `// PROMPT CRAFTING GUIDE`

A framework for writing prompts that consistently produce useful output. Stop guessing. Start crafting.

### The CRAFT Method

Every effective prompt has five components. Use this framework when writing new prompts or debugging ones that aren't performing.

| Letter | Component | What It Means | Example |
|--------|-----------|--------------|---------|
| C | Context | Background information the AI needs | "You are reviewing a Next.js 14 codebase with TypeScript" |
| R | Role | Who the AI should act as | "Act as a senior technical writer with 10 years of experience" |
| A | Action | The specific task to perform | "Write a comprehensive API reference for the following endpoints" |
| F | Format | How the output should be structured | "Use markdown with H2 headers, code blocks, and a summary table" |
| T | Tone | The voice and style of the output | "Professional but approachable, avoid jargon where possible" |

### CRAFT in Practice

**Bad prompt:**
```
Write me a blog post about AI tools.
```

**Why it's bad:** No context (which tools? for whom?), no role (generic voice), vague action (what angle?), no format (how long? what structure?), no tone (corporate? casual?).

**Good prompt (using CRAFT):**
```
Context: I run a newsletter for solo developers who use AI tools to ship faster.
My audience is technical but time-poor. They want practical recommendations,
not hype.

Role: Act as a senior developer who has personally tested 20+ AI coding tools
in production projects over the past year.

Action: Write a 1200-word blog post comparing Claude, ChatGPT, and Gemini
for code review tasks. Include specific examples of prompts that work well
for each model, and a clear recommendation for different use cases.

Format: Start with a one-paragraph TLDR. Use H2 headers for each model.
Include a comparison table at the end. Add a "Bottom Line" section with
actionable advice.

Tone: Direct and opinionated. Take a clear stance. Avoid hedging language
like "it depends" without explaining what it depends on.
```

### More Good vs Bad Examples

**Email writing:**

Bad: `Write an email to my client about a delay.`

Good: `Context: Our software project is 2 weeks behind schedule due to a third-party API integration issue. The client expects delivery on 15 April. Role: Act as a project manager who is transparent but solution-oriented. Action: Write a professional email informing the client of the delay, explaining the cause, and proposing a new timeline of 30 April with a mitigation plan. Format: Subject line + email body, under 200 words. Tone: Calm, confident, accountability without over-apologising.`

**Data analysis:**

Bad: `Analyse this data.`

Good: `Context: This CSV contains 6 months of e-commerce sales data with columns for date, product, revenue, units sold, and region. Role: Act as a data analyst preparing a board-level summary. Action: Identify the top 3 revenue trends, flag any anomalies, and recommend 2 actions based on the data. Format: Executive summary (3 bullet points), then a detailed section with supporting numbers. Include a markdown table of monthly revenue by region. Tone: Concise and data-driven. Lead with insights, not methodology.`

### Prompt Iteration Process

```
Version 1.0: Write the prompt using CRAFT
Version 1.1: Run it, review the output, fix obvious gaps
Version 1.2: Add constraints (word count, exclusions, edge cases)
Version 2.0: Major rewrite based on 5+ uses and consistent issues
Version 3.0: Refined prompt that consistently scores 4-5 stars

Most prompts shouldn't need to go past v2.0.
If a prompt needs constant rewriting, the task might be too complex for a single prompt.
Split it into a workflow instead.
```

### Common Prompt Mistakes

```
1. Too vague       -> Add specifics: numbers, names, constraints
2. Too long        -> If over 300 words, split into a workflow
3. No format spec  -> Always tell the AI what shape the output should take
4. No examples     -> Include 1-2 examples of what good output looks like
5. No constraints  -> Tell the AI what NOT to include (often more useful than what to include)
6. Wrong model     -> Some prompts work better on Claude vs ChatGPT -- test and note it
```

---

## `// ANALYTICS`

Track which prompts perform best and where your library needs work.

### Usage Patterns

Monitor these metrics weekly to keep your library sharp:

```
HEALTHY LIBRARY INDICATORS:
  80%+ of prompts rated 4-5 stars
  Average use count above 10
  No prompt untouched for 60+ days
  At least 1 workflow per major task type
  Prompts versioned past 1.0 (means you're iterating)

WARNING SIGNS:
  More than 10 prompts rated below 3
  Duplicate prompts for the same task
  Workflows with success rate below 70%
  Prompts you copy-paste from elsewhere instead of your library
  Categories with fewer than 3 prompts (underdeveloped area)
```

### Linked Database: Usage Log

> *Create a linked database view here pointing to the Usage Log database*
> Recommended views:
> - **Recent Usage** -- sorted by Date descending
> - **By Category** -- grouped by Category column
> - **By Model** -- grouped by Model Used column
> - **High Performers** -- filtered to Rating Given >= 4 and Output Quality = Excellent or Good
> - **Time Saved** -- sorted by Time Saved descending

### Rating Guide

Use this scale consistently so your ratings mean something:

| Rating | Meaning | Action |
|--------|---------|--------|
| 5 | Perfect output, used as-is or with minimal edits | Protect this prompt. Don't change it |
| 4 | Good output, needed minor tweaks | Note what you changed -- consider baking it in |
| 3 | Acceptable but required significant editing | Rewrite the prompt -- something is missing |
| 2 | Poor output, mostly had to redo it | Major rewrite or archive |
| 1 | Useless output, wasted time | Delete or completely reimagine the approach |

### Monthly Analytics Review

```
At the end of each month, answer these questions:

1. Which 5 prompts saved me the most time?
2. Which category has the weakest prompts?
3. Are there tasks I'm still doing manually that could be prompted?
4. Which workflows have the highest success rate?
5. What new prompts did I create this month -- and are they any good?
```

---

## `// MONTHLY REVIEW`

Block 15 minutes on the last day of each month. Go through this checklist.

### Monthly Prompt Library Maintenance

```
REVIEW PROMPTS (5 min)
- [ ] Archive any prompts not used in 60+ days
- [ ] Review all prompts rated below 3 -- rewrite or delete
- [ ] Check for duplicate prompts doing the same job
- [ ] Update version numbers for any prompts you refined this month

REVIEW WORKFLOWS (5 min)
- [ ] Run through each active workflow mentally -- still accurate?
- [ ] Update success rates based on actual results
- [ ] Retire workflows for tasks you no longer do
- [ ] Identify new tasks that should become workflows

GROW THE LIBRARY (5 min)
- [ ] Add any prompts you've been using outside the library
- [ ] Check each category -- any gaps?
- [ ] Ask: "What did I spend the most time on this month that AI could help with?"
- [ ] Set one goal for next month (e.g. "Build a workflow for client reporting")
```

---

## `// RESOURCES`

### Useful Links

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) -- official Claude prompting best practices
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering) -- ChatGPT prompting guide
- [Google AI Prompt Design](https://ai.google.dev/docs/prompt_best_practices) -- Gemini prompting strategies
- [Prompt Engineering Guide](https://www.promptingguide.ai/) -- community-maintained resource
- [FlowTech Templates](https://flowtech.gumroad.com) -- more Notion templates for creators and builders

### Prompt Library Health Indicators

```
GREEN (healthy):
  80%+ prompts rated 4-5 stars
  All categories have 5+ prompts
  Workflows cover your weekly repeating tasks
  You check the library before writing a new prompt

YELLOW (needs attention):
  50-80% prompts rated 4-5 stars
  Some categories sparse or empty
  You sometimes write prompts from scratch for tasks you've done before
  Workflows exist but aren't regularly used

RED (fix now):
  Under 50% prompts rated 4-5 stars
  You rarely open the library
  No workflows built
  Prompts haven't been updated in months
```

---

*Organise your AI. Prompt smarter. Ship faster.*
*Version 1.0 | Last updated: March 2026*
