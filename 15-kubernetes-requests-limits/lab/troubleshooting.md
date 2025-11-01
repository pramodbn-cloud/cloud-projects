# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Kubernetes Requests + Limits lab.

In this module, the most common failures usually come from confusing requests with limits, assuming that requests are optional in shared clusters, using unrealistic values, or thinking that a successful deployment automatically means the workload is well governed. The goal is to strengthen resource-governance reasoning, not only fix manifests.

---

## Common issue 1 — The learner confuses requests and limits

### Symptoms
- the learner treats requests and limits as the same thing
- the values are copied mechanically without understanding
- scheduling and runtime behavior feel conceptually mixed together

### Likely cause
The learner has not yet separated placement logic from runtime boundary logic.

### Fix
Reframe the difference like this:
- requests are what the scheduler plans around
- limits are what the container runtime enforces
- requests help place the workload
- limits help contain the workload

### Re-validation
After the fix:
- confirm the learner can explain the difference in one or two clear sentences without reading from YAML

---

## Common issue 2 — The workload is unschedulable after adding requests

### Symptoms
- the deployment was previously accepted
- after adding requests, the pod cannot be scheduled
- the learner assumes Kubernetes is behaving incorrectly

### Likely cause
The requested CPU or memory may exceed what the cluster can currently place on available nodes.

### Fix
- inspect node capacity and current cluster usage
- reduce the requested values to something realistic for the lab
- confirm the scheduler is rejecting based on real capacity constraints, not arbitrary behavior

### Re-validation
After the fix:
- confirm the pod now schedules successfully with realistic requests
- explain why the scheduler behaved correctly

---

## Common issue 3 — The workload runs, but the learner still does not see why requests matter

### Symptoms
- the pod schedules successfully
- the YAML now contains requests
- the learner feels the cluster would have worked anyway

### Likely cause
The learner may be looking only at the immediate happy path and not at multi-workload or capacity-planning behavior.

### Fix
Reframe requests like this:
- without requests, the scheduler has weaker resource intent from the workload
- in shared clusters, that increases ambiguity
- requests make placement and planning more predictable
- predictability matters more as workload count grows

### Re-validation
After the fix:
- confirm the learner can explain one shared-cluster advantage of explicit requests

---

## Common issue 4 — Limits are set, but the learner does not understand why they help

### Symptoms
- the YAML contains limits
- the learner sees them as optional decoration
- the idea of runtime containment feels abstract

### Likely cause
The learner may not yet be thinking in terms of noisy-neighbor protection or runaway resource use.

### Fix
Reframe limits like this:
- limits define the maximum allowed CPU or memory usage
- they help stop one workload from consuming resources without bound
- this matters especially in shared clusters where other workloads also need protection

### Re-validation
After the fix:
- confirm the learner can explain one runtime-stability reason for setting limits

---

## Common issue 5 — The learner thinks this module is less important than ingress/TLS

### Symptoms
- the module feels less visible because there is no public endpoint change
- the learner sees it as internal tuning only
- the production-readiness value feels lower

### Likely cause
The learner may be prioritizing public-facing behavior over internal workload stability.

### Fix
Reframe the module like this:
- ingress and TLS make the application reachable and trusted from outside
- requests and limits make the application behave responsibly inside
- public readiness without internal discipline still leaves the platform fragile

### Re-validation
After the fix:
- confirm the learner can explain why “well exposed” is not the same as “well governed”

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the workload healthy first?
- are the request values realistic for the cluster?
- are the limit values realistic for the workload?
- am I mixing scheduler logic and runtime logic together?
- can I explain the shared-cluster value of these settings?

## Escalation rule
If the resource-governance story still feels weak:
1. simplify to one workload  
2. inspect cluster capacity clearly  
3. set one small realistic request  
4. set one slightly higher realistic limit  
5. compare before and after explicitly  
6. explain the scheduler/runtime difference again  
7. prioritize predictability reasoning over YAML memorization  
