# Folder 19 — Azure DevOps with AKS
![Week-19 Plan](../Posts/19.png)

## Overview
This module connects Azure DevOps delivery automation directly to AKS runtime deployment. It helps the learner understand how source code, container image build, ACR push, and AKS deployment can be tied together into one controlled pipeline flow.

This is where the AKS track becomes a true platform-delivery story instead of a set of separate infrastructure and runtime topics. The learner is no longer only working with clusters, registries, and manifests manually. The learner is now thinking in terms of repeatable CI/CD execution that moves workloads into AKS safely and visibly.

## Why this module matters
A production-ready AKS platform should not depend on manual image pushes and manual kubectl deployment steps for every change. Teams need a delivery flow that is consistent, reviewable, and traceable from code to container image to cluster rollout.

Microsoft documents Azure Pipelines workflows that build a container image, push it to ACR, and then deploy to AKS using deployment jobs and the `KubernetesManifest` task. Microsoft also documents that the Kubernetes manifest task supports deployment, creation of image pull secrets, manifest baking, rollout-oriented actions, and stability checks before marking the deployment successful.

## What you will learn
- How Azure DevOps pipelines connect to ACR and AKS
- How build, push, and deploy become one end-to-end pipeline
- Why service connections and deployment tasks matter in AKS delivery
- Why pipeline-driven deployment is a major platform maturity step

## Workflow position
This module builds directly on:
- Folder 18 — ACR with AKS
- earlier Azure DevOps foundation modules
- the AKS runtime and ingress modules already completed

Now that the learner has a trusted registry and a working AKS platform, the next step is to make image promotion and deployment repeatable through Azure DevOps.

This module also prepares the learner directly for:
- later rollout strategy thinking
- autoscaling and production-cluster operations
- more advanced platform automation patterns

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain Azure DevOps-to-AKS delivery flow clearly
- build and push an image to ACR from a pipeline
- deploy that image to AKS from the same delivery path
- explain why this pattern is stronger than manual image/deployment workflows

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the build-push-deploy lifecycle carefully  
5. Do not move ahead until Azure DevOps with AKS feels clear as a platform delivery pattern, not only a YAML pipeline  

## Next module
The next module is **AKS HTTP Application Routing**.

That module shifts the focus back to ingress-management options in AKS, but now with a much stronger understanding of how applications actually reach the cluster through a delivery pipeline.
