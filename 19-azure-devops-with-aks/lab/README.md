# Lab Guide — Azure DevOps with AKS

## Lab objective
The objective of this lab is to help the learner implement a pipeline-driven deployment flow from Azure DevOps to AKS using ACR as the registry handoff point.

This lab focuses on build automation, registry push, pipeline-to-cluster trust, manifest-driven deployment, and rollout visibility. The goal is not to design a full enterprise promotion model yet, but to make the learner comfortable with the core CI/CD path that takes a code change and turns it into a running AKS workload.

## What you will build or configure
In this lab, you will configure or review a pipeline that:
- builds a container image
- pushes that image to ACR
- deploys the workload to AKS using manifests and an Azure DevOps deployment task

This creates the first full build-to-runtime pipeline pattern in the AKS phase.

## Why this lab matters
Without a pipeline, image supply and cluster deployment remain partially manual and operationally fragile. A mature platform needs a repeatable path that can build, publish, deploy, and surface rollout status consistently.

Microsoft documents Azure Pipelines examples for AKS that use build stages to publish images to ACR and deployment jobs that use `KubernetesManifest` for cluster rollout. Microsoft also documents that `KubernetesManifest` adds deployment traceability and checks object stability before declaring success.

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
- a build-and-push pipeline path to ACR
- a deployment path from Azure DevOps to AKS
- a working workload updated through the pipeline
- confidence in explaining the end-to-end delivery lifecycle

## Skills gained
- Connecting Azure DevOps pipelines to ACR and AKS
- Thinking in terms of end-to-end platform delivery
- Understanding service connections and deployment jobs
- Preparing for more advanced rollout and production automation patterns

## Real-world relevance
In real AKS platforms, CI/CD is where registry trust, image versioning, service connections, manifests, and runtime rollout all converge. Microsoft’s documentation and task guidance position Azure Pipelines as a first-class way to build images, publish to ACR, and deploy to Kubernetes using manifest-based tasks.

## Completion standard
A learner should not mark this lab complete until:
- the pipeline flow is clear
- the image reaches ACR
- the workload reaches AKS through the pipeline
- validation confirms the delivery lifecycle end to end
