# Lab Guide — CD Pipelines: Deployments + Approvals + Rollback

## Lab objective
The objective of this lab is to help the learner understand and configure a simple Continuous Delivery workflow in Azure DevOps using the artifact produced in the CI module.

This lab focuses on deployment stages, environment awareness, promotion flow, approval thinking, and rollback preparedness. The goal is not to build a complex enterprise release system, but to make the learner comfortable with the core logic of safe delivery.

## What you will build or configure
In this lab, you will create a simple stage-based deployment flow that takes a previously validated artifact and moves it through one or more deployment targets or logical environments.

You will also introduce approval awareness and rollback thinking so that the learner sees delivery as a controlled process rather than a direct push into runtime.

## Why this lab matters
CI proves that a change is technically valid enough to continue. CD determines how that change is promoted safely.

This lab matters because delivery quality depends not only on successful builds, but on controlled release behavior, visibility between stages, responsible approvals, and the ability to recover confidently when something goes wrong.

## Estimated time
45 to 60 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a simple CD flow tied to the CI artifact
- stage-based delivery understanding
- awareness of approval checkpoints
- a practical understanding of rollback readiness
- confidence in explaining how artifacts move into environments

## Skills gained
- Designing a simple release flow using validated artifacts
- Understanding environments and promotion boundaries
- Introducing approvals as delivery controls
- Thinking about rollback as part of responsible deployment design

## Real-world relevance
In real engineering teams, deployment is rarely just a technical action. It is a controlled workflow involving confidence gates, promotion decisions, environment visibility, and recovery planning.

This lab reflects that same real-world delivery discipline in a simplified but meaningful way.

## Completion standard
A learner should not mark this lab complete until:
- the deployment flow is created and understandable
- the artifact handoff from CI is clear
- stage or environment logic is visible
- approval thinking is understood
- rollback strategy is explained clearly
