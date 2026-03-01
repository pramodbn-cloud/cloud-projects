# Lab Guide — Azure Policy with AKS

## Lab objective
The objective of this lab is to help the learner understand and implement Azure Policy for AKS so that Kubernetes workloads and cluster components can be evaluated and governed against centralized policy definitions.

This lab focuses on policy assignment, audit versus deny behavior, compliance visibility, and policy-driven prevention of noncompliant Kubernetes objects. The goal is not to build a full compliance program yet, but to make the learner comfortable with how governance rules become enforceable in AKS.

## What you will build or configure
In this lab, you will enable or review the Azure Policy add-on for AKS, assign or inspect one or more built-in AKS/Kubernetes policies, and validate how a compliant or noncompliant workload is handled.

This creates the first true platform-governance-enforcement workflow in the course.

## Why this lab matters
Without policy enforcement, organizational rules remain advisory. Teams can still deploy workloads that ignore resource guidance, skip security settings, or violate best practices.

Azure Policy helps enforce organizational standards and assess compliance at scale. In AKS, after you install the Azure Policy add-on, you can apply built-in policy definitions or initiatives to the cluster. Azure’s governance guidance also explains that the AKS add-on extends Gatekeeper for enforcement.

## Estimated time
55 to 70 minutes

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
- a clear understanding of the Azure Policy add-on for AKS
- one policy assignment or clearly reviewed policy scenario
- one example of compliant versus noncompliant behavior
- confidence in explaining how governance becomes enforceable in the cluster

## Skills gained
- Understanding Azure Policy in AKS platform terms
- Thinking in terms of audit and deny enforcement
- Connecting cluster governance to earlier workload and namespace discipline
- Preparing for stronger production security and compliance posture

## Real-world relevance
In real AKS platforms, centralized policy becomes one of the strongest controls for reducing drift and improving consistency. Azure also provides built-in AKS policy definitions and now offers deployment safeguards to enforce recommended best practices through Azure Policy.

## Completion standard
A learner should not mark this lab complete until:
- the Azure Policy concept is clear
- at least one AKS policy scenario is understandable
- compliant and noncompliant outcomes can be explained
- validation confirms the governance-enforcement lifecycle end to end
