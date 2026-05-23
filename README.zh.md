# marketing-skills — Claude Code / Codex 营销技能包

> 把消费者洞察、活动简报、内容规划、上市推广、节气营销海报等工作流沉淀成可复用的 Agent skills。

### 中文说明

---

## 安装

### Claude Code 快速安装

在 Claude Code 中添加这个 GitHub 仓库作为插件市场来源：

```text
/plugin marketplace add saibodafu/marketing-skills
```

然后安装插件：

```text
/plugin install marketing-skills
```

重启 Claude Code 后，用 `/skills` 检查是否已加载营销技能。

### Claude Code 手动安装

如果你想直接从本地目录加载：

```bash
git clone https://github.com/saibodafu/marketing-skills.git
cc --plugin-dir ./marketing-skills
```

也可以使用 SSH：

```bash
git clone git@github.com:saibodafu/marketing-skills.git
cc --plugin-dir ./marketing-skills
```

### Codex 使用

在 Codex 中打开本仓库目录即可使用：

```bash
git clone https://github.com/saibodafu/marketing-skills.git
cd marketing-skills
```

Codex 会读取 `AGENTS.md`、`.codex-plugin/plugin.json`、`commands/` 和 `skills/` 中的说明。你可以直接说：

```text
使用 marketing-skills 的 campaign-brief，帮我把这个新品活动整理成可执行简报。
```

或者：

```text
使用 consumer-insight，围绕中国市场的某个品类拆解核心人群、痛点、痒点、爽点和产品机会。
```

也可以使用：

```text
使用 product-concept，基于新品方向生成 Product Concept Board、核心价值承诺和信任状。
```

还可以使用：

```text
使用 product-copywriting，把这个产品卖点转成 10 句短买点文案。
```

或者：

```text
使用 jiangxiaobai-style-copywriting，为这个产品写 10 句江小白级情绪短文案。
```

也可以使用：

```text
使用 seasonal-poster-generator，基于“立夏，宠物猫粮”直接生成节气海报文案、生图提示词和成品海报。
```

或者：

```text
使用 qianchuan-viral-video-script-generator，为这个产品生成 10 条千川爆款视频脚本。
```

### 其他 Agent 工具

只要工具支持读取 GitHub 仓库或本地目录，就可以按这个顺序接入：

1. 先读取 `AGENTS.md`，理解语言、质量和协作规则。
2. 再根据任务读取 `skills/<skill-name>/SKILL.md`。
3. 如果需要命令入口，读取 `commands/marketing.md`。
4. 如果需要插件描述，读取 `.claude-plugin/` 或 `.codex-plugin/`。

---

## 使用方式

### Claude Code 命令

```text
/marketing campaign-brief 为一个新品上市活动生成活动简报
/marketing consumer-insight 分析中国市场某个品类的核心人群和产品机会
/marketing product-concept 为一个新品方向生成产品概念板
/marketing product-copywriting 把产品功能和卖点转成短买点文案
/marketing jiangxiaobai-style-copywriting 为产品生成江小白级情绪短文案
/marketing seasonal-poster-generator 基于节气和产品生成品牌海报创意、生图提示词和成品海报
/marketing qianchuan-viral-video-script-generator 为产品生成 10 条 15-30 秒千川爆款视频脚本
```

以下自然语言也适合触发：

- “帮我写一份活动简报”
- “把这个新品推广想法整理成 brief”
- “分析这个品类在中国市场的核心消费者”
- “拆解用户痛点、痒点、爽点和产品机会”
- “帮我做一个新品 Product Concept”
- “把这个产品方向整理成概念测试文案”
- “帮我写 10 句产品买点文案”
- “把这个功能转成用户愿意买单的短文案”
- “给这个卖点起几个更有感知的名字”
- “写 10 句江小白级文案”
- “把这个产品写得更走心、更有情绪”
- “给这个新品写适合海报和社媒的情绪短句”
- “立夏，宠物猫粮，直接生成节气海报”
- “给这个产品做二十四节气借势海报”
- “输出节气海报文案和 AI 生图提示词”
- “帮我写 10 条千川爆款视频脚本”
- “形式：口播，主题：这个产品”
- “这个产品怎么拍抖音投放素材”

### 脚本方式

`campaign-brief` 带有一个轻量脚本，可以把结构化输入生成 Markdown 简报：

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

