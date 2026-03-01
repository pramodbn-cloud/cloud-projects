# Validation Checks

## Purpose of this file
This file confirms whether the AKS with Terraform lab is complete and correct.

The goal is not only to verify that Terraform created resources, but to confirm that the learner understands the full declarative infrastructure lifecycle for AKS.

## Validation approach
For this lab, validation is based on:
- Terraform structure correctness
- provider/state understanding
- plan/apply understanding
- AKS resource correctness
- reproducibility understanding
- learner explanation ability

## Check 1 — The Terraform structure is clear
Confirm that:
- the configuration has a readable structure
- the learner can explain the role of provider, variables, resources, and outputs
- the Terraform layout is intentional rather than accidental

This proves that the configuration is maintainable.

## Check 2 — The learner understands provider and version discipline
Confirm that:
- the learner knows why Azure provider configuration matters
- the learner understands that AKS evolves quickly and provider discipline affects infrastructure behavior

This proves the learner is thinking operationally, not only syntactically.

## Check 3 — The learner understands plan before apply
Confirm that:
- the learner can explain the value of Terraform plan
- the learner treats plan as a review step, not just a command to skip

This is one of the most important IaC maturity checks in the module.

## Check 4 — The AKS resource path is correct
Confirm that:
- the AKS cluster resource is defined meaningfully
- supporting resources are aligned to the cluster design
- the learner can explain what Azure infrastructure is being created and why

This proves that the Terraform code is expressing a real platform foundation.

## Check 5 — The cluster is provisioned or clearly modeled successfully
Confirm that:
- the apply phase succeeded or is clearly understood in a modeled scenario
- the resulting AKS cluster and relevant Azure resources are visible
- the learner understands that the platform is now infrastructure-defined

This is the main technical success signal for the module.

## Check 6 — The learner understands Terraform state
Confirm that:
- the learner can explain why state matters
- the learner understands state as part of infrastructure trust and lifecycle control

This proves real Terraform understanding rather than command memorization.

## Check 7 — The learner understands why Terraform is better than manual provisioning here
Confirm that:
- the learner can explain repeatability
- the learner can explain reviewability
- the learner can explain environment consistency

This proves that the module changed the learner’s provisioning model.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why AKS should be provisioned as code
- how Terraform defines and creates the cluster
- why plan/apply/state matter
- why this module belongs near the end of the course
- why it naturally leads into Terraform + Azure DevOps

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- Terraform structure is readable
- the cluster definition is clear
- the learner understands state and plan/apply
- the provisioned cluster is validated
- the learner is ready for pipeline-driven IaC delivery

## If validation fails
If any validation step fails:
- simplify the Terraform structure
- revisit provider and state concepts
- re-check the AKS resource definition
- re-run plan reasoning before apply
- use `troubleshooting.md` for common AKS + Terraform issues
