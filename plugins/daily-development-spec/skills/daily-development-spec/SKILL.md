---
name: daily-development-spec
description: >-
  Standardized daily development workflow for incremental requirements: new features, APIs, scripts, interfaces, and optimizations. Ensures code consistency, clear progress tracking, and cross-conversation context recovery.
  Triggers on: "new feature", "add interface", "new script", "modify UI", "optimize performance", "fix bug","규범对齐", "add endpoint", "implement", "develop", "规范".
  Chinese keywords: "新功能", "新接口", "新脚本", "修改界面", "性能优化", "修复", "规范", "开发", "实现".
  
version: 1.0.0
---

# Daily Development Specification Workflow

You are executing the **Daily Development Specification Workflow** — a standardized pipeline for incremental requirements (new features, APIs, scripts, interfaces). Your job is to ensure every requirement follows team standards, has clear progress tracking, and supports cross-conversation context recovery.

## Before You Begin: Cross-Conversation Continuity Check

**CRITICAL**: Before starting any phase, check if `docs/progress/MASTER.md` already exists in the project.

- If it **exists**: Read it immediately. You are resuming an in-progress task. Identify which phase you are in, what has been completed, and continue from the exact point where the previous conversation left off. Do NOT restart from Phase 0.
- If it **does not exist**: This is a fresh start. Proceed to Phase 0.

After loading your current state from MASTER.md, populate the platform's native task tracking tool (e.g. TodoWrite) with the active phase's pending tasks. For each task, set content to the task description, status to "in-progress" for the currently active task and "todo" for the rest, and priority mapped as P0=high, P1=medium, P2=low. This gives the user real-time visual progress in their IDE. If no native task tool is available, skip this step — MASTER.md alone is sufficient.

---

## Phase 0: Requirement Clarification & Standard Template Selection

**Goal**: Understand the requirement and select the appropriate team standard template.

**Actions**:

1. Clarify the requirement:
   - **Type**: What kind of requirement? (new API, new script, new feature, UI change, performance optimization, bug fix)
   - **Scope**: Which modules/files affected?
   - **Dependencies**: Any external services, databases, or APIs involved?
   - **Constraints**: Timeline, backward compatibility, performance targets?

2. Select the appropriate standard template:
   - **For new API**: Use `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_interface.md`
   - **For new script**: Use `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_script.md`
   - **For new feature**: Use `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/new_feature.md`
   - **For UI changes**: Use `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/ui_modification.md`
   - **For optimization**: Use `plugins/daily-development-spec/skills/daily-development-spec/references/scenario-templates/performance_optimization.md`

3. Review relevant standards:
   - Code style guide for this project
   - Parameter handling conventions
   - Error handling patterns
   - Testing requirements

**Output**: Clear requirement definition + selected standard template for this task.

---

## Phase 1: Compliance Check & Architecture Design

**Goal**: Verify the new code will follow team standards and design the architecture for this requirement.

**Actions**:

1. **Compliance & Style Check**:
   - Verify code style consistency (naming conventions, indentation, patterns used)
   - Check parameter handling (how are parameters passed, validated?)
   - Review error handling approach (exceptions, retries, logging)
   - Validate testing strategy (unit tests required, integration tests?)
   - Check API/data contracts (response format, versioning)

2. **Architecture Design**:
   - Design function/class signatures aligned with project patterns
   - Plan data structures and API contracts
   - Identify dependencies and integration points
   - Plan the implementation order (what needs to be done first)

3. **Create Design Document** (lightweight, in `docs/progress/`):
   - Current requirement + selected standard template
   - Compliance checklist from Phase 1 (all items should be green)
   - Architecture decisions and rationale
   - Implementation plan (steps in order)

**Output**: Design document confirming all compliance checks passed + clear architecture for implementation.

---

## Phase 2: Implementation & Testing

**Goal**: Write code following the design and ensure quality through testing.

**Actions**:

1. **Implement according to design**:
   - Follow the compliance checklist from Phase 1
   - Use the architecture design as blueprint
   - Add comprehensive comments and docstrings
   - Log progress: completed function X, then Y, etc.

2. **Write tests**:
   - Unit tests for each function (happy path + edge cases)
   - Integration tests if external dependencies involved
   - Test error handling (what happens when things fail?)
   - Aim for 80%+ code coverage

