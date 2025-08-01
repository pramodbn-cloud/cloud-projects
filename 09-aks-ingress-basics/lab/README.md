# Lab Guide — AKS Ingress Basics

## Lab objective
The objective of this lab is to help the learner understand and implement a basic ingress workflow in AKS so that traffic can reach an application through a controlled entry layer rather than through ad hoc exposure patterns.

This lab focuses on ingress architecture, ingress controller behavior, service-to-ingress relationship, and end-to-end traffic understanding. The goal is not to build a highly customized ingress platform yet, but to make the learner comfortable with the basic runtime flow that later advanced ingress modules will build on.

## What you will build or configure
In this lab, you will use a simple application and Kubernetes service inside AKS, ensure an ingress controller path is available, define an ingress resource, and validate that traffic reaches the intended backend through the ingress layer.

This creates the first true traffic-engineering workflow in the course.

## Why this lab matters
Ingress is one of the most important runtime concepts in Kubernetes platform operations because it changes how applications are exposed and controlled. A team that understands ingress is no longer thinking only about deploying workloads — it is thinking about how users reach workloads safely and predictably.

AKS documentation explains ingress as the traffic-management resource for external HTTP-like access to services, and current AKS guidance recommends the managed application routing add-on for NGINX-based ingress scenarios.

## Estimated time
50 to 65 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a clear ingress architecture understanding
- a simple application exposed through ingress
- an understanding of how ingress relates to services and controllers
- confidence in explaining the external-to-internal traffic path in AKS

## Skills gained
- Understanding ingress in the context of AKS platform design
- Connecting application services to an ingress-based entry point
- Thinking about traffic flow rather than only workload deployment
- Preparing for later routing, DNS, and TLS modules

## Real-world relevance
In real AKS environments, ingress often becomes the first major platform layer that application teams depend on. It centralizes external traffic entry and becomes the base for routing, certificates, domain mapping, and operational traffic troubleshooting. Microsoft also documents both managed and unmanaged NGINX ingress patterns for AKS, with the managed application routing approach being recommended.

## Completion standard
A learner should not mark this lab complete until:
- the ingress concept is clear
- the ingress-to-service flow is visible
- traffic reaches the intended backend correctly
- validation confirms the runtime path is understandable end to end
