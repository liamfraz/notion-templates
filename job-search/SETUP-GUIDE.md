# Job Search CRM 2026 -- Setup Guide

Get your job search dashboard running in your Notion workspace in about 20 minutes.

---

## Step 1: Import the Main Template

1. Open Notion and navigate to your workspace sidebar
2. Click **Import** (at the bottom of the sidebar)
3. Select **Markdown** and upload `job-search-main.md`
4. Notion will create a new page with all the sections

Alternatively, create a new page and paste the markdown content directly.

---

## Step 2: Create Databases from CSVs

For each CSV file in the `databases/` folder, create a Notion database:

### Applications Database

1. In Notion, create a new **Full-page database**
2. Name it `Applications`
3. Click the `...` menu at the top right of the database
4. Select **Merge with CSV** and upload `databases/applications.csv`
5. Set column types:
   - Company: `Title`
   - Role: `Text`
   - Status: `Select` (options: Applied, Screening, Phone Screen, Technical Interview, Onsite, Offer, Rejected, Withdrawn, Ghosted)
   - Applied Date: `Date`
   - Source: `Select` (options: LinkedIn, Company Website, Referral, Indeed, Glassdoor, Recruiter Outreach, Networking Event)
   - Salary Range: `Text`
   - Location: `Select` (options: Sydney, Melbourne, Remote (AU), Remote (Global), and add others as needed)
   - Type: `Select` (options: Full-time, Contract, Remote, Hybrid, On-site)
   - Resume Version: `Text`
   - Cover Letter: `Select` (options: Yes, No)
   - Priority: `Select` (options: Dream Job, Strong Fit, Good Option, Safety Net, Practice)

### Interviews Database

1. Create a new **Full-page database** named `Interviews`
2. Merge with `databases/interviews.csv`
3. Set column types:
   - Company: `Title`
   - Round: `Select` (options: Phone Screen, Technical 1, Technical 2, System Design, Behavioral, Culture Fit, Final, Hiring Manager)
   - Type: `Select` (options: Video Call, In-Person, Take-Home, Live Coding, Panel, Case Study)
   - Date: `Date`
   - Status: `Select` (options: Scheduled, Completed, Passed, Failed, Cancelled, No Show)
   - Duration (min): `Number`
   - Interviewer: `Text`
   - Prep Notes: `Text`
   - Outcome: `Select` (options: Advanced, Rejected, Pending, Offer Extended)
   - Follow-up: `Text`

### Contacts Database

1. Create a new **Full-page database** named `Contacts`
2. Merge with `databases/contacts.csv`
3. Set column types:
   - Name: `Title`
   - Company: `Text`
   - Role: `Text`
   - Relationship: `Select` (options: Recruiter, Hiring Manager, Referral, Mentor, Former Colleague, Alumni)
   - Last Contact: `Date`
   - Source: `Select` (options: LinkedIn, Meetup, Conference, Former Workplace, University)
   - Status: `Select` (options: Active, Warm, Cold, Follow Up, Connected)
   - Notes: `Text`
   - LinkedIn URL: `URL`

### Salary Research Database

1. Create a new **Full-page database** named `Salary Research`
2. Merge with `databases/salary-research.csv`
3. Set column types:
   - Company: `Title`
   - Role: `Text`
   - Level: `Select` (options: Junior, Mid, Senior, Staff, Principal, Lead, Manager)
   - Location: `Select`
   - Base Salary ($): `Number` (format: Australian Dollar)
   - Total Comp ($): `Number` (format: Australian Dollar)
   - Source: `Select` (options: Glassdoor, Levels.fyi, Blind, Recruiter Shared, Offer Letter, Industry Report)
   - Date Verified: `Date`
   - Notes: `Text`

### Offers Database