当前脚本只依赖 Python 标准库，无需额外安装依赖。

---

## 当前 Skills

### campaign-brief

把粗略的营销输入整理成一份可执行的活动简报，适合新品推广、渠道活动、内容选题、销售物料前置规划等场景。

输出重点：

- 活动目标
- 目标人群
- 核心洞察
- 信息策略
- 创意方向
- 渠道执行
- CTA 和衡量方式

### consumer-insight

围绕中国市场具体品类梳理潜在消费者画像，筛选品牌优先进入的核心人群，并拆解痛点、痒点、爽点和产品机会。

输出重点：

- 人群分层
- 优先目标用户
- 消费场景
- 购买动因
- 痛点 / 痒点 / 爽点
- 产品和传播机会

### product-concept

把产品方向、消费者洞察、功能卖点、情绪价值和信任状整理成完整 Product Concept Board，适合新品立项、概念测试、创意 brief 和品牌策略讨论。

输出重点：

- 概念所需消费者洞察
- 核心价值点发散与评估
- 差异化核心价值承诺
- 核心价值承诺词
- 信任状筛选
- 完整 Product Concept Board

### product-copywriting

把产品功能、卖点、成分、技术、设计或使用体验转化为短句式、高感知、可直接用于电商详情页、广告图和种草内容的买点文案。

输出重点：

- 产品信息理解
- 卖点到买点转译
- 10句「功能价值 + 买点」短文案

### jiangxiaobai-style-copywriting

把产品信息、核心卖点和使用场景转化为“江小白级”的极简情绪短文案，适合产品海报、社交媒体、包装短句和品牌内容。

输出重点：

- 产品信息理解
- 情绪-场景定位
- 表达方向
- 10句江小白级情绪短文案
- 海报、社媒、包装推荐用句

### seasonal-poster-generator

把节气、产品和品牌调性转化为二十四节气品牌海报方案，适合小红书、朋友圈、公众号头图、电商活动图和品牌节气借势内容。

输出重点：

- 节气 × 产品洞察
- 海报主文案和备选文案
- 视觉创意
- AI 生图提示词
- 成品海报生成执行

### qianchuan-viral-video-script-generator

为产品、服务或主题生成 10 条 15-30 秒千川 / 抖音转化型爆款视频脚本，适合全品类投放素材、短视频带货和多素材方向测试。

输出重点：

- 信息确认与假设
- 爆款五步结构脚本
- 三秒抓注意、痛点刺痛、唯一解法、具象价值呈现和行动机制
- 口播、剧情、密语、科普、生活流等风格适配
- 全行业通用黄金句式库调用

---

## GitHub 仓库

- HTTPS：[https://github.com/saibodafu/marketing-skills](https://github.com/saibodafu/marketing-skills)
- SSH：`git@github.com:saibodafu/marketing-skills.git`

---

## 项目结构

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
    ├── consumer-insight/
    │   └── SKILL.md
    ├── product-concept/
    │   └── SKILL.md
    ├── product-copywriting/
    │   └── SKILL.md
    ├── jiangxiaobai-style-copywriting/
        ├── SKILL.md
        └── knowledge/
            └── jiangxiaobai-style-patterns.md
    ├── qianchuan-viral-video-script-generator/
    │   └── SKILL.md
    └── seasonal-poster-generator/
        └── SKILL.md
```

---

## 新增 Skill

1. 创建 `skills/<skill-name>/SKILL.md`。
2. 如果 workflow 需要复用脚本，把脚本放在 `skills/<skill-name>/scripts/`。
3. 如果需要命令入口，在 `commands/` 下新增 markdown 命令文件。
4. 如果市场定位、关键词或产品描述变化，同步更新 `.claude-plugin/marketplace.json` 和 `.codex-plugin/plugin.json`。

新增 skill 时，应先澄清场景、目标用户、输入、输出、边界、触发条件和质量标准；确认方向后再写入 skill 文件。

---

## 说明

- `.claude-plugin` 用于 Claude Code 插件和 marketplace 风格描述。
- `.codex-plugin` 用于 Codex 插件清单兼容。
- `commands/marketing.md` 提供 `/marketing` 命令入口。
- `skills/` 是每个营销 workflow 的主说明。
- 输出应能直接交给营销、内容、设计、销售或产品团队使用，不编造市场数据或客户案例。
