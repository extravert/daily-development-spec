[English](./README.md) | **中文**

# Daily Development Specification

**面向日常增量开发的标准化工作流：一个 Markdown 文件，适配任意 Coding Agent。**

Daily Development Specification 是一个轻量、平台无关的 AI Agent Skill，面向高频日常开发场景：新功能、API 接口、脚本、UI 调整与性能优化。

核心理念是：需求只描述一次，后续由统一流程自动推进——需求澄清、规范校验、架构设计、80%+ 测试覆盖、进度追踪与跨会话续做。

## 四阶段工作流

```
Phase 0: Requirement Clarification & Template Selection
       ↓（选择场景模板：new_interface / new_script / new_feature / ui_modification / performance_optimization）
Phase 1: Compliance Check & Architecture Design
       ↓（规范评审 + 设计文档）
Phase 2: Implementation & Testing
       ↓（编码实现 + 测试 + 评审清单）
Phase 3: Progress Tracking & Delivery
       ↓（归档、文档、交接）
```

不陷入过度分析，不做无休止规划。每个阶段都有清晰标准，并可自动保留跨会话进度。

## 为什么这件事重要

多数 AI 编程流程通常会落入两种极端：

1. **过于刚性**：框架高度预设，限制编码方式，绑定单一平台，接入成本高。
2. **过于松散**："直接让 AI 写"，缺少一致标准，进度分散，跨会话容易丢上下文。

Daily Development Specification 走的是中间路线：**有结构但不僵化，有标准但不笨重，可持续且易落地**。

### 解决了什么问题

- **避免代码风格漂移**：Phase 1 在实现前先做规范校验。
- **避免进度丢失**：`docs/progress/MASTER.md` 记录跨会话状态。
- **避免测试不足**：Phase 2 强制 80%+ 覆盖率目标。
- **避免中途返工**：Phase 0 先把需求边界说清楚。
- **避免平台锁定**：可用于 Claude Code、Cursor、Windsurf、Cline、Continue 等任意可读 Markdown 的助手。

### 适用场景

- **持续做增量开发的团队**：日常功能、接口、小脚本，而非一次性大重构。
- **AI 协助开发流程**：描述一次需求，后续交给流程做质量控制。
- **跨团队统一协作标准**：同一套四阶段清单、同一套代码规范。
- **长周期任务推进**：会话可能跨天或跨周，进度不断档。

## 快速开始

### 分发方式（推荐）

根据团队实际情况，推荐二选一：

1. **GitHub 分发（团队协作推荐）**
   - 以本仓库为统一发布源，便于版本管理与协作同步。
   - 用户通过安装脚本接入，后续重复执行即可更新。
   - 适合多人协作、长期维护。

2. **直接复制 `SKILL.md`（快速试用推荐）**
   - 仅复制 `plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`。
   - 适合单项目验证或无脚本安装环境。
   - 后续更新需手动同步。

### 各平台安装

#### VS Code Copilot（Skills）
在项目根目录执行以下命令，将 skill 安装到 `.github/skills`：

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/extravert/daily-development-spec.git daily-development-spec-tmp
Set-Location daily-development-spec-tmp
git sparse-checkout set plugins/daily-development-spec/skills/daily-development-spec
mkdir -p ..\.github\skills -ErrorAction SilentlyContinue
Copy-Item "plugins/daily-development-spec/skills/daily-development-spec" -Destination "..\.github\skills\daily-development-spec" -Recurse
Set-Location ..
Remove-Item daily-development-spec-tmp -Recurse -Force
Get-Item .\.github\skills\daily-development-spec\SKILL.md
```

#### Qoder
```bash
npx skills add https://github.com/extravert/daily-development-spec --skill daily-development-spec -a qoder
```

#### VS Code Codex Plugin
```text
/skill-installer https://github.com/extravert/daily-development-spec.git
```

### 最快上手：Claude Code 插件

```text
/plugin add extravert/daily-development-spec
/plugin install daily-development-spec@latest
```

重载插件后，即可使用（以 qoder 风格为例）：

```text
/daily-development-spec 实现一个新脚本，导出 t_model_image_score_ali 表数据。
```

流程会自动按四个阶段推进，并持续生成进度文件。

### 通用方式：直接使用 SKILL.md

适用于 Cursor、Windsurf、Cline 或其他助手：

1. 下载 [SKILL.md](plugins/daily-development-spec/skills/daily-development-spec/SKILL.md)
2. 放入你的项目目录，或粘贴到系统提示词/自定义指令
3. 发起需求："请按 Daily Development Specification 从 Phase 0 开始处理这个需求"

该文件可独立工作，无额外依赖、无平台专属代码。

### 通过 GitHub 脚本安装（Cursor / Codex）

```bash
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-cursor.sh)
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-codex.sh)
```

脚本支持从 GitHub 安装并进行版本化更新。

### 场景模板

Phase 0 可按任务类型选择模板：

- `new_interface`：REST API、SDK 方法、服务边界
- `new_script`：CLI 工具、批处理、自动化脚本
- `new_feature`：业务能力与用户可见功能
- `ui_modification`：样式、布局、交互行为
- `performance_optimization`：速度、内存、吞吐优化

每个模板都定义了产出物、测试策略与评审标准。

## 使用方式

### 示例：新增一个 API 接口

```text
用户: "在认证服务中新增一个用户注册 POST 接口"