1. Create a new **Full-page database** named `Offers`
2. Merge with `databases/offers.csv`
3. Set column types:
   - Company: `Title`
   - Role: `Text`
   - Base Salary ($): `Number` (format: Australian Dollar)
   - Equity/RSU ($): `Number` (format: Australian Dollar)
   - Sign-on Bonus ($): `Number` (format: Australian Dollar)
   - Benefits: `Text`
   - PTO (days): `Number`
   - Status: `Select` (options: Pending, Negotiating, Accepted, Declined, Expired)
   - Deadline: `Date`
   - Notes: `Text`

### Companies Database

1. Create a new **Full-page database** named `Companies`
2. Merge with `databases/companies.csv`
3. Set column types:
   - Company: `Title`
   - Industry: `Select` (options: SaaS, FinTech, HealthTech, E-commerce, Consulting, Gov Tech, AI/ML)
   - Size: `Select` (options: Startup (1-50), Scale-up (50-500), Mid-market (500-5K), Enterprise (5K+))
   - Culture Rating: `Select` (options: Excellent, Good, Mixed, Unknown)
   - Glassdoor Score: `Number` (format: 1 decimal)
   - Tech Stack: `Text`
   - Location: `Select`
   - Status: `Select` (options: Researching, Applied, Interviewing, Offer, Rejected, Not Interested)
   - Priority: `Select` (options: Target, Interested, Maybe, Backup)
   - Notes: `Text`

---

## Step 3: Set Up Relations

Notion relations link databases together. Set up these connections:

### Applications <-> Companies
1. Open the Applications database
2. Add a new `Relation` property pointing to `Companies`
3. Name it "Company Details"
4. This lets you click through from an application to see full company research

### Applications <-> Interviews
1. Open the Applications database
2. Add a new `Relation` property pointing to `Interviews`
3. Name it "Interview Rounds"
4. Link applications to their interview rounds for a complete timeline

### Applications <-> Contacts
1. Open the Applications database
2. Add a new `Relation` property pointing to `Contacts`
3. Name it "Related Contacts"
4. Track which contacts helped with each application (referrals, hiring managers)

### Offers <-> Applications
1. Open the Offers database
2. Add a new `Relation` property pointing to `Applications`
3. Name it "Application"
4. Link each offer back to its application for the full journey

### Salary Research <-> Companies
1. Open the Salary Research database
2. Add a new `Relation` property pointing to `Companies`
3. Name it "Company Info"
4. Cross-reference salary data with company details

---

## Step 4: Link Databases to the Main Page

1. Go back to the main Job Search CRM page
2. In each section that says "Create a linked database view here", type `/linked` and select **Create linked view of database**
3. Point each linked view to the appropriate database
4. Set up the recommended views listed in each section (filters, sorts, grouping)

### Recommended Dashboard Layout

For the Mission Control section:
- Create a **Board view** of Applications grouped by Status (Kanban-style pipeline)
- Create a **Calendar view** of Interviews showing upcoming dates
- Create a **List view** of Contacts filtered to Status = Follow Up

---

## Step 5: Set Up Weekly Review Routine

1. Create a recurring calendar event: **Sunday 30 min -- Job Search Review**
2. In the Weekly Review section of the main page, duplicate the template each week
3. Fill in your numbers, wins, setbacks, and next week's focus
4. Update the Mission Control metrics at the top of the page

---

## Tips

- **Start with Applications and Contacts.** These are the most immediately useful. Add Salary Research and Offers when you need them.
- **Update daily.** Spend 5 minutes at the end of each day logging any changes. Stale data is useless data.
- **Use the Kanban board view.** Seeing your applications as a pipeline (Applied -> Screening -> Interview -> Offer) is motivating and informative.
- **Track the source.** After 20+ applications, you'll see which sources (LinkedIn, referrals, direct) actually lead to interviews. Double down on what works.
- **Be honest with yourself.** If a company has ghosted you for 3 weeks, mark it Ghosted and move on. Don't let phantom applications inflate your pipeline.
- **Review offers holistically.** The highest salary isn't always the best offer. Use the comparison framework to weigh all factors.

---

*Questions? Feature requests? Reach out on X or open an issue.*
