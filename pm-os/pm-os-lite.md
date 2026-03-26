# PM OS Lite — Project Management Essentials

> A free starter template for project managers. Track your projects, tasks, and goals in one workspace.

> **Want the full version?** PM OS (the complete package) includes weekly reviews, meeting notes, stakeholder register, risk log, decision register, resource planning, three dashboards, and full automation recipes. [Get PM OS →]

---

## Quick Start

1. Duplicate this page to your Notion workspace
2. Delete the sample data and start entering your own projects
3. Create the three databases below from the included CSV files (or build them manually)

---

## Projects

Track all your active and upcoming projects in one place.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Project Name | Title | The project name |
| Project Code | Text | Internal project identifier |
| Client/Sponsor | Text | Client or project sponsor |
| Budget | Number (Currency) | Total project budget |
| Status | Select | Planning / Active / On Hold / Closing / Complete |
| Start Date | Date | Project kick-off date |
| End Date | Date | Target completion date |
| Priority | Select | Critical / High / Medium / Low |
| Owner | Text | Project manager or lead |
| % Complete | Number (%) | Overall completion |
| Health | Select | Green / Amber / Red |
| Notes | Text | Additional context or updates |

### Sample Data

| Project Name | Project Code | Client/Sponsor | Budget | Status | % Complete |
|-------------|-------------|----------------|--------|--------|-----------|
| Mobile App Redesign | MAR-2026-001 | Horizon Financial | $450,000 | Active | 38% |
| Data Platform Migration | DPM-2025-089 | Internal IT | $1,200,000 | Active | 65% |
| Q3 Marketing Campaign | QMC-2026-012 | Marketing Dept | $180,000 | Planning | 8% |

### Recommended Views

- **Board View** — Group by Status. Drag projects through stages.
- **Table View** — All project details at a glance, sort by Priority.

---

## Tasks

Track work items across all your projects from assignment through to completion.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Task Name | Title | What needs to be done |
| Project | Relation | Links to Projects database |
| Assignee | Text | Person responsible |
| Status | Select | To Do / In Progress / In Review / Blocked / Done |
| Priority | Select | Critical / High / Medium / Low |
| Due Date | Date | Task deadline |
| Estimated Hours | Number | Estimated effort in hours |
| Notes | Text | Additional context or blockers |

### Sample Data

| Task Name | Project | Assignee | Status | Priority | Due Date |
|-----------|---------|----------|--------|----------|----------|
| Build authentication API endpoints | Mobile App Redesign | Tom Bradley | In Progress | High | 2026-04-04 |
| Migrate customer transaction database | Data Platform Migration | Wei Zhang | In Progress | Critical | 2026-03-28 |
| Draft creative brief for agency | Q3 Marketing Campaign | Lisa Nakamura | In Progress | Medium | 2026-03-30 |
| Write integration test suite for new APIs | Data Platform Migration | Anika Patel | To Do | High | 2026-04-11 |

### Recommended Views

- **Board View** — Group by Status. Your task workflow.
- **Table View** — Filter by Project, sort by Priority.

---

## Goals

Set objectives and track progress with measurable key results.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Goal Name | Title | The objective |
| Type | Select | Company / Team / Personal / Project |
| Status | Select | Not Started / In Progress / Achieved / Missed |
| Key Results | Text | Measurable outcomes that define success |
| Progress % | Number (%) | Overall progress toward the goal |
| Due Date | Date | Target completion date |

### Sample Data

| Goal Name | Type | Status | Progress % | Due Date |
|-----------|------|--------|-----------|----------|
| Deliver all Q1-Q2 projects within 5% of budget | Company | In Progress | 55% | 2026-06-30 |
| Improve team velocity by 15% across sprints | Team | In Progress | 40% | 2026-03-31 |
| Obtain PMP certification | Personal | In Progress | 60% | 2026-06-15 |

### Recommended Views

- **Board View** — Group by Type. See goals across all levels.
- **Table View** — Sort by Due Date, filter by Status.

> **Weekly habit:** Review your goals every Monday morning. Update progress percentages and flag anything at risk before your status meetings.

---

## Setting Up Relations

To connect your databases:

1. In the **Tasks** database, add a **Relation** property pointing to **Projects**
2. For each task, select the relevant project

This means when you open a project, you'll see all its tasks linked automatically.

---

## What You're Missing (Full PM OS)

PM OS Lite covers the essentials. The full PM OS template adds:

| Feature | Why It Matters |
|---------|---------------|
| Weekly Reviews | Structured weekly reflection with wins, blockers, and next-week priorities |
| Meeting Notes | Capture agendas, decisions, and action items linked to projects and stakeholders |
| Stakeholder Register | Track influence, communication preferences, and engagement levels for every stakeholder |
| Risk Register | Log risks with probability, impact, mitigation plans, and risk owners |
| Decision Log | Record key decisions with rationale, who approved, and what alternatives were considered |
| Resource Planning | Track team capacity, allocation across projects, and utilisation rates |
| Project Dashboard | Linked views across all databases — see your entire portfolio in one screen |
| Team Dashboard | Workload distribution, velocity trends, and blocked items at a glance |
| Personal Dashboard | Your tasks, upcoming deadlines, and goal progress in one view |
| Full Database Relations | Complete relationship map connecting all 9 databases |
| Notion Formulas | Days-until-due, overdue flags, budget variance calculations, health scoring |
| Automation Recipes | Auto-date on status change, overdue notifications, weekly review reminders |

[Get the full PM OS template →]

---

> **Built by a project manager.** Not a template designer. Every field in this template exists because it solved a real problem on a real project.
