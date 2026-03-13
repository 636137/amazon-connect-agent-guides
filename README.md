# Amazon Connect Agent Guides

Production-quality **Step-by-Step Guides** (Cards Views) for Amazon Connect agent desktops.

## Repository Structure

```
├── README.md                      # This file
├── skill/                         # 📦 Copilot Skill (copy to ~/.copilot/skills/)
│   ├── SKILL.md                   # Skill definition
│   ├── README.md                  # Skill documentation  
│   ├── cards_view_builder.py      # Python helper functions
│   └── reference_example.json     # Production example (5 IRS cards)
│
└── irs-agent-views/               # 🏛️ IRS Implementation Example
    ├── SETUP_GUIDE.md             # Amazon Connect configuration
    ├── irs_enhanced_cards.json    # Deployed cards JSON
    └── *.json                     # Individual card definitions
```

## Install the Skill

```bash
# Copy skill to your Copilot skills folder
cp -r skill ~/.copilot/skills/cards-view-generator
```

Then invoke:
```
Use the cards-view-generator skill to create an agent guide for [your use case]
```

## Live Demo

| Instance | Phone | Agent Login |
|----------|-------|-------------|
| **Treasury Connect** | +1 833-289-6602 | [Agent Workspace](https://treasury-connect-prod.my.connect.aws/agent-app-v2) |

## Features

- ✅ Rich HTML tables with styled headers and color-coded rows
- ✅ Warning boxes with highlighted backgrounds  
- ✅ Checklists with checkbox indicators
- ✅ External resource links
- ✅ 4 action buttons per card
- ✅ Emoji-enhanced headings

## Deploy to Amazon Connect

```json
{
  "Type": "ShowView",
  "Parameters": {
    "ViewResource": {
      "Id": "arn:aws:connect:us-east-1:aws:view/cards"
    },
    "ViewData": { /* Generated JSON from skill */ }
  }
}
```

**Important:** Use `aws` as account ID: `arn:aws:connect:REGION:aws:view/cards`

## Card Structure

```json
{
  "Heading": "Dashboard Title",
  "CardsPerRow": "1",
  "Cards": [
    {
      "Summary": {
        "Id": "card-id",
        "Icon": "document",
        "Heading": "💰 Card Title",
        "Status": "HIGH VOLUME",
        "Description": "Brief description"
      },
      "Detail": {
        "Heading": "Detail Title",
        "Description": "Context description",
        "Sections": [
          {"TemplateString": "<h4>🔐 Section</h4><ul><li>Item</li></ul>"},
          {"TemplateString": "<h4>📊 Table</h4><table>...</table>"},
          {"TemplateString": "<h4>⚠️ Warning</h4><div style='background:#fff3cd;'>...</div>"},
          {"TemplateString": "<h4>🔗 Links</h4><a href='...'>Link</a>"}
        ],
        "Actions": ["Action 1", "Action 2", "Action 3", "Action 4"]
      }
    }
  ]
}
```

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

## Valid Icons

| Icon | Emoji | Use For |
|------|-------|---------|
| `document` | 📄 | Forms, records |
| `shield` | 🛡️ | Security, verification |
| `wallet` | 💳 | Payments, financial |
| `alert` | ⚠️ | Warnings, urgent |
| `home` | 🏠 | Household |
| `plus` | ➕ | Create new |

## License

MIT
