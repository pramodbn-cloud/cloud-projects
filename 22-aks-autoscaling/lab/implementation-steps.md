# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS Autoscaling lab.

The goal is to create one clear elasticity path where workload demand can drive pod scaling and, when necessary, cluster node-pool scaling.

---

## Step 1 — Understand the autoscaling goal
Before enabling any autoscaler, understand what this module is trying to teach.

This lab is not only about turning on HPA or Cluster Autoscaler. It is about learning a full elasticity chain:

- the workload experiences demand
- HPA increases pod replicas
- scheduling pressure increases
- Cluster Autoscaler adds node capacity if needed
- the platform adapts rather than depending on manual intervention

At the end of this lab, you should have:
- one workload elasticity policy
- one node-pool elasticity policy
- one clear explanation of how they work together

## Step 2 — Reconfirm workload resource definitions
Before touching autoscaling, inspect the sample workload and confirm that its requests are defined clearly.

This is critical because requests influence scheduling decisions, and node autoscaling relies on unschedulable pods whose resource requests cannot currently be satisfied. Kubernetes and AKS guidance both emphasize the importance of resource requests in scaling-related behavior.

Do not treat autoscaling as independent from Folder 15.

## Step 3 — Reconfirm cluster and node-pool readiness
Now inspect:
- cluster health
- node-pool health
- current node count
- current min/max autoscaler boundaries if they exist

This gives the learner a baseline before any scaling event occurs.

## Step 4 — Review HPA as the workload-scaling layer
Now focus on the HPA side first.

Kubernetes documents HPA as the controller that automatically updates the replica count of workloads such as Deployments or StatefulSets to match observed demand.

At this stage, the learner should understand:
- HPA scales pods, not nodes
- HPA depends on observed metrics
- HPA is the first layer of response to workload pressure

## Step 5 — Create or review the HPA policy
Now define an HPA for the sample workload.

Keep the first scenario simple:
- one deployment target
- one metric such as CPU utilization
- a clear minimum and maximum replica range

The goal is to make the autoscaling policy easy to reason about and easy to validate.

## Step 6 — Review Cluster Autoscaler as the infrastructure-scaling layer
Now focus on the node side.

AKS documents Cluster Autoscaler as the component that scales node pools up when pods can’t be scheduled and scales nodes down when underused. AKS also documents enabling or updating it with node-pool min and max bounds.

The learner should understand:
- Cluster Autoscaler reacts to scheduling pressure
- it does not create demand on its own
- it is the infrastructure response to workload growth

## Step 7 — Enable or review Cluster Autoscaler settings
Now enable or inspect Cluster Autoscaler for the relevant node pool.

At this stage, confirm:
- min count
- max count
- whether autoscaling is active on the intended node pool
- whether the learner understands the scale boundaries

If needed, review cluster autoscaler profile concepts as a later tuning layer rather than the first learning focus. AKS documents cluster-wide autoscaler profiles and notes that one profile affects all node pools using Cluster Autoscaler.

## Step 8 — Trigger or simulate workload demand
Now create or observe a simple demand increase for the sample workload.

The learner does not need to build a complex load platform here. The important point is to produce a clear reason for the workload to need more replicas.

This is where the elasticity chain begins to become observable.

## Step 9 — Observe HPA behavior
Now watch the workload and inspect:
- current utilization behavior
- desired versus current replica counts
- whether HPA increases the replica count as expected

This is the first major runtime moment of the module.

## Step 10 — Observe scheduling pressure
Once the HPA creates more replicas, inspect whether:
- the new pods are scheduled immediately, or
- some pods remain pending because node capacity is insufficient

Pending pods are one of the key operational signals in the AKS cluster-autoscaling model. AKS docs explicitly describe Cluster Autoscaler reacting when pods can’t be scheduled because of resource constraints.

## Step 11 — Observe Cluster Autoscaler behavior
If pending pods appear or capacity pressure exists, observe:
- whether Cluster Autoscaler detects the need
- whether node count changes within the configured bounds
- whether the pending pods become schedulable after new capacity arrives

This is the core infrastructure-elasticity moment of the module.

## Step 12 — Compare pod scaling and node scaling explicitly
Now compare the two layers clearly.

The learner should be able to explain:
- HPA changes how many pods the workload wants
- Cluster Autoscaler changes how many nodes the cluster provides
- both are needed when workload growth exceeds current cluster capacity

This is the most important conceptual checkpoint in the module.

## Step 13 — Review scale-down and cost thinking
Now look beyond scale-up.

AKS also supports scale-down behavior when nodes become underutilized, and autoscaler profile tuning can change how aggressively that happens. AKS cost and autoscaler guidance connect scale-down behavior directly to efficiency and spend control.

The learner should understand:
- autoscaling is not only about adding capacity
- removing unused capacity safely is also part of the design
- scale-down behavior affects both cost and workload stability

## Step 14 — Explain the autoscaling lifecycle end to end
Now explain the flow in plain language:

- workload demand increases
- HPA requests more pod replicas
- the scheduler tries to place them
- if there is not enough room, pods remain pending
- Cluster Autoscaler adds node capacity
- the workload eventually runs at the desired scale

If the learner can explain this clearly, the module is doing its real job.

## Step 15 — Reflect on autoscaling as runtime elasticity engineering
Pause and think beyond the feature settings.

In this module, autoscaling means:
- workloads can respond automatically to demand
- clusters can add and remove capacity within policy bounds
- requests, scheduling, and node pools all matter together
- elasticity becomes an engineered platform behavior rather than a manual reaction

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the workload has clear resource requests
- an HPA policy exists or is clearly understood
- Cluster Autoscaler is enabled or clearly understood on the node pool
- the learner can observe or reason through load, replicas, and capacity interaction
- the learner understands why HPA and Cluster Autoscaler solve different parts of the same problem

## Step 16 — Prepare for governance enforcement
Before moving to the next module, understand what changes next.

The next module is **Azure Policy with AKS**. That means the learner will now shift from runtime elasticity into platform governance enforcement, where the cluster can evaluate whether workloads comply with policy requirements.

This is the bridge from scale control into compliance control.

---

## Implementation notes
- keep the first autoscaling scenario simple and observable
- always validate requests before validating autoscaling
- distinguish HPA events from Cluster Autoscaler events clearly
- do not rush into profile tuning before the basic chain is understood
- focus on elasticity behavior, not only enabled settings

## End-of-implementation summary
In this lab, you:
- revalidated workload resource definitions
- created or reviewed an HPA policy
- enabled or reviewed Cluster Autoscaler settings
- observed workload demand propagation through pods and nodes
- compared pod scaling with infrastructure scaling
- connected autoscaling to capacity and cost behavior
- practiced the first true runtime-elasticity pattern in the AKS phase

You are now ready to validate whether the AKS autoscaling lifecycle is clean, correct, and explainable.
