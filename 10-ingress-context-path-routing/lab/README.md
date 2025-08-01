# Lab Guide — Ingress Context Path Routing

## Lab objective
The objective of this lab is to help the learner implement path-based routing in AKS so that one ingress entry point can send requests to different backend services depending on the requested URL path.

This lab focuses on routing logic, multi-service traffic flow, ingress rule design, backend service mapping, and runtime reasoning. The goal is not to build a highly customized API gateway, but to make the learner comfortable with one of the most important ingress patterns used in Kubernetes application exposure.

## What you will build or configure
In this lab, you will deploy or reuse multiple backend applications and services, define an ingress resource with multiple path rules, and validate that different request paths are forwarded to the intended backends through one shared ingress entry point.

This is the first real multi-service ingress design pattern in the course.

## Why this lab matters
Path-based routing is often one of the earliest signs that a team is moving from “application deployment” into “platform traffic design.” Instead of exposing each service separately, the ingress layer becomes a shared request router.

Azure ingress-controller guidance explicitly describes using a single ingress controller and ingress rules to route traffic to multiple services through one IP address, and the StackSimplify advanced AKS sequence places context-path routing immediately after ingress basics for that exact reason.

## Estimated time
55 to 70 minutes

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
- multiple backend services running in AKS
- one ingress resource with multiple path rules
- one ingress entry point serving multiple applications
- confidence in explaining how URL paths determine backend selection

## Skills gained
- Designing path-based ingress rules in AKS
- Mapping multiple services behind one ingress layer
- Thinking in terms of runtime request routing
- Preparing for domain-based routing and TLS in later modules

## Real-world relevance
In real AKS environments, path-based routing is useful for multi-app exposure, transitional architectures, internal portals, or platform-managed service grouping behind a single ingress layer. It is also a strong way to teach deterministic routing behavior before introducing domain and certificate complexity.

## Completion standard
A learner should not mark this lab complete until:
- the path-based routing concept is clear
- multiple services are reachable through one ingress
- path rules forward traffic correctly
- validation confirms that each path reaches the intended backend
