# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Terraform + Azure DevOps for AKS lab.

The goal is to create one clear infrastructure CI/CD path where Terraform-based AKS provisioning is executed through Azure DevOps rather than through unmanaged local workflows.

---

## Step 1 — Understand the infrastructure-pipeline goal
Before building the pipeline, understand what this module is trying to teach.

This lab is not only about running Terraform from Azure DevOps. It is about turning infrastructure delivery into a governed lifecycle:

- Terraform code lives in source control
- Azure DevOps runs the Terraform workflow
- plan visibility improves review
- apply becomes controlled and repeatable
- infrastructure provisioning becomes part of platform engineering discipline

At the end of this lab, you should have:
- one Terraform pipeline path
- one clear separation between plan and apply
- one clear explanation of why this is the course capstone

## Step 2 — Reconfirm the Terraform foundation from Folder 24
Before building the pipeline, verify that:
- the AKS Terraform configuration is already valid
- the learner understands the resources being created
- the learner understands the state model and execution expectations

Do not move straight into pipelines if the Terraform code itself is still unclear.

## Step 3 — Reconfirm Azure DevOps repository and service connection readiness
Now inspect:
- repository access
- pipeline access
- Azure service connection readiness

The learner should understand:
- Azure DevOps needs a trusted way to act against Azure
- service connections are infrastructure trust boundaries just like earlier delivery modules

This is the first major governance checkpoint in the module.

## Step 4 — Design the pipeline stages
Now define the intended pipeline shape.

Recommended first structure:
- init
- validate or plan
- controlled apply

The learner should understand that:
- plan is the review stage
- apply is the change stage
- these should not be treated as the same thing

This is one of the most important capstone design moments.

## Step 5 — Create or review the Terraform pipeline definition
Now define the Azure DevOps pipeline.

At this stage, focus on:
- readable stage names
- trust path clarity
- proper execution order
- enough visibility that a team can understand what the pipeline is doing

The goal is not only automation. The goal is auditable automation.

## Step 6 — Implement Terraform init in the pipeline
Now add the Terraform init stage.

The learner should understand:
- the pipeline must initialize the Terraform working directory
- provider and backend/state context must be established before plan or apply
- this is the beginning of infrastructure lifecycle execution

## Step 7 — Implement Terraform validation and/or plan
Now add the validation and plan logic.

This stage should make the intended infrastructure change visible before it is applied.

The learner should understand:
- plan is where infrastructure review becomes possible
- this is what makes infrastructure CI/CD more governable than direct local apply

This is the core reviewability moment of the module.

## Step 8 — Implement the controlled apply stage
Now define the apply stage.

At this stage, the learner should focus on:
- controlled sequencing
- environment targeting clarity
- separating “we know what will change” from “we are now changing it”

This is where infrastructure actually becomes delivery.

## Step 9 — Run the pipeline
Now execute the pipeline.

Observe:
- init behavior
- validation/plan behavior
- apply behavior
- whether the AKS infrastructure is created or updated successfully

Do not only look for green success. Understand the lifecycle step by step.

## Step 10 — Review resulting Azure infrastructure
Once the pipeline completes successfully, validate that:
- the expected AKS resources exist or were updated
- the infrastructure matches what the Terraform plan intended
- the learner can connect pipeline execution to real Azure outcomes

This proves that the pipeline is governing real infrastructure, not only running commands.

## Step 11 — Compare local Terraform execution to pipeline Terraform execution
Now reflect on the difference between:
- running Terraform locally
- running Terraform through Azure DevOps

Ask:
- why is the pipeline path more reviewable?
- why is it easier to standardize across a team?
- why does this reduce reliance on one operator’s local context?

This is the core platform reasoning moment of the capstone.

## Step 12 — Review state and lifecycle trust in a pipeline context
Now revisit state in the context of pipeline execution.

The learner should understand:
- once Terraform runs in CI/CD, state discipline becomes even more important
- pipeline-driven infrastructure assumes lifecycle continuity and trustworthy state handling
- the infrastructure pipeline is only as reliable as its lifecycle model

This is a major capstone maturity point.

## Step 13 — Explain the infrastructure-delivery lifecycle end to end
Now explain the flow in plain language:

- Terraform code defines AKS infrastructure
- Azure DevOps triggers the pipeline
- the pipeline initializes Terraform
- the pipeline reviews the intended changes
- the pipeline applies the changes in a controlled stage
- AKS infrastructure is provisioned through a governed CI/CD path

If the learner can explain this clearly, the module is doing its real job.

## Step 14 — Reflect on this as the course capstone
Pause and think beyond the pipeline file.

In this module, Terraform + Azure DevOps for AKS means:
- platform foundations are codified
- infrastructure changes are pipeline-governed
- reviewability and repeatability are built into cluster provisioning
- the learner now understands both runtime and infrastructure delivery for AKS

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- Terraform code for AKS exists and is understandable
- Azure DevOps can reach the repository and Azure target
- the pipeline separates init, plan, and apply meaningfully
- the AKS infrastructure is provisioned or updated through the pipeline
- the learner understands why this is stronger than manual Terraform execution

## Step 15 — Close the course with the end-state view
At the end of this module, the learner should be able to look back and connect:

- AKS runtime architecture
- ingress and DNS
- security and workload governance
- scaling and policy
- registry and CI/CD
- Terraform provisioning
- Terraform infrastructure delivery through Azure DevOps

That is the capstone state of the course.

---

## Implementation notes
- keep the first infrastructure pipeline simple and readable
- always separate plan from apply
- focus on trust path and reviewability
- do not overcomplicate the first capstone pipeline with too many environments at once
- treat this as infrastructure delivery engineering, not only Terraform automation

## End-of-implementation summary
In this lab, you:
- reused the Terraform AKS foundation from Folder 24
- prepared Azure DevOps service connection and repository access
- created a Terraform pipeline structure
- separated init, plan, and apply stages
- ran infrastructure provisioning through Azure DevOps
- validated resulting AKS infrastructure
- completed the final capstone pattern of the course

You are now ready to validate whether the Terraform + Azure DevOps for AKS lifecycle is clean, correct, and explainable.
