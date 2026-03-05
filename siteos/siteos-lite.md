# SiteOS Lite — Construction Essentials

> A free starter template for construction project managers. Track your projects, defects, and daily site diary in one workspace.

> **Want the full version?** SiteOS (the complete package) includes RFI tracking, variation register, safety incident logging, progress claims, meeting minutes, subcontractor compliance, and a unified dashboard. [Get SiteOS →]

---

## Quick Start

1. Duplicate this page to your Notion workspace
2. Delete the sample data and start entering your own projects
3. Create the three databases below from the included CSV files (or build them manually)

---

## Project Tracker

Track all your active and upcoming projects in one place.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Project Name | Title | The project name |
| Project Number | Text | Internal project code |
| Client | Text | Client or principal |
| Contract Value | Number (AUD) | Head contract value |
| Status | Select | Tender / Pre-Construction / Active / Defects / Handover / Complete |
| Start Date | Date | Site start date |
| End Date | Date | Practical completion date |
| Site Address | Text | Full site address |
| Project Manager | Text | Assigned PM |
| % Complete | Number (%) | Overall completion |

### Sample Data

| Project Name | Project Number | Client | Contract Value | Status | % Complete |
|-------------|---------------|--------|---------------|--------|-----------|
| Melbourne Quarter Tower 3 | MQ-2024-003 | Lendlease Development | $185,000,000 | Active | 42% |
| Geelong Grammar Science Wing | GG-2024-017 | Geelong Grammar School | $28,500,000 | Pre-Construction | 5% |
| Chadstone Retail Expansion | CR-2023-041 | Vicinity Centres | $67,000,000 | Defects | 97% |

### Recommended Views

- **Board View** — Group by Status. Drag projects through stages.
- **Table View** — All project details at a glance.

---

## Defect List

Track defects from identification through to close-out.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Defect ID | Title | DEF-001, DEF-002, etc. |
| Project | Relation | Links to Projects database |
| Location | Text | Building, level, room |
| Description | Text | What the defect is |
| Category | Select | Structural / Finishing / Waterproofing / Electrical / Plumbing / HVAC / Fire / Other |
| Priority | Select | Critical / High / Medium / Low |
| Status | Select | Open / In Progress / Pending Verification / Closed |
| Assigned To | Text | Subcontractor responsible |
| Date Reported | Date | When logged |
| Date Due | Date | Rectification deadline |

### Sample Data

| Defect ID | Project | Location | Category | Priority | Status |
|-----------|---------|----------|----------|----------|--------|
| DEF-001 | Chadstone Retail Expansion | Level 2, Tenancy T2.14 | Waterproofing | Critical | In Progress |
| DEF-002 | Chadstone Retail Expansion | Ground Floor, Entry Lobby | Structural | High | Open |
| DEF-003 | Chadstone Retail Expansion | Level 1, Common Mall Area | Finishing | Medium | Pending Verification |

### Recommended Views

- **Board View** — Group by Status. Your defects workflow.
- **Table View** — Filter by Project, sort by Priority.

---

## Site Diary

Daily site record. One entry per project per day.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Date | Date | Entry date |
| Project | Relation | Links to Projects database |
| Weather | Select | Fine / Overcast / Rain / Storm |
| Temperature | Number | Degrees Celsius |
| Workforce Count | Text | Total headcount and breakdown |
| Key Activities | Text | What happened on site |
| Delays/Issues | Text | Anything that impacted progress |
| Materials Delivered | Text | Significant deliveries |
| Prepared By | Text | Who wrote the entry |

### Sample Data

| Date | Project | Weather | Workforce Count | Key Activities |
|------|---------|---------|----------------|---------------|
| 2025-02-10 | Melbourne Quarter Tower 3 | Fine | 142 | Level 22 slab pour, facade install Levels 10-12 |
| 2025-02-10 | Geelong Grammar Science Wing | Overcast | 28 | C-Block demolition strip-out, new footing set-out |
| 2025-02-10 | Chadstone Retail Expansion | Fine | 14 | Defect rectification, waterproofing remediation Level 2 |

### Recommended Views

- **Table View** — Filter by Project, sort by Date descending.
- **Calendar View** — See entries by day, spot missing entries.

> **Daily habit:** Fill in the site diary at the same time every day. End of shift, before you leave site. These records are critical if anything goes to dispute.

---

## Setting Up Relations

To connect your databases:

1. In the **Defects** database, add a **Relation** property pointing to **Projects**
2. In the **Site Diary** database, add a **Relation** property pointing to **Projects**
3. For each defect and diary entry, select the relevant project

This means when you open a project, you'll see all its defects and diary entries linked automatically.

---

## What You're Missing (Full SiteOS)

SiteOS Lite covers the essentials. The full SiteOS template ($99) adds:

| Feature | Why It Matters |
|---------|---------------|
| RFI Register | Track questions to consultants with response deadlines and cost/time impact flags |
| Variation Register | Full variation pipeline from draft through to client approval with cost rollups |
| Safety Incident Register | Log near misses, first aid, and serious incidents with root cause and corrective actions |
| Progress Claims Tracker | Head contract and subcontractor claims with retention tracking |
| Meeting Minutes | Site meetings, toolbox talks, client meetings with action item tracking |
| Subcontractor Register | Insurance expiry, licensing, and induction compliance tracking |
| Unified Dashboard | Linked views across all databases — see your entire operation in one screen |
| Database Relations | Full relationship map connecting all 9 databases |
| Notion Formulas | Days-until-due, overdue flags, variation cost rollups |
| Automation Recipes | Auto-date on status change, expiry notifications, overdue alerts |

[Get the full SiteOS template →]

---

> **Built by a construction professional.** Not a template designer. Every field in this template exists because it solved a real problem on a real construction site.
