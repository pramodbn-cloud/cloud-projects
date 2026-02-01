# Validation Checks

## Purpose of this file
This file confirms whether the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab is complete and correct.

The goal is not only to verify that a user can access the cluster, but to confirm that the learner understands the difference between authentication and authorization and can reason about least-privilege access in AKS.

## Validation approach
For this lab, validation is based on:
- Entra authentication understanding
- RBAC role correctness
- binding correctness
- scope correctness
- allowed/denied behavior correctness
- learner explanation ability

## Check 1 — The learner understands Microsoft Entra ID as the authentication layer
Confirm that:
- the learner knows Entra is the identity provider for user authentication
- the learner can explain that authentication answers “who is the user?”
- the learner understands that successful authentication alone does not imply broad access

Microsoft documents AKS integration with Microsoft Entra ID for user authentication. 

## Check 2 — The learner understands Kubernetes RBAC as the authorization layer
Confirm that:
- the learner can explain that RBAC decides what actions are allowed
- the learner can distinguish Role/ClusterRole from RoleBinding/ClusterRoleBinding
- the learner keeps authentication and authorization conceptually separate

Microsoft documents Kubernetes RBAC with Entra identity/group membership in AKS. 

## Check 3 — The Role is scoped correctly
Confirm that:
- the Role or ClusterRole reflects the intended permission level
- the permissions are not broader than needed
- the learner can explain the minimum required action set

This proves least-privilege reasoning.

## Check 4 — The binding is correct
Confirm that:
- the RoleBinding or ClusterRoleBinding points to the intended subject
- the learner understands whether the subject is a user or group
- the access path is intentional and readable

This proves that the authorization path is real and auditable.

## Check 5 — Namespace scope is understood
Confirm that:
- the learner can explain why namespace-scoped access is usually safer for early grants
- the learner understands how namespace boundaries from Folder 16 make RBAC more meaningful

This proves the course progression is being connected correctly.

## Check 6 — Allowed and denied behaviors are both understood
Confirm that:
- the learner can identify one allowed action and why it succeeds
- the learner can identify one denied action and why it is blocked
- denial is understood as healthy governance, not tool failure

This is one of the most important practical checks in the module.

## Check 7 — Group-based access value is understood
Confirm that:
- the learner can explain why group-based access is often stronger operationally than per-user binding sprawl
- the learner understands that Entra group membership can be used to control Kubernetes RBAC access in AKS

This proves operational maturity. 

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why AKS should authenticate users through Microsoft Entra ID
- how Kubernetes RBAC scopes access
- why least privilege matters
- why namespace structure helps access design
- why this is a major production-readiness step after runtime and delivery work

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the learner clearly distinguishes authentication and authorization
- the RBAC example is narrow and intentional
- allowed and denied actions are understandable
- group-based access design is present
- the learner is ready for broader AKS governance and autoscaling topics

## If validation fails
If any validation step fails:
- revisit authentication versus authorization
- re-check the Role and RoleBinding scope
- revisit namespace-scoped design
- simplify the first access model further
- use `troubleshooting.md` for common AKS access-governance issues
