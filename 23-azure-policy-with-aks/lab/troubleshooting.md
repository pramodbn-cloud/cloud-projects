# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Azure Policy with AKS lab.

In this module, the most common failures usually come from assuming policy assignment alone is enough, misunderstanding audit versus deny effects, picking an over-broad policy too early, or treating noncompliance as a platform bug instead of a governance outcome. The goal is to strengthen policy-governance reasoning, not only fix assignment steps.

---

## Common issue 1 — The learner assigns a policy but does not understand why nothing appears enforced

### Symptoms
- a policy assignment exists
- the learner expects immediate blocking behavior
- the cluster behavior feels unchanged
- the learner assumes Azure Policy is not working

### Likely cause
The most common causes are:
- the AKS policy add-on is not actually active
- the chosen effect is audit rather than deny
- the learner is looking for admission blocking when the policy is only reporting compliance

### Fix
- confirm the AKS policy add-on is enabled
- inspect the assigned policy effect carefully
- separate compliance reporting from admission blocking in the learner’s reasoning

### Re-validation
After the fix:
- confirm the learner can explain whether the policy is supposed to audit or deny and why the observed behavior matches that

---

## Common issue 2 — The learner confuses Azure Policy with generic Kubernetes advice

### Symptoms
- the learner knows the best practice
- the learner does not see why Azure Policy adds value
- policy feels like documentation in another place

### Likely cause
The learner may not yet appreciate the difference between advice and enforceable control.

### Fix
Reframe Azure Policy like this:
- documentation tells people what they should do
- policy lets the platform evaluate or enforce what they actually do
- policy reduces drift and scales governance beyond manual review

### Re-validation
After the fix:
- confirm the learner can explain one concrete advantage of enforcement over best-practice documentation alone

---

## Common issue 3 — The first chosen policy is too broad or too disruptive

### Symptoms
- workloads are blocked unexpectedly
- the lab becomes harder to reason about
- the learner loses confidence in the policy layer

### Likely cause
The chosen policy may be too broad for a first-learning scenario, or the learner moved too quickly to deny-style enforcement without first understanding audit behavior.

### Fix
- simplify to one narrow, easy-to-understand built-in policy
- begin with audit-style understanding where possible
- introduce deny-style reasoning only after the effect is fully understood

### Re-validation
After the fix:
- confirm the learner can clearly explain the selected policy and its effect before retesting broader enforcement

---

## Common issue 4 — The learner sees a denied workload and assumes the cluster is broken

### Symptoms
- a manifest is blocked
- the learner assumes there is an AKS failure
- the governance lesson feels like platform instability

### Likely cause
The learner may still be associating “healthy platform” with “all workloads are accepted.”

### Fix
Reframe the denial like this:
- denial can be the correct and intended governance result
- a blocked noncompliant workload often proves the policy is functioning properly
- enforcement is part of healthy platform behavior when used intentionally

### Re-validation
After the fix:
- confirm the learner can explain one denied workload as evidence of successful governance rather than failure

---

## Common issue 5 — The learner does not understand why this module follows autoscaling and access governance

### Symptoms
- the module feels disconnected
- autoscaling, RBAC, and policy seem like separate topics
- the full governance story feels incomplete

### Likely cause
The learner may not yet see that a mature platform needs:
- runtime elasticity
- human-access control
- workload-behavior control

### Fix
Reframe the progression like this:
- Folder 21 controlled who can operate the cluster
- Folder 22 controlled how the cluster reacts to demand
- Folder 23 controls what kinds of workloads/configurations are allowed into the cluster

### Re-validation
After the fix:
- confirm the learner can explain why access governance and policy governance are different but complementary layers

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the AKS policy add-on actually active?
- what is the policy effect?
- am I expecting audit behavior or deny behavior?
- is this a policy problem or a misunderstanding of policy outcome?
- did I choose a policy scenario that is simple enough to learn from clearly?

## Escalation rule
If the policy-governance story still feels weak:
1. confirm the add-on is present  
2. choose one narrow built-in policy  
3. state the intended effect clearly  
4. test one compliant example  
5. test one noncompliant example  
6. review central compliance state  
7. prioritize governance reasoning over assignment count  
