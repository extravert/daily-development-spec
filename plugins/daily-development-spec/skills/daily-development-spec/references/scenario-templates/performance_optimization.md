# Scenario Template: performance_optimization

## Goal
Improve measurable performance metrics without functional regressions.

## Requirement Checklist
- Baseline metric and measurement method
- Target metric and threshold
- Scope of optimization (CPU, memory, latency, throughput)
- Constraints (correctness, compatibility, readability)
- Rollback strategy if regressions appear

## Deliverables
- Optimization changes with rationale
- Benchmark or measurement results (before/after)
- Regression tests for behavior correctness
- Documentation of tradeoffs and residual risks
- Progress update in `docs/progress/MASTER.md`

## Acceptance Criteria
- Target metric improvement is demonstrated
- Functional tests still pass
- No critical regression in adjacent areas
- Delivery notes include benchmark method and data

