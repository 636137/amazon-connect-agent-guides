# Amazon Connect Agent Guides

Production-quality **Step-by-Step Guides** (Cards Views) for Amazon Connect agent desktops.

## Features

- ✅ Rich HTML tables with styled headers and color-coded rows
- ✅ Warning boxes with highlighted backgrounds  
- ✅ Checklists with checkbox indicators
- ✅ External resource links
- ✅ 4 action buttons per card
- ✅ Emoji-enhanced headings

## Live Demo

| Instance | Phone | Agent Login |
|----------|-------|-------------|
| **Treasury Connect** | +1 833-289-6602 | [Agent Workspace](https://treasury-connect-prod.my.connect.aws/agent-app-v2) |

## Files

```
├── README.md                    # This file
├── SKILL.md                     # Copilot skill documentation
├── cards_view_builder.py        # Python helper functions
├── reference_example.json       # Production IRS Agent Guide (5 cards)
└── irs-agent-views/
    ├── SETUP_GUIDE.md           # Amazon Connect configuration
    ├── irs_enhanced_cards.json  # Deployed cards JSON
    └── *.json                   # Individual card definitions
```

## Quick Start

### 1. Use the Skill

```
Use the cards-view-generator skill to create an agent guide for [your use case]
```

### 2. Deploy to Amazon Connect

```json
{
  "Type": "ShowView",
  "Parameters": {
    "ViewResource": {
      "Id": "arn:aws:connect:us-east-1:aws:view/cards"
    },
    "ViewData": { /* Generated JSON */ }
  }
}
```

**Important:** Use `aws` as account ID: `arn:aws:connect:REGION:aws:view/cards`

## Card Structure

```json
{
  "Summary": {
    "Id": "refund-status",
    "Icon": "document",
    "Heading": "💰 Refund Status Inquiry",
    "Status": "HIGH VOLUME",
    "Description": "Check refund status and timelines"
  },
  "Detail": {
    "Heading": "Refund Status Procedures",
    "Description": "Verify caller identity and check IDRS",
    "Sections": [
      {"TemplateString": "<h4>🔐 Auth</h4><ul><li>Full SSN</li></ul>"},
      {"TemplateString": "<h4>📊 Table</h4><table>...</table>"},
      {"TemplateString": "<h4>⚠️ Warning</h4><div style='background:#fff3cd;'>...</div>"},
      {"TemplateString": "<h4>🔗 Links</h4><a href='...'>Resource</a>"}
    ],
    "Actions": ["Open IDRS", "Send Letter", "Escalate", "Transfer"]
  }
}
```

## HTML Templates

### Styled Table
```html
<table style='width:100%; border-collapse:collapse;'>
  <tr style='background:#f0f0f0;'><th style='padding:8px;'>Header</th></tr>
  <tr style='background:#d4edda;'><td style='padding:8px;'>Success</td></tr>
  <tr style='background:#f8d7da;'><td style='padding:8px;'>Warning</td></tr>
</table>
```

### Warning Box
```html
<div style='background:#fff3cd; padding:10px; border-radius:5px;'>
  <b>STOP if:</b><ul><li>Condition</li></ul>
</div>
```

## Valid Icons

| Icon | Emoji | Use For |
|------|-------|---------|
| `document` | 📄 | Forms, records |
| `shield` | 🛡️ | Security, verification |
| `wallet` | 💳 | Payments, financial |
| `alert` | ⚠️ | Warnings, urgent |
| `home` | 🏠 | Household |
| `plus` | ➕ | Create new |

## Architecture

```
📞 Caller → Contact Flow → UpdateContactEventHooks (DefaultAgentUI)
                                    ↓
                           Agent accepts call
                                    ↓
                           Event Flow → ShowView
                                    ↓
                           📋 Cards appear in Agent Workspace
```

## License

MIT
