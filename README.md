**English** | [中文](./README.zh-CN.md)

# Daily Development Specification

**Standardized workflow for daily incremental development. One Markdown file. Any coding assistant.**

Daily Development Specification is a lightweight, platform-agnostic AI agent skill that ensures consistent code quality, compliance verification, test coverage, and cross-conversation context recovery for everyday development tasks: new features, APIs, scripts, UI changes, and performance optimizations.

Core idea: instead of ad-hoc coding or switching between tools, describe your requirement once — and the workflow handles everything: requirement clarification, compliance checks, architecture design, 80%+ test coverage enforcement, progress tracking, and seamless multi-session continuity.

## Four-Phase Workflow

```
Phase 0: Requirement Clarification & Template Selection
       ↓ (select scenario: new_interface, new_script, new_feature, ui_modification, performance_optimization)
Phase 1: Compliance Check & Architecture Design  
       ↓ (standards review, design doc creation)
Phase 2: Implementation & Testing
       ↓ (code, tests, code review checklist)
Phase 3: Progress Tracking & Delivery
       ↓ (archive, document, handoff)
```

No analysis paralysis. No endless planning. Clear criteria at each phase. Automatic progress memory across conversations.

## Why This Matters

Most AI coding workflows fall into one of two traps:

1. **Too rigid**: Opinionated frameworks that dictate *how* you code, lock you into one platform, or require heavy setup
2. **Too loose**: "Just ask the AI to code it" with zero consistent standards, scattered progress, lost context across sessions

Daily Development Specification finds the middle: **structured but flexible, standardized but lightweight, persistent but easy to use**.

### What It Solves

- **No code consistency drift**: Phase 1 ensures your requirement follows project standards before implementation starts
- **No lost progress**: `docs/progress/MASTER.md` remembers everything across conversation sessions
- **No inadequate testing**: Phase 2 enforces 80%+ test coverage — no skipping
- **No rework**: Clear requirement clarity in Phase 0 prevents scope creep mid-implementation  
- **No platform lock-in**: Works with Claude Code, Cursor, Windsurf, Cline, Continue, or any assistant that reads Markdown

### Ideal For

- **Teams building incrementally**: Daily features, APIs, small scripts — not giant rewrites
- **AI-assisted development workflows**: You describe it once; the system ensures quality control
- **Cross-team consistency**: Everyone follows the same 4-phase checklist; same code standards
- **Persistent development**: Sessions last days or weeks; progress never gets lost

## Quick Start

### Application Methods

