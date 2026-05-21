# Marketing Skills

A marketplace-ready skeleton for a marketing skills package.

This project follows the lightweight structure from the reference project:

```text
.
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── commands/
│   └── marketing.md
└── skills/
    └── campaign-brief/
        ├── SKILL.md
        └── scripts/
            └── build_campaign_brief.py
```

## Included Demo Skill

`campaign-brief` turns rough campaign context into a concise marketing campaign brief.

Example:

```bash
python3 skills/campaign-brief/scripts/build_campaign_brief.py \
  --campaign "Summer Menu Push" \
  --audience "Regional restaurant chain operators" \
  --offer "Limited-time potato side bundle" \
  --objective "Increase sales meetings" \
  --channel "WeChat article and sales one-pager" \
  --proof "Existing menu photos, margin story, and prep-time advantage" \
  --cta "Book a 20-minute menu review"
```

## Add A New Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Add scripts under `skills/<skill-name>/scripts/` only when the workflow benefits from reusable automation.
3. Add a command in `commands/` when the skill should be available as a slash-command style entry.
4. Update `.claude-plugin/marketplace.json` keywords and description if the package positioning changes.

## Notes

- `.claude-plugin` mirrors the reference project structure.
- `.codex-plugin` is included so the same package has a Codex plugin manifest.
- Keep demo skills small and execution-oriented.
