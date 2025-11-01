# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Kubernetes Namespaces lab.

In this module, the most common failures usually come from treating namespaces as only folders, placing workloads inconsistently, assuming namespaces provide full isolation automatically, or creating too many namespaces without a real organizational reason. The goal is to strengthen cluster-organization reasoning, not only fix kubectl commands.

---

## Common issue 1 — The learner sees namespaces as only labels or folders

### Symptoms
- namespaces are created, but their operational value feels weak
- the learner understands the command but not the platform reason
- the module feels less important than ingress or TLS modules

### Likely cause
The learner may still be thinking in single-application terms instead of shared-cluster terms.

### Fix
Reframe namespaces like this:
- they create meaningful cluster boundaries
- they make resource views cleaner
- they provide the scope for future quotas, limits, and access controls
- they help multi-team and multi-environment clusters stay understandable

### Re-validation
After the fix:
- confirm the learner can explain one strong operational advantage of namespaces beyond “organization”

---

## Common issue 2 — Workloads are deployed into the wrong namespace

### Symptoms
- the intended namespace exists
- the workload appears somewhere else
- the learner becomes confused when viewing resources
- resource listings look inconsistent

### Likely cause
The namespace may not have been specified consistently during deployment or update.

### Fix
- inspect the workload metadata carefully
- verify which namespace the object actually lives in
- redeploy or update the workload in the intended namespace
- keep the first lab simple so placement is easy to verify

### Re-validation
After the fix:
- confirm the workload appears in the correct namespace-scoped view

---

## Common issue 3 — The learner creates too many namespaces too early

### Symptoms
- many namespaces exist
- the learner cannot clearly explain why each one exists
- the cluster now feels more cluttered, not less

### Likely cause
The learner may be trying to demonstrate complexity rather than meaningful structure.

### Fix
- reduce the design to one or two strong namespace examples
- ensure each namespace has one clear reason to exist
- focus on readability and reuse, not quantity

### Re-validation
After the fix:
- confirm every retained namespace has a clear operational purpose

---

## Common issue 4 — The learner assumes namespaces automatically provide full security isolation

### Symptoms
- the learner overstates what namespaces do
- namespaces are treated as complete isolation boundaries
- later governance concepts feel redundant

### Likely cause
The learner may not yet distinguish logical organization from full security/network isolation.

### Fix
Reframe namespaces like this:
- namespaces provide logical separation and scope many controls
- they are important governance boundaries
- they do not automatically solve every security or network boundary concern
- other controls are still needed for stronger isolation models

### Re-validation
After the fix:
- confirm the learner can explain both the value and the limitation of namespaces clearly

---

## Common issue 5 — The learner understands namespaces but not why this module follows requests and limits

### Symptoms
- the module feels disconnected from the previous one
- the learner sees namespaces and resource controls as unrelated
- the governance progression feels weak

### Likely cause
The learner may not yet see that requests/limits are workload-level controls, while namespaces provide the broader scope where policy can later be enforced.

### Fix
Reframe the progression like this:
- requests and limits govern one workload
- namespaces group many workloads
- grouped workloads can then receive namespace-level quotas, defaults, and access controls
- this is why namespace structure naturally follows workload resource discipline

### Re-validation
After the fix:
- confirm the learner can explain why namespace governance is the natural next step after per-workload resource governance

---

## Troubleshooting mindset
While debugging this module, always ask:
- does each namespace have a clear purpose?
- are workloads placed intentionally?
- am I treating namespaces as governance-friendly boundaries, not just names?
- do I understand their limits as well as their value?
- can I explain how they prepare the cluster for later policy controls?

## Escalation rule
If the namespace story still feels weak:
1. simplify to one or two namespaces  
2. place one workload clearly in each  
3. compare flat cluster view versus namespace view explicitly  
4. connect the design to future quotas and RBAC  
5. explain value and limitation together  
6. prioritize platform reasoning over command repetition  
