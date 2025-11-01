# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Kubernetes Namespaces lab.

This module is about cluster organization and governance boundaries, so the prerequisites are centered on a working AKS environment and at least one deployable workload.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- kubectl access to that cluster
- the ability to create namespaces and deploy workloads into them

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing or applying manifests

## Required permissions
You should be able to:
- create namespaces
- deploy or update workloads
- view resources across namespaces
- inspect resource placement and metadata

## Required prior understanding
Before starting this module, the learner should already understand:
- basic Deployments and Pods
- basic Services
- requests and limits from Folder 15
- that workloads in one cluster need organizational structure as the platform grows

## Required environment state
Before starting:
- an AKS cluster should already exist
- at least one simple workload should be available or easy to deploy
- the learner should be ready to compare flat cluster usage with namespace-structured usage
- the cluster should be healthy enough for multiple test deployments or resource views

## Namespace strategy recommendation
Keep the lab simple and meaningful.

Recommended example:
- one namespace for app A
- one namespace for app B
or
- one namespace for dev
- one namespace for test

This keeps the separation pattern easy to explain and prepares naturally for later governance controls.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- namespace: `team-a`
- namespace: `team-b`
- namespace: `dev`
- namespace: `test`
- workload names that remain readable inside each namespace

Keep names readable so later quota, RBAC, and production-cluster modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- namespaces can be created
- a sample workload can be deployed
- the learner is ready to think about cluster organization, not only single-workload behavior
