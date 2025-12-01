# Validation Checks

## Purpose of this file
This file confirms whether the ACR with AKS lab is complete and correct.

The goal is not only to verify that an image exists in ACR, but to confirm that the learner understands the full private-image supply chain from build to registry to cluster pull.

## Validation approach
For this lab, validation is based on:
- registry correctness
- image correctness
- AKS identity integration correctness
- AcrPull authorization correctness
- runtime image pull success
- learner explanation ability

## Check 1 — The ACR registry is correct
Confirm that:
- the registry exists
- the learner can identify the correct login server
- the registry is the intended trusted image source for the lab

This proves that the supply source is real and readable.

## Check 2 — The sample image exists in ACR
Confirm that:
- the image was pushed successfully
- the repository path is correct
- the tag is clear and intentional

This proves that the cluster has something valid to pull. ACR best-practice guidance also emphasizes strong tagging/versioning discipline.

## Check 3 — AKS–ACR integration is correct
Confirm that:
- the AKS cluster is attached to ACR or has equivalent registry authorization
- the learner understands which identity is performing the pull
- the AcrPull relationship is conceptually clear

This is one of the most important technical understanding checks in the module. Microsoft’s docs state that attach-acr configures AcrPull for the managed identity.

## Check 4 — The workload references the private image correctly
Confirm that:
- the full image path is correct
- the tag is correct
- the deployment points at the intended ACR image

This proves that the workload is asking for the right artifact.

## Check 5 — The pod pulls and starts successfully
Confirm that:
- the pod can pull the image from ACR
- the pod enters a healthy running state
- the learner can distinguish successful deployment from successful image-pull behavior

This is the main technical success signal for the module.

## Check 6 — The learner understands identity-based pull flow
Confirm that the learner can clearly explain:
- which AKS identity is pulling
- why AcrPull matters
- why this is cleaner than ad hoc image-pull secret distribution in the standard AKS–ACR pattern

This proves that the module has moved beyond “registry exists” into trust-path understanding.

## Check 7 — The learner understands image identity and tagging discipline
Confirm that:
- the learner can explain why image tags matter operationally
- the learner understands why ambiguous image identity increases deployment risk
- the learner can explain why ACR is part of deployment quality, not only storage

This proves supply-chain maturity.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why AKS needs a trusted private image source
- how ACR integrates with AKS
- why managed identity plus AcrPull is important
- why image supply is a production-readiness concern
- why this module had to come before Azure DevOps deployment automation

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the image is in ACR
- AKS has the right pull authorization
- the workload starts from the private image
- the learner understands registry trust and image identity clearly
- the learner is ready to connect ACR into pipeline-driven deployment

## If validation fails
If any validation step fails:
- re-check image push success
- re-check the full image reference
- re-check AKS identity and AcrPull integration
- inspect pod events carefully
- use `troubleshooting.md` for common ACR/AKS pull issues
