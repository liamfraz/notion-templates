# PM OS — Project Manager Personal OS

> Your entire project operation in one workspace. Built by a project manager who has lived in status reports, stakeholder meetings, and risk registers — not a template designer who Googled "project management best practices."

---

## Quick Start

1. **Duplicate** this template to your Notion workspace
2. **Follow** the Setup Guide (included separately) to import databases
3. **Customise** the Dashboard with your active projects and team details
4. **Invite** your team and assign database permissions

> **Why PM OS exists:** Project managers juggle tasks in spreadsheets, meeting notes in email threads, risks in someone's head, and stakeholder updates in slide decks nobody reads. PM OS puts it all in one place — with the relationships between them intact. One task links to one project links to one goal. No more hunting.

---

## Dashboard

The Dashboard is your daily command view. Set it up with linked database views (instructions in the Setup Guide) to see everything at a glance.

### This Week

| View | What It Shows | Database |
|------|--------------|----------|
| This Week's Tasks | Filtered to tasks due this week, sorted by Priority | Tasks |
| Upcoming Meetings | Next 7 days of meetings, sorted by Date | Meeting Notes |
| Overdue Items | Tasks and risks past their due date with Status not Done/Closed | Tasks / Risks |

### Active Projects

| View | What It Shows | Database |
|------|--------------|----------|
| Projects Board | Kanban by Status (Planning → Complete) | Projects |
| Health Summary | Filtered to Active projects, grouped by Health | Projects |
| Budget Tracker | Active projects with Budget and % Complete visible | Projects |

### Goal Tracker

| View | What It Shows | Database |
|------|--------------|----------|
| Quarterly Goals | Filtered to current quarter, sorted by Progress % | Goals |
| Key Results Status | Grouped by Status (Not Started → Achieved) | Goals |

### Quick Actions

- Create New Task
- Log Meeting Notes
- Add Risk
- Record Decision
- Start Weekly Review

> **Tip:** Pin your most-used databases as full-page views in your sidebar. The Dashboard gives you the overview; full-page views give you the workspace.

---

## Projects

The backbone of PM OS. Every other database relates back to a Project.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | The project name |
| Code | Text | Your internal project code (e.g., PRJ-2026-003) |
| Client/Sponsor | Text | Client name or executive sponsor |
| Budget | Number (currency) | Total approved budget |
| Status | Select | Planning / Active / On Hold / Closing / Complete |
| Start Date | Date | Planned or actual start date |
| End Date | Date | Target completion date |
| Priority | Select | Critical / High / Medium / Low |
| Owner | Person | Assigned project manager |
| % Complete | Number (%) | Overall project completion |
| Health | Select | On Track / At Risk / Off Track |
| Notes | Text | General notes |

### Linked Databases (Relations)

Each project automatically links to:
- **Tasks** assigned to that project
- **Goals** aligned to that project
- **Meeting Notes** held for that project
- **Stakeholders** related to that project
- **Risks** identified on that project
- **Decisions** made on that project
- **Weekly Reviews** that reference that project

### Recommended Views

1. **Board View** — Group by Status. Drag projects through stages.
2. **Timeline View** — Gantt-style view using Start Date to End Date.
3. **Table View** — Full detail with all properties visible. Filter by Owner.
4. **Gallery View** — Project cards showing Health, Priority, and % Complete.

---

## Tasks

Where the actual work lives. Every deliverable, action item, and to-do tracked from creation to completion.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Task Name | Title | Clear, actionable task name |
| Project | Relation | Links to Projects database |
| Assignee | Person | Who owns this task |
| Status | Select | To Do / In Progress / In Review / Blocked / Done |
| Priority | Select | Critical / High / Medium / Low |
| Due Date | Date | When this task needs to be done |
| Estimated Hours | Number | Planned effort in hours |
| Actual Hours | Number | Actual effort spent |
| Tags | Select | Planning / Design / Development / Testing / Documentation / Admin |
| Dependencies | Text | What needs to happen before this task can start |
| Notes | Text | Context, links, details |

### Recommended Views

1. **Board View** — Group by Status. Your task workflow.
2. **Table View** — Filter by Project and Assignee, sort by Priority then Due Date.
3. **Calendar View** — Due dates across all projects. Spot overload weeks.
4. **Filtered View** — "My Tasks" — Assignee is me, Status is not Done.