1. **GitHub**
   - Install via GitHub repository to `.github/skills` (Refer to [Platform Install](#Platform Install)).

2. **Directly Copy `SKILL.md`**
   - Only copy `plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`.
   - Suitable for any platform; simply place it in your project directory or system prompt. Progress files cannot be automatically generated, but the methodology is fully usable.

### Platform Install

#### VS Code Copilot (Skills)
Run the following in your project root to install the skill into `.github/skills`:

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

Linux/macOS (bash):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/extravert/daily-development-spec.git daily-development-spec-tmp
cd daily-development-spec-tmp
git sparse-checkout set plugins/daily-development-spec/skills/daily-development-spec
mkdir -p ../.github/skills
cp -r plugins/daily-development-spec/skills/daily-development-spec ../.github/skills/daily-development-spec
cd ..
rm -rf daily-development-spec-tmp
ls -la ./.github/skills/daily-development-spec/SKILL.md
```

#### Qoder
```bash
npx skills add https://github.com/extravert/daily-development-spec --skill daily-development-spec -a qoder
```

#### Vs Code Codex Plugin
```text
/skill-installer https://github.com/extravert/daily-development-spec.git
```

### Quickest Start: Claude Code Plugin

```
/plugin add extravert/daily-development-spec
/plugin install daily-development-spec@latest
```

Reload plugins. Then use skill command（e.g. qoder's):

```
/daily-development-spec 实现一个新脚本，导出 t_model_image_score_ali 表数据。
```

That's it. The workflow runs automatically through 4 phases, creating progress files as it goes.

### Generic Start: Copy SKILL.md

For Cursor, Windsurf, Cline, or any other assistant:

1. Download [SKILL.md](plugins/daily-development-spec/skills/daily-development-spec/SKILL.md)
2. Place it in your project or paste into a custom instruction field
3. Start a requirement: "Process this requirement using Daily Development Specification, starting with Phase 0"

The file works standalone — no dependencies, no platform-specific code.

### Script Install from GitHub (Cursor / Codex)

```bash
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-cursor.sh)
bash <(curl -sL https://raw.githubusercontent.com/extravert/daily-development-spec/main/scripts/install-codex.sh)
```

These scripts install from the GitHub repo and support version-aware updates.

### Scenario Templates

The framework includes templates for common daily task types. Reference these in Phase 0:

- `new_interface`: REST API, SDK method, service boundary
- `new_script`: CLI tool, batch processor, automation
- `new_feature`: Business logic, user-facing capability
- `ui_modification`: Styling, layout, interaction patterns
- `performance_optimization`: Speed, memory, throughput improvements

Each template details expected deliverables, testing approach, and review criteria.

### Cross-Session Continuity

Start a requirement, then pause. Days or weeks later, run the same requirement again. The assistant checks `docs/progress/MASTER.md`, sees you're in Phase 2 with 3 tests remaining, and continues exactly where you left off.

No "remind me where we were" needed. The Markdown file *is* the memory.

### Native Task Tracking (Claude Code)

The workflow automatically loads phase tasks into TodoWrite (Claude Code's native task tool). You get real-time progress in your sidebar while MASTER.md remains the persistent source of truth.

### Progress Export

Convert progress to JSON for integration with Linear, Jira, Notion, or other tools:

```bash
python scripts/export-progress.py docs/progress/
```

Output includes per-phase task details, completion status, and timeline estimates.

## Project Structure

```
daily-development-spec/
├── plugins/daily-development-spec/
│   ├── skills/daily-development-spec/
│   │   ├── SKILL.md                         # Core workflow (works on ANY platform)
│   │   └── references/
│   │       ├── doc-templates.md             # Phase output templates
│   │       └── scenario-templates/          # new_interface, new_script, etc.
│   ├── commands/spec-dev.md                 # `/spec-dev` command (Claude Code)
│   └── .claude-plugin/plugin.json           # Plugin configuration
├── scripts/
│   └── export-progress.py                   # Convert progress to JSON
├── example/                                 # Sample scripts
├── docs/progress/                           # Created when you start a requirement
│   ├── MASTER.md                            # Progress memory across sessions
│   └── completed/                           # Archived completed requirements
└── LICENSE
```

**Key file: `plugins/daily-development-spec/skills/daily-development-spec/SKILL.md`**

This is the entire workflow. Standalone, no dependencies. Works on any AI coding assistant.

## Design Philosophy

### Lightweight but Complete

- Single 200-line Markdown file carries the entire methodology
- No SDK, no runtime, no platform hooks
- Graceful degradation: features work independently
- All state lives in Markdown files — human-readable, version-controllable

### Structured but Non-Dogmatic

- Four clear phases: Requirement → Compliance → Implementation → Delivery
- Each phase has a checklist, not a rigid recipe
- You and your team adapt the details to match your project

### Persistent Memory

- `docs/progress/MASTER.md` is your AI assistant's "memory" across conversation sessions
- No context lost between sessions  
- Perfect for ongoing development with hours or days between conversations

### Quality Built-In

- 80%+ test coverage enforcement in Phase 2
- Code review checklist before handoff
- Compliance checks in Phase 1 prevent rework
- Standards are documented and visible

## Key Features

| Feature | Benefit |
|---------|---------|
| **4-Phase Workflow** | Clear progression: clarify → design → implement → deliver |
| **Requirement Templates** | Scenarios (API, script, feature, UI, optimization) match high-frequency task types |
| **Cross-Conversation Memory** | `MASTER.md` state file remembers progress across sessions |
| **Test Coverage Enforcement** | Phase 2 requires 80%+ coverage — no exceptions |
| **Compliance Checks** | Phase 1 prevents code drift before implementation |
| **Markdown-as-Database** | Progress, designs, specs all human-readable and version-controllable |
| **Platform-Agnostic** | SKILL.md works with Claude Code, Cursor, Windsurf, Cline, or any Markdown-capable assistant |

## Comparison with Other Approaches

| Approach | Pros | Cons |
|----------|------|------|
| **No structure** (standard chat) | Flexible, minimal setup | Inconsistent quality, lost context, duplicated testing effort |
| **Heavy framework** (Superpowers, oh-my-claude) | Comprehensive, all features built-in | Slow, locked to one platform, harder to customize |
| **This workflow** | Lightweight, persistent, versatile, clear phases | Requires discipline to follow checklist, progress lives in your repo |

## License

MIT