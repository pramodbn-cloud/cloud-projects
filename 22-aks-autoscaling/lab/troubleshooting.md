# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS Autoscaling lab.

In this module, the most common failures usually come from confusing HPA with Cluster Autoscaler, trying to autoscale workloads that lack meaningful requests, expecting HPA to create node capacity, or treating a configured autoscaler as proof that elasticity is actually working. The goal is to strengthen runtime-elasticity reasoning, not only fix manifests.

---

## Common issue 1 — The learner confuses HPA with Cluster Autoscaler

### Symptoms
- the learner says “autoscaling” but cannot specify which layer
- pod and node behavior are described interchangeably
- troubleshooting becomes unclear very quickly

### Likely cause
The learner is treating all scaling behavior as one feature instead of two linked controllers.

### Fix
Reframe the layers like this:
- HPA changes the number of pods
- Cluster Autoscaler changes the number of nodes
- HPA reacts to workload metrics
- Cluster Autoscaler reacts to scheduling pressure

### Re-validation
After the fix:
- confirm the learner can explain one scaling event at the pod layer and one at the node layer separately

---

## Common issue 2 — HPA is configured, but the workload does not scale meaningfully

### Symptoms
- the HPA object exists
- replicas do not change as expected
- the learner assumes autoscaling is broken

### Likely cause
The workload may not be generating enough metric pressure, or the metric source/target is not aligned to the lab scenario.

### Fix
- confirm the workload is a valid scaling candidate
- confirm the metric target is reasonable
- keep the first lab scenario simple, such as CPU-based scaling
- verify that the cluster exposes the required metrics for HPA

### Re-validation
After the fix:
- confirm that the HPA now has a meaningful reason to increase or decrease replicas

---

## Common issue 3 — HPA increases replicas, but pods remain pending

### Symptoms
- HPA appears to work
- replica count increases
- some pods do not run
- the learner assumes HPA failed

### Likely cause
This often means HPA worked correctly, but there is not enough node capacity to host the new pods.

### Fix
- inspect pod scheduling status
- check for pending pods
- verify whether Cluster Autoscaler is enabled and correctly bounded
- confirm the node pool can scale within min/max settings

### Re-validation
After the fix:
- confirm that pending pods become schedulable once node capacity increases

---

## Common issue 4 — The learner expects Cluster Autoscaler to solve poor workload resource definitions

### Symptoms
- scaling feels inconsistent
- the learner expects node autoscaling to compensate for unclear workload definitions
- requests are weak or absent

### Likely cause
Cluster Autoscaler reasons from schedulability, which depends heavily on resource requests. Weak workload contracts make the autoscaling story less predictable.

### Fix
Reframe the dependency like this:
- requests and limits are the workload’s resource contract
- autoscaling builds on that contract
- autoscaling cannot replace clear resource definitions

### Re-validation
After the fix:
- confirm the learner can explain why Folder 15 was a prerequisite for this module

---

## Common issue 5 — The learner treats enabled autoscaling as proof of good scaling design

### Symptoms
- the learner enables HPA and Cluster Autoscaler
- the design is assumed to be complete
- there is little thought about bounds, cost, or workload fit

### Likely cause
The learner may be focusing on feature activation rather than elasticity engineering.

### Fix
Reframe autoscaling like this:
- autoscaling is only useful when the workload, thresholds, and node-pool bounds make sense
- poor min/max settings can still create bad behavior
- scale-down behavior matters as much as scale-up
- load testing is needed to validate real scaling quality

AKS well-architected guidance explicitly recommends load testing both pod and cluster autoscaler behavior.

### Re-validation
After the fix:
- confirm the learner can explain one reason “enabled” is not the same as “well tuned”

---

## Troubleshooting mindset
While debugging this module, always ask:
- is this a pod-scaling issue or a node-scaling issue?
- does the workload have meaningful requests?
- are the HPA metrics appropriate?
- are pods pending because capacity is insufficient?
- is Cluster Autoscaler enabled with realistic bounds?
- am I validating scale behavior, not just object existence?

## Escalation rule
If the autoscaling story still feels weak:
1. simplify to one workload  
2. validate requests clearly  
3. validate HPA behavior alone  
4. validate Cluster Autoscaler settings alone  
5. observe pending pods explicitly  
6. compare pod and node scaling again  
7. prioritize elasticity reasoning over feature toggles  
