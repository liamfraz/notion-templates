# SiteOS — Construction Project Command Center

> Your entire construction operation in one workspace. Built by a construction professional with 3+ years at Kane Constructions — not a template designer who Googled "construction project management."

---

## Quick Start

1. **Duplicate** this template to your Notion workspace
2. **Follow** the Setup Guide (included separately) to import databases
3. **Customise** the Dashboard with your company details and active projects
4. **Invite** your team and assign database permissions

> **Why SiteOS exists:** Construction PMs juggle defects in spreadsheets, RFIs in email chains, variations on sticky notes, and progress claims in folders nobody can find. SiteOS puts it all in one place — with the relationships between them intact. One defect links to one project links to one subcontractor. No more hunting.

---

## Dashboard

The Dashboard is your daily command view. Set it up with linked database views (instructions in the Setup Guide) to see everything at a glance.

### Active Project Summary

| View | What It Shows | Database |
|------|--------------|----------|
| Active Projects Board | Kanban by Status (Tender → Complete) | Projects |
| This Week's Defects | Filtered to Critical + High priority, sorted by due date | Defects |
| Open RFIs | Filtered to Open status, sorted by Date Required | RFIs |
| Pending Variations | Filtered to Draft + Submitted status | Variations |
| Recent Safety Incidents | Last 30 days, sorted by date | Safety Incidents |
| Upcoming Claims | Due within 14 days | Progress Claims |
| Today's Site Diary | Filtered to today's date | Site Diary |

### Quick Actions

- Create New Defect
- Log Safety Incident
- Submit RFI
- Record Site Diary Entry
- Create Progress Claim

> **Tip:** Pin your most-used databases as full-page views in your sidebar. The Dashboard gives you the overview; full-page views give you the workspace.

---

## Project Tracker

The backbone of SiteOS. Every other database relates back to a Project.

### Database Properties

| Property | Type | Purpose |
|----------|------|---------|
| Project Name | Title | The project name |
| Project Number | Text | Your internal project numbering (e.g., MQ-2024-003) |
| Client | Text | Client or principal name |
| Contract Value | Number (AUD) | Head contract value |
| Status | Select | Tender / Pre-Construction / Active / Defects / Handover / Complete |
| Start Date | Date | Contract or site start date |
| End Date | Date | Practical completion date |
| Site Address | Text | Full site address |
| Project Manager | Person | Assigned PM |
| Superintendent | Person | Assigned Super |
| % Complete | Number (%) | Overall project completion |
| Notes | Text | General notes |

### Linked Databases (Relations)

Each project automatically links to:
- **Defects** assigned to that project
- **RFIs** raised on that project
- **Variations** against that project
- **Safety Incidents** logged on that project
- **Progress Claims** for that project
- **Site Diary** entries for that project
- **Meetings** held for that project

### Recommended Views

1. **Board View** — Group by Status. Drag projects through stages.
2. **Timeline View** — Gantt-style view using Start Date → End Date.
3. **Table View** — Full detail with all properties visible. Filter by PM.

---

## Defect Management

Track every defect from identification through to close-out and retention release.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Defect ID | Title | Auto-format: DEF-001, DEF-002, etc. |
| Project | Relation | Links to Projects database |
| Location | Text | Building, level, room, grid reference |
| Description | Text | Clear description of the defect |
| Category | Select | Structural / Finishing / Waterproofing / Electrical / Plumbing / HVAC / Fire / Other |
| Priority | Select | Critical / High / Medium / Low |
| Status | Select | Open / In Progress / Pending Verification / Closed |
| Reported By | Text | Person who identified the defect |
| Assigned To | Text | Subcontractor or trade responsible |
| Date Reported | Date | When defect was logged |
| Date Due | Date | Rectification deadline |
| Date Closed | Date | When defect was verified and closed |
| Photo Link | URL | Link to photo evidence (use Notion image block or external link) |
| Notes | Text | Remediation details, correspondence, etc. |

### Recommended Views

1. **Board View** — Group by Status. Your defects workflow.
2. **Table View** — Filter by Project, sort by Priority then Date Due.
3. **Calendar View** — Due dates for defect rectification deadlines.
4. **Gallery View** — Thumbnail of defect photos with key details.

