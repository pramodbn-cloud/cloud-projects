# Validation Checks

## Purpose of this file
This file confirms whether the Terraform + Azure DevOps for AKS lab is complete and correct.

The goal is not only to verify that the pipeline ran, but to confirm that the learner understands how Terraform-based infrastructure delivery becomes governed through Azure DevOps.

## Validation approach
For this lab, validation is based on:
- pipeline structure correctness
- service-connection trust correctness
- Terraform lifecycle separation
- infrastructure outcome correctness
- capstone reasoning
- learner explanation ability

## Check 1 — The pipeline structure is clear
Confirm that:
- the pipeline stages are readable
- the learner can explain the role of init, plan, and apply
- the structure is intentional and not collapsed into one opaque execution block

This proves the infrastructure lifecycle is understandable.

## Check 2 — The trust path to Azure is correct
Confirm that:
- the learner can explain which service connection is being used
- the pipeline has the right access to manage Azure resources
- the trust bridge is clear and auditable

This proves the infrastructure delivery path is real.

## Check 3 — Plan and apply are clearly separated
Confirm that:
- the learner understands that plan is for review
- the learner understands that apply is for change execution
- the pipeline reflects that separation meaningfully

This is one of the most important capstone checks.

## Check 4 — The AKS infrastructure is created or updated correctly
Confirm that:
- the resulting AKS resources exist or changed as expected
- the learner can connect the pipeline outcome to real Azure infrastructure state

This is the main technical success signal for the module.

## Check 5 — The learner understands why pipeline-driven Terraform is better than local-only Terraform
Confirm that:
- the learner can explain repeatability
- the learner can explain reviewability
- the learner can explain why pipeline execution reduces local-operator dependency

This proves platform-delivery maturity.

## Check 6 — The learner understands state significance in CI/CD
Confirm that:
- the learner can explain why Terraform state matters even more in a pipeline model
- the learner understands that infrastructure CI/CD still depends on trustworthy lifecycle/state handling

This proves real IaC maturity.

## Check 7 — The learner can explain how this module closes the course
Confirm that the learner can connect:
- AKS architecture
- governance
- delivery
- Terraform provisioning
- pipeline execution

This proves the capstone is landing correctly.

## Check 8 — You can explain why this is the right final module
This is the most important validation for this module.

The learner should now be able to explain:
- why Terraform came before this module
- why Azure DevOps comes back in this final capstone
- why infrastructure delivery should be pipeline-governed
- why this is a strong endpoint for the course

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the pipeline is readable and governed
- the infrastructure is provisioned successfully
- plan/apply separation is understood
- state and trust-path reasoning are present
- the learner now sees the full platform-engineering lifecycle end to end

## If validation fails
If any validation step fails:
- revisit the Terraform foundation from Folder 24
- re-check service-connection trust
- re-check stage separation
- re-check resulting Azure infrastructure
- use `troubleshooting.md` for common Terraform + Azure DevOps issues
