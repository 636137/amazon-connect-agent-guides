---
name: cards-view-generator
description: Interactive wizard to generate Amazon Connect Cards View JSON for agent dashboards with rich HTML content, tables, action buttons, links, and warning boxes.
user-invocable: true
disable-model-invocation: false
---

# Cards View JSON Generator Skill

Generate **production-quality** Amazon Connect Cards View JSON with rich interactive elements through a guided workflow.

## Purpose

This skill creates enterprise-grade agent desktop Cards Views matching the quality standard of the IRS Agent Guide implementation. It produces cards with:
- Rich HTML tables with styled headers and rows
- Ordered/unordered procedural lists
- Warning boxes with highlighted backgrounds
- Clickable external links to resources
- Multiple action buttons per card
- Checklists with checkbox indicators

## Quality Standard

All generated cards MUST match this enhanced format (see reference: `irs_enhanced_cards.json`):

```json
{
  "Heading": "Dashboard Title",
  "SubHeading": "Optional subtitle",
  "CardsPerRow": "1",
  "Cards": [
    {
      "Summary": {
        "Id": "unique-id",
        "Icon": "document",
        "Heading": "💰 Card Title with Emoji",
        "Status": "HIGH VOLUME",
        "Description": "Brief one-line description"
      },
      "Detail": {
        "Heading": "Detailed Procedures",
        "Description": "Context for this guide section",
        "Sections": [
          {
            "TemplateString": "<h4>🔐 Section Heading</h4><ul><li>Bullet point 1</li><li>Bullet point 2</li></ul>"
          },
          {
            "TemplateString": "<h4>📊 Reference Table</h4><table style='width:100%; border-collapse:collapse;'><tr style='background:#f0f0f0;'><th style='padding:8px;'>Column 1</th><th style='padding:8px;'>Column 2</th></tr><tr><td style='padding:8px;'>Data</td><td style='padding:8px;'>Value</td></tr></table>"
          },
          {
            "TemplateString": "<h4>⚠️ Warning</h4><div style='background:#fff3cd; padding:10px; border-radius:5px;'><b>Important:</b> Warning text here</div>"
          },
          {
            "TemplateString": "<h4>🔗 Resources</h4><p><a href='https://example.com' target='_blank'>External Link Text</a></p>"
          }
        ],
        "Actions": ["Primary Action", "Secondary Action", "Escalate", "Transfer"]
      }
    }
  ]
}
```

## Required Elements Per Card

Each card MUST include:

1. **Summary** with emoji in heading and status badge
2. **4 Detail Sections** minimum:
   - Procedural steps (numbered or bulleted list)
   - Reference table with styled rows
   - Warning/alert box OR checklist
   - Resource links section
3. **4 Action Buttons** for agent workflows

## HTML Templates

### Styled Table
```html
<h4>📊 Reference Data</h4>
<table style='width:100%; border-collapse:collapse;'>
  <tr style='background:#f0f0f0;'>
    <th style='padding:8px; text-align:left;'>Header 1</th>
    <th style='padding:8px;'>Header 2</th>
  </tr>
  <tr>
    <td style='padding:8px;'>Cell 1</td>
    <td style='padding:8px;'>Cell 2</td>
  </tr>
  <tr style='background:#d4edda;'>
    <td style='padding:8px;'><b>Highlighted Row</b></td>
    <td style='padding:8px;'>Success indicator</td>
  </tr>
  <tr style='background:#f8d7da;'>
    <td style='padding:8px;'><b>Warning Row</b></td>
    <td style='padding:8px;'>Requires attention</td>
  </tr>
</table>
```

### Warning Box
```html
<h4>⚠️ Important Notice</h4>
<div style='background:#fff3cd; padding:10px; border-radius:5px;'>
  <b>STOP if:</b>
  <ul style='margin:5px 0;'>
    <li>Condition 1</li>
    <li>Condition 2</li>
  </ul>
</div>
```

### Checklist
```html
<h4>✅ Verification Checklist</h4>
<ul>
  <li>☐ Item to verify 1</li>
  <li>☐ Item to verify 2</li>
  <li>☐ <b>Supervisor approval required</b></li>
</ul>
```