> **Construction reality check:** Your defects list will grow fast during the DLP. Don't panic. The Board View lets you see what's actually moving vs. what's stuck. Focus on Critical and High — the Low ones can wait for the next defect inspection round.

---

## RFI Register

Formal tracking for Requests for Information. Captures the question, the response, and the impact.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| RFI Number | Title | Sequential: RFI-0001, RFI-0002, etc. |
| Project | Relation | Links to Projects database |
| Subject | Text | Brief subject line |
| Description | Text | Full RFI question with drawing/spec references |
| From | Text | Who is asking |
| To | Text | Consultant or party being asked |
| Date Submitted | Date | When RFI was sent |
| Date Required | Date | When a response is needed by |
| Date Responded | Date | When a response was received |
| Status | Select | Open / Responded / Closed |
| Response Summary | Text | Summary of the response received |
| Impact on Cost | Select | Yes / No / Possible |
| Impact on Time | Select | Yes / No / Possible |

### Recommended Views

1. **Table View** — Default. Sort by Date Required to see what needs chasing.
2. **Board View** — Group by Status. See Open vs. Responded vs. Closed at a glance.
3. **Filtered View** — "Overdue RFIs" — Date Required is before today AND Status is Open.

> **Pro tip:** RFIs with "Possible" cost or time impact should trigger a Variation. Set up a Notion automation or just make it a habit: every time you close an RFI with a cost/time impact, create the corresponding Variation entry.

---

## Variation Register

Track every variation from identification through to approval (or rejection).

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Variation Number | Title | Sequential: VAR-001, VAR-002, etc. |
| Project | Relation | Links to Projects database |
| Description | Text | What the variation involves |
| Reason | Select | Client Request / Design Change / Site Condition / Regulatory / Error |
| Status | Select | Draft / Submitted / Approved / Rejected / Pending |
| Cost Impact ($) | Number (AUD) | Dollar value of the variation |
| Time Impact (Days) | Number | Extension of time in days |
| Submitted Date | Date | When submitted to client/principal |
| Approved Date | Date | When approved |
| Approved By | Text | Who approved it |
| Notes | Text | Supporting details, quote references |

### Recommended Views

1. **Table View** — Sort by Status then Cost Impact descending.
2. **Board View** — Group by Status. Track variation approval pipeline.
3. **Summary View** — Rollup total approved cost impact per project.

### Rollup Formulas

Set up a **Rollup** property in the Projects database to sum approved variation values. This gives you a live "Approved Variations Total" on each project card.

---

## Safety Incident Register

Every near miss, first aid, and serious incident documented and tracked through to close-out.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Incident ID | Title | Format: INC-YYYY-NNN |
| Project | Relation | Links to Projects database |
| Date | Date | Incident date |
| Time | Text | Time of incident |
| Location | Text | Specific location on site |
| Type | Select | Near Miss / First Aid / Medical Treatment / Lost Time / Dangerous Occurrence |
| Description | Text | What happened |
| Persons Involved | Text | Names and companies |
| Immediate Action | Text | What was done straight away |
| Root Cause | Text | Why it happened |
| Corrective Action | Text | What's being done to prevent recurrence |
| Status | Select | Reported / Investigating / Closed |
| Reported By | Text | Who reported the incident |

### Recommended Views

1. **Table View** — Sort by Date descending. Most recent first.
2. **Board View** — Group by Status. See what's still under investigation.
3. **Filtered View** — By Type. Useful for safety reporting and trend analysis.

> **Non-negotiable:** Every near miss gets logged. The near misses you don't log are the serious incidents waiting to happen. If your team isn't reporting near misses, the system isn't working — the hazards are still there, you just can't see them.

---

## Progress Claims

Track head contract claims and subcontractor claims. Know exactly where every dollar is.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Claim Number | Title | Format: PC-[ProjectCode]-NNN |
| Project | Relation | Links to Projects database |
| Period | Text | Claim period (e.g., "January 2025" or "Final Claim") |
| Claim Type | Select | Head Contract / Subcontractor |
| Contractor | Text | Who is claiming |
| Amount Claimed ($) | Number (AUD) | Amount submitted |
| Amount Approved ($) | Number (AUD) | Amount certified |
| Retention Held ($) | Number (AUD) | Retention deducted |
| Net Payment ($) | Number (AUD) | What gets paid |
| Date Submitted | Date | Submission date |
| Date Approved | Date | Certification date |
| Status | Select | Draft / Submitted / Under Review / Approved / Paid |

