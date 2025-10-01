# Lab Guide — Domain Name Based Routing

## Lab objective
The objective of this lab is to help the learner implement hostname-based routing in AKS so that one ingress layer can send traffic to different backend services based on the requested domain name.

This lab focuses on host rules, DNS-backed ingress exposure, multi-service hostname mapping, and runtime request-selection logic. The goal is not to build a large multi-tenant ingress estate yet, but to make the learner comfortable with one of the most important production-style ingress patterns used in Kubernetes platforms.

## What you will build or configure
In this lab, you will deploy or reuse multiple backend applications and services, define one or more ingress rules using hostnames inside the Azure-controlled DNS zone, and validate that requests for different hostnames are forwarded to the intended backends.

This creates the first real hostname-driven ingress architecture pattern in the course.

## Why this lab matters
Path-based routing is useful, but many real environments benefit from giving each application or service a distinct hostname. This makes ownership clearer, certificates cleaner, URL design more natural, and traffic behavior easier to reason about externally.

The StackSimplify AKS learning path explicitly includes Domain Name based Routing using Ingress with ExternalDNS. AKS ingress guidance also states that ingress supports name-based virtual hosting, which is exactly the capability this module operationalizes.

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
- ingress rules based on hostnames instead of only paths
- DNS records aligned to those hostnames
- confidence in explaining how hostname-based requests select the intended backend

## Skills gained
- Designing host-based ingress rules in AKS
- Mapping public DNS names to specific backend services
- Thinking in terms of application identity through hostname
- Preparing for TLS and certificate-based ingress security

## Real-world relevance
In real AKS platforms, host-based routing is often preferred for cleaner public application identity, clearer application separation, and simpler TLS management. Azure’s AKS architecture guidance for multitenant solutions also explicitly references host-based routing as a valid and often important design pattern.

## Completion standard
A learner should not mark this lab complete until:
- the host-based routing concept is clear
- multiple hostnames resolve correctly
- ingress rules route each hostname to the intended backend
- validation confirms the runtime and DNS behavior end to end
