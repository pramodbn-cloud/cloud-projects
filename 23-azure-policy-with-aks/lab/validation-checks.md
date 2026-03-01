# Validation Checks

## Purpose of this file
This file confirms whether the Azure Policy with AKS lab is complete and correct.

The goal is not only to verify that a policy was assigned, but to confirm that the learner understands how Azure Policy evaluates or enforces standards against AKS workloads and surfaces compliance state centrally.

## Validation approach
For this lab, validation is based on:
- add-on correctness
- built-in policy correctness
- policy-effect understanding
- compliant/noncompliant scenario understanding
- central compliance visibility
- learner explanation ability

## Check 1 — The learner understands the Azure Policy add-on for AKS
Confirm that:
- the learner can explain why the add-on is needed
- the learner understands that it connects Azure Policy to AKS/Kubernetes evaluation
- the learner knows that policy assignment without cluster integration is not enough

This proves the platform-control path is understood.

## Check 2 — The learner understands Gatekeeper’s role in the design
Confirm that:
- the learner knows the AKS policy add-on extends Gatekeeper
- the learner can explain that this enables admission-controller-style governance behavior

This proves enforcement architecture understanding.

## Check 3 — A meaningful built-in policy scenario is selected
Confirm that:
- the chosen policy is relevant to AKS/Kubernetes workload governance
- the learner can explain what the policy is trying to enforce
- the assignment scope is intentional

This proves that the policy is not arbitrary.

## Check 4 — Audit versus deny behavior is clearly understood
Confirm that the learner can clearly explain:
- audit = surface/report noncompliance
- deny/enforce = block noncompliant workloads

This is one of the most important operational understanding checks in the module.

## Check 5 — Compliant and noncompliant behavior can be explained
Confirm that:
- the learner can identify one compliant example
- the learner can identify one noncompliant example
- the learner understands why each outcome happens

This proves that the learner understands policy as behavior, not only as assignment metadata.

## Check 6 — Central compliance visibility is understood
Confirm that:
- the learner understands Azure Policy provides centralized compliance reporting
- the learner can explain why this matters in shared or multi-cluster environments

This proves the learner understands governance at scale.

## Check 7 — The learner understands how this module connects to earlier governance modules
Confirm that:
- the learner can explain how policy relates to namespaces, requests/limits, and access governance
- the learner sees policy enforcement as another layer of platform control

This proves that the course architecture is landing correctly.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why Azure Policy matters in AKS
- how the policy add-on connects Azure governance to Kubernetes enforcement
- why audit and deny have different operational consequences
- why centralized compliance reporting matters
- why this is a major platform-governance step

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the add-on model is understood
- one built-in policy scenario is clear
- compliant/noncompliant outcomes are understandable
- central compliance visibility is understood
- the learner is ready to move into workload identity patterns

## If validation fails
If any validation step fails:
- revisit the add-on purpose first
- revisit the chosen built-in policy
- re-check audit versus deny reasoning
- re-check the compliant/noncompliant examples
- use `troubleshooting.md` for common Azure Policy with AKS issues