### Recommended Views

1. **Table View** — Group by Project. Filter by Claim Type.
2. **Board View** — Group by Status. Track the claims pipeline.
3. **Calendar View** — Submission dates to manage your monthly claims cycle.

### Rollup Formulas

- **Total Claimed vs. Approved** — Rollup on Projects database to see cumulative claim values
- **Outstanding Retention** — Sum of Retention Held where Status is not "Paid"

---

## Site Diary

Daily site records. The single most important document if anything goes to dispute.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Date | Title (Date) | One entry per project per day |
| Project | Relation | Links to Projects database |
| Weather | Select | Fine / Overcast / Rain / Storm |
| Temperature | Number | Degrees Celsius |
| Workforce Count | Text | Total and breakdown (e.g., "Kane 18, Subbies 124") |
| Key Activities | Text | What happened on site today |
| Visitors | Text | Who visited site and why |
| Safety Observations | Text | Any safety matters noted |
| Delays/Issues | Text | Anything that impacted progress |
| Materials Delivered | Text | Significant deliveries |
| Plant on Site | Text | Major plant and equipment |
| Prepared By | Text | Who wrote the entry |

### Recommended Views

1. **Table View** — Filter by Project, sort by Date descending.
2. **Calendar View** — See entries by day. Spot gaps (missing diary entries).
3. **Board View** — Group by Weather. Quick visual of lost weather days.

> **Site diary discipline:** Fill it in the same time every day — end of shift, before you leave site. If you leave it until tomorrow, you'll forget half of what happened. And when a claim dispute happens 18 months later, these entries are gold.

---

## Meetings & Minutes

Track all site meetings, design meetings, client meetings, and toolbox talks.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Meeting Type | Select | Site Meeting / Design Meeting / Client Meeting / Toolbox Talk / Safety Committee |
| Project | Relation | Links to Projects database |
| Date | Date | Meeting date |
| Time | Text | Start time |
| Attendees | Text | Who was there |
| Agenda Items | Text | What was discussed |
| Minutes Summary | Text | Key outcomes and decisions |
| Action Items | Text | What needs to happen and who owns it |
| Next Meeting Date | Date | When the next meeting is scheduled |

### Recommended Views

1. **Table View** — Filter by Meeting Type and Project.
2. **Calendar View** — See all meetings across projects.
3. **Board View** — Group by Meeting Type.

---

## Subcontractor Register

Your approved subcontractor list with insurance, licensing, and induction tracking.

### Database Properties

| Property | Type | Options |
|----------|------|---------|
| Company Name | Title | Subcontractor company name |
| Trade | Select | Electrical / Plumbing / Concrete / Steel / Carpentry / Painting / Tiling / Glazing / Roofing / Demolition / Landscaping / Other |
| Contact Person | Text | Primary contact |
| Phone | Phone | Contact number |
| Email | Email | Contact email |
| ABN | Text | Australian Business Number |
| Insurance Expiry | Date | Public liability / WorkCover expiry |
| License Number | Text | Trade license or registration number |
| License Expiry | Date | License expiry date |
| Induction Status | Select | Pending / Complete / Expired |
| Approved | Checkbox | Approved to work on your projects |
| Notes | Text | Performance notes, capacity, etc. |

### Recommended Views

1. **Table View** — Sort by Trade. Filter by Approved = Yes.
2. **Board View** — Group by Induction Status. See who needs renewal.
3. **Filtered View** — "Expiring Soon" — Insurance or License Expiry within 30 days.

> **Compliance is non-negotiable:** An expired insurance policy or lapsed license is a ticking bomb. Set up Notion reminders on the Insurance Expiry and License Expiry dates — 30 days before expiry, chase the subbie for updated documents.

---

## Database Relationships Map

Here is how all databases connect:

