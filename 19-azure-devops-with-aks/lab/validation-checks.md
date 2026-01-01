# Validation Checks

## Purpose of this file
This file confirms whether the Azure DevOps with AKS lab is complete and correct.

The goal is not only to verify that a pipeline ran, but to confirm that the learner understands the full build-to-registry-to-cluster delivery lifecycle and the trust boundaries that support it.

## Validation approach
For this lab, validation is based on:
- pipeline correctness
- image build correctness
- ACR push correctness
- deployment-stage correctness
- rollout visibility
- learner explanation ability

## Check 1 — The pipeline structure is correct
Confirm that:
- the pipeline includes a build path
- the pipeline includes an ACR push path
- the pipeline includes an AKS deployment path
- the learner can explain what each stage is for

This proves that the delivery lifecycle has been modeled correctly.

## Check 2 — The image is built and pushed correctly
Confirm that:
- the build succeeds
- the image is pushed into ACR
- the tag is visible and intentional

Microsoft documents Azure Pipelines patterns for building and pushing images into ACR.

This proves the artifact handoff point is real.

## Check 3 — The deployment stage is correctly connected to AKS
Confirm that:
- the pipeline can reach AKS using the intended trusted connection model
- manifests are applied successfully
- the learner understands how service connections enable this deployment step

This proves the deployment trust path is real.

## Check 4 — The deployed workload is healthy
Confirm that:
- the workload is updated in AKS
- the pod or deployment reaches a healthy state
- the cluster is actually running the expected new image

This is the main runtime success signal for the module.

## Check 5 — The learner understands image identity flow
Confirm that:
- the learner can explain which image was built
- the learner can explain which tag was pushed
- the learner can explain how that image became the deployed workload

This proves supply-chain clarity.

## Check 6 — The learner understands rollout visibility
Confirm that:
- the learner can inspect pipeline run details
- the learner can explain deployment outcome from pipeline and cluster views
- the learner understands why rollout visibility matters

Microsoft documents that the KubernetesManifest task performs stability checks and supports traceability-related behavior.

This proves operational maturity.

## Check 7 — The learner understands why pipeline deployment is better than manual deployment
Confirm that the learner can explain:
- repeatability
- traceability
- auditability
- easier rollback or re-run thinking later

This proves the module has changed the learner’s delivery model rather than only added YAML.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why ACR had to come before this module
- how Azure DevOps builds and pushes the image
- how AKS receives the deployment
- why service connections and manifest deployment matter
- why this is a major production-readiness step

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the pipeline runs cleanly
- the image appears in ACR
- the workload updates in AKS
- the learner understands the end-to-end delivery lifecycle
- the learner is ready to think about more advanced rollout and runtime patterns

## If validation fails
If any validation step fails:
- re-check build and push first
- re-check service connections and AKS deployment trust path
- re-check manifest/image reference alignment
- inspect cluster rollout status carefully
- use `troubleshooting.md` for common Azure DevOps + AKS issues
