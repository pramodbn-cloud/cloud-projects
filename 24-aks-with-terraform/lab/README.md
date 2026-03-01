# Lab Guide — AKS with Terraform

## Lab objective
The objective of this lab is to help the learner understand and implement AKS provisioning through Terraform so that cluster infrastructure can be created in a repeatable, version-controlled, and reviewable way.

This lab focuses on Terraform structure, AKS resource definition, supporting Azure resources, state awareness, and basic apply/validate flow. The goal is not to build a giant enterprise Terraform platform yet, but to make the learner comfortable with the core AKS IaC pattern.

## What you will build or configure
In this lab, you will define or review Terraform configuration for an AKS cluster and its supporting components, run through the Terraform lifecycle, and validate that the cluster is created and usable through code rather than manual setup.

This creates the first true infrastructure-as-code foundation workflow in the AKS course.

## Why this lab matters
Manual AKS creation can work for isolated demos, but it becomes fragile for real platform operations. Terraform adds repeatability, version control, team review, environment consistency, and a cleaner change model.

Terraform’s AzureRM provider supports AKS through `azurerm_kubernetes_cluster`, and HashiCorp also documents provisioning AKS clusters on Azure with Terraform as a standard workflow.

## Estimated time
60 to 75 minutes

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
- a clear AKS Terraform configuration pattern
- a Terraform lifecycle understanding for AKS provisioning
- a cluster created or clearly modeled through IaC
- confidence in explaining why Terraform belongs at the end of the AKS learning path

## Skills gained
- Understanding AKS provisioning through Terraform
- Thinking in terms of infrastructure declaration instead of manual creation
- Connecting Azure resources and AKS dependencies in code
- Preparing for pipeline-driven Terraform delivery later

## Real-world relevance
In real platform teams, Terraform is often used to define AKS foundations such as clusters, node pools, networking, and related Azure resources. This makes AKS repeatable, reviewable, and easier to evolve across environments.

## Completion standard
A learner should not mark this lab complete until:
- the Terraform AKS provisioning model is clear
- the apply/validate lifecycle is understandable
- the learner can explain the Terraform resource flow end to end
- validation confirms the IaC pattern clearly
