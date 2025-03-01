# Azure DevOps + AKS Job-Ready Learning Repository
![Posts/index.png](Posts/index.png)

A structured, hands-on learning repository designed to take learners from Azure DevOps foundations to advanced AKS platform and delivery engineering through practical, workflow-driven modules.

This repository is built as a **course-first, lab-driven learning system**.  
It is not just a notes repository and not just a demo collection.  
Every module is designed to teach:

- what the topic is
- why it matters in real projects
- how it fits into the full delivery workflow
- how to practice it step by step
- how to validate, troubleshoot, and explain it confidently

---

## Course Vision

This repository is designed to help learners build a **job-ready understanding** of:

- Azure DevOps foundations
- Agile planning and traceability
- Source control strategy
- CI/CD pipeline workflows
- Package management
- DevSecOps basics
- Monitoring and automation
- AKS ingress, DNS, routing, TLS, registry, RBAC, autoscaling, policy, and platform governance
- Terraform-based AKS provisioning
- Terraform + Azure DevOps infrastructure delivery

The learning journey progresses in a structured way so that each module builds naturally on the previous one.

---

## Repository Design Philosophy

This repository follows four principles:

### 1. Course-first structure
Every folder is designed like a proper learning module, not just a technical dump.

### 2. Hands-on workflow orientation
Every module contains a practical lab flow that explains implementation, validation, troubleshooting, and cleanup.

### 3. Real-world relevance
Each topic is positioned in the context of actual engineering workflows, not only theory.

### 4. Step-by-step progression
The repository starts with foundations and moves toward production-grade AKS platform understanding, governance, and infrastructure delivery maturity.

---

## Learning Phases

## Phase 1 — Azure DevOps Foundations
This phase builds the core understanding of how teams plan, track, build, test, secure, release, and monitor delivery workflows using Azure DevOps.

Modules included:

1. Azure DevOps Foundation Setup  
2. Agile Planning + Traceability  
3. Source Control Strategy  
4. CI Pipelines: Build + Test + Artifacts  
5. CD Pipelines: Deployments + Approvals + Rollback  
6. Azure Artifacts: Package Management Strategy  
7. Security + Compliance: DevSecOps Basics  
8. Instrumentation + Automation + Capstone  

## Phase 2 — Advanced AKS Delivery Engineering
This phase applies delivery engineering concepts to AKS and production-style Kubernetes workflows on Azure.

Modules included:

9. AKS Ingress Basics  
10. Ingress Context Path Routing  
11. Domain Delegation to Azure DNS  
12. ExternalDNS with Azure DNS  
13. Domain Name Based Routing  
14. Ingress SSL with Let’s Encrypt  
15. Kubernetes Requests + Limits  
16. Kubernetes Namespaces  
17. AKS Virtual Nodes  
18. ACR with AKS  
19. Azure DevOps with AKS  
20. AKS Application Routing  
21. AKS Authentication with Microsoft Entra ID + Kubernetes RBAC  
22. AKS Autoscaling  
23. Azure Policy with AKS  
24. AKS with Terraform  
25. Terraform + Azure DevOps for AKS  
26. Enterprise Private AKS Landing Zone with Terraform  
27. Zero-Trust AKS Security with mTLS + Azure API Management  

---

## What Each Module Contains

Every module folder in this repository is designed to contain:

- `README.md`  
  A course-facing module overview explaining what the topic is, why it matters, and what the learner will gain.

- `post-assets/` *(when included for that module)*  
  The visual learning asset or post image connected to that module.

- `lab/`  
  A structured hands-on workflow containing:
  - lab overview
  - architecture flow
  - prerequisites
  - implementation steps
  - validation checks
  - troubleshooting
  - cleanup
  - proof-of-execution (commands, outputs, screenshots, and evidence links)

This makes the repository easy to follow, consistent, and professional.

---

## Who This Repository Is For

This repository is designed for:

- beginners who want a structured path into Azure DevOps and AKS
- learners who prefer workflow-based practical understanding
- engineers preparing for real delivery and platform work
- candidates who want strong project and interview explanation ability
- trainers or content builders who want a high-quality, course-ready structure

---

## How to Use This Repository

Recommended flow for every module:

1. Read the module `README.md`
2. Understand why the topic matters
3. Review the post visual in `post-assets/` *(or in README file)*
4. Open the `lab/README.md`
5. Follow the lab in order
6. Validate outcomes using `validation-checks.md`
7. Use `troubleshooting.md` if needed
8. Complete cleanup before moving to the next module
   
---

## Expected Learning Outcome

By the end of this repository, the learner should be able to:

- explain the Azure DevOps lifecycle clearly
- implement practical DevOps workflows
- understand secure CI/CD patterns
- manage package and release workflows
- explain AKS exposure and routing models
- connect DNS, TLS, registry, RBAC, autoscaling, and policy into one platform architecture
- understand what makes a platform more production-ready
- provision AKS through Terraform
- explain both application delivery and infrastructure delivery through Azure DevOps
- present a complete end-to-end Azure DevOps + AKS platform story with confidence

---


---

## Evidence and Validation Standards

To strengthen real-world credibility and portfolio quality, each module should include a `lab/proof-of-execution.md` file with:

- exact commands used
- key output snippets or status checks
- screenshots or links to execution evidence
- short notes on what was validated

This keeps the repository practical, reviewable, and suitable for interview or community demonstration.

You can run `scripts/validate-repo.sh` to verify module structure and documentation hygiene before opening a PR/MR.

## Repository Standards

To keep the repository clean and premium:

- every module follows the same core structure
- file names remain consistent across folders
- explanations stay outcome-oriented
- labs remain practical and validation-driven
- advanced modules include real-world positioning and operational understanding
- late-stage modules connect runtime, governance, IaC, and delivery into one coherent story

---

## Next Recommended Reading

Please start with:

- `COURSE-ROADMAP.md`
- `COURSE-SETUP.md`
- `LEARNING-PATH.md`

These files explain the journey, required tools, and the recommended study approach for the full repository.

---

## Final Goal

The final goal of this repository is not only learning.  
It is to create a **clear, practical, interview-ready, and project-ready understanding** of Azure DevOps and AKS delivery engineering.
