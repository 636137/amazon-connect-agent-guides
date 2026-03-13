#!/usr/bin/env python3
"""
Cards View JSON Generator - Enhanced Version
Generates production-quality Amazon Connect Cards View JSON with rich HTML content,
tables, action buttons, links, and warning boxes.

Reference: IRS Agent Guide implementation (irs_enhanced_cards.json)
"""

import json
from typing import Optional, List, Dict

VALID_ICONS = ["plus", "home", "alert", "wallet", "document", "shield"]
VALID_LINK_TYPES = ["case", "external"]

# Emoji mapping for icons
ICON_EMOJIS = {
    "plus": "➕",
    "home": "🏠",
    "alert": "⚠️",
    "wallet": "💳",
    "document": "📄",
    "shield": "🛡️"
}

# Section heading emojis
SECTION_EMOJIS = {
    "auth": "🔐",
    "steps": "📋",
    "table": "📊",
    "time": "⏱️",
    "warning": "⚠️",
    "links": "🔗",
    "checklist": "✅",
    "info": "ℹ️",
    "money": "💵",
    "phone": "📞",
    "email": "📧",
    "calendar": "📅"
}


def generate_enhanced_cards_view(
    heading: str,
    sub_heading: str = "",
    cards: Optional[List[Dict]] = None,
    attribute_bar: Optional[List[Dict]] = None
) -> dict:
    """Generate production-quality Cards View JSON."""
    
    result = {
        "Heading": heading,
        "CardsPerRow": "1"  # Always 1 for detailed guides
    }
    
    if sub_heading:
        result["SubHeading"] = sub_heading
    
    if attribute_bar:
        result["AttributeBar"] = attribute_bar
    
    result["Cards"] = cards if cards else []
    
    return result


def create_styled_table(
    title: str,
    headers: List[str],
    rows: List[List[str]],
    highlight_rows: Optional[Dict[int, str]] = None,
    emoji: str = "📊"
) -> str:
    """Create an HTML table with styling.
    
    Args:
        title: Section heading
        headers: List of column headers
        rows: List of row data (each row is a list of cell values)
        highlight_rows: Dict mapping row index to background color
                       (e.g., {0: '#d4edda'} for green, {2: '#f8d7da'} for red)
        emoji: Emoji for section heading
    """
    html = f"<h4>{emoji} {title}</h4>"
    html += "<table style='width:100%; border-collapse:collapse;'>"
    
    # Header row
    html += "<tr style='background:#f0f0f0;'>"
    for i, header in enumerate(headers):
        align = "text-align:left;" if i == 0 else ""
        html += f"<th style='padding:8px; {align}'>{header}</th>"
    html += "</tr>"
    
    # Data rows
    highlight_rows = highlight_rows or {}
    for i, row in enumerate(rows):
        bg = f"background:{highlight_rows[i]};" if i in highlight_rows else ""
        html += f"<tr style='{bg}'>"
        for cell in row:
            html += f"<td style='padding:8px;'>{cell}</td>"
        html += "</tr>"
    
    html += "</table>"
    return html


def create_warning_box(
    title: str,
    items: List[str],
    prefix: str = "STOP if:"
) -> str:
    """Create a warning box with yellow background."""
    html = f"<h4>⚠️ {title}</h4>"
    html += "<div style='background:#fff3cd; padding:10px; border-radius:5px;'>"
    html += f"<b>{prefix}</b>"
    html += "<ul style='margin:5px 0;'>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul></div>"
    return html


def create_checklist(
    title: str,
    items: List[str],
    emoji: str = "✅"
) -> str:
    """Create a checklist with checkbox indicators."""
    html = f"<h4>{emoji} {title}</h4>"
    html += "<ul>"
    for item in items:
        html += f"<li>☐ {item}</li>"
    html += "</ul>"
    return html


def create_bullet_list(
    title: str,
    items: List[str],
    emoji: str = "📋"
) -> str:
    """Create a bulleted list."""
    html = f"<h4>{emoji} {title}</h4>"
    html += "<ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return html


def create_numbered_list(
    title: str,
    items: List[str],
    emoji: str = "📋"
) -> str:
    """Create a numbered/ordered list."""
    html = f"<h4>{emoji} {title}</h4>"
    html += "<ol>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ol>"
    return html


def create_links_section(
    title: str,
    links: List[Dict[str, str]],
    emoji: str = "🔗"
) -> str:
    """Create a section with external links.
    
    Args:
        links: List of dicts with 'text' and 'url' keys
    """
    html = f"<h4>{emoji} {title}</h4>"
    for link in links:
        html += f"<p><a href='{link['url']}' target='_blank'>{link['text']}</a></p>"
    return html


