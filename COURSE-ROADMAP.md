# Course Roadmap

This roadmap explains how the full learning journey is structured from foundation to advanced implementation.

---

## Course Structure Overview

The repository is divided into two major phases:

### Phase 1 — Azure DevOps Foundations
This phase builds the delivery workflow mindset.

### Phase 2 — Advanced AKS Delivery Engineering
This phase applies delivery engineering concepts to Kubernetes workloads on Azure.

---

## Why the Course Is Structured This Way

A learner should not jump directly into advanced AKS topics such as ingress, DNS, SSL, RBAC, autoscaling, or production architecture without first understanding delivery flow.

That is why this repository begins with:

- planning
- source control
- build pipelines
- release pipelines
- package reuse
- security
- monitoring
- automation

Once those are clear, the learner is ready to understand AKS not as isolated Kubernetes topics, but as part of a complete engineering workflow.

---

## Phase 1 — Azure DevOps Foundations

### 01 — Azure DevOps Foundation Setup
Establishes the platform, local environment, and course starting point.

### 02 — Agile Planning + Traceability
Builds understanding of work planning, sprint structure, and traceability from requirement to execution.

### 03 — Source Control Strategy
Introduces safe collaboration using repositories, branches, pull requests, and merge protection.

### 04 — CI Pipelines: Build + Test + Artifacts
Shows how code changes are validated and converted into build outputs.

### 05 — CD Pipelines: Deployments + Approvals + Rollback
Introduces controlled deployment workflows, gated promotions, and rollback thinking.

### 06 — Azure Artifacts: Package Management Strategy
Builds understanding of internal package feeds, reuse, and versioning.

### 07 — Security + Compliance: DevSecOps Basics
Introduces secure pipeline access, secret handling, and protection-first delivery thinking.

### 08 — Instrumentation + Automation + Capstone
Connects dashboards, alerts, notifications, automation, and end-to-end workflow understanding.

---

## Phase 2 — Advanced AKS Delivery Engineering

### 09 — AKS Ingress Basics
Introduces traffic entry into AKS workloads.

### 10 — Ingress Context Path Routing
Shows how multiple services can share one entry point using path rules.

### 11 — Domain Delegation to Azure DNS
Introduces DNS ownership and domain delegation principles.

### 12 — ExternalDNS with Azure DNS
Automates DNS record management from Kubernetes resources.

### 13 — Domain Name Based Routing
Moves to hostname-based application exposure.

### 14 — Ingress SSL with Let’s Encrypt
Secures application entry with HTTPS and certificate automation.

### 15 — Kubernetes Requests + Limits
Introduces resource governance for stable workloads.

### 16 — Kubernetes Namespaces
Builds workload separation and environment/team isolation understanding.

### 17 — AKS Virtual Nodes
Introduces flexible node-extension concepts and advanced AKS execution models.

### 18 — ACR with AKS
Connects private registry workflows with AKS image deployment.

### 19 — Azure DevOps with AKS
Brings CI/CD and AKS together into one deployment pipeline flow.

### 20 — AKS HTTP Application Routing
Shows a managed application exposure model in AKS.

### 21 — AKS Authentication + RBAC
Introduces access control, identity, authorization, and governance.

### 22 — AKS Autoscaling
Builds scaling understanding at both pod and infrastructure levels.

### 23 — Azure Policy with AKS
Introduces centralized governance and policy-driven compliance for AKS workloads.

### 24 — AKS with Terraform
Codifies AKS platform provisioning using infrastructure as code.

### 25 — Terraform + Azure DevOps for AKS
Turns Terraform workflows into pipeline-driven infrastructure delivery.

### 26 — Enterprise Private AKS Landing Zone with Terraform
Designs a private, enterprise-grade AKS platform boundary with Terraform.

### 27 — Zero-Trust AKS Security with mTLS + Azure API Management
Applies high-assurance API security patterns using APIM, mTLS, and identity-aware controls.
---

## Recommended Learning Pattern

For each module:

1. Understand the concept
2. Learn the workflow position
3. Follow the practical lab
4. Validate outcomes
5. Troubleshoot if needed
6. Clean up responsibly
7. Summarize the module in your own words

---

## Suggested Study Rhythm

A practical rhythm for learners:

- 1 module at a time
- concept first
- lab second
- notes third
- revision after every 3–4 modules

Do not rush through the advanced modules.  
Those should be studied with stronger attention to architecture, dependencies, and real-world interpretation.

---

## Final Capstone Mindset

By the final modules, the learner should not think in isolated topics.

Instead, the learner should think like this:

- how code moves
- how builds are validated
- how images are produced
- how workloads are deployed
- how traffic reaches them
- how DNS and SSL secure them
- how permissions protect them
- how scaling keeps them reliable
- how architecture becomes production-aware

That full-system thinking is the real end goal of this course.

---

## Course End State

At the end of the repository, the learner should be able to explain an end-to-end Azure DevOps + AKS workflow with both conceptual clarity and practical confidence.
