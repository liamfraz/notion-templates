"""
Import all 3 Notion templates with premium visual design.
Creates pages with covers, colored callouts, colored headings,
and databases with select properties with colored options.
"""

import csv
import os
import time
import requests
from notion_config import (
    COVERS, THEMES, CATEGORY_ROTATION,
    should_be_select, get_select_color,
)

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
PARENT_PAGE_ID = "31b44bd6-79ca-80ec-b416-d0814cb5b1cb"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# API Helpers
# ============================================================

def notion_request(method, endpoint, data=None, retries=3):
    """Make a Notion API request with retry logic."""
    for attempt in range(retries):
        resp = getattr(requests, method)(
            f"{BASE_URL}{endpoint}", headers=HEADERS, json=data
        )
        if resp.status_code == 429:
            wait = float(resp.headers.get("Retry-After", 1))
            print(f"  Rate limited, waiting {wait}s...")
            time.sleep(wait)
            continue
        if resp.status_code >= 400:
            print(f"  Error {resp.status_code}: {resp.text[:300]}")
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
        return resp.json()
    return None


def delete_child_pages(parent_id):
    """Archive all child pages/databases under a parent page."""
    result = notion_request("get", f"/blocks/{parent_id}/children?page_size=100")
    if not result:
        return
    for block in result.get("results", []):
        block_type = block.get("type")
        if block_type == "child_page":
            notion_request("patch", f"/pages/{block['id']}", {"archived": True})
            print(f"  Archived page: {block.get(block_type, {}).get('title', 'unknown')}")
            time.sleep(0.35)
        elif block_type == "child_database":
            notion_request("patch", f"/databases/{block['id']}", {"archived": True})
            print(f"  Archived db: {block.get(block_type, {}).get('title', 'unknown')}")
            time.sleep(0.35)


# ============================================================
# Visual Block Builders
# ============================================================

def toc_block():
    return {"object": "block", "type": "table_of_contents",
            "table_of_contents": {"color": "gray"}}


def divider():
    return {"object": "block", "type": "divider", "divider": {}}


def colored_heading(content, level=2, color="default"):
    h = f"heading_{level}"
    return {"object": "block", "type": h, h: {
        "rich_text": [{"text": {"content": content}}],
        "color": color, "is_toggleable": False,
    }}


def colored_callout(content, icon="💡", color="blue_background"):
    return {"object": "block", "type": "callout", "callout": {
        "icon": {"type": "emoji", "emoji": icon},
        "color": color,
        "rich_text": [{"text": {"content": content}}],
    }}


def quote_block(content, color="default"):
    return {"object": "block", "type": "quote", "quote": {
        "color": color,
        "rich_text": [{"text": {"content": content},
                       "annotations": {"italic": True}}],
    }}


def bulleted(content, color="default"):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"text": {"content": content}}],
                "color": color,
            }}


def text_block(content, color="default", bold=False):
    return {"object": "block", "type": "paragraph", "paragraph": {
        "rich_text": [{"text": {"content": content},
                       "annotations": {"bold": bold, "color": color}}],
    }}


# ============================================================
# Page & Database Creation
# ============================================================

def create_page(parent_id, title, icon, cover_url=None, children=None):
    """Create a Notion page with optional cover image."""
    data = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "icon": {"type": "emoji", "emoji": icon},
        "properties": {"title": [{"text": {"content": title}}]},
    }
    if cover_url:
        data["cover"] = {"type": "external", "external": {"url": cover_url}}
    if children:
        data["children"] = children[:100]
    result = notion_request("post", "/pages", data)
    if result:
        print(f"  Created page: {title}")
        if children and len(children) > 100:
            append_blocks(result["id"], children[100:])
    return result


def append_blocks(page_id, blocks):
    """Append blocks to a page in batches of 100."""
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i + 100]
        notion_request("patch", f"/blocks/{page_id}/children", {"children": batch})
        time.sleep(0.4)


