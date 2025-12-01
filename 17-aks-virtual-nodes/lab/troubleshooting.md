# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS Virtual Nodes lab.

In this module, the most common failures usually come from missing Azure CNI compatibility, misunderstanding what the virtual node actually represents, targeting workloads incorrectly, or assuming that every workload should use virtual nodes just because the feature exists. The goal is to strengthen execution-model reasoning, not only fix setup steps.

---

## Common issue 1 — Virtual nodes do not work because the cluster networking is incompatible

### Symptoms
- the learner tries to enable or use virtual nodes
- the setup path fails or the feature cannot be used properly
- the execution model never becomes available in a clean way

### Likely cause
The most common cause is that the cluster does not meet the networking requirement.

Microsoft explicitly documents that AKS virtual nodes require advanced networking / Azure CNI. StackSimplify’s AKS virtual-node guide calls out the same requirement.

### Fix
- inspect the AKS networking model carefully
- confirm whether the cluster uses advanced networking
- do not continue assuming the feature should work on an incompatible cluster
- if needed, shift to a compatible cluster design for the lab

### Re-validation
After the fix:
- confirm that the cluster now matches the networking requirement
- retry the virtual-node configuration path

---

## Common issue 2 — The learner understands the feature, but not what actually runs the workload

### Symptoms
- the learner knows the term “virtual node”
- the learner assumes there is a hidden AKS VM node behind it
- the runtime model still feels vague

### Likely cause
The learner may not yet distinguish Kubernetes scheduling abstractions from actual Azure runtime backing.

### Fix
Reframe the execution path like this:
- AKS still orchestrates the workload
- the virtual node is the Kubernetes-facing abstraction
- Azure Container Instances is the serverless runtime that actually runs the pod

### Re-validation
After the fix:
- confirm the learner can explain the execution model end to end without calling the virtual node a normal worker VM

---

## Common issue 3 — The workload does not land on the intended virtual-node path

### Symptoms
- the cluster is healthy
- virtual-node capability exists
- the workload is deployed but not on the intended execution model
- the learner assumes the platform is inconsistent

### Likely cause
The placement intent may not have been expressed clearly or correctly in the workload definition.

### Fix
- inspect the workload spec carefully
- confirm how the workload is targeted to virtual-node execution
- reduce the test scenario to one simple workload with one clear placement goal
- reapply only after the targeting logic is unambiguous

### Re-validation
After the fix:
- confirm the workload now lands on the intended execution path

---

## Common issue 4 — The learner thinks virtual nodes replace standard node pools

### Symptoms
- the learner sees the feature working
- the learner starts treating virtual nodes as the default better choice
- the trade-off thinking becomes weak

### Likely cause
The learner may be focusing on burst convenience and ignoring workload-fit and platform design trade-offs.

### Fix
Reframe the model like this:
- standard node pools remain the normal durable execution model for many workloads
- virtual nodes provide an additional option for certain scenarios
- the right choice depends on workload characteristics and platform goals

### Re-validation
After the fix:
- confirm the learner can explain one good-fit virtual-node scenario and one reason standard node pools still matter

---

## Common issue 5 — The learner does not see why this module belongs after namespaces

### Symptoms
- the module feels disconnected from Folder 16
- namespace organization and execution-model flexibility feel unrelated
- the progression seems weak

### Likely cause
The learner may not yet see that workload governance has multiple layers:
- logical placement
- resource placement
- execution placement

### Fix
Reframe the progression like this:
- Folder 15 governed workload resources
- Folder 16 governed workload grouping
- Folder 17 governs where and how workloads execute
- this is a natural platform-architecture progression

### Re-validation
After the fix:
- confirm the learner can explain why namespace structure and execution-model choice both matter in a mature cluster

---

## Troubleshooting mindset
While debugging this module, always ask:
- does the cluster meet the virtual-node networking requirement?
- do I understand that ACI is the actual runtime backing?
- have I targeted the workload intentionally?
- am I comparing virtual-node and standard-node execution clearly?
- am I treating virtual nodes as one option, not the only option?

## Escalation rule
If the virtual-node story still feels weak:
1. confirm networking compatibility  
2. confirm virtual-node capability visibility  
3. simplify to one lightweight workload  
4. make the placement intent explicit  
5. compare standard versus virtual execution again  
6. explain orchestration versus runtime backing clearly  
7. prioritize execution-model reasoning over feature memorization  
