# AI Prompt Library & Workflow Manager -- Lite

> A free starter template for organising your AI prompts. Want the full version with workflows, collections, analytics, and the complete CRAFT framework? Upgrade to the Premium version.

---

## `// PROMPT DATABASE`

Store and organise every AI prompt you use. Rate them, track usage, and stop rewriting the same prompt twice.

### How to Use

Add a row for each prompt with:
- A clear name describing what it does
- Which category it falls into (Writing, Coding, Marketing, etc.)
- The full prompt text with [VARIABLES] for customisation
- A rating based on output quality (1-5 stars)
- Which AI model it works best with

### Sample Prompts

| Name | Category | Model | Rating | Use Count |
|------|----------|-------|--------|-----------|
| Blog Post Outline Generator | Writing | Any | 5 | 89 |
| Python Code Reviewer | Coding | Claude | 4 | 156 |
| SEO Meta Description Writer | Marketing | ChatGPT | 4 | 67 |
| CSV Data Summariser | Analysis | Claude | 5 | 43 |
| Product Name Brainstorm | Creative | Any | 4 | 31 |

> **Tip:** Convert this table to a Notion database for filtering and sorting. Select the table, then click "Turn into database." Then import the full `prompts.csv` from the Premium version for 50 ready-to-use prompts.

### Quick Category Guide

| Category | What Goes Here |
|----------|---------------|
| Writing | Blog posts, emails, newsletters, copy |
| Coding | Code generation, review, debugging, docs |
| Marketing | SEO, ads, audience research, strategy |
| Analysis | Data interpretation, reports, trends |
| Research | Literature review, competitive intel |
| Creative | Brainstorming, naming, storytelling |
| Business | Proposals, strategy, OKRs, meetings |
| Productivity | Task management, planning, decisions |

---

## `// BASIC WORKFLOWS`

Chain prompts together to handle multi-step tasks consistently.

### What's a Workflow?

Instead of running one prompt at a time and improvising the next step, a workflow links 2-5 prompts in sequence. The output of each prompt feeds into the next.

### Example: Content Pipeline

```
Step 1: Research Prompt -> "Summarise the latest developments in [TOPIC]"
Step 2: Outline Prompt -> "Create a blog outline based on this research: [PASTE STEP 1]"
Step 3: Draft Prompt  -> "Write a 1500-word blog post following this outline: [PASTE STEP 2]"
Step 4: Edit Prompt   -> "Edit this draft for clarity and tone: [PASTE STEP 3]"
```

### Example: Code Review

```
Step 1: Scan Prompt    -> "List all potential issues in this code: [PASTE CODE]"
Step 2: Fix Prompt     -> "Suggest fixes for each issue: [PASTE STEP 1]"
Step 3: Test Prompt    -> "Write unit tests covering the edge cases identified: [PASTE STEP 1]"
```

> **Tip:** In the Premium version, you get 12 pre-built workflows with success rate tracking and a dedicated Workflows database.

---

## `// PROMPT CRAFTING GUIDE`

### The CRAFT Method

Write better prompts by including five components every time:

| Letter | Component | What It Means |
|--------|-----------|--------------|
| C | Context | Background information the AI needs |
| R | Role | Who the AI should act as |
| A | Action | The specific task to perform |
| F | Format | How the output should be structured |
| T | Tone | The voice and style of the output |

### Example

**Bad prompt:**
```
Write me a blog post about AI tools.
```

**Good prompt (using CRAFT):**
```
Context: I run a newsletter for solo developers who use AI tools to ship faster.
Role: Act as a senior developer who has tested 20+ AI coding tools in production.
Action: Write a 1200-word blog post comparing Claude, ChatGPT, and Gemini for
  code review tasks with specific prompt examples for each.
Format: TLDR paragraph, H2 per model, comparison table, "Bottom Line" section.
Tone: Direct and opinionated. Take a clear stance.
```

The difference is night and day. CRAFT takes 60 seconds longer to write and saves 20 minutes of back-and-forth.

---

## `// WHAT'S IN THE FULL VERSION?`

The Premium AI Prompt Library & Workflow Manager includes everything above plus:

- **Prompt Database** -- 50 pre-built, genuinely useful prompts across 8 categories with ratings, version tracking, and model compatibility notes
- **Workflows Database** -- 12 pre-built workflows with success rate tracking, time estimates, and step-by-step prompt chains
- **Collections Database** -- 8 curated prompt sets (Newsletter Writer Kit, Code Ship Cycle, Product Launch Kit, and more)
- **Usage Log** -- track every prompt use with ratings, time saved, and output quality
- **Full CRAFT Guide** -- complete framework with multiple good vs bad examples, iteration process, and common mistakes
- **Analytics Section** -- monitor prompt performance, identify weak spots, optimise your library
- **Monthly Review Workflow** -- 15-minute maintenance checklist to keep your library sharp
- **Dashboard** -- "Prompt of the Day" system, usage stats, and quick actions
- **4 CSV databases** with realistic sample data ready to import
- **Step-by-step setup guide** with database relations and view configurations

[Get AI Prompt Library & Workflow Manager Premium ->](YOUR_GUMROAD_LINK_HERE)

---

*Organise your AI. Prompt smarter. Ship faster.*