3. **Code Review Checklist** (before submitting):
   - [ ] Code follows style guide from Phase 1
   - [ ] All error paths handled (no silent failures)
   - [ ] All tests pass locally
   - [ ] No console.log / print statements left (use logging framework)
   - [ ] Comments explain why, not what
   - [ ] No hardcoded secrets/credentials
   - [ ] Documentation updated

4. **Performance Check**:
   - Measure execution time (slow? optimize before submitting)
   - Check memory usage (memory leaks?)
   - Run load test if applicable (can this scale?)

**Output**: Complete implementation + passing test suite + code review checklist all green.

---

## Phase 3: Progress Tracking & Delivery

**Goal**: Create cross-conversation progress tracking and prepare for code delivery.

**Actions**:

1. **Create progress file** `docs/progress/MASTER.md`:
   - Requirement name and description (from Phase 0)
   - Status: Design completed / Implementation in progress / Testing / Ready for review
   - Current blockers (if any)
   - Next steps (what to do if conversation resumes)

2. **Update progress checkpoint**:
   - Mark: [ ] Phase 0 completed
   - Mark: [ ] Phase 1 (Compliance Check) completed ✓
   - Mark: [ ] Phase 2 (Implementation) completed ✓
   - Mark: [ ] Phase 2 (Testing) completed ✓
   - Mark: [ ] Ready for code review

3. **Create delivery summary**:
   - Files modified/created
   - Key design decisions made
   - Test coverage percentage
   - Performance metrics (if applicable)
   - Known limitations (if any)

4. **Cross-conversation continuity**:
   - If this requirement spans multiple conversations, save state in docs/progress/MASTER.md
   - When resuming: read MASTER.md first to understand current status
   - Update MASTER.md after completing each phase in new conversation

**Output**: Complete progress file + delivery summary ready for code review.

---

## Phase 4: Code Review & Finalization

**Goal**: Conduct code review and prepare code for merge.

**Actions**:

1. **Self-review checklist** (before submitting to team):
   - [ ] All Phase 2 checklist items completed
   - [ ] Tests pass 100%
   - [ ] No debugging code left (console.log, print statements, etc.)
   - [ ] Comments are clear (why, not what)
   - [ ] Documentation updated (README, API docs, etc.)
   - [ ] Commit messages are descriptive

2. **Team code review** (if available):
   - Address reviewer feedback
   - Update code based on suggestions
   - Verify tests still pass after changes

3. **Final validation**:
   - Run full test suite one more time
   - Verify against Phase 1 compliance checklist (all items should still be ✓)
   - Confirm performance benchmarks still meet requirements

4. **Prepare for merge**:
   - Create clean commit message following team conventions
   - Update MASTER.md status to "READY FOR MERGE"
   - Document any post-deployment steps (migrations, config changes, etc.)

5. **Archive progress**:
   - Move completed progress file to `docs/progress/completed/`
   - This serves as a record for future similar requirements

**Output**: Code approved, tests passing, all standards met, ready for merge and deployment.

---

## Important Behavioral Rules

1. **Always start with Phase 0**. Clarify the requirement and select the right template. Even 2-minute requirements benefit from this clarity.

2. **Follow the compliance checklist from Phase 1**. Don't skip this—it catches style issues early and saves code review time.

3. **Tests are required, not optional**. No code ships without tests. Aim for 80%+ coverage.

4. **Document as you code**. Add comments explaining *why* (not what). Update README/API docs before submitting.

5. **Use MASTER.md for state**. If a requirement spans multiple conversations, save progress in `docs/progress/MASTER.md`. Next conversation: read MASTER.md first.

6. **Code review checklist is your friend**. Complete all items in Phase 2 before submitting to team. Saves time for everyone.

7. **Performance matters**. Measure it. If slow, optimize before submitting. Benchmark results should be in the progress file.

8. **Commit messages tell a story**. Use descriptive messages that explain *what changed and why*. Future you will thank you.

9. **When in doubt, ask**. Better to clarify requirements in Phase 0 than rewrite code in Phase 3.

10. **Keep it simple**. Each requirement should take 1-3 conversations. If longer, break it into smaller pieces.
