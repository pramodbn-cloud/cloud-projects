# Validation Checks

## Purpose of this file
This file confirms whether the AKS Autoscaling lab is complete and correct.

The goal is not only to verify that scaling settings exist, but to confirm that the learner understands the complete elasticity chain from workload demand to pod scaling to node scaling.

## Validation approach
For this lab, validation is based on:
- workload readiness
- request correctness
- HPA correctness
- Cluster Autoscaler correctness
- elasticity-chain understanding
- learner explanation ability

## Check 1 — The workload has meaningful resource requests
Confirm that:
- the workload defines requests clearly
- the learner understands why requests matter for scheduling and autoscaling
- the workload is a valid candidate for autoscaling reasoning

This proves the elasticity model has a useful resource contract to work with.

## Check 2 — The learner understands HPA correctly
Confirm that:
- the learner can explain that HPA scales pod replicas
- the HPA is tied to a supported metric signal such as CPU or memory
- the learner understands HPA as workload elasticity, not node elasticity

Kubernetes documents HPA as a controller that automatically updates workload replica count based on observed metrics.

## Check 3 — The learner understands Cluster Autoscaler correctly
Confirm that:
- the learner can explain that Cluster Autoscaler scales node pools
- the learner understands that it reacts to unschedulable pods and underutilized nodes
- the learner knows the min/max range or autoscaler boundaries for the lab

AKS documents Cluster Autoscaler behavior and node-pool min/max configuration explicitly.

## Check 4 — HPA and Cluster Autoscaler are not being confused
Confirm that the learner can clearly explain:
- HPA = desired pod count changes
- Cluster Autoscaler = available node capacity changes

This is one of the most important technical understanding checks in the module.

## Check 5 — The learner understands the role of pending pods
Confirm that:
- the learner knows pending pods are a key signal for node-level scaling
- the learner can explain why HPA can succeed logically while pods still wait for node capacity
- the learner understands why pod scaling alone may be insufficient

This proves platform-runtime maturity. AKS documents that HPA can still run even if Cluster Autoscaler is disabled, but pods can remain unscheduled if resources are exhausted.

## Check 6 — Scale-up and scale-down reasoning are both present
Confirm that:
- the learner can explain not only how capacity grows, but also why scale-down matters
- the learner understands that autoscaling affects both performance and cost efficiency

AKS cost and autoscaler guidance tie scale-down behavior to efficiency and spend.

## Check 7 — The learner understands this module as a continuation of Folder 15
Confirm that:
- the learner can explain why requests and limits had to come before autoscaling
- the learner sees this module as extending resource-governance into elasticity behavior

This proves the course progression is coherent.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why HPA and Cluster Autoscaler solve different parts of scaling
- why requests matter
- why unschedulable pods matter
- why load testing and tuning both layers together is important
- why autoscaling is a major production-readiness step

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the workload is a valid autoscaling candidate
- HPA behavior is understood
- Cluster Autoscaler behavior is understood
- the learner can explain the full elasticity chain
- the learner is ready to move into policy and governance enforcement

## If validation fails
If any validation step fails:
- revisit workload requests first
- revisit HPA and Cluster Autoscaler definitions separately
- re-check node-pool autoscaler boundaries
- re-check pending-pod reasoning
- use `troubleshooting.md` for common AKS autoscaling issues