def create_enhanced_card(
    card_id: str,
    icon: str,
    heading: str,
    status: str = "",
    description: str = "",
    detail_heading: str = "",
    detail_description: str = "",
    sections: Optional[List[str]] = None,
    actions: Optional[List[str]] = None
) -> dict:
    """Create a fully enhanced card with summary and detail sections.
    
    Args:
        card_id: Unique identifier (kebab-case recommended)
        icon: One of: plus, home, alert, wallet, document, shield
        heading: Card title (emoji will be added automatically)
        status: Status badge text (e.g., "HIGH VOLUME", "REQUIRED")
        description: Brief one-line description
        detail_heading: Heading for detail panel
        detail_description: Context description for detail panel
        sections: List of HTML template strings (use helper functions)
        actions: List of action button labels (4 recommended)
    """
    
    # Validate and default icon
    if icon not in VALID_ICONS:
        icon = "document"
    
    # Add emoji to heading if not present
    emoji = ICON_EMOJIS.get(icon, "📄")
    if not any(e in heading for e in ICON_EMOJIS.values()):
        heading = f"{emoji} {heading}"
    
    card = {
        "Summary": {
            "Id": card_id,
            "Icon": icon,
            "Heading": heading,
            "Status": status,
            "Description": description
        },
        "Detail": {
            "Heading": detail_heading or heading.replace(emoji, "").strip(),
            "Description": detail_description,
            "Sections": [{"TemplateString": s} for s in (sections or [])],
            "Actions": actions or []
        }
    }
    
    return card


def create_attribute_entry(
    label: str,
    value: str,
    link_type: Optional[str] = None,
    resource_id: Optional[str] = None,
    url: Optional[str] = None,
    copyable: bool = False
) -> dict:
    """Create an attribute bar entry."""
    
    entry = {
        "Label": label,
        "Value": value
    }
    
    if link_type == "case" and resource_id:
        entry["LinkType"] = "case"
        entry["ResourceId"] = resource_id
        entry["Copyable"] = copyable
    elif link_type == "external" and url:
        entry["LinkType"] = "external"
        entry["Url"] = url
    elif copyable:
        entry["Copyable"] = copyable
    
    return entry


def validate_enhanced_cards_view(data: dict) -> List[str]:
    """Validate enhanced Cards View JSON and return list of errors."""
    
    errors = []
    
    # Required: Heading
    if not data.get("Heading"):
        errors.append("Heading is required")
    
    # Required: Cards array
    if not data.get("Cards") or len(data["Cards"]) == 0:
        errors.append("At least one card is required")
    
    # Validate CardsPerRow
    cpr = data.get("CardsPerRow", "1")
    if cpr not in ["1", "2", "3"]:
        errors.append(f"CardsPerRow must be 1, 2, or 3 (got: {cpr})")
    
    # Validate cards
    card_ids = set()
    for i, card in enumerate(data.get("Cards", [])):
        summary = card.get("Summary", {})
        detail = card.get("Detail", {})
        
        # Required: Id
        card_id = summary.get("Id")
        if not card_id:
            errors.append(f"Card {i+1}: Id is required")
        elif card_id in card_ids:
            errors.append(f"Card {i+1}: Duplicate Id '{card_id}'")
        else:
            card_ids.add(card_id)
        
        # Validate icon
        icon = summary.get("Icon", "")
        if icon and icon not in VALID_ICONS:
            errors.append(f"Card {i+1}: Invalid icon '{icon}'. Valid: {VALID_ICONS}")
        
        # Recommend minimum sections
        sections = detail.get("Sections", [])
        if len(sections) < 3:
            errors.append(f"Card {i+1}: Recommend at least 3 sections (has {len(sections)})")
        
        # Recommend minimum actions
        actions = detail.get("Actions", [])
        if len(actions) < 3:
            errors.append(f"Card {i+1}: Recommend at least 3 actions (has {len(actions)})")
    
    return errors


def format_json_output(data: dict) -> str:
    """Format JSON with proper indentation."""
    return json.dumps(data, indent=2, ensure_ascii=False)


# Example: Generate IRS-style enhanced cards
if __name__ == "__main__":
    # Build example IRS card
    refund_card = create_enhanced_card(
        card_id="refund-status",
        icon="document",
        heading="Refund Status Inquiry",
        status="HIGH VOLUME",
        description="Check refund status, timelines, and IDRS codes",
        detail_heading="Refund Status Procedures",
        detail_description="Verify caller identity and check refund status in IDRS",
        sections=[
            create_bullet_list(
                "Authentication Required",
                [
                    "Full SSN (last 4 not sufficient)",
                    "Date of Birth",
                    "Filing Status (Single/MFJ/MFS/HOH)",
                    "Exact refund amount from return"
                ],
                emoji="🔐"
            ),
            create_styled_table(
                "Processing Times",
                ["Type", "Timeline"],
                [
                    ["E-file + Direct Deposit", "<b>21 days</b>"],
                    ["E-file + Paper Check", "4-6 weeks"],
                    ["Paper Return", "6-8 weeks"],
                    ["Amended (1040-X)", "16-20 weeks"]
                ],
                highlight_rows={0: "#d4edda"},
                emoji="⏱️"
            ),
            create_links_section(
                "Resources",
                [
                    {"text": "Where's My Refund (IRS.gov)", "url": "https://www.irs.gov/refunds"},
                    {"text": "IRM Part 21", "url": "https://www.irs.gov/irm/part21"}
                ]
            )
        ],
        actions=[
            "Open IDRS IMFOL",
            "Send Refund Status Letter",
            "Escalate to Supervisor",
            "Transfer to Refund Hotline"
        ]
    )
    
    result = generate_enhanced_cards_view(
        heading="IRS Taxpayer Services",
        sub_heading="Agent Quick Reference Guide",
        cards=[refund_card]
    )
    
    errors = validate_enhanced_cards_view(result)
    if errors:
        print("Validation warnings:")
        for e in errors:
            print(f"  - {e}")
        print()
    
    print(format_json_output(result))
