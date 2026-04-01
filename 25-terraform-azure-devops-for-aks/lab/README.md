# Lab Guide — Terraform + Azure DevOps for AKS

## Lab objective
The objective of this lab is to help the learner implement a pipeline-driven Terraform workflow for AKS so that infrastructure provisioning is no longer manual but governed through Azure DevOps.

This lab focuses on Terraform stages, Azure DevOps pipeline structure, validation versus apply, environment-aware execution, and infrastructure-delivery discipline. The goal is not to build a giant enterprise IaC platform yet, but to make the learner comfortable with the capstone workflow that joins infrastructure as code with CI/CD governance.

## What you will build or configure
In this lab, you will create or review an Azure DevOps pipeline that runs Terraform for AKS provisioning, including initialization, validation/plan behavior, and controlled apply behavior.

This creates the first true infrastructure-delivery capstone workflow in the course.

## Why this lab matters
Manual Terraform execution can still work, but it is less consistent, less auditable, and harder to coordinate across teams than a governed pipeline model. Azure DevOps adds reviewable, repeatable execution around Terraform so infrastructure changes are treated with the same discipline as application changes.

The source course materials and related pipeline repo explicitly center provisioning AKS with Terraform through Azure DevOps. Microsoft also documents Azure Pipelines for AKS-related delivery automation, which supports the broader Azure-native delivery story. 

## Estimated time
60 to 80 minutes

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
- a pipeline structure for Terraform-based AKS provisioning
- a clear Terraform init/plan/apply pipeline understanding
- a governed infrastructure-delivery model
- confidence in explaining why this is the final capstone of the course

## Skills gained
- Understanding infrastructure CI/CD for AKS
- Connecting Terraform lifecycle to Azure DevOps governance
- Thinking in terms of plan review and controlled apply
- Preparing for real-world platform engineering workflows

## Real-world relevance
In real platform teams, Terraform and CI/CD are often combined so infrastructure is versioned, reviewed, planned, and applied in a controlled delivery process. That is one of the clearest indicators that infrastructure has become part of the platform engineering system rather than only an admin task.

## Completion standard
A learner should not mark this lab complete until:
- the Terraform pipeline concept is clear
- the init/plan/apply lifecycle is understandable in Azure DevOps
- the learner can explain why this is stronger than manual Terraform execution
- validation confirms the infrastructure-delivery lifecycle end to end