```
                    PROJECTS (Central Hub)
                         |
        +--------+-------+-------+--------+--------+
        |        |       |       |        |        |
    Defects    RFIs  Variations Safety  Claims  Site Diary  Meetings
        |                         |
        +--- Subcontractors ------+
             (via Assigned To)
```

**Key Relations:**
- Every database links back to **Projects** (many-to-one)
- **Defects** reference **Subcontractors** via the Assigned To field
- **Progress Claims** reference **Subcontractors** via the Contractor field
- **RFIs** with cost impact should trigger **Variations**

---

## Formulas & Automations

### Useful Notion Formulas

**Days Until Due (Defects):**
```
dateBetween(prop("Date Due"), now(), "days")
```

**Overdue Flag (RFIs):**
```
if(and(prop("Status") == "Open", prop("Date Required") < now()), "OVERDUE", "")
```

**Net Variation Position (Projects rollup):**
```
Sum of Approved Variations - Sum of Rejected Variations
```

### Recommended Automations (Notion Automations)

1. **When** a Defect Status changes to "Closed" → **Set** Date Closed to today
2. **When** an RFI Date Required is within 3 days and Status is "Open" → **Send notification** to PM
3. **When** Insurance Expiry is within 30 days → **Send notification** to update records
4. **When** a new Site Diary entry is created → **Set** Prepared By to creator

---

## Templates Within Databases

### Defect Entry Template
Pre-filled template for new defect entries:
- Status: Open
- Priority: Medium (change as needed)
- Date Reported: Today
- Prompt text in Description: "Describe the defect. Include location, extent, and any relevant drawing references."

### Site Diary Entry Template
Pre-filled template for daily diary:
- Date: Today
- Weather: Fine (change as needed)
- Prompt text in each field to guide the Super through what to record

### RFI Template
Pre-filled template:
- Status: Open
- Date Submitted: Today
- Prompt in Description: "State the question clearly. Reference specific drawing numbers, specification clauses, or details that need clarification."

---

## Tips for Construction Teams

<details>
<summary><strong>Getting your Superintendent to actually use this</strong></summary>

The Super's buy-in makes or breaks any site system. Here is what works:

1. **Start with the Site Diary only.** Don't dump 9 databases on them Day 1.
2. **Make it faster than their current method.** If they're handwriting diaries, the template with pre-filled fields and dropdowns is already faster.
3. **Show them the search.** "Remember that concrete pour from 3 months ago? Here it is in 2 seconds."
4. **Use the Notion mobile app.** Supers live on site, not at a desk. The mobile app lets them log defects and diary entries from their phone.
5. **Don't make them enter data twice.** If it's in SiteOS, it doesn't need to go in another spreadsheet.

</details>

<details>
<summary><strong>Scaling from 1 project to 5+ projects</strong></summary>

SiteOS works for a single project but shines when you're running multiple projects:

1. **Dashboard filtered views** — Set up a master Dashboard with "All Projects" views, plus individual project pages with filtered views.
2. **Project Manager filter** — Use Person property on Projects and filter views by current user. Each PM sees only their projects.
3. **Weekly reporting** — Export Table Views to PDF for weekly client or management reports.
4. **Team workspace** — Create a Team page with links to each project's filtered views. New team member? Point them to their project page.

</details>

<details>
<summary><strong>What to track vs. what to skip</strong></summary>

Not everything belongs in SiteOS. Here is the line:

**Track in SiteOS:**
- Defects, RFIs, Variations, Safety Incidents, Progress Claims, Site Diary, Meetings, Subcontractor compliance

**Keep in your existing systems:**
- Detailed cost reporting (use your ERP/cost system — Procore, Presto, or Excel cost reports)
- Detailed construction program (use Primavera P6 or MS Project — Notion is not a scheduling tool)
- Document management (use Aconex, Procore, or SharePoint for formal document control)
- Procurement and purchase orders (use your finance system)

**SiteOS is your operational command center, not a replacement for specialist software.**

</details>

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 2026 | Initial release |

---

> **Built by a construction professional.** SiteOS was designed on real construction sites, managing real projects. Every database, every property, every view exists because it solved a real problem. If something doesn't work for you, it's a bug — reach out and I'll fix it.
