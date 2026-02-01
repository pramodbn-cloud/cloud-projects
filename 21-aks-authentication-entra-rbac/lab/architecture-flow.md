# Architecture Flow

## Purpose of this file
This file explains the logical identity-and-authorization flow used in the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab before implementation begins.

This module is about cluster-access governance — how a human identity is authenticated, how that identity is mapped into Kubernetes authorization, and how access is restricted to the minimum required scope.

## High-level architecture view
The workflow begins with a user who wants to interact with the AKS cluster. That user should not be treated as an anonymous or long-lived static cluster credential holder. Instead, authentication should come from Microsoft Entra ID, and authorization should then be handled through Kubernetes RBAC.

At a high level, the flow looks like this:

- the AKS cluster is integrated with Microsoft Entra ID
- a user signs in and obtains an Entra-based token for cluster access
- Kubernetes receives the authenticated identity information
- RBAC rules determine what that identity may do
- Roles or ClusterRoles define permissions
- RoleBindings or ClusterRoleBindings connect those permissions to users or groups
- access is allowed only at the intended scope

This turns cluster access from “whoever has admin credentials” into a governed identity model.

## Component roles

- **Microsoft Entra ID** — the identity provider for cluster user authentication  
- **AKS Cluster** — the target environment receiving authenticated requests  
- **User or Group** — the human principal requesting cluster access  
- **Kubernetes RBAC** — the authorization system deciding what actions are allowed  
- **Role / ClusterRole** — the permission definition  
- **RoleBinding / ClusterRoleBinding** — the binding between subject and permission scope  
- **Namespace / Cluster Scope** — the resource boundary where access applies  

## End-to-end flow

1. The AKS cluster is configured to use Microsoft Entra ID for user authentication.  
2. A user authenticates through Entra and presents a valid token.  
3. Kubernetes receives the authenticated identity context.  
4. RBAC rules are evaluated.  
5. If a matching RoleBinding or ClusterRoleBinding exists, the user gains the allowed actions only for that scope.  
6. If no matching authorization exists, access is denied.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- namespace understanding from Folder 16
- platform-governance maturity from earlier modules

This module also prepares the learner for:
- stronger production-cluster governance
- Azure RBAC for Kubernetes Authorization comparisons
- more advanced security and policy models

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- central identity integration
- least-privilege authorization
- group-based access design
- namespace scope versus cluster scope
- avoiding standing broad admin access
- access lifecycle as part of platform operations

These are the qualities that make cluster access defensible in real environments.

## What to keep in mind before implementation
Before starting the steps:
- authentication and authorization are different concerns
- Entra answers “who is this user?”
- RBAC answers “what may this user do?”
- namespace scope should be used intentionally where possible
- the goal is governed access, not only successful login
