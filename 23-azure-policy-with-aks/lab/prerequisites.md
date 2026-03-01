# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Azure Policy with AKS lab.

This module depends on both AKS readiness and Azure-side governance control, so the prerequisites are cluster- and compliance-oriented.

## Required account access
You should have working access to:
- Azure
- Azure Policy
- an AKS cluster you can manage
- the ability to inspect or enable AKS add-ons
- kubectl access to the cluster

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- optional Azure portal access for compliance views and policy assignment inspection
- a code editor for sample workload manifests

## Required permissions
You should be able to:
- enable or inspect the Azure Policy add-on on AKS
- assign or inspect Azure Policy definitions or initiatives
- deploy sample workloads for compliant/noncompliant behavior checks
- inspect compliance state in Azure

## Required prior understanding
Before starting this module, the learner should already understand:
- requests and limits from Folder 15
- namespaces from Folder 16
- AKS access governance from Folder 21
- that policy can be used to enforce behavior across workloads and teams

## Required environment state
Before starting:
- an AKS cluster should already exist
- the learner should know whether the Azure Policy add-on is already enabled
- at least one simple workload manifest should be available or easy to create for policy testing
- the learner should be ready to compare compliant and noncompliant resource behavior

## Policy strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- use one built-in AKS/Kubernetes policy
- begin in audit or warn-oriented understanding first
- then reason about deny behavior carefully
- use one clear compliant/noncompliant manifest example

This keeps the governance effect easy to understand and avoids needless disruption.

## Built-in-policy note
Microsoft provides built-in policy definitions specifically for AKS, and also provides built-in initiatives such as pod security standards and deployment safeguards.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- policy assignment names that reflect the control goal clearly
- manifest names that indicate compliant versus noncompliant examples
- namespace selection that stays simple for the first test

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- Azure Policy access is available
- the learner understands the difference between advisory guidance and enforced governance
- a simple workload policy scenario is ready to test
