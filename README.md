# Marketing Skills 营销技能市场

这是一个面向 skills market 的营销技能包骨架，用来沉淀可复用的营销工作流能力，例如消费者洞察、活动简报、内容规划、上市推广、渠道执行和销售物料准备。

English summary: A marketplace-ready marketing skills package for reusable consumer insight, campaign, content, and go-to-market workflows.

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
    ├── campaign-brief/
    │   ├── SKILL.md
    │   └── scripts/
    │       └── build_campaign_brief.py
    └── consumer-insight/
        └── SKILL.md
```

## GitHub 仓库

当前仓库远程地址：

- SSH：`git@github.com:saibodafu/marketing-skills.git`
- HTTPS：[https://github.com/saibodafu/marketing-skills](https://github.com/saibodafu/marketing-skills)

可以用以下命令克隆：

```bash
git clone git@github.com:saibodafu/marketing-skills.git
```

如果你的环境没有配置 GitHub SSH key，也可以使用 HTTPS：

```bash
git clone https://github.com/saibodafu/marketing-skills.git
```

## 在 Agent 工具中使用

这个仓库的核心用法，是让 Claude Code、Codex 等 Agent 工具读取其中的 `skills/`、`commands/` 和插件描述文件，把营销工作流当成可复用能力调用。

### Claude Code

适合在 Claude Code 里作为本地营销技能包使用。

1. 把仓库克隆到本地。
2. 在 Claude Code 中打开仓库目录。
3. 让 Agent 先阅读 `AGENTS.md`，再按需读取 `skills/<skill-name>/SKILL.md`。
4. 如果要执行活动简报脚本，可运行：

```bash
python3 skills/campaign-brief/scripts/build_campaign_brief.py \
  --campaign "新品上市活动" \
  --audience "区域连锁餐饮客户" \
  --offer "限时菜单组合方案" \
  --objective "提升销售约访" \
  --channel "企业微信话术和销售单页" \
  --proof "菜单图片、毛利故事、出餐效率优势" \
  --cta "预约 20 分钟菜单共创"
```

### Codex

适合在 Codex 中作为插件式营销技能包使用。

1. 克隆仓库后，在 Codex 中打开本目录。
2. Codex 会优先参考 `AGENTS.md` 中的协作规则。
3. 插件清单位于 `.codex-plugin/plugin.json`。
4. 当你需要营销工作流时，可以直接对 Codex 说：

```text
使用 marketing-skills 的 campaign-brief，帮我把这个新品活动整理成可执行简报。
```

或者：

```text
使用 consumer-insight，围绕中国市场的某个品类拆解核心人群、痛点、痒点、爽点和产品机会。
```

### 其他 Agent 或自动化工具

如果工具支持读取本地目录或 GitHub 仓库，可以按以下顺序接入：

1. 先读取 `AGENTS.md`，理解本项目的语言、质量和协作规则。
2. 根据任务选择 `skills/<skill-name>/SKILL.md`。
3. 如果 skill 带有 `scripts/`，优先复用脚本生成结构化输出。
4. 如需命令入口，可读取 `commands/marketing.md`。
5. 如需插件市场描述，可读取 `.claude-plugin/` 或 `.codex-plugin/`。

使用这些 skills 时，不要把它们当成泛泛的营销知识库，而应把它们当成面向具体业务问题的执行流程：输入越清楚，输出越能直接交给营销、内容、设计、销售或产品团队使用。

## Skills

`campaign-brief` 用来把粗略的营销输入整理成一份可执行的活动简报，适合用于新品推广、渠道活动、内容选题、销售物料前置规划等场景。

English: `campaign-brief` turns rough campaign context into a concise, execution-ready marketing brief.

`consumer-insight` 用来围绕中国市场具体品类梳理潜在消费者画像，筛选品牌优先进入的核心人群，并进一步拆解痛点、痒点、爽点和产品机会。

English: `consumer-insight` maps consumer segments, priority target users, emotional drivers, and product opportunities for China-market categories.

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
- skills 先保持小而可执行，方便后续扩展。
- 产品描述默认采用中文为主、英文为辅的双语表达。
