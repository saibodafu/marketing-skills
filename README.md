# Marketing Skills 营销技能市场

这是一个面向 skills market 的营销技能包骨架，用来沉淀可复用的营销工作流能力，例如活动简报、内容规划、上市推广、渠道执行和销售物料准备。

English summary: A marketplace-ready marketing skills package for reusable campaign, content, and go-to-market workflows.

## 产品说明 / Product Description

`marketing-skills` 不是单个营销模板，而是一组可以持续扩展的营销 skills 集合。每个 skill 聚焦一个明确的营销任务，并尽量输出可直接执行的文档、脚本或结构化结果。

English: `marketing-skills` is a collection of reusable marketing workflow skills. Each skill targets one concrete marketing job and produces practical, execution-ready outputs.

## 当前结构

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

## Demo Skill：campaign-brief

`campaign-brief` 用来把粗略的营销输入整理成一份可执行的活动简报，适合用于新品推广、渠道活动、内容选题、销售物料前置规划等场景。

English: `campaign-brief` turns rough campaign context into a concise, execution-ready marketing brief.

### 示例

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
2. 如果 workflow 需要复用脚本，把脚本放在 `skills/<skill-name>/scripts/`。
3. 如果需要命令入口，在 `commands/` 下新增 markdown 命令文件。
4. 如果市场定位、关键词或产品描述变化，同步更新 `.claude-plugin/marketplace.json` 和 `.codex-plugin/plugin.json`。

English: Add a new skill by creating `skills/<skill-name>/SKILL.md`, placing reusable automation under `scripts/`, and updating plugin metadata when the package positioning changes.

## 说明

- `.claude-plugin` 保持和参考项目一致，用于 marketplace 风格的插件描述。
- `.codex-plugin` 用于 Codex 插件清单兼容。
- demo skill 先保持小而可执行，方便后续扩展。
- 产品描述默认采用中文为主、英文为辅的双语表达。
