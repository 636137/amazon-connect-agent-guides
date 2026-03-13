# Cards View JSON Generator

Generate **production-quality** Amazon Connect Cards View JSON for agent step-by-step guides with rich interactive content.

## Features

- ✅ Rich HTML tables with styled headers and color-coded rows
- ✅ Warning boxes with highlighted backgrounds
- ✅ Checklists with checkbox indicators
- ✅ External resource links
- ✅ 4 action buttons per card
- ✅ Emoji-enhanced headings
- ✅ Automatic validation

## Quick Start

Invoke the skill by saying:
```
Use the cards-view-generator skill to create an enhanced dashboard for [use case]
```

Or:
```
Generate Cards View with tables and action buttons for IRS agents
```

## Quality Standard

All generated cards match the **IRS Agent Guide** implementation standard with:
- 4 HTML sections per card (procedures, tables, warnings, links)
- 4 action buttons per card
- Styled tables with highlighted rows
- Warning/alert boxes
- External resource links

See `reference_example.json` for the full enhanced format.

## Enhanced JSON Structure

```json
{
  "Heading": "IRS Taxpayer Services",
  "SubHeading": "Agent Quick Reference Guide",
  "CardsPerRow": "1",
  "Cards": [
    {
      "Summary": {
        "Id": "refund-status",
        "Icon": "document",
        "Heading": "💰 Refund Status Inquiry",
        "Status": "HIGH VOLUME",
        "Description": "Check refund status, timelines, and IDRS codes"
      },
      "Detail": {
        "Heading": "Refund Status Procedures",
        "Description": "Verify caller identity and check refund status in IDRS",
        "Sections": [
          {"TemplateString": "<h4>🔐 Authentication</h4><ul><li>Full SSN</li><li>DOB</li></ul>"},
          {"TemplateString": "<h4>📊 Timelines</h4><table style='...'><tr>...</tr></table>"},
          {"TemplateString": "<h4>⚠️ Warning</h4><div style='background:#fff3cd;'>...</div>"},
          {"TemplateString": "<h4>🔗 Links</h4><a href='...' target='_blank'>IRS.gov</a>"}
        ],
        "Actions": ["Open IDRS", "Send Letter", "Escalate", "Transfer"]
      }
    }
  ]
}
```

## HTML Templates

### Styled Table
```html
<table style='width:100%; border-collapse:collapse;'>
  <tr style='background:#f0f0f0;'><th style='padding:8px;'>Header</th></tr>
  <tr style='background:#d4edda;'><td style='padding:8px;'>Success row</td></tr>
  <tr style='background:#f8d7da;'><td style='padding:8px;'>Warning row</td></tr>
</table>
```

### Warning Box
```html
<div style='background:#fff3cd; padding:10px; border-radius:5px;'>
  <b>STOP if:</b><ul><li>Condition 1</li></ul>
</div>
```

### Resource Links
```html
<a href='https://example.com' target='_blank'>Link Text</a>
```

## Valid Icons

| Icon | Emoji | Use For |
|------|-------|---------|
| `document` | 📄 | Forms, records, transcripts |
| `shield` | 🛡️ | Security, verification, compliance |
| `wallet` | 💳 | Payments, financial |
| `alert` | ⚠️ | Warnings, urgent items |
| `home` | 🏠 | Household, residence |
| `plus` | ➕ | Create, add new |

## Files

- `SKILL.md` - Full skill documentation with all templates
- `cards_view_builder.py` - Python helper functions
- `reference_example.json` - Production example (IRS Agent Guide)
- `README.md` - This file

## Deployment

Use with AWS managed Cards view:

```json
{
  "ViewResource": {
    "Id": "arn:aws:connect:REGION:aws:view/cards"
  },
  "ViewData": { /* generated JSON */ }
}
```

**Important:** Use `aws` as account ID for managed views: `arn:aws:connect:us-east-1:aws:view/cards`
