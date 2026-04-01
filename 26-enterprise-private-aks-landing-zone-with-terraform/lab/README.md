# Lab Guide — Enterprise Private AKS Landing Zone with Terraform

## Lab objective
The objective of this lab is to help the learner understand and model a **private, enterprise-grade AKS landing zone** using Terraform.

This lab focuses on:
- private control-plane access
- segmented network architecture
- private endpoints
- private DNS zone integration
- managed identity
- observability and security baseline thinking
- Terraform-driven landing-zone composition

The goal is not to dump every Azure service into one design. The goal is to help the learner build a **clear, defensible, enterprise-ready AKS platform baseline**.

## What you will build or configure
In this lab, you will design or implement a landing zone that includes:
- a resource and environment boundary
- virtual network and subnet planning
- private AKS API exposure
- private endpoint strategy for core supporting services
- private DNS design
- managed identity and access patterns
- Terraform-based deployment structure

This creates the first true **enterprise AKS landing-zone architecture** in the repository.

## Why this lab matters
Microsoft’s baseline AKS architecture guidance explicitly frames AKS as a system that crosses networking, identity, security, and operations boundaries. Private clusters restrict control-plane access by exposing the API server over a private endpoint, and private DNS must be configured correctly for the control plane and supporting private services to resolve properly. AVM exists to standardize good infrastructure-as-code module quality and is well aligned to this type of enterprise platform design.

## Estimated time
75 to 100 minutes

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
- a clear private AKS landing-zone design
- a Terraform structure that represents enterprise platform intent
- a sound understanding of private control-plane and private dependency design
- confidence in explaining why this architecture is stronger than a default cluster setup

## Skills gained
- Enterprise AKS architecture thinking
- Private control-plane design
- Private endpoint and private DNS reasoning
- Terraform-led landing-zone composition
- Platform security and observability baseline design

## Real-world relevance
This is exactly the kind of architecture pattern that stands out in real platform engineering, cloud architecture, and DevSecOps interviews. It shows the learner understands not just AKS usage, but **AKS platform design under enterprise constraints**. Microsoft’s architecture guidance, multitenant guidance, and private-cluster guidance all support this style of platform reasoning.

## Completion standard
A learner should not mark this lab complete until:
- the private AKS landing-zone model is clear
- the network and DNS logic is understandable
- the Terraform structure reflects the architecture cleanly
- the learner can explain why this is a top-tier enterprise design
