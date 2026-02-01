# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab.

The goal is to create one clear access-governance path where a human identity is authenticated through Microsoft Entra ID and is then authorized only for the intended Kubernetes scope.

---

## Step 1 — Understand the access-governance goal
Before changing any cluster settings or applying RBAC manifests, understand what this module is trying to teach.

This lab is not only about getting a user to connect to the cluster. It is about creating a trustworthy access model:

- Microsoft Entra ID authenticates the user
- Kubernetes RBAC authorizes only the intended actions
- access is scoped intentionally
- broad admin access is not treated as the default answer

At the end of this lab, you should have:
- one identity-aware cluster access path
- one RBAC permission pattern
- one clear explanation of authentication versus authorization

## Step 2 — Reconfirm the AKS authentication model
Before focusing on RBAC, inspect the AKS cluster and confirm whether Microsoft Entra integration is enabled or already in place.

Microsoft documents AKS integration with Microsoft Entra ID for cluster-user authentication. This should be treated as the identity entry point for human access. 

Do not continue until the learner is clear about how the cluster authenticates users.

## Step 3 — Reconfirm namespace scope for the lab
Now choose the namespace boundary you will use for the first RBAC example.

Keep it simple:
- one namespace
- one clearly named workload or resource set
- one bounded scope for access validation

This matters because namespace-scoped permissions are the cleanest way to learn least-privilege behavior first.

## Step 4 — Design the permission model
Now decide what the user or group should be allowed to do.

Recommended first pattern:
- read-only or low-risk access in one namespace

The learner should understand that RBAC design begins with the question:
- what minimum set of actions is actually needed?

This is the core least-privilege reasoning moment of the module.

## Step 5 — Create or review the Kubernetes Role
Now define a Role for the namespace-scoped permission set.

At this stage, focus on:
- limiting actions intentionally
- keeping scope narrow
- making the role name clearly reflect purpose

Kubernetes RBAC is designed exactly for this kind of scoped permission control, and Microsoft’s AKS docs explicitly support using Kubernetes RBAC with Entra identities and groups. 

## Step 6 — Bind the Role to a user or group
Now create a RoleBinding that attaches the Role to the intended Entra-authenticated subject.

Recommended approach:
- prefer a group rather than a single individual user where possible

Microsoft’s AKS documentation explicitly discusses granting access based on user identity or group membership, and operator best-practice guidance recommends least-privilege and Entra-based group management. 

This is one of the most important learning moments in the module because it turns abstract permission design into a real governed access path.

## Step 7 — Review how the authenticated identity reaches Kubernetes RBAC
Now step back and connect the two layers:

- Entra authenticates the human user
- Kubernetes RBAC reads that identity or group context
- RoleBindings determine the allowed actions

The learner should understand that a successful Entra login alone does not automatically grant broad cluster power.

## Step 8 — Validate the allowed actions
Now test or reason through the allowed operations for the bound subject.

Confirm:
- the allowed action works in the intended namespace
- the learner can identify exactly why it works
- the permission comes from the binding, not from broad admin inheritance

This is the core authorization validation point.

## Step 9 — Validate the denied actions
Now test or reason through at least one action that should not be allowed.

Confirm:
- the denied action is outside the granted scope
- the learner can explain why it is denied
- denial is treated as a sign of good governance, not failure

This is a critical maturity point in access-control learning.

## Step 10 — Compare namespace-scoped and cluster-scoped access
Now compare:
- a namespace Role/RoleBinding
- a broader ClusterRole/ClusterRoleBinding model

The learner should understand:
- namespace-scoped access is usually safer for first grants
- cluster-scoped access should be used only when truly necessary
- broader access increases governance risk

## Step 11 — Review Azure RBAC as a related but different path
Now briefly connect this lab to the broader AKS authorization landscape.

Microsoft also supports Azure RBAC for Kubernetes Authorization, which unifies access control using Azure role assignments, but this lab intentionally starts with Kubernetes RBAC so the learner understands native Kubernetes permission scope clearly first. 

This keeps the course architecture strong and layered.

## Step 12 — Explain the authentication-and-authorization lifecycle end to end
Now explain the flow in plain language:

- the user authenticates through Microsoft Entra ID
- the AKS cluster recognizes the authenticated identity
- Kubernetes RBAC checks Roles and RoleBindings
- access is granted only for the intended resources and actions

If the learner can explain this clearly, the module is doing its real job.

## Step 13 — Reflect on cluster access as platform governance
Pause and think beyond the YAML.

In this module, Entra + Kubernetes RBAC means:
- cluster access is centrally authenticated
- authorization is explicit and scoped
- group-based access is cleaner than unmanaged individual admin sprawl
- platform operations become safer and more governable

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the cluster authentication path through Microsoft Entra ID is understood
- one namespace-scoped RBAC example exists or is clearly modeled
- the learner understands Role versus RoleBinding
- allowed and denied access patterns are both understandable
- the learner understands the difference between namespace-scope and cluster-scope permissions

## Step 14 — Prepare for cluster elasticity
Before moving to the next module, understand what changes next.

The next module is **AKS Autoscaling**. That means the learner will now shift from human-access governance into runtime elasticity and capacity response.

This is the bridge from access control into scale control.

---

## Implementation notes
- keep the first RBAC scenario narrow and easy to explain
- prefer group-based binding over user-specific sprawl for the first model
- validate denied actions as carefully as allowed ones
- keep authentication and authorization conceptually separate at all times
- focus on least privilege, not only successful access

## End-of-implementation summary
In this lab, you:
- reviewed AKS authentication through Microsoft Entra ID
- chose a namespace-scoped access model
- created or reviewed a Kubernetes Role
- bound that role to a user or group
- validated allowed and denied access behavior
- compared namespace-scoped and cluster-scoped access
- practiced the first true human-access-governance pattern in the AKS phase

You are now ready to validate whether the AKS authentication and RBAC lifecycle is clean, correct, and explainable.