> **Reality check:** Your task list will grow faster than you can complete it. That is normal. The Board View lets you see what is actually moving vs. what is stuck. Focus on Critical and High priority items — the Low ones can wait for a quiet week that never comes.

---

## Goals

Connect daily work to outcomes. Track company objectives, team targets, and personal development goals in one place.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Goal Name | Title | Clear, measurable goal statement |
| Type | Select | Company / Team / Personal / Project |
| Time Frame | Select | Annual / Quarterly / Monthly |
| Status | Select | Not Started / In Progress / Achieved / Missed |
| Key Results | Text | Measurable outcomes that define success |
| Progress % | Number (%) | How far along this goal is |
| Owner | Person | Who is accountable for this goal |
| Due Date | Date | Target completion date |
| Notes | Text | Context, blockers, updates |

### Recommended Views

1. **Board View** — Group by Status. See goal progress at a glance.
2. **Table View** — Filter by Type and Time Frame. Quarterly planning view.
3. **Filtered View** — "This Quarter" — Time Frame is Quarterly, Due Date within current quarter.

> **Pro tip:** Goals without Key Results are just wishes. Write Key Results that are specific and measurable: "Reduce average project delivery time by 15%" beats "Deliver projects faster." If you cannot measure it, you cannot manage it.

---

## Weekly Reviews

The habit that separates reactive PMs from effective ones. A structured weekly reflection to stay ahead of your projects.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Week Starting | Date (Title) | Monday of the review week |
| Energy Level | Select | High / Medium / Low |
| Top 3 Wins | Text | Best outcomes from the week |
| Challenges | Text | What went wrong or felt hard |
| Lessons Learned | Text | What you would do differently |
| Next Week Priorities | Text | Top 3-5 priorities for next week |
| Projects Reviewed | Relation | Links to Projects database |
| Score | Number | Self-assessment 1-10 |
| Notes | Text | Anything else worth capturing |

### Recommended Views

1. **Table View** — Sort by Week Starting descending. Most recent first.
2. **Gallery View** — Week cards showing Score and Energy Level. Spot trends.
3. **Filtered View** — "Last 4 Weeks" — Quick look at recent trajectory.

> **Weekly review discipline:** Block 30 minutes every Friday afternoon. No exceptions. Review each active project, score your week honestly, and set next week's priorities before you close your laptop. The PM who reviews weekly catches problems at Week 2. The PM who doesn't catches them at Month 3 — when it is too late.

---

## Meeting Notes

Stop losing decisions and action items in email threads. Every meeting documented, every action tracked.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Meeting Title | Title | Descriptive name for the meeting |
| Date | Date | Meeting date |
| Type | Select | 1-on-1 / Team Standup / Client Call / Steering Committee / Workshop / Retrospective |
| Project | Relation | Links to Projects database |
| Attendees | Text | Who was present |
| Agenda | Text | Topics to cover |
| Key Decisions | Text | What was decided (and by whom) |
| Action Items | Text | What needs to happen, who owns it, and by when |
| Follow-up Date | Date | When to follow up on action items |
| Notes | Text | Additional context and discussion points |

### Recommended Views

1. **Table View** — Filter by Project and Type. Sort by Date descending.
2. **Calendar View** — See all meetings across projects. Plan your week.
3. **Board View** — Group by Type. See the balance of your meeting load.
4. **Filtered View** — "Open Actions" — Follow-up Date is before today.

> **Pro tip:** Write action items as "Person — Action — Due Date" on a single line each. When the meeting ends, transfer them to Tasks immediately. An action item that lives only in meeting notes is an action item that never gets done.

---

## Stakeholders

Know who matters, how much they matter, and how to keep them engaged. The stakeholder register that actually gets used.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Name | Title | Stakeholder full name |
| Role/Title | Text | Job title or role on the project |
| Organisation | Text | Company or department |
| Email | Email | Contact email |
| Phone | Phone | Contact number |
| Influence Level | Select | High / Medium / Low |
| Interest Level | Select | High / Medium / Low |
| Communication Preference | Select | Email / Slack / Teams / In Person / Phone |
| Engagement Strategy | Text | How you plan to keep this stakeholder informed and aligned |
| Related Projects | Relation | Links to Projects database |
| Notes | Text | Relationship context, preferences, history |

