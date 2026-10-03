# Duties and Responsibilities for eBPF Network Packet Drop Diagnoser Agent

## Dual-Control Architecture
Maker:
drop-trace-sampler

Checker:
congestion-cause-checker

## Operational Workflow
1. The Maker (drop-trace-sampler) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (congestion-cause-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
