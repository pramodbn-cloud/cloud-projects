# Validation Checks

## Purpose of this file
This file confirms whether the AKS Virtual Nodes lab is complete and correct.

The goal is not only to verify that a workload can run on a virtual node, but to confirm that the learner understands why virtual nodes exist, how they depend on networking, and how they differ from standard VM-backed node pools.

## Validation approach
For this lab, validation is based on:
- cluster readiness
- networking compatibility
- virtual-node capability correctness
- workload placement correctness
- execution-model understanding
- learner explanation ability

## Check 1 — The cluster is compatible with virtual nodes
Confirm that:
- the AKS cluster is healthy
- the learner has verified the required networking model
- the learner understands that advanced networking / Azure CNI is required

This is one of the most important technical validation points in the module.

## Check 2 — The learner understands the ACI-backed execution model
Confirm that:
- the learner can explain what actually runs the pod when virtual nodes are used
- the learner understands that AKS still orchestrates the pod
- the learner understands that ACI provides the underlying serverless execution backing

This proves that the module has moved beyond feature usage into architecture understanding.

## Check 3 — The virtual-node capability is active or clearly validated
Confirm that:
- the learner can identify the virtual-node execution option in the cluster
- the setup path used for the lab is clear
- the learner can explain what was enabled or reviewed

This proves that the execution extension is real and visible.

## Check 4 — The workload is targeted correctly
Confirm that:
- the sample workload was intentionally placed on the virtual-node path
- the learner can explain how that placement intent was expressed
- the resulting workload behavior matches the design expectation

This proves that execution-model choice is being used intentionally.

## Check 5 — Placement and runtime behavior are observable
Confirm that:
- the learner can inspect where the workload landed
- the learner can distinguish virtual-node-backed execution from standard-node execution
- the execution path is understandable and not assumed blindly

This proves that the learner is reading the system, not just applying manifests.

## Check 6 — The learner understands when virtual nodes are useful
Confirm that the learner can explain:
- why fast burst capacity can be useful
- why virtual nodes may reduce wait time compared to scaling VM nodes
- why not every workload automatically belongs on virtual nodes

This proves platform-design maturity. Microsoft explicitly highlights rapid scale-up without waiting for cluster autoscaler-provisioned VMs.

## Check 7 — The learner understands the trade-off against standard node pools
Confirm that:
- the learner can compare the two execution models clearly
- the learner understands that standard node pools still remain important
- the learner can explain why virtual nodes are a targeted platform option rather than a universal replacement

This proves operational realism.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- what virtual nodes are
- why Azure CNI matters first
- how ACI fits into the design
- why virtual nodes help with burst and fast-start workloads
- why this module is a real platform-capacity step, not only an AKS feature demo

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- networking compatibility is understood
- the virtual-node execution path is clear
- the workload is targeted intentionally
- the learner understands ACI-backed execution clearly
- the learner is ready to move into secure image supply and later scaling topics

## If validation fails
If any validation step fails:
- re-check networking compatibility first
- re-check the virtual-node setup path
- re-check workload placement intent
- revisit the difference between orchestration and execution backing
- use `troubleshooting.md` for common virtual-node issues