def read_csv_file(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def create_database(parent_id, title, icon, csv_path):
    """Create a database with smart select detection and colored options."""
    headers, rows = read_csv_file(csv_path)
    if not headers:
        print(f"  Skipping empty CSV: {csv_path}")
        return None

    # Collect column values for select detection
    col_values = {h.strip(): [] for h in headers}
    for row in rows:
        for i, h in enumerate(headers):
            if i < len(row):
                col_values[h.strip()].append(row[i].strip())

    # Build properties with smart type detection
    properties = {}
    select_columns = {}  # track which columns are select
    for i, h in enumerate(headers):
        col_name = h.strip()
        if i == 0:
            properties[col_name] = {"title": {}}
            continue

        values = col_values.get(col_name, [])
        if should_be_select(col_name, values):
            # Filter out values with commas (Notion doesn't allow them in selects)
            unique_vals = sorted(set(v for v in values if v and "," not in v))
            if not unique_vals:
                properties[col_name] = {"rich_text": {}}
                continue
            options = []
            rotation_idx = 0
            for val in unique_vals:
                color = get_select_color(val, col_name)
                if color is None:
                    color = CATEGORY_ROTATION[rotation_idx % len(CATEGORY_ROTATION)]
                    rotation_idx += 1
                options.append({"name": val, "color": color})
            properties[col_name] = {"select": {"options": options}}
            select_columns[col_name] = True
        else:
            properties[col_name] = {"rich_text": {}}

    data = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "icon": {"type": "emoji", "emoji": icon},
        "title": [{"text": {"content": title}}],
        "properties": properties,
    }

    result = notion_request("post", "/databases", data)
    if not result:
        print(f"  Failed to create database: {title}")
        return None

    db_id = result["id"]
    print(f"  Created database: {title} ({len(rows)} rows, "
          f"{len(select_columns)} select cols)")

    # Add rows
    for row in rows[:10]:
        row_props = {}
        for i, h in enumerate(headers):
            col_name = h.strip()
            val = row[i].strip() if i < len(row) else ""
            if i == 0:
                row_props[col_name] = {"title": [{"text": {"content": val}}]}
            elif col_name in select_columns and val and "," not in val:
                row_props[col_name] = {"select": {"name": val}}
            else:
                row_props[col_name] = {"rich_text": [{"text": {"content": val}}]}
        notion_request("post", "/pages", {
            "parent": {"type": "database_id", "database_id": db_id},
            "properties": row_props,
        })
        time.sleep(0.35)

    return db_id


# ============================================================
# Template Builders
# ============================================================

def build_siteos(parent_id):
    print("\n🏗️  Building SiteOS (orange theme)...")
    theme = THEMES["siteos"]

    children = [
        toc_block(),
        divider(),
        quote_block("Your entire construction operation in one workspace. "
                     "Built by a construction professional with 3+ years at "
                     "Kane Constructions."),
        colored_callout(
            "SiteOS brings together projects, subcontractors, defects, RFIs, "
            "variations, safety, claims, diary, and meetings — all linked.",
            "🏗️", theme["primary_callout"]),
        divider(),
        colored_heading("Quick Start", 2, theme["heading"]),
        bulleted("Duplicate this template to your workspace"),
        bulleted("Review the 9 databases below — they contain sample data"),
        bulleted("Customise project details, subcontractor list, and categories"),
        bulleted("Delete sample data and start adding your own"),
        divider(),
        colored_heading("Databases", 2, theme["heading"]),
        colored_callout(
            "Each database contains realistic Australian construction project "
            "data. Status, Priority, and Category columns use colored select "
            "options for instant visual scanning.",
            "📊", theme["info_callout"]),
    ]

    page = create_page(parent_id, "SiteOS — Construction Project Command Center",
                       "🏗️", COVERS["siteos"], children)
    if not page:
        return
    page_id = page["id"]

    db_dir = os.path.join(BASE_DIR, "siteos", "databases")
    databases = [
        ("Projects", "📋", "projects.csv"),
        ("Subcontractors", "👷", "subcontractors.csv"),
        ("Defects & Snags", "🔍", "defects.csv"),
        ("RFIs", "❓", "rfis.csv"),
        ("Variations", "📝", "variations.csv"),
        ("Safety Incidents", "⚠️", "safety-incidents.csv"),
        ("Progress Claims", "💰", "progress-claims.csv"),
        ("Site Diary", "📖", "site-diary.csv"),
        ("Meetings", "🤝", "meetings.csv"),
    ]

    for title, icon, csv_file in databases:
        csv_path = os.path.join(db_dir, csv_file)
        if os.path.exists(csv_path):
            append_blocks(page_id, [
                colored_heading(title, 3, theme["heading"]),
            ])
            create_database(page_id, title, icon, csv_path)
            time.sleep(0.5)

    append_blocks(page_id, [
        divider(),
        colored_heading("Setup Guide", 2, theme["heading"]),
        colored_callout(
            "For detailed setup instructions including database relations, "
            "formula configurations, and team rollout strategy, see the "
            "SETUP-GUIDE.md file.", "📚", theme["info_callout"]),
        colored_heading("Pricing", 2, theme["heading"]),
        colored_callout(
            "SiteOS — $99 AUD (one-time). Includes all 9 databases, "
            "free updates, and setup support.", "💲", theme["success_callout"]),
    ])
    print("  ✅ SiteOS complete!")
    return page_id


