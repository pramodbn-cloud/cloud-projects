# Architecture Flow

## Purpose of this file
This file explains the logical governance-enforcement flow used in the Azure Policy with AKS lab before implementation begins.

This module is about compliance control — how centrally defined rules are attached to the AKS cluster and then evaluated against workloads and cluster resources so that violations can be surfaced or blocked.

## High-level architecture view
The workflow begins with an AKS cluster that already runs workloads. Those workloads may or may not conform to expected standards. Azure Policy introduces a central evaluation and enforcement layer.

At a high level, the flow looks like this:

- the Azure Policy add-on is installed or enabled for the AKS cluster
- one or more built-in policy definitions or initiatives are assigned
- cluster components and workloads are evaluated against those rules
- the policy effect determines the result, such as audit or deny
- compliance is reported centrally
- the platform operator can now enforce standards instead of only recommending them

This turns governance from documentation into a control system.

## Component roles

- **Azure Policy** — the centralized governance and compliance engine  
- **Azure Policy Add-on for AKS** — the cluster integration layer for Kubernetes policy evaluation  
- **Built-in Policy Definition / Initiative** — the actual rule set being enforced or audited  
- **AKS Cluster** — the target environment where policy applies  
- **Kubernetes Workload / Object** — the resource being evaluated  
- **Compliance View** — the centralized reporting and state-tracking output  
- **Admission / Enforcement Layer** — the runtime point where noncompliant resources may be blocked depending on policy effect  

## End-to-end flow

1. Azure Policy is connected to the AKS cluster through the AKS policy add-on.  
2. A built-in AKS/Kubernetes policy or initiative is assigned.  
3. Kubernetes resources are evaluated against the policy rule.  
4. Compliant resources pass as expected.  
5. Noncompliant resources are either audited or denied, depending on policy effect.  
6. Compliance state becomes visible centrally in Azure.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- namespace and workload-governance understanding
- access to Azure Policy assignment and review

This module also prepares the learner for:
- stronger security baselines
- image and workload integrity controls
- production compliance and platform-hardening workflows

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- policy scope
- audit versus deny choice
- rollout safety
- governance visibility
- policy-to-workload interaction
- avoiding uncontrolled cluster drift

These are the qualities that make policy useful in real environments.

## What to keep in mind before implementation
Before starting the steps:
- Azure Policy is not a replacement for understanding Kubernetes
- policy effect matters as much as policy definition
- audit mode and deny mode have very different operational consequences
- safe rollout of policy matters
- the goal is enforceable consistency, not only more rules
