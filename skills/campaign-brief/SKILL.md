---
name: Campaign Brief Builder
description: Use this skill when the user asks to create a marketing campaign brief, content campaign plan, launch brief, promotion concept, or channel-specific campaign draft from rough business inputs.
version: 0.1.0
---

# Campaign Brief Builder

Create a compact, execution-ready marketing campaign brief from incomplete or rough context.

## When To Use

Use this skill when the user asks for:

- a campaign brief
- a product launch brief
- a content campaign direction
- a promotion plan
- a social or channel activation concept
- a marketing plan that needs to become an executable brief

## Core Principle

Turn fuzzy marketing input into a brief that a designer, copywriter, or channel owner can act on immediately. Keep strategy connected to the audience, offer, message, and next action.

## Required Inputs

Gather or infer these fields:

- Campaign name
- Product or offer
- Target audience
- Business objective
- Primary channel
- Key proof points
- Call to action

If the user omits a field, make the lightest reasonable assumption and label it as an assumption.

## Output Format

Use this structure:

```markdown
## Campaign Brief

**Campaign Name:** ...
**Objective:** ...
**Audience:** ...
**Offer:** ...
**Primary Channel:** ...

### Core Insight
...

### Message Strategy
- Main message: ...
- Supporting proof: ...
- Tone: ...

### Creative Direction
- Visual direction: ...
- Copy direction: ...
- Content modules: ...

### Channel Execution
- Format: ...
- CTA: ...
- Measurement: ...

### Assumptions
- ...
```

## Helper Script

Use the bundled script when the user wants a fast generated draft or when you need a consistent markdown structure:

```bash
python3 {PLUGIN_DIR}/skills/campaign-brief/scripts/build_campaign_brief.py \
  --campaign "Quarterly Growth Push" \
  --audience "Category managers at chain restaurants" \
  --offer "Frozen potato product portfolio" \
  --objective "Increase sales meetings" \
  --channel "WeChat article and sales one-pager"
```

## Quality Bar

- The brief must be specific enough to execute.
- The message must clearly connect audience pain to product value.
- Claims must be supportable by the provided context.
- Avoid generic words like "innovative", "premium", or "empowering" unless the brief explains what they mean in this market.
