# Validation Checks

## Purpose of this file
This file confirms whether the Kubernetes Requests + Limits lab is complete and correct.

The goal is not only to verify that resource values exist in the manifest, but to confirm that the learner understands how those values affect scheduling, runtime protection, and overall cluster behavior.

## Validation approach
For this lab, validation is based on:
- workload readiness
- request correctness
- limit correctness
- scheduler understanding
- runtime-boundary understanding
- learner explanation ability

## Check 1 — The workload is healthy
Confirm that:
- the sample deployment or pod is running
- the cluster accepted the workload cleanly
- the learner can inspect the workload state successfully

This proves that the lab is working from a stable application baseline.

## Check 2 — CPU and memory requests are explicitly defined
Confirm that:
- the workload includes CPU requests
- the workload includes memory requests
- the learner can explain that these values are primarily scheduler-facing

This proves that the workload now communicates resource expectations to the cluster.

## Check 3 — CPU and memory limits are explicitly defined
Confirm that:
- the workload includes CPU limits
- the workload includes memory limits
- the learner can explain that these values are runtime guardrails

This proves that the workload now has explicit containment boundaries.

## Check 4 — The learner understands the difference between requests and limits
Confirm that the learner can clearly explain:
- requests = what the scheduler plans around
- limits = what runtime consumption must not exceed

This is one of the most important technical understanding checks in the module.

## Check 5 — The “before” and “after” comparison is understood
Confirm that the learner can explain:
- how the workload looked before clear resource definitions
- how the workload behaves conceptually after adding them
- why the cluster is easier to reason about now

This proves that the module has changed the learner’s model, not only the YAML.

## Check 6 — Shared-cluster reasoning is present
Confirm that the learner can explain:
- why a workload without defined resources is harder to operate safely
- how requests and limits reduce noisy-neighbor risk
- why shared cluster fairness depends on explicit workload contracts

This proves that the learner is thinking like a platform engineer.

## Check 7 — The learner understands the connection to later namespace policy
Confirm that:
- the learner knows requests and limits connect naturally to LimitRange and ResourceQuota controls
- the learner understands this module as part of a broader governance chain, not an isolated topic

This proves that the resource-discipline story is maturing.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why requests help scheduling
- why limits help runtime protection
- why AKS best practices recommend defining them
- why this is a major production-readiness step after ingress/TLS work

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the workload is healthy
- requests and limits are explicit
- the learner understands scheduler versus runtime differences
- shared-cluster reasoning is present
- the learner is ready to move into namespace-level governance

## If validation fails
If any validation step fails:
- re-check workload health first
- re-check resource field placement and values
- revisit the difference between scheduling and runtime enforcement
- simplify the before/after comparison
- use `troubleshooting.md` for common resource-governance issues