### Recommended Views

1. **Table View** — Sort by Influence Level descending. Know who to focus on.
2. **Board View** — Group by Influence Level. Your stakeholder power map.
3. **Filtered View** — "High Influence + High Interest" — These are the stakeholders who need the most attention.

> **Stakeholder reality:** The stakeholders who are quiet are not necessarily happy — they might just be disengaged. High Influence + Low Interest is the most dangerous combination. They do not care until they do, and by then you have a problem. Check in with them proactively.

---

## Risks

Track what could go wrong before it does. Every risk identified, assessed, and managed through to resolution.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Risk ID | Title | Format: RSK-001, RSK-002, etc. |
| Project | Relation | Links to Projects database |
| Description | Text | Clear description of the risk event |
| Category | Select | Technical / Resource / Budget / Schedule / Scope / External |
| Probability | Select | High / Medium / Low |
| Impact | Select | High / Medium / Low |
| Risk Score | Formula | Probability x Impact (High=3, Medium=2, Low=1) |
| Status | Select | Open / Mitigating / Accepted / Closed |
| Mitigation Plan | Text | What you are doing to reduce the probability or impact |
| Owner | Person | Who is responsible for managing this risk |
| Date Identified | Date | When the risk was first logged |
| Review Date | Date | When to reassess this risk |
| Notes | Text | Updates, triggers, related issues |

### Recommended Views

1. **Table View** — Sort by Risk Score descending. Highest risks first.
2. **Board View** — Group by Status. See what is Open vs. Mitigating vs. Closed.
3. **Filtered View** — "Review Due" — Review Date is before today AND Status is Open or Mitigating.
4. **Board View (Category)** — Group by Category. Spot where your risks are clustering.

> **Risk management truth:** A risk register that gets updated once at project kickoff and never again is theatre. Review your top 10 risks every week. Close the ones that have passed. Add the new ones you discovered this week. The register is alive or it is useless.

---

## Decisions

Track every significant decision so you never have the "wait, when did we decide that?" conversation again.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Decision ID | Title | Format: DEC-001, DEC-002, etc. |
| Project | Relation | Links to Projects database |
| Decision | Text | The decision that was made |
| Context/Background | Text | Why this decision was needed |
| Options Considered | Text | What alternatives were evaluated |
| Rationale | Text | Why this option was chosen over the others |
| Made By | Text | Who made or approved the decision |
| Date | Date | When the decision was made |
| Status | Select | Proposed / Approved / Reversed / Superseded |
| Impact | Text | What this decision affects (scope, timeline, budget, etc.) |
| Notes | Text | Supporting documents, meeting references, follow-up items |

### Recommended Views

1. **Table View** — Sort by Date descending. Most recent decisions first.
2. **Board View** — Group by Status. Track the decision pipeline.
3. **Filtered View** — By Project. See all decisions for a specific project in one view.

> **Decision hygiene:** Log the decision the same day it is made. Include the rationale and the options you rejected. Six months from now, someone will ask "why didn't we go with Option B?" and you will have the answer in 10 seconds instead of digging through email chains.

---

## Database Relationships Map

Here is how all databases connect:

```
                        PROJECTS (Central Hub)
                             |
     +--------+--------+----+----+--------+--------+--------+
     |        |        |         |        |        |        |
   Tasks    Goals   Meetings  Stakeholders  Risks  Decisions  Weekly
                                                              Reviews
     |
     +--- Goals (via Project alignment)
```

**Key Relations:**
- Every database links back to **Projects** (many-to-one)
- **Tasks** are where daily work happens — create them from Meeting action items
- **Risks** with high scores should generate **Tasks** for mitigation actions
- **Decisions** should reference the **Meeting Notes** where they were made
- **Weekly Reviews** pull in **Projects** for structured reflection
- **Stakeholders** map to **Projects** to track who cares about what

---

## Formulas & Automations

### Useful Notion Formulas

**Days Until Due (Tasks):**
```
dateBetween(prop("Due Date"), now(), "days")
```

**Overdue Flag (Tasks):**
```
if(and(prop("Status") != "Done", prop("Due Date") < now()), "OVERDUE", "")
```

