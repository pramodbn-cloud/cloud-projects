# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab.

In this module, the most common failures usually come from confusing authentication with authorization, binding the wrong subject, over-scoping permissions, or assuming that a successful login means RBAC is working correctly. The goal is to strengthen access-governance reasoning, not only fix YAML.

---

## Common issue 1 — The learner confuses Microsoft Entra authentication with Kubernetes authorization

### Symptoms
- the learner signs in successfully
- access is still denied
- the learner assumes the cluster or login is broken

### Likely cause
The most common cause is that authentication succeeded but authorization was never granted for the requested action.

### Fix
Reframe the access path like this:
- Entra proves who the user is
- Kubernetes RBAC decides what that user can do
- successful authentication does not automatically grant permissions

### Re-validation
After the fix:
- confirm the learner can explain why a valid login and a denied action can both be correct at the same time

---

## Common issue 2 — The wrong subject is bound

### Symptoms
- the Role appears correct
- access behavior is unexpected
- the learner is unsure whether the right user or group is actually bound

### Likely cause
The RoleBinding or ClusterRoleBinding may reference the wrong Entra user or group subject.

### Fix
- inspect the binding carefully
- verify the intended user/group identity
- prefer a simple group-based example so the subject is easy to reason about
- avoid changing multiple layers at once

### Re-validation
After the fix:
- confirm that the binding now points to the intended subject
- retest the allowed action reasoning

---

## Common issue 3 — The learner grants cluster-wide access too early

### Symptoms
- the learner uses a ClusterRoleBinding immediately
- the example works, but the governance value feels weak
- later least-privilege reasoning becomes harder to recover

### Likely cause
The learner may be optimizing for quick success rather than safe scope.

### Fix
- reduce the design to one namespace-scoped Role and RoleBinding
- keep the first lab intentionally narrow
- expand to cluster scope only when the use case really requires it

### Re-validation
After the fix:
- confirm the learner can explain why namespace-scoped access is usually the better first learning pattern

---

## Common issue 4 — The learner thinks denied access means the lab failed

### Symptoms
- a blocked action occurs
- the learner becomes concerned that the configuration is broken
- the governance lesson feels negative rather than useful

### Likely cause
The learner may still be associating success only with “everything works” rather than “the right things work and the wrong things are blocked.”

### Fix
Reframe denied access like this:
- a denied action often proves that RBAC is working correctly
- least privilege means intentionally not granting unnecessary power
- blocked actions are part of a healthy governance model

### Re-validation
After the fix:
- confirm the learner can explain one denied action as a sign of good governance

---

## Common issue 5 — The learner does not understand why this module follows namespaces

### Symptoms
- namespaces and RBAC still feel like separate topics
- the module ordering feels weak
- the learner sees access design as arbitrary

### Likely cause
The learner may not yet see that namespace boundaries create the exact scope where least-privilege access becomes more practical and safer.

### Fix
Reframe the progression like this:
- Folder 16 created logical boundaries
- Folder 21 uses those boundaries to scope access
- namespace structure makes RBAC simpler, clearer, and safer

### Re-validation
After the fix:
- confirm the learner can explain why namespace design strengthens RBAC design

---

## Troubleshooting mindset
While debugging this module, always ask:
- did authentication succeed?
- did authorization also exist for this action?
- is the Role scoped correctly?
- is the binding attached to the right subject?
- am I validating both allowed and denied behavior?
- am I using namespace scope intentionally?

## Escalation rule
If the access-governance story still feels weak:
1. simplify to one namespace  
2. create one narrow Role  
3. bind one clearly identified group  
4. validate one allowed action  
5. validate one denied action  
6. explain authentication and authorization separately again  
7. prioritize least-privilege reasoning over “bigger access means easier success”  
