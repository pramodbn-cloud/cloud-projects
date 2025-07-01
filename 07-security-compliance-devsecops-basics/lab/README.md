# Lab Guide — Security + Compliance: DevSecOps Basics

## Lab objective
The objective of this lab is to help the learner understand and configure the core security surfaces that protect Azure DevOps delivery workflows.

This lab focuses on permission awareness, service connection safety, secret handling, variable groups, and basic governance thinking. The goal is not to build a full compliance program, but to make the learner comfortable with the main control points that influence pipeline trust and delivery safety.

## What you will build or configure
In this lab, you will review and apply a simple security model around your Azure DevOps project and pipeline flow. You will examine permissions at a practical level, create or review a service connection, introduce shared variables or secrets using safer patterns, and think through basic access discipline.

This creates the learner’s first true security-oriented view of the DevOps lifecycle.

## Why this lab matters
Delivery systems become risky when powerful connections are created casually, secrets are exposed in unsafe ways, or permissions are granted too broadly.

Azure DevOps recommends using secret variables in the UI, variable groups, or Key Vault-backed variable groups rather than storing secrets in plain text YAML. Variable groups can centralize shared values and secrets across pipelines, and service connections are the mechanism pipelines use to access external services.

This lab matters because security must be part of normal engineering workflow, not a separate emergency topic.

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
- a clear view of the main Azure DevOps security control points
- a basic service connection understanding or working example
- a safer secret/variable handling pattern
- awareness of least-privilege thinking and inherited permissions
- confidence in explaining basic DevSecOps design choices

## Skills gained
- Understanding project-level security surfaces in Azure DevOps
- Thinking carefully about service connections as trust boundaries
- Using variable groups or secret variables more safely
- Building a least-privilege and governance mindset for delivery workflows

## Real-world relevance
In real engineering teams, delivery incidents often come from misconfigured access, exposed credentials, weak controls around external connections, or over-trusting automation identities. Azure DevOps security guidance and permissions design exist to reduce exactly those risks.

## Completion standard
A learner should not mark this lab complete until:
- the main security surfaces are understood
- service connection purpose is clear
- secret handling is improved from naive patterns
- permissions and governance thinking are visible
- validation confirms the workflow is explainable and safer
