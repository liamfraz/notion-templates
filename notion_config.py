"""
Configuration and color mappings for Notion template visual design.
Defines select column detection, color assignments, and template themes.
"""

# Unsplash cover images (free-to-use, no auth needed for external URLs)
COVERS = {
    "siteos": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1500",
    "agentops": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1500",
    "consultant": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1500",
    "pm_os": "https://images.unsplash.com/photo-1611224923853-80b023f02d71?w=1500",
    "ai_sidehustle": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1500",
    "creator_os": "https://images.unsplash.com/photo-1611162616475-46b635cb6868?w=1500",
    "job_search": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1500",
    "youtube_calendar": "https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?w=1500",
    "tiktok_machine": "https://images.unsplash.com/photo-1611605698335-8b1569810432?w=1500",
    "creator_biz": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1500",
}

# Template color themes
THEMES = {
    "siteos": {
        "heading": "orange",
        "primary_callout": "orange_background",
        "info_callout": "yellow_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "agentops": {
        "heading": "purple",
        "primary_callout": "purple_background",
        "info_callout": "blue_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "consultant": {
        "heading": "blue",
        "primary_callout": "blue_background",
        "info_callout": "green_background",
        "success_callout": "green_background",
        "alert_callout": "yellow_background",
    },
    "pm_os": {
        "heading": "green",
        "primary_callout": "green_background",
        "info_callout": "blue_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "ai_sidehustle": {
        "heading": "pink",
        "primary_callout": "pink_background",
        "info_callout": "red_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "creator_os": {
        "heading": "yellow",
        "primary_callout": "yellow_background",
        "info_callout": "orange_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "job_search": {
        "heading": "blue",
        "primary_callout": "blue_background",
        "info_callout": "green_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "youtube_calendar": {
        "heading": "red",
        "primary_callout": "red_background",
        "info_callout": "orange_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "tiktok_machine": {
        "heading": "pink",
        "primary_callout": "pink_background",
        "info_callout": "purple_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
    "creator_biz": {
        "heading": "green",
        "primary_callout": "green_background",
        "info_callout": "blue_background",
        "success_callout": "green_background",
        "alert_callout": "red_background",
    },
}

# Semantic color mapping for select option values
STATUS_COLORS = {
    "active": "blue", "in progress": "blue", "investigating": "yellow",
    "complete": "green", "completed": "green", "done": "green", "closed": "green",
    "resolved": "green", "approved": "green", "paid": "green",
    "on hold": "yellow", "paused": "yellow", "pending": "yellow",
    "pending verification": "yellow", "under review": "yellow", "sent": "blue",
    "cancelled": "red", "rejected": "red", "overdue": "red",
    "draft": "gray", "not started": "gray", "past": "gray",
    "pre-construction": "gray", "defects": "yellow",
    "open": "blue", "responded": "green", "submitted": "blue",
    "development": "blue", "prospect": "green", "new lead": "gray",
    "qualified": "blue", "proposal sent": "yellow", "negotiation": "orange",
    "lost": "red", "success": "green", "partial": "yellow",
    "viral": "green", "posted": "green", "archived": "gray",
    "scripting": "blue", "filming": "blue", "editing": "yellow",
    "scheduled": "blue", "published": "green", "evergreen": "green",
    "idea": "gray", "thumbnail": "yellow",
    "trending": "green", "peak": "orange", "declining": "red",
    "growing": "blue", "new": "gray",
    "lead": "gray", "pitched": "blue", "negotiating": "yellow",
    "contracted": "blue", "delivered": "green", "invoiced": "yellow",
    "declined": "red", "skipped": "gray",
    "cold": "gray", "warm": "yellow", "hot": "orange",
    "active partner": "green", "past partner": "gray",
    "testing": "yellow", "winner": "green", "retired": "gray",
    "coming soon": "blue", "behind": "red", "ahead": "green",
    "on track": "green",
}

PRIORITY_COLORS = {
    "critical": "red", "high": "orange", "medium": "yellow",
    "low": "gray", "none": "default",
    "important": "yellow", "nice-to-have": "gray",
}

HEALTH_COLORS = {
    "healthy": "green", "green": "green",
    "at risk": "yellow", "amber": "yellow",
    "critical": "red", "red": "red",
}

PROFICIENCY_COLORS = {
    "expert": "green", "advanced": "blue",
    "intermediate": "yellow", "beginner": "gray",
}

# Rotating colors for general categories
CATEGORY_ROTATION = ["blue", "purple", "pink", "green", "orange", "brown", "red", "yellow", "gray"]

# Column names that should be select type (case-insensitive partial match)
SELECT_KEYWORDS = [
    "status", "priority", "type", "category", "health", "stage",
    "rating", "level", "phase", "severity", "state", "outcome",
    "source", "platform", "tool", "trade", "induction", "approved",
    "billable", "proficiency", "weather", "provider", "model",
    "rate type", "engagement", "claim type", "reason",
    "ai-specific", "cost (free/paid)",
    "effort", "growth rate", "roi rating", "performance rating",
    "content type", "potential", "round", "relationship",
    "resume version", "cover letter", "culture rating",
    "payment method", "payment status", "tax deductible",
    "hook type", "seo score", "seo potential", "competition",
    "search volume", "thumbnail status", "strategy",
    "niche", "relationship stage", "platform fit", "industry",
    "frequency", "quarter", "avg performance rating",
]


# Column names that should NEVER be select (dates, IDs, free text)
EXCLUDE_KEYWORDS = [
    "date", "expiry", "id", "number", "phone", "email", "abn",
    "address", "url", "link", "description", "notes", "summary", "client",
    "action", "agenda", "minutes", "prepared by", "reported by",
    "assigned to", "from", "to", "contact", "person", "name",
    "deliverables", "risks", "tags", "last used", "last contact",
    "last updated", "last modified", "last run", "first engaged",
    "created date", "resolved date", "submitted date", "approved date",
    "approved by", "responded", "workforce", "temperature",
    "amount", "cost", "budget", "standard rate", "discounted rate",
    "premium rate", "revenue", "payment",
    "hours", "tokens", "count", "impact", "%",
    "config location", "documentation", "version",
    "visitors", "materials", "plant on site", "attendees",
    "key activities", "delays", "safety observations",
    "root cause", "corrective action", "immediate action",
    "persons involved", "location", "subject", "response summary",
    "file/module", "estimated effort", "prompt text", "check item",
    "certification", "learning goal", "expected close",
    "company", "month", "brand", "followers", "views", "likes",
    "comments", "shares", "fee", "base salary", "equity", "sign-on",
    "glassdoor", "duration", "deadline", "target", "current",
    "content frequency", "monthly growth", "primary format",
    "salary range", "started", "role",
    "effort", "growth", "net profit", "engagement goal",
    "cover letter", "expenses",
    "hook text", "sound", "content ideas", "time slot",
    "day", "handle", "vendor", "contact name", "contact email",
    "invoice number", "paid date", "issue date", "due date",
    "launch date", "first spotted", "last updated",
    "posts using", "avg views when used", "times used",
    "units sold", "price", "deal value", "deal history",
    "target audience", "avg completion rate",
    "completion rate", "saves", "watch hours",
    "avg view duration", "impressions", "subscribers gained",
    "videos count", "total views", "target length",
]


def should_be_select(col_name, values):
    """Determine if a column should be select type based on name and data."""
    name_lower = col_name.lower().strip()

    # Exclude date-like, ID-like, and free-text columns
    for excl in EXCLUDE_KEYWORDS:
        if excl in name_lower:
            return False

    # Check if column name matches select keywords
    for kw in SELECT_KEYWORDS:
        if kw in name_lower:
            return True

    # Check data: short values that repeat (< 10 unique, all < 25 chars, no commas)
    unique = set(v.strip() for v in values if v.strip())
    if (1 < len(unique) <= 10
            and all(len(v) < 25 for v in unique)
            and all("," not in v for v in unique)):
        return True
    return False


def get_select_color(value, col_name=""):
    """Get the appropriate color for a select option value."""
    val_lower = value.lower().strip()
    name_lower = col_name.lower().strip()

    # Check specific mappings based on column context
    if any(kw in name_lower for kw in ["status", "stage", "state", "approved",
                                         "billable", "induction", "outcome"]):
        if val_lower in STATUS_COLORS:
            return STATUS_COLORS[val_lower]
        # Yes/No pattern
        if val_lower in ("yes", "true"):
            return "green"
        if val_lower in ("no", "false"):
            return "red"

    if any(kw in name_lower for kw in ["priority", "severity"]):
        if val_lower in PRIORITY_COLORS:
            return PRIORITY_COLORS[val_lower]

    if any(kw in name_lower for kw in ["health"]):
        if val_lower in HEALTH_COLORS:
            return HEALTH_COLORS[val_lower]

    if any(kw in name_lower for kw in ["proficiency", "level"]):
        if val_lower in PROFICIENCY_COLORS:
            return PROFICIENCY_COLORS[val_lower]

    # Check all semantic maps as fallback
    if val_lower in STATUS_COLORS:
        return STATUS_COLORS[val_lower]
    if val_lower in PRIORITY_COLORS:
        return PRIORITY_COLORS[val_lower]

    return None  # Will be assigned from rotation
