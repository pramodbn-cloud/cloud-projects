# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Ingress Context Path Routing lab.

This module is a direct extension of ingress basics, so the prerequisites are strongly runtime- and routing-oriented.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- kubectl access to that AKS cluster
- the ability to create or modify ingress resources and backend services

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing or applying manifests
- optional browser or curl-style testing capability for traffic validation

If using an unmanaged ingress-controller pattern, Helm may also be required depending on the controller installation method. AKS continues to recommend the managed application routing add-on for ingress scenarios.

## Required permissions
You should be able to:
- deploy multiple workloads into AKS
- create multiple Services
- create or modify Ingress resources
- inspect ingress-controller behavior
- test external traffic against the ingress endpoint

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- Kubernetes Services
- how an ingress controller implements ingress rules
- the difference between internal service exposure and external traffic routing

## Required environment state
Before starting:
- an AKS cluster should already exist
- an ingress-controller strategy should already be active
- at least one working ingress example from Folder 09 should be understood or available
- two or more simple backend services should be ready or easy to deploy

## Ingress-class awareness
Keep the current ingress class pattern in mind. The StackSimplify course update explicitly notes using `spec.ingressClassName: nginx` in the ingress sections instead of the older deprecated annotation-only style.

## Path-routing scenario recommendation
Keep the lab simple and deterministic.

Recommended example:
- `/app1` routes to backend service A
- `/app2` routes to backend service B

This keeps validation and troubleshooting easy to understand before moving into hostname-based routing later.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- deployment: `app1-web`
- deployment: `app2-web`
- service: `app1-service`
- service: `app2-service`
- ingress: `multi-app-path-ingress`

Keep names readable so later advanced routing modules can extend them cleanly.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- ingress basics are already understood
- multiple backend services can be deployed or reused
- one ingress-controller strategy is active and known
- the learner is ready to think in multi-service routing terms
