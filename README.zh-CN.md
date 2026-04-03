[English](./README.md) | **中文**

# Daily Development Specification

**面向日常增量开发的规范化工作流：一个 Markdown 文件，适配任意 Coding Agent。**

Daily Development Specification 是一个轻量、平台无关的 AI Agent Skill，用于处理高频日常需求：新功能、接口、脚本、UI 调整、性能优化。

核心思路：你只描述一次需求，后续由标准流程自动推进——需求澄清、规范校验、实现与测试、进度追踪与交付，确保一致性并支持跨会话续做。

## 四阶段流程

```
Phase 0: Requirement Clarification & Template Selection
       -> 选择场景模板（new_interface/new_script/new_feature/ui_modification/performance_optimization）
Phase 1: Compliance Check & Architecture Design
       -> 规范检查 + 设计文档
Phase 2: Implementation & Testing
       -> 编码实现 + 测试覆盖（目标 80%+）
Phase 3: Progress Tracking & Delivery
       -> 进度归档 + 交付说明
```

## 为什么有用

- 避免“想到哪写到哪”导致质量漂移
- 通过 `docs/progress/MASTER.md` 保留跨会话上下文
- 把测试要求前置，不再靠临时补救
- 统一团队协作口径，减少返工

## 快速开始

### 分发方式选择（建议）

根据使用场景，建议二选一：

1. **GitHub 分发（团队默认推荐）**
   - 以仓库为统一发布源，便于版本管理与协作同步。
   - 用户可通过安装脚本接入，后续重复执行即可更新。
   - 适合多人协作、长期维护。

2. **直接复制 `SKILL.md`（快速试用推荐）**
   - 只复制 `plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`。
   - 适合临时验证、单项目快速落地。
   - 后续升级需要手动替换文件。

如果你在决定“给其他人怎么用”，优先用 **GitHub 分发**；直接复制模式可作为兜底方案。

### Claude Code（插件方式）

```
/plugin add extravert/daily-development-spec
/plugin install daily-development-spec@latest
```

### 通用方式（任意 Agent）

直接使用核心文件：

- `plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`

把该文件放入你的技能目录，或粘贴到系统提示词/自定义指令中。

### Cursor / Codex 脚本安装

```bash
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-cursor.sh)
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-codex.sh)
```

以上脚本从 GitHub 仓库安装，并支持基于版本号的更新判断。

## 使用示例

```
/spec-dev add user authentication API
```

Agent 会按四阶段推进，并在 `docs/progress/` 下持续更新状态。

## 场景模板

对应模板位于：

- `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_interface.md`
- `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_script.md`
- `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_feature.md`
- `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/ui_modification.md`
- `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/performance_optimization.md`

## 进度导出

```bash
python scripts/export-progress.py docs/progress/
```

输出为 JSON，可对接 Jira、Linear、Notion 等系统。

## 项目结构

```
daily-development-spec/
├── plugins/daily-development-spec/
│   ├── skills/daily-development-spec/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── doc-templates.md
│   │       └── scenario-templates/
│   ├── agents/
│   │   └── daily-development-agent.md
│   ├── commands/spec-dev.md
│   └── .claude-plugin/plugin.json
├── scripts/
│   ├── install-cursor.sh
│   ├── install-codex.sh
│   ├── install-all.sh
│   └── export-progress.py
├── example/
└── LICENSE
```

关键入口：`plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`

## 许可证

MIT