Phase 0：助手先澄清
- 范围：仅 auth service，不做邮箱校验
- 成功标准：接口可调用、成功返回 user ID、校验必填字段
- 测试要求：参数校验单测 + DB 集成测试

Phase 1：助手做规范检查
- 命名风格符合约定（camelCase / PascalCase）
- 与现有接口无冲突
- 明确 API 规范与错误码
- 设计链路：参数校验 → 密码哈希 → 入库 → 返回响应

Phase 2：助手实现与测试
- 接口 + 哈希 + 错误处理
- 单测（覆盖率 >80%）
- 测试库集成测试
- 安全检查：防注入、输入校验

Phase 3：助手归档交付
- 更新进度文件
- 将设计文档移动至 docs/progress/completed/
- 更新 API 文档
- 状态标记为可评审、可部署
```

### 跨会话续做

任务做到一半暂停，几天后继续时再次发起同一需求。助手会先读取 `docs/progress/MASTER.md`，识别你当前处于 Phase 2、还剩哪些测试，然后从中断点继续。

不需要再手动回忆上下文，Markdown 文件就是可持续的状态存储。

### 原生任务追踪（Claude Code）

流程可自动将阶段任务同步到 TodoWrite（Claude Code 原生任务工具）。你能在侧边栏实时看到执行进度，同时 `MASTER.md` 仍是可持久化的真实来源。

### 进度导出

可将进度导出为 JSON，接入 Linear、Jira、Notion 等系统：

```bash
python scripts/export-progress.py docs/progress/
```

输出包含各阶段任务、完成状态与时间线估算信息。

## 项目结构

```text
daily-development-spec/
├── plugins/daily-development-spec/
│   ├── skills/daily-development-spec/
│   │   ├── SKILL.md                         # 核心工作流（适配任意平台）
│   │   └── references/
│   │       ├── doc-templates.md             # 阶段产出模板
│   │       └── scenario-templates/          # new_interface、new_script 等
│   ├── commands/spec-dev.md                 # `/spec-dev` 命令（Claude Code）
│   └── .claude-plugin/plugin.json           # 插件配置
├── scripts/
│   └── export-progress.py                   # 进度转 JSON
├── example/                                 # 示例脚本
├── docs/progress/                           # 开始需求后自动创建
│   ├── MASTER.md                            # 跨会话进度记忆
│   └── completed/                           # 已完成需求归档
└── LICENSE
```

**关键文件：`plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`**

整个方法论都在这个文件里。可独立使用、无依赖、跨平台。

## 设计理念

### 轻量但完整

- 单个约 200 行 Markdown 文件承载完整方法论
- 无 SDK、无运行时、无平台钩子
- 功能可独立退化，不互相强耦合
- 状态全部落在 Markdown，易读、可版本管理

### 结构化但不教条

- 四阶段清晰推进：需求 -> 规范 -> 实现 -> 交付
- 每阶段是检查清单，而非死板流程图
- 团队可按项目实际做适配

### 持久化记忆

- `docs/progress/MASTER.md` 充当助手的跨会话记忆
- 会话切换不丢上下文
- 特别适合跨小时/跨天持续推进的开发节奏

### 内建质量保障

- Phase 2 强制 80%+ 测试覆盖目标
- 提交前有代码评审清单
- Phase 1 提前做规范校验，减少返工
- 标准可见、可追踪、可审计

## 关键特性

| 特性 | 价值 |
|------|------|
| **四阶段工作流** | 清晰推进路径：澄清 -> 设计 -> 实现 -> 交付 |
| **需求场景模板** | API、脚本、功能、UI、性能等高频任务有标准模板 |
| **跨会话记忆** | `MASTER.md` 持久记录进度状态 |
| **覆盖率约束** | Phase 2 要求 80%+ 覆盖率（默认标准） |
| **规范校验机制** | Phase 1 先校验，减少代码风格漂移 |
| **Markdown 即数据库** | 进度、设计、规格可读、可版本管理 |
| **平台无关** | SKILL.md 可在多种助手环境中复用 |

## 与其他方式对比

| 方式 | 优点 | 局限 |
|------|------|------|
| **无结构**（普通对话） | 灵活、上手快 | 质量不稳定、上下文易丢、测试容易重复劳动 |
| **重型框架**（Superpowers、oh-my-claude） | 功能全面、一体化 | 成本高、偏慢、平台绑定更强 |
| **本工作流** | 轻量、可持续、通用性强、阶段清晰 | 需要团队按清单执行，进度文件保存在仓库中 |

## 许可证

MIT
