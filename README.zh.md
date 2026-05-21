# Marketing Skills

这是一个面向 skills market 的营销技能包骨架。

目录结构参考 `/Users/saibodafu/Downloads/docx-editor-main`：

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

## Demo Skill

`campaign-brief` 用来把粗略的营销输入整理成可执行的活动简报。

示例：

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

## 新增 Skill 的方式

1. 创建 `skills/<skill-name>/SKILL.md`。
2. 如果需要复用脚本，把脚本放在 `skills/<skill-name>/scripts/`。
3. 如果需要命令入口，在 `commands/` 下新增 markdown 命令文件。
4. 如果市场定位变化，同步更新 `.claude-plugin/marketplace.json`。

## 说明

- `.claude-plugin` 保持和参考项目一致。
- `.codex-plugin` 用于 Codex 插件清单兼容。
- demo skill 先保持小而可执行，方便后续扩展。
