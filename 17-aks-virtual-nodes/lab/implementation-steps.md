# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS Virtual Nodes lab.

The goal is to create one clear alternative-execution path where a selected workload runs through the virtual-node model backed by Azure Container Instances.

---

## Step 1 — Understand the virtual-node goal
Before enabling anything, understand what this module is trying to teach.

This lab is not about replacing all AKS worker nodes. It is about learning that AKS can expose more than one compute model under one Kubernetes control plane:

- standard VM-backed nodes for many normal workloads
- ACI-backed virtual-node execution for fast and flexible burst-style scenarios

At the end of this lab, you should have:
- one virtual-node execution path
- one sample workload targeted to it
- one clear explanation of how this differs from standard node-pool execution

## Step 2 — Reconfirm AKS cluster and networking compatibility
Before working on virtual nodes, verify:
- the AKS cluster is healthy
- the current context is correct
- the cluster uses the networking model required for virtual nodes

Microsoft’s AKS documentation states that virtual nodes require advanced networking / Azure CNI. This is one of the most important readiness checks in the module.

Do not proceed until this prerequisite is clear.

## Step 3 — Review the role of ACI in the design
Now step back and understand what is actually providing the execution.

The learner should understand:
- the Kubernetes control plane remains AKS
- the virtual node is the Kubernetes-facing abstraction
- the actual runtime backing is Azure Container Instances

This is the first major conceptual checkpoint in the module.

## Step 4 — Enable or review the virtual-node capability
Now enable or review the virtual-node configuration for the cluster using the chosen approach for your environment.

Microsoft provides both portal and CLI guidance for creating AKS clusters that use virtual nodes, and also provides separate Azure Container Instances virtual-node guidance.

At this stage, focus on:
- the networking/subnet relationship
- successful virtual-node presence in the cluster
- clarity about which node representation corresponds to the ACI-backed path

## Step 5 — Inspect the node view
Once the virtual-node capability is active, inspect the node view in the cluster.

The learner should verify:
- the virtual node appears as a schedulable target pattern
- the cluster now exposes both standard and virtual execution options
- the execution model shift is visible at the Kubernetes layer

This is where the feature becomes real from the operator perspective.

## Step 6 — Prepare a lightweight workload for virtual-node placement
Now choose a lightweight sample workload and prepare it for the virtual-node path.

Keep the first scenario simple. The goal is not to stress the platform, but to observe execution placement and understand why the platform now has another compute option.

## Step 7 — Target the workload to the virtual-node path
Now configure the workload so it is intentionally directed to the virtual-node execution model.

At this stage, the learner should pay attention to:
- how placement intent is expressed
- how this differs from a generic deployment with no execution preference
- how Kubernetes can still manage the workload while the runtime backing changes

This is the most important implementation moment in the module.

## Step 8 — Apply the workload and inspect placement
Apply the workload and inspect:
- whether it is scheduled successfully
- whether it is running through the intended virtual-node path
- whether the node-placement result matches the design expectation

Do not assume success only because the deployment object exists. Validate actual placement behavior.

## Step 9 — Compare the execution model with standard node pools
Now compare:
- how the workload would run on a normal AKS node pool
- how it runs through the virtual-node path

The learner should focus on:
- provisioning model differences
- speed and elasticity reasoning
- where this is useful operationally
- where standard node pools still remain the better fit

This is the core platform-engineering reasoning moment of the module.

## Step 10 — Review networking implications
Now revisit the networking side.

The learner should understand:
- why Azure CNI / advanced networking mattered
- why ACI-backed pods still need cluster communication
- why networking must be designed correctly before virtual nodes become useful

This is an important realism check: virtual-node success depends on more than deployment syntax.

## Step 11 — Reflect on workload suitability
Now think about which workloads make sense here.

The learner should consider:
- bursty workloads
- transient workloads
- fast-start scenarios
- cases where waiting for VM scale-out is undesirable

Microsoft explicitly highlights rapid scale-up as a core advantage of virtual nodes on ACI.

## Step 12 — Explain the execution lifecycle end to end
Now explain the flow in plain language:

- the AKS cluster exists
- virtual-node capability extends the cluster with ACI-backed compute
- a workload is targeted to that execution path
- AKS still orchestrates it
- the runtime backing is different from a standard VM node
- the platform gains faster burst-style execution options

If the learner can explain this clearly, the module is doing its real job.

## Step 13 — Reflect on virtual nodes as capacity design
Pause and think beyond the configuration.

In this module, virtual nodes mean:
- one AKS cluster can expose more than one execution model
- burst capacity does not always have to wait for VM growth
- workload placement becomes a platform design choice
- execution flexibility becomes part of cluster architecture

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the AKS cluster networking prerequisites are understood
- a virtual-node execution path is active or clearly understood
- a lightweight workload has been targeted to it
- the learner can inspect placement behavior
- the learner understands why ACI-backed execution is different from VM-backed execution

## Step 14 — Prepare for secure image delivery
Before moving to the next module, understand what changes next.

The next module is **ACR with AKS**. That means the learner will now shift from execution-model flexibility into image-supply discipline, which is essential no matter where workloads actually run.

This is the bridge from execution design into secure workload sourcing.

---

## Implementation notes
- keep the first virtual-node scenario simple and lightweight
- validate networking prerequisites before everything else
- focus on placement reasoning rather than feature novelty
- compare virtual and standard execution explicitly
- think of this as a platform-capacity pattern, not a generic node feature

## End-of-implementation summary
In this lab, you:
- reconfirmed AKS networking compatibility
- reviewed the ACI-backed virtual-node execution model
- enabled or reviewed the virtual-node capability
- targeted a lightweight workload to the virtual-node path
- validated placement behavior
- compared virtual-node execution with standard node-pool execution
- practiced the first true hybrid-execution pattern in the AKS phase

You are now ready to validate whether the virtual-node lifecycle is clean, correct, and explainable.
