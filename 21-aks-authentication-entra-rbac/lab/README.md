# Lab Guide — AKS Authentication with Microsoft Entra ID and Kubernetes RBAC

## Lab objective
The objective of this lab is to help the learner understand and implement a governed AKS access pattern using Microsoft Entra ID for authentication and Kubernetes RBAC for authorization.

This lab focuses on identity integration, group-based access, namespace-scoped permissions, and least-privilege reasoning. The goal is not to design a full enterprise access model yet, but to make the learner comfortable with the core cluster-access pattern used in secure AKS environments.

## What you will build or configure
In this lab, you will review or configure AKS authentication through Microsoft Entra ID, create or review Kubernetes Role/ClusterRole and RoleBinding/ClusterRoleBinding patterns, and validate that access is granted only to the intended scope.

This creates the first true cluster-human-governance workflow in the AKS phase.

## Why this lab matters
A private registry, a secure ingress, and a working pipeline are still not enough if cluster access remains over-broad or poorly controlled. Authentication and authorization must become deliberate platform concerns.

Microsoft documents using Microsoft Entra ID for AKS authentication and Kubernetes RBAC for controlling cluster-resource access based on user identity or group membership. Microsoft’s best-practices guidance explicitly recommends Entra integration and least-privilege access assignments. 

## Estimated time
55 to 70 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a clear understanding of AKS authentication through Microsoft Entra ID
- a working or modeled Kubernetes RBAC permission pattern
- at least one namespace-scoped access example
- confidence in explaining why least-privilege cluster access matters

## Skills gained
- Understanding identity-aware AKS access
- Creating or reasoning about Roles and RoleBindings
- Thinking in terms of group-based authorization
- Connecting access control to earlier namespace and governance design

## Real-world relevance
In real AKS platforms, user access should be centrally authenticated and carefully scoped. Microsoft’s AKS documentation explicitly supports Entra-based authentication with Kubernetes RBAC, and also highlights Azure RBAC for Kubernetes authorization as another supported model depending on governance goals. 

## Completion standard
A learner should not mark this lab complete until:
- the Entra authentication concept is clear
- the RBAC model is understandable
- namespace- or cluster-scoped permission boundaries are visible
- validation confirms the access-governance flow end to end
