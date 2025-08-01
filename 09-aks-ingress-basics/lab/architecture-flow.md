# Architecture Flow

## Purpose of this file
This file explains the logical runtime and traffic flow used in the AKS Ingress Basics lab before implementation begins.

This module is about traffic-entry architecture — how external traffic reaches workloads inside Kubernetes through a controlled ingress layer rather than through direct and fragmented exposure models.

## High-level architecture view
The workflow begins with an application running inside AKS behind a Kubernetes Service. That service is reachable inside the cluster, but it is not yet presented through a clean external traffic management layer.

Ingress adds that missing layer.

At a high level, the flow looks like this:

- the application runs in pods
- a Kubernetes Service provides stable internal access to those pods
- an ingress controller watches ingress resources and implements their routing logic
- an ingress resource defines how incoming external HTTP/HTTPS traffic should be handled
- external requests arrive at the ingress entry point
- the ingress controller forwards the request to the correct service
- the service forwards traffic to the correct pods

This is the basic traffic chain the learner must fully understand before moving to advanced routing patterns.

## Component roles

- **Client / External User** — sends the incoming HTTP or HTTPS request  
- **Ingress Endpoint** — the external entry point exposed by the ingress controller  
- **Ingress Resource** — the Kubernetes object that defines traffic rules  
- **Ingress Controller** — the implementation layer that watches ingress rules and enforces them  
- **Kubernetes Service** — the stable internal service endpoint for the application  
- **Pods / Workload** — the backend application instances that actually serve the request  
- **AKS Cluster Network** — the environment where all of this traffic is coordinated  

## End-to-end flow

1. A backend application is deployed into AKS.  
2. A Kubernetes Service exposes that application internally.  
3. An ingress controller is installed or made available in the cluster.  
4. An ingress resource is created to define how incoming traffic should be routed.  
5. External traffic reaches the ingress endpoint.  
6. The ingress controller maps the request to the intended service.  
7. The service forwards the request to the application pods.  
8. The response returns back through the same layered path.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- a basic deployed application or sample workload
- an ingress controller strategy in the cluster

This module also prepares the learner for:
- path-based routing
- hostname-based routing
- DNS automation
- TLS termination and ingress security
- ingress-level troubleshooting and performance analysis

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- clear traffic boundaries
- service-to-ingress relationship
- ingress controller ownership
- external IP or endpoint readiness
- routing determinism
- runtime observability of the path

These are the qualities that make ingress usable in a real environment rather than only technically present.

## What to keep in mind before implementation
Before starting the steps:
- ingress does not replace the service; it sits above it
- an ingress resource alone does nothing without a controller
- think in terms of request path, not only YAML objects
- keep the first scenario simple and deterministic
- aim to understand the chain from client to pod fully
