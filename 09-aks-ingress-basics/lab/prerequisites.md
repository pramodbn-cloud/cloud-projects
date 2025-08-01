# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS Ingress Basics lab.

This module is the beginning of the advanced AKS phase, so the prerequisites are more platform-oriented than the earlier Azure DevOps foundation modules.

## Required account access
You should have working access to:
- Azure
- an AKS cluster that you can manage
- kubectl access to that AKS cluster
- the ability to inspect cluster resources and apply manifests

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell, Bash, or similar
- a code editor for reviewing or applying manifests
- optional browser access for Azure portal inspection

If you plan to use Helm for an unmanaged ingress controller scenario, Helm should also be available.

## Required permissions
You should be able to:
- access AKS cluster credentials
- deploy workloads into the cluster
- create Services
- create Ingress resources
- inspect ingress controller resources
- view public endpoint or load balancer behavior associated with ingress

## Required prior understanding
Before starting this module, the learner should already understand:
- basic Kubernetes Pods and Deployments
- basic Kubernetes Services
- Azure DevOps foundation concepts from earlier modules
- the idea that application deployment and traffic exposure are different concerns

## Required environment state
Before starting:
- an AKS cluster should already exist
- a simple backend application or sample workload should be available or easy to deploy
- an ingress-controller approach should be chosen

Recommended options:
- AKS application routing add-on with managed NGINX ingress
- or an unmanaged NGINX ingress controller pattern if your environment intentionally uses that

Current AKS guidance recommends the application routing add-on for ingress in AKS, while unmanaged ingress-controller setup is still documented for certain scenarios and troubleshooting flows.

## Ingress-class awareness
The StackSimplify course update notes that for ingress sections, the deprecated annotation-based class pattern should be replaced with `spec.ingressClassName: nginx`. The learner should be aware of this before beginning.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- deployment: `sample-webapp`
- service: `sample-webapp-clusterip-service`
- ingress: `sample-webapp-ingress`

Keep names readable so later advanced routing modules can build on them cleanly.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- kubectl is working
- a sample workload can be deployed
- an ingress-controller strategy is chosen
- the learner is ready to think in terms of runtime traffic architecture