**Risk Score (Risks):**
```
lets(
  prob, if(prop("Probability") == "High", 3, if(prop("Probability") == "Medium", 2, 1)),
  imp, if(prop("Impact") == "High", 3, if(prop("Impact") == "Medium", 2, 1)),
  prob * imp
)
```

**Effort Variance (Tasks):**
```
if(prop("Actual Hours") > 0, round((prop("Actual Hours") - prop("Estimated Hours")) / prop("Estimated Hours") * 100), 0)
```

### Recommended Automations (Notion Automations)

1. **When** a Task Status changes to "Done" → **Set** a completion timestamp
2. **When** a Risk Review Date is within 3 days and Status is "Open" → **Send notification** to Owner
3. **When** a Meeting Follow-up Date is today → **Send notification** to review action items
4. **When** a new Task is created → **Set** Status to "To Do" and Priority to "Medium"

---

## Templates Within Databases

### Task Entry Template
Pre-filled template for new tasks:
- Status: To Do
- Priority: Medium (change as needed)
- Prompt text in Notes: "Describe the deliverable. Include acceptance criteria and any dependencies."

### Meeting Notes Template
Pre-filled template for meeting notes:
- Date: Today
- Prompt text in Agenda: "List topics to cover. Number them for easy reference."
- Prompt text in Action Items: "Format: Person — Action — Due Date"

### Risk Entry Template
Pre-filled template:
- Status: Open
- Date Identified: Today
- Prompt in Description: "Describe the risk event. What could happen, and what would trigger it?"
- Prompt in Mitigation Plan: "What actions will reduce the probability or impact of this risk?"

### Weekly Review Template
Pre-filled template:
- Week Starting: This Monday
- Prompt in Top 3 Wins: "What went well this week? Be specific."
- Prompt in Next Week Priorities: "What are the 3-5 things that matter most next week?"

---

## Tips for Project Managers

<details>
<summary><strong>Getting your team to actually use this</strong></summary>

Team adoption makes or breaks any PM system. Here is what works:

1. **Start with Tasks and Meeting Notes only.** Don't dump 8 databases on them Day 1.
2. **Make it faster than their current method.** If they are tracking tasks in email, the board view with drag-and-drop is already faster.
3. **Show them the search.** "Remember that decision we made about the API migration? Here it is in 2 seconds."
4. **Use the Notion mobile app.** Not everyone lives at a desk. The mobile app lets people update task status from anywhere.
5. **Don't make them enter data twice.** If it is in PM OS, it does not need to go in another spreadsheet or status email.

</details>

<details>
<summary><strong>Scaling from solo to team</strong></summary>

PM OS works for a single PM but shines when your team is using it:

1. **Dashboard filtered views** — Set up a master Dashboard with "All Projects" views, plus individual project pages with filtered views.
2. **Owner/Assignee filters** — Use Person properties on Projects and Tasks and filter views by current user. Each team member sees only their work.
3. **Weekly reporting** — Export Table Views for weekly stakeholder or management reports.
4. **Onboarding** — New team member? Point them to their project page. Everything they need is already filtered and waiting.

</details>

<details>
<summary><strong>What to track vs. what to skip</strong></summary>

Not everything belongs in PM OS. Here is the line:

**Track in PM OS:**
- Projects, Tasks, Goals, Weekly Reviews, Meeting Notes, Stakeholders, Risks, Decisions

**Keep in your existing systems:**
- Detailed financial reporting (use your ERP or finance tool — PM OS tracks budget at the project level, not line-item costs)
- Detailed scheduling (use MS Project, Smartsheet, or Monday.com for complex Gantt charts and resource levelling — Notion is not a scheduling engine)
- Document management (use SharePoint, Google Drive, or Confluence for formal document control and version management)
- Time tracking (use Harvest, Toggl, or Clockify for detailed time logging — PM OS captures estimated vs. actual hours at the task level only)

**PM OS is your operational command center, not a replacement for specialist software.**

</details>

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 2026 | Initial release |

---

> **Built by a project manager.** PM OS was designed in the trenches — managing real projects with real stakeholders, real deadlines, and real scope creep. Every database, every property, every view exists because it solved a real problem. If something doesn't work for you, it's a bug — reach out and I'll fix it.
