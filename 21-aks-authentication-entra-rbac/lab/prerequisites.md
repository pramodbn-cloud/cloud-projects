# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab.

This module depends on both identity-provider readiness and Kubernetes authorization concepts, so the prerequisites are cluster- and governance-oriented.

## Required account access
You should have working access to:
- Azure
- Microsoft Entra ID
- an AKS cluster you can manage
- kubectl access to the cluster
- the ability to inspect or configure AKS identity/authentication settings

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for RBAC manifests
- optional Entra group-management access if doing the lab practically with groups

## Required permissions
You should be able to:
- inspect AKS authentication configuration
- create or review Kubernetes Roles and RoleBindings
- inspect namespaces
- test access behavior using the intended identity model
- review Azure-side identity or group configuration if needed

## Required prior understanding
Before starting this module, the learner should already understand:
- namespaces from Folder 16
- that workloads and teams need boundaries inside the cluster
- that AKS platform maturity includes not only workload governance but also human-access governance
- the difference between authentication and authorization conceptually

## Required environment state
Before starting:
- an AKS cluster should already exist
- the learner should know whether the cluster is already integrated with Microsoft Entra ID
- at least one namespace should already exist for scoped-access examples
- the learner should be ready to work with group-based access design

## Authorization-model note
This module is centered on:
- Microsoft Entra ID for authentication
- Kubernetes RBAC for authorization

Microsoft also documents Azure RBAC for Kubernetes Authorization as another supported authorization model, but this lab is intentionally centered on the Kubernetes RBAC pattern first so the learner understands native Kubernetes permission design clearly. 

## Access-design recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one namespace
- one read-only or limited role
- one group-based binding

This keeps the first access-governance pattern easy to validate.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- namespace: `team-a`
- role: `namespace-reader`
- rolebinding: `team-a-readers-binding`
- group names that reflect function clearly

Keep names readable so later governance and Azure RBAC comparisons remain understandable.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- the identity model is understood
- at least one namespace exists
- the learner is ready to think about least-privilege access rather than broad cluster admin habits