def build_agentops(parent_id):
    print("\n🤖 Building AgentOps (purple theme)...")
    theme = THEMES["agentops"]

    children = [
        toc_block(),
        divider(),
        quote_block("The first Notion workspace built specifically for tracking "
                     "AI agent operations. Zero competition on Notion Marketplace."),
        colored_callout(
            "Track your AI sessions, automation flows, API costs, and prompt "
            "library in one workspace. Built for developers who ship with AI.",
            "🤖", theme["primary_callout"]),
        divider(),
        colored_heading("Quick Start", 2, theme["heading"]),
        bulleted("Review the databases below — they contain realistic sample data"),
        bulleted("Start logging your Claude Code, ChatGPT, and Copilot sessions"),
        bulleted("Track API costs across providers monthly"),
        bulleted("Build your prompt library with ratings and version history"),
        divider(),
        colored_heading("Databases", 2, theme["heading"]),
        colored_callout(
            "Each database is pre-loaded with sample data. Tool, Model, Status, "
            "and Category columns use colored select options.",
            "⚡", theme["info_callout"]),
    ]

    page = create_page(parent_id, "AgentOps — AI Agent & Automation Dashboard",
                       "🤖", COVERS["agentops"], children)
    if not page:
        return
    page_id = page["id"]

    db_dir = os.path.join(BASE_DIR, "agentops", "databases")
    databases = [
        ("AI Sessions", "🧠", "ai-sessions.csv"),
        ("Prompt Library", "📝", "prompt-library.csv"),
        ("Automation Flows", "⚡", "automation-flows.csv"),
        ("API Costs", "💵", "api-costs.csv"),
        ("Code Review Checklist", "✅", "code-review-checklist.csv"),
        ("Tech Debt Log", "🔧", "tech-debt.csv"),
        ("Tool Registry", "🛠️", "tool-registry.csv"),
    ]

    for title, icon, csv_file in databases:
        csv_path = os.path.join(db_dir, csv_file)
        if os.path.exists(csv_path):
            append_blocks(page_id, [
                colored_heading(title, 3, theme["heading"]),
            ])
            create_database(page_id, title, icon, csv_path)
            time.sleep(0.5)

    append_blocks(page_id, [
        divider(),
        colored_heading("Monthly Ops Report", 2, theme["heading"]),
        colored_callout(
            "At the end of each month, review: total sessions, API spend vs "
            "budget, prompt library growth, automation error rates, and tech "
            "debt trend.", "📊", theme["info_callout"]),
        colored_heading("Pricing", 2, theme["heading"]),
        colored_callout(
            "AgentOps — $29 AUD (intro) / $49 AUD (full). First-mover in "
            "AI operations tracking.", "💲", theme["success_callout"]),
    ])
    print("  ✅ AgentOps complete!")
    return page_id


def build_consultant_os(parent_id):
    print("\n💼 Building Consultant OS (blue theme)...")
    theme = THEMES["consultant"]

    children = [
        toc_block(),
        divider(),
        quote_block("Run your consulting business from one workspace. "
                     "Pays for itself in 12 minutes at $250/hr."),
        colored_callout(
            "Client pipeline, project delivery, time tracking, invoicing, "
            "and knowledge base — designed for technical professionals.",
            "💼", theme["primary_callout"]),
        divider(),
        colored_heading("Quick Start", 2, theme["heading"]),
        bulleted("Review the sample clients, projects, and time entries below"),
        bulleted("Set up your rate card with your actual rates"),
        bulleted("Import existing clients into the CRM database"),
        bulleted("Start logging time against projects"),
        divider(),
        colored_heading("Databases", 2, theme["heading"]),
        colored_callout(
            "All databases use AUD currency with realistic Australian consulting "
            "rates ($200-$450/hr). Pipeline Stage, Invoice Status, and Health "
            "Score use colored select options.",
            "💰", theme["info_callout"]),
    ]

    page = create_page(parent_id, "Technical Consultant OS",
                       "💼", COVERS["consultant"], children)
    if not page:
        return
    page_id = page["id"]

    db_dir = os.path.join(BASE_DIR, "consultant-os", "databases")
    databases = [
        ("Client CRM", "🏢", "clients.csv"),
        ("Lead Pipeline", "🎯", "leads.csv"),
        ("Projects", "📋", "projects.csv"),
        ("Time Entries", "⏱️", "time-entries.csv"),
        ("Invoices", "🧾", "invoices.csv"),
        ("Rate Card", "💳", "rate-card.csv"),
        ("Knowledge Base", "📚", "knowledge-base.csv"),
        ("Skills Matrix", "🎓", "skills.csv"),
    ]

    for title, icon, csv_file in databases:
        csv_path = os.path.join(db_dir, csv_file)
        if os.path.exists(csv_path):
            append_blocks(page_id, [
                colored_heading(title, 3, theme["heading"]),
            ])
            create_database(page_id, title, icon, csv_path)
            time.sleep(0.5)

    append_blocks(page_id, [
        divider(),
        colored_heading("SOW Template", 2, theme["heading"]),
        colored_callout(
            "A full Statement of Work template with a worked example "
            "(Power Automate Expense Claims Implementation, $28,000 "
            "engagement) is included.", "📄", theme["info_callout"]),
        colored_heading("Monthly Business Review", 2, theme["heading"]),
        colored_callout(
            "Monthly review template covering revenue, client health, "
            "pipeline, utilisation, and P&L.", "📊", theme["info_callout"]),
        colored_heading("Pricing", 2, theme["heading"]),
        colored_callout(
            "Technical Consultant OS — $49 AUD (one-time). Pays for itself "
            "in 12 minutes at $250/hr.", "💲", theme["success_callout"]),
    ])
    print("  ✅ Consultant OS complete!")
    return page_id