### Resource Links
```html
<h4>🔗 Quick Links</h4>
<p><a href='https://example.com/resource1' target='_blank'>Resource Name 1</a></p>
<p><a href='https://example.com/resource2' target='_blank'>Resource Name 2</a></p>
```

### Ordered Procedure Steps
```html
<h4>📋 Procedure Steps</h4>
<ol>
  <li>First step description</li>
  <li>Second step with <b>emphasis</b></li>
  <li>Third step</li>
</ol>
```

## Valid Icons

| Icon | Emoji | Use For |
|------|-------|---------|
| `plus` | ➕ | New/create actions |
| `home` | 🏠 | Household/residence related |
| `alert` | ⚠️ | Warnings/urgent items |
| `wallet` | 💳 | Financial/payment related |
| `document` | 📄 | Documents/forms/records |
| `shield` | 🛡️ | Security/compliance/verification |

## Workflow

### Step 1: Use Case Context
Ask the user to describe their domain (IRS, Census, Healthcare, Financial, etc.)

### Step 2: Dashboard Metadata
- **Heading**: Dashboard title with organization name
- **SubHeading**: Optional subtitle (agent guide, quick reference, etc.)
- **CardsPerRow**: Always use "1" for detailed guides

### Step 3: Card Topics
For each card, gather:
- Topic name and icon
- Status badge (HIGH VOLUME, REQUIRED, URGENT, or empty)
- Key procedures (will become table/list)
- Warning conditions (will become alert box)
- External resource URLs
- Action button labels (4 recommended)

### Step 4: Generate Enhanced JSON
Transform inputs into full enhanced format with:
- Emoji prefixes in headings
- Styled HTML tables
- Warning boxes
- Resource links
- Action buttons

## Example: IRS Tax Services

```json
{
  "Heading": "IRS Taxpayer Services",
  "SubHeading": "MAXIMUS Agent Quick Reference Guide",
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
          {
            "TemplateString": "<h4>🔐 Authentication Required</h4><ul><li>Full SSN (last 4 not sufficient)</li><li>Date of Birth</li><li>Filing Status (Single/MFJ/MFS/HOH)</li><li>Exact refund amount from return</li></ul>"
          },
          {
            "TemplateString": "<h4>⏱️ Processing Times</h4><table style='width:100%; border-collapse:collapse;'><tr style='background:#f0f0f0;'><th style='padding:8px; text-align:left;'>Type</th><th style='padding:8px;'>Timeline</th></tr><tr><td style='padding:8px;'>E-file + Direct Deposit</td><td style='padding:8px;'><b>21 days</b></td></tr><tr><td style='padding:8px;'>Paper Return</td><td style='padding:8px;'>6-8 weeks</td></tr></table>"
          },
          {
            "TemplateString": "<h4>🔗 Resources</h4><p><a href='https://www.irs.gov/refunds' target='_blank'>Where's My Refund (IRS.gov)</a></p>"
          }
        ],
        "Actions": ["Open IDRS IMFOL", "Send Status Letter", "Escalate to Supervisor", "Transfer to Hotline"]
      }
    }
  ]
}
```

## Validation Rules

1. **Heading** is required
2. **Cards** array must have at least one card
3. **Card.Summary.Id** must be unique (use kebab-case)
4. **Icon** must be valid: plus, home, alert, wallet, document, shield
5. **Each card Detail must have 3-5 Sections**
6. **Each card must have 3-4 Actions**
7. **Tables must have inline styles** (no CSS classes)
8. **Links must have target='_blank'**

## Deployment

The generated JSON goes into a ShowView block's ViewData parameter:

```json
{
  "Type": "ShowView",
  "Parameters": {
    "ViewResource": {
      "Id": "arn:aws:connect:REGION:aws:view/cards"
    },
    "ViewData": { /* Generated JSON here */ }
  }
}
```

**Important:** Use AWS managed view ARN: `arn:aws:connect:REGION:aws:view/cards` (with `aws` as account ID)

## How to Invoke

```
Use the cards-view-generator skill to create a dashboard for [domain] agents
```

Or:
```
Generate an enhanced Cards View with tables and action buttons for [use case]
```
