# Lab Guide — AKS Virtual Nodes

## Lab objective
The objective of this lab is to help the learner understand and implement a basic AKS virtual-node workflow so that selected workloads can run on Azure Container Instances while still being orchestrated through AKS.

This lab focuses on the execution model, networking prerequisites, workload targeting, and runtime reasoning around when virtual nodes are useful. The goal is not to build a complete production serverless platform, but to make the learner comfortable with one of the most important AKS execution-extension patterns.

## What you will build or configure
In this lab, you will confirm the AKS networking prerequisites, deploy or review the virtual-node capability, target a sample workload to the virtual-node-backed execution path, and compare that behavior with standard VM-node execution.

This creates the first true alternative-execution-capacity workflow in the course.

## Why this lab matters
A mature platform is not defined only by how it exposes applications or organizes workloads. It is also defined by how flexibly it can place workloads when speed, elasticity, or cost model differences matter.

Microsoft documents that virtual nodes run AKS pods on ACI and let you scale quickly without waiting for traditional VM node provisioning. Microsoft also documents portal and CLI-based setup flows for virtual nodes, and notes the advanced-networking prerequisite.

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
- a clear understanding of how AKS virtual nodes work
- a configured or reviewed virtual-node capability
- a workload targeted to the virtual-node execution model
- confidence in explaining when virtual nodes make operational sense

## Skills gained
- Understanding AKS virtual nodes as an ACI-backed execution pattern
- Thinking about workload placement beyond standard node pools
- Connecting Kubernetes scheduling intent to hybrid execution backends
- Preparing for more advanced scaling and cluster-design discussions later

## Real-world relevance
In real AKS environments, virtual nodes can be useful for burst capacity, transient workloads, or cases where waiting for VM node provisioning is undesirable. Microsoft explicitly highlights rapid scale-up and pay-for-runtime characteristics because ACI provides serverless backing for those pods.

## Completion standard
A learner should not mark this lab complete until:
- the virtual-node concept is clear
- the networking and execution prerequisites are understood
- a workload can be targeted to the virtual-node path
- validation confirms that the execution-model difference is understandable