def build_pm_os(parent_id):
    print("\n📋 Building PM OS (green theme)...")
    theme = THEMES["pm_os"]

    children = [
        toc_block(),
        divider(),
        quote_block("Your projects are scattered across Jira, Asana, spreadsheets, "
                     "and Slack threads. PM OS fixes that."),
        colored_callout(
            "8 connected databases covering projects, tasks, risks, decisions, "
            "stakeholders, goals, weekly reviews, and meeting notes — built by "
            "a PM who actually manages projects.",
            "📋", theme["primary_callout"]),
        divider(),
        colored_heading("Quick Start", 2, theme["heading"]),
        bulleted("Review the 8 databases below — they contain realistic sample data"),
        bulleted("Connect databases with relations using the Setup Guide"),
        bulleted("Run your first weekly review to see everything surface automatically"),
        bulleted("Delete sample data and start adding your own projects"),
        divider(),
        colored_heading("Databases", 2, theme["heading"]),
        colored_callout(
            "Every database is pre-loaded with sample data from a realistic "
            "multi-project portfolio. Status, Priority, Health, and Type columns "
            "use colored select options for instant visual scanning.",
            "📊", theme["info_callout"]),
    ]

    page = create_page(parent_id, "PM OS — Project Manager Personal OS",
                       "📋", COVERS["pm_os"], children)
    if not page:
        return
    page_id = page["id"]

    db_dir = os.path.join(BASE_DIR, "pm-os", "databases")
    databases = [
        ("Projects", "📁", "projects.csv"),
        ("Tasks", "✅", "tasks.csv"),
        ("Goals", "🎯", "goals.csv"),
        ("Weekly Reviews", "📝", "weekly-reviews.csv"),
        ("Meeting Notes", "🤝", "meeting-notes.csv"),
        ("Stakeholders", "👥", "stakeholders.csv"),
        ("Risks", "⚠️", "risks.csv"),
        ("Decisions", "⚖️", "decisions.csv"),
    ]

    for title, icon, csv_file in databases:
        csv_path = os.path.join(db_dir, csv_file)
        if os.path.exists(csv_path):
            append_blocks(page_id, [
                colored_heading(title, 3, theme["heading"]),
            ])
            create_database(page_id, title, icon, csv_path)
            time.sleep(0.5)

    append_blocks(page_id, [
        divider(),
        colored_heading("Weekly Review System", 2, theme["heading"]),
        colored_callout(
            "Every Friday: run through overdue tasks, escalating risks, "
            "pending decisions, and stakeholder updates. Everything surfaces "
            "automatically — no digging required.",
            "🔄", theme["info_callout"]),
        colored_heading("Pricing", 2, theme["heading"]),
        colored_callout(
            "PM OS — $49 AUD (one-time). 8 databases, 3 dashboards, "
            "setup guide, and free updates.",
            "💲", theme["success_callout"]),
    ])
    print("  ✅ PM OS complete!")
    return page_id


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Notion Template Visual Redesign")
    print("=" * 50)

    print("\nStep 1: Cleaning up existing pages...")
    delete_child_pages(PARENT_PAGE_ID)

    print("\nStep 2: Building redesigned templates...")
    build_siteos(PARENT_PAGE_ID)
    build_agentops(PARENT_PAGE_ID)
    build_consultant_os(PARENT_PAGE_ID)
    build_pm_os(PARENT_PAGE_ID)

    print("\n" + "=" * 50)
    print("✅ All 4 templates redesigned with visual enhancements!")
    print("Features added: covers, colored callouts, colored headings,")
    print("select properties with colored options, TOC, quote blocks.")
    print("Open Notion and check your pages.")
    print("=" * 50)
