# Scenario Template: new_interface

## Goal
Define and deliver a new API/service interface with clear contracts and test coverage.

## Requirement Checklist
- Interface type (REST, RPC, SDK method)
- Request/response schema
- Validation and error codes
- Backward compatibility expectations
- Authentication/authorization constraints

## Deliverables
- Interface specification (inputs, outputs, errors)
- Implementation in target module
- Unit tests for validation and core logic
- Integration tests for end-to-end behavior
- Progress update in `docs/progress/MASTER.md`

## Acceptance Criteria
- Endpoint/interface callable with valid payload
- Invalid input returns expected errors
- Tests pass and new/changed code reaches target coverage
- Documentation updated

