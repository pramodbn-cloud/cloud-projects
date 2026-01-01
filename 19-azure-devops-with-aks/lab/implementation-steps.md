# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Azure DevOps with AKS lab.

The goal is to create one clear CI/CD lifecycle where code becomes a container image, the image becomes an ACR artifact, and the artifact becomes a running AKS workload through Azure DevOps automation.

---

## Step 1 — Understand the pipeline-delivery goal
Before configuring any pipeline, understand what this module is trying to teach.

This lab is not only about running a pipeline successfully. It is about creating a trustworthy end-to-end delivery path:

- source code changes start the lifecycle
- the pipeline builds the container image
- the pipeline pushes the image into ACR
- the deployment stage rolls the workload into AKS
- rollout status becomes visible and repeatable

At the end of this lab, you should have:
- one build path
- one ACR push path
- one AKS deployment path
- one clear explanation of the end-to-end lifecycle

## Step 2 — Reconfirm the ACR and AKS trust path
Before starting the pipeline, verify that:
- ACR exists and is reachable
- AKS exists and is reachable
- the AKS-to-ACR pull path from Folder 18 is already valid

This matters because the pipeline can succeed at image push and still fail operationally later if the cluster cannot actually pull the image.

## Step 3 — Prepare the application and manifests
Now prepare:
- the application source code
- the Dockerfile or build definition
- the Kubernetes manifests

Keep the first scenario simple:
- one application
- one image repository
- one deployment manifest
- one service if needed

This keeps the focus on the delivery path rather than application complexity.

## Step 4 — Review the Azure DevOps service connections
Now inspect the service connections that the pipeline will rely on.

The learner should understand:
- one trust path is needed for working with Azure resources and ACR
- another trust path may be used for the AKS deployment target, depending on the chosen setup
- service connections are pipeline trust boundaries

Do not treat these as background setup only. They are part of the deployment architecture.

## Step 5 — Create or review the build-and-push stage
Now define the pipeline stage that will:
- build the container image
- tag it clearly
- push it to ACR

Microsoft documents Docker-template-based pipelines for building and pushing images to Azure Container Registry, and also documents more general image-push patterns in Azure Pipelines.

At this stage, focus on:
- image identity
- tag clarity
- successful push into the intended ACR repository

## Step 6 — Create or review the deployment stage
Now define the stage that deploys to AKS.

Recommended approach:
- use manifest-driven deployment
- keep the first path simple and deterministic
- use Azure DevOps’ Kubernetes manifest deployment pattern

Microsoft’s AKS pipeline documentation uses deployment jobs and the `KubernetesManifest` task to deploy manifests to AKS.

This is the second major learning moment in the module because the pipeline is now crossing from CI into runtime change.

## Step 7 — Connect image identity to deployment manifests
Now make sure the deployment stage uses the image that was just built and pushed.

The learner should understand:
- the deployment should not point to an old or ambiguous image
- image identity must flow cleanly from build to deploy
- this is where supply-chain trust and deployment quality connect directly

This step is operationally critical.

## Step 8 — Run the pipeline
Now execute the pipeline.

Observe:
- build behavior
- push-to-ACR behavior
- deployment-stage behavior
- where the delivery flow transitions from registry artifact into cluster rollout

Do not only look for green success. Try to understand what each stage is doing.

## Step 9 — Review build and registry results
After the build stage, verify:
- the image was built correctly
- the image was pushed into ACR
- the intended tag is visible

This confirms the artifact handoff point of the pipeline.

## Step 10 — Review AKS deployment results
After the deployment stage, verify:
- the manifests were applied
- the workload updated correctly
- the cluster accepted the new deployment
- the pod or deployment is healthy

Microsoft’s KubernetesManifest task documentation notes that the task checks object stability before reporting success, which is a key operational quality of this deployment approach.

## Step 11 — Review rollout visibility and traceability
Now inspect the run from a platform-operations perspective.

The learner should understand:
- which image was built
- which image tag was deployed
- which manifests were applied
- how Azure DevOps helps trace source change to runtime change

This is where the module becomes more than “pipeline runs.” It becomes delivery traceability.

## Step 12 — Compare this to manual deployment
Now reflect on the difference between:
- building and deploying manually
- building and deploying through Azure DevOps

Ask:
- why is the pipeline path more repeatable?
- why is it easier to audit?
- why is it easier to reproduce or troubleshoot later?

This is the core platform reasoning moment of the module.

## Step 13 — Explain the pipeline lifecycle end to end
Now explain the flow in plain language:

- code changes enter the repo
- Azure DevOps builds the image
- Azure DevOps pushes the image to ACR
- Azure DevOps deploys manifests to AKS
- AKS pulls the new image and starts the updated workload

If the learner can explain this clearly, the module is doing its real job.

## Step 14 — Reflect on pipeline-driven AKS delivery as platform maturity
Pause and think beyond the YAML.

In this module, Azure DevOps with AKS means:
- registry and runtime are now connected through automation
- image identity flows from CI into deployment
- rollout becomes visible and traceable
- the platform is becoming reproducible rather than manually operated

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the source repository is connected to Azure DevOps
- the pipeline can build and push an image to ACR
- the pipeline can deploy manifests to AKS
- the workload updates successfully through the pipeline
- the learner understands the handoff from source to registry to cluster

## Step 15 — Prepare for AKS-managed routing options
Before moving to the next module, understand what changes next.

The next module is **AKS HTTP Application Routing**. That means the learner will shift from build-and-deploy lifecycle into another ingress-management pattern supported by AKS.

This is the bridge from deployment automation back into AKS runtime exposure design.

---

## Implementation notes
- keep the first pipeline-to-AKS flow simple and deterministic
- validate build/push and deploy separately, then together
- use very clear image tags during learning
- inspect deployment-stage stability, not only pipeline success
- focus on lifecycle traceability as much as technical success

## End-of-implementation summary
In this lab, you:
- reconfirmed the ACR and AKS trust path
- prepared application source and manifests
- created or reviewed a build-and-push stage
- created or reviewed a deployment stage to AKS
- ran the full pipeline
- validated image creation, registry handoff, and cluster rollout
- practiced the first true end-to-end Azure DevOps-to-AKS delivery pattern in the AKS phase

You are now ready to validate whether the Azure DevOps with AKS lifecycle is clean, correct, and explainable.
