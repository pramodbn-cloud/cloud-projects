# Folder 18 — ACR with AKS
![Week-18 Plan](../Posts/18.png)

## Overview
This module introduces Azure Container Registry as the trusted image source for workloads running in AKS. It helps the learner understand how container images move from build output into a private registry, and how AKS authenticates to that registry so workloads can be pulled and started safely.

This is where the course shifts from execution-model flexibility into image-supply discipline. The learner is no longer only asking where a pod runs. The learner is now asking which image source the platform trusts, how that trust is granted, and how that affects workload startup and runtime reliability.

## Why this module matters
A mature AKS platform should not depend casually on unmanaged public image pull behavior. Teams need a reliable and governed registry source, predictable tagging/versioning, and a secure pull path from cluster to registry.

Microsoft documents AKS–ACR integration through `az aks create --attach-acr` or `az aks update --attach-acr`, which automatically assigns the AcrPull role to the AKS managed identity over the registry. Azure’s operator guidance also notes that attaching a registry to an AKS cluster grants AcrPull to the managed identity associated with the agent pools. ACR best-practices guidance also emphasizes image and repository hygiene and strong tagging/versioning strategy.

## What you will learn
- What ACR is in practical AKS platform terms
- How AKS authenticates to ACR to pull private images
- Why image supply is a platform trust and governance concern
- Why registry integration is a major production-readiness step

## Workflow position
This module builds directly on Folder 17, where the learner expanded execution options inside AKS. Now the learner focuses on what images those workloads should actually run, and how the cluster should obtain them safely.

This module also prepares the learner directly for:
- Azure DevOps with AKS deployment patterns
- image lifecycle and promotion thinking
- production-grade cluster design and supply-chain discipline

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain AKS–ACR integration clearly
- understand why AcrPull and managed identity matter
- push an image to ACR and deploy it from AKS
- explain why private-registry-backed workloads are operationally stronger than ad hoc image sourcing

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the image-pull and deployment flow carefully  
5. Do not move ahead until ACR feels clear as a supply-chain trust layer, not only a registry service  

## Next module
The next module is **Azure DevOps with AKS**.

That module builds directly on this one by connecting image build and registry push workflows to deployment automation, so image supply and workload rollout become part of one pipeline-driven platform lifecycle.
