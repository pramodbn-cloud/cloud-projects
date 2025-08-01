# Architecture Flow

## Purpose of this file
This file explains the logical runtime and routing flow used in the Ingress Context Path Routing lab before implementation begins.

This module is about multi-service traffic routing — how a single ingress entry point can inspect the request path and direct traffic to different backend services in the cluster.

## High-level architecture view
The workflow begins with multiple applications running in AKS, each exposed internally through its own Kubernetes Service. Instead of creating a separate public exposure pattern for each service, one ingress layer handles all incoming requests and routes them according to path rules.

At a high level, the flow looks like this:

- multiple backend applications run in separate pod groups
- each backend application is exposed internally through a Service
- one ingress controller watches a single ingress resource with multiple rules
- the ingress resource defines path-based routing logic
- the client sends a request to one shared ingress entry point
- the ingress controller inspects the path and selects the correct backend service
- the selected service forwards traffic to its corresponding pods

This turns ingress from a simple front door into a route-selection layer. Azure documentation supports this pattern by describing ingress rules and controllers as the mechanism to route one IP to multiple services.

## Component roles

- **Client / External User** — sends requests with specific URL paths  
- **Shared Ingress Endpoint** — the single public entry point for multiple applications  
- **Ingress Resource** — defines multiple routing rules based on URL path  
- **Ingress Controller** — interprets and enforces those rules  
- **Service A / Service B / Service N** — internal stable service endpoints for each backend  
- **Pods / Workloads** — the actual application instances that serve the request  
- **AKS Cluster Network** — the runtime environment where the routing is implemented  

## End-to-end flow

1. Multiple backend applications are deployed into AKS.  
2. Each backend is exposed internally through its own Service.  
3. One ingress controller is available in the cluster.  
4. One ingress resource defines multiple path rules.  
5. A client request arrives at the shared ingress endpoint.  
6. The ingress controller evaluates the request path.  
7. The matching backend service is selected.  
8. The selected service forwards the request to the correct pods.  
9. The response returns through the same ingress path to the client.  

## Dependency awareness
This module depends on:
- Folder 09 for ingress fundamentals
- a working AKS cluster
- multiple sample workloads or services ready for routing

This module also prepares the learner for:
- hostname-based routing
- DNS integration
- TLS termination
- more production-style traffic and naming patterns

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- shared entry-point design
- deterministic rule matching
- path naming clarity
- backend isolation behind one front door
- ease of troubleshooting route-to-service mapping
- readiness for later DNS and TLS layering

These are the qualities that make path routing manageable in real environments.

## What to keep in mind before implementation
Before starting the steps:
- path routing works on top of ingress fundamentals
- services remain the real internal targets
- one ingress rule set can front multiple applications
- path design should stay intentional and readable
- the goal is deterministic routing, not manifest complexity
