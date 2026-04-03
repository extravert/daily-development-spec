---
description: Start Daily Development Workflow for incremental requirements
argument-hint: <requirement description, e.g. "add user authorization API">
allowed-tools: [Read, Glob, Grep, Bash, LS, Write, NotebookRead, WebFetch, TodoWrite, WebSearch, BashOutput]
---

# Daily Development Specification

You are executing the **Daily Development Specification** workflow. This standardized pipeline ensures consistent code quality, compliance verification, test coverage, and progress tracking for incremental daily requirements: new features, APIs, scripts, UI modifications, and performance optimizations.

## Requirement Input

The user's requirement description: $ARGUMENTS

## Cross-Conversation Continuity Check

**CRITICAL**: Before anything else, check if `docs/progress/MASTER.md` exists in the project.

- If it **exists**: Read it now. You are resuming an in-progress requirement. Identify current phase and remaining tasks, then continue from that exact point. Do NOT restart.
- If it **does not exist**: This is a fresh start. Proceed with Phase 0 below.

---

## Workflow Phases

Execute the following 4 phases in order. Confirm with the user before moving to the next phase.

### Phase 0: Requirement Clarification & Template Selection

1. Parse and classify requirement type:
   - `new_interface`: API/service boundary changes
   - `new_script`: scripts, automation, CLI
   - `new_feature`: business logic feature
   - `ui_modification`: UI behavior/style/layout
   - `performance_optimization`: speed/memory/throughput improvements
2. Confirm scope, dependencies, constraints, and out-of-scope items.
3. Confirm success criteria and acceptance checks.
4. Select a scenario template from:
   - `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_interface.md`
   - `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_script.md`
   - `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_feature.md`
   - `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/ui_modification.md`
   - `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/performance_optimization.md`

### Phase 1: Compliance Check & Architecture Design

1. Check coding conventions, parameter and error handling, and test expectations.
2. Design implementation shape: affected files, function/class contracts, data flow, risks.
3. Create design note under `docs/progress/` using the phase template in
   `plugins/daily-development-spec/skills/daily-development-spec/references/doc-templates.md`.
4. Ask user for confirmation before implementation.

### Phase 2: Implementation & Testing

1. Implement according to Phase 1 design.
2. Write tests (unit + integration when needed) and target >= 80% coverage for new/changed code.
3. Run checklist before proceeding:
   - [ ] Style/structure consistency maintained
   - [ ] Error paths are handled
   - [ ] Tests pass locally
   - [ ] No debug prints/temporary code left
   - [ ] Documentation/comments updated

### Phase 3: Progress Tracking & Delivery

1. Create or update `docs/progress/MASTER.md`.
2. Update phase completion status and current blocker/next-step fields.
3. Archive completed design notes to `docs/progress/completed/` when done.
4. Provide delivery handoff: changed files, tests run, coverage status, and remaining risks.

---

## Rules

- Never skip phases; confirm each boundary.
- Always read `docs/progress/MASTER.md` first in resumed conversations.
- Keep updates concise and track progress in both markdown and native task tools when available.
- If requirement scope is unclear or risky, stop and ask targeted clarification questions.
