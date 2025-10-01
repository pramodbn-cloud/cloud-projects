# Architecture Flow

## Purpose of this file
This file explains the logical runtime and naming flow used in the Domain Name Based Routing lab before implementation begins.

This module is about hostname-driven traffic selection — how one ingress layer can inspect the requested host header and route traffic to the correct backend service.

## High-level architecture view
The workflow begins with multiple backend applications running in AKS, each exposed internally through its own Kubernetes Service. Instead of distinguishing these applications only by URL path, each application receives its own hostname inside the Azure-controlled DNS zone.

At a high level, the flow looks like this:

- multiple backend applications run in the cluster
- each backend is exposed internally through a Service
- Azure DNS contains hostnames for each application
- ExternalDNS can help keep those hostnames aligned to the ingress endpoint
- the ingress resource defines rules based on hostname
- a client request arrives with a specific hostname
- the ingress controller inspects the host and selects the correct backend service
- the selected Service forwards traffic to the corresponding pods

This turns public application identity into part of the routing decision itself.

## Component roles

- **Client / External User** — sends the request to a specific hostname  
- **Azure DNS** — resolves the hostname to the ingress-facing endpoint  
- **Ingress Endpoint** — the shared external entry point  
- **Ingress Resource** — contains hostname-based routing rules  
- **Ingress Controller** — interprets and enforces the host rules  
- **Service A / Service B / Service N** — internal stable service endpoints  
- **Pods / Workloads** — the backend application instances serving the requests  

## End-to-end flow

1. Multiple backend applications run in AKS.  
2. Each backend is exposed internally with its own Service.  
3. Azure DNS provides hostnames for each application within the delegated zone.  
4. ExternalDNS can automate those records based on ingress intent.  
5. A client sends a request to a specific hostname.  
6. The ingress controller inspects the host rule.  
7. The matching backend service is selected.  
8. The selected service forwards traffic to the correct pods.  
9. The response returns to the client through the ingress layer.  

## Dependency awareness
This module depends on:
- Folder 09 for ingress fundamentals
- Folder 10 for route-selection thinking
- Folder 11 for Azure DNS authority
- Folder 12 for Azure DNS automation through ExternalDNS

This module also prepares the learner for:
- TLS and certificate integration
- production-style hostname design
- later environment or tenant separation strategies

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- hostname clarity
- DNS-to-ingress alignment
- ingress rule readability
- service isolation under shared ingress
- future certificate boundaries
- ease of reasoning about public application identity

These are the qualities that make host-based routing practical in real environments.

## What to keep in mind before implementation
Before starting the steps:
- host-based routing depends on DNS and ingress working together
- hostname rules are often cleaner than path rules for public app separation
- the host header becomes the routing key
- each hostname should belong clearly inside the delegated Azure DNS scope
- the goal is predictable application identity and routing, not only successful requests
