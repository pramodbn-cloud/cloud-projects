# Folder 25 — Terraform + Azure DevOps for AKS
![Week-25 Plan](../Posts/25.png)

## Overview
This module is the capstone of the course. It combines Terraform-based AKS provisioning with Azure DevOps pipeline automation so that cluster infrastructure itself can be delivered through a governed CI/CD workflow.

This is where the course reaches full platform maturity. The learner is no longer only provisioning clusters as code or deploying applications through pipelines. The learner is now orchestrating infrastructure provisioning through the same kind of delivery discipline used for application deployment.

## Why this module matters
If Terraform is run only manually, infrastructure still depends too heavily on local execution habits and operator timing. A mature platform benefits from pipeline-driven validation, plan visibility, controlled apply behavior, and environment-aware infrastructure delivery.

The source course materials explicitly end with provisioning AKS through Terraform and Azure DevOps. Microsoft also documents Azure Pipelines as a CI/CD engine for AKS-related automation, and Azure DevOps is widely used to run Terraform init/plan/apply stages in controlled workflows. 

## What you will learn
- How Terraform and Azure DevOps fit together for AKS infrastructure delivery
- Why remote execution and pipeline review improve IaC governance
- How infrastructure stages differ from application deployment stages
- Why this module is the natural capstone for the entire course

## Workflow position
This module closes the course intentionally.

The learner now understands:
- AKS runtime architecture
- ingress, DNS, TLS
- workload governance and scaling
- image supply and CI/CD delivery
- AKS provisioning with Terraform

The final step is to put infrastructure provisioning itself under pipeline governance.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain Terraform + Azure DevOps for AKS clearly
- structure a pipeline for Terraform validation and provisioning
- understand why infrastructure delivery should be governed and reviewable
- explain how this capstone ties the whole course together

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the Terraform pipeline lifecycle carefully  
5. Do not move ahead until the infrastructure CI/CD model feels clear as the endgame of platform engineering  

## Next module
There is no further module in this course.

This folder is the end capstone. It should leave the learner with a complete picture of:
- platform runtime
- platform governance
- platform delivery
- platform provisioning as code
- platform provisioning through pipelines
