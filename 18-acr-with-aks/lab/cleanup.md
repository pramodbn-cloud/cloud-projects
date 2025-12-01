# Cleanup

## Purpose of this file
This file defines how to leave the ACR with AKS lab in a clean and reusable state.

This module can create registries, repositories, tags, and multiple test deployments. Cleanup should preserve the learning value while removing confusing image variants or misleading cluster-to-registry trust experiments.

## What should be removed
Remove or clean up:
- duplicate test images that no longer support the final learning scenario
- confusing or accidental tags
- abandoned deployments using incorrect image references
- notes or manifests that mix multiple registry trust patterns confusingly
- trial image-pull experiments that are no longer part of the final model

If something creates supply-chain confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean ACR registry
- the final sample image repository and tag
- the confirmed AKS–ACR trust path
- the final working deployment from the private image
- the validated explanation of registry-to-cluster image pull flow

These will directly support the next module, where Azure DevOps pipelines will build, push, and deploy through this registry path.

## Cleanup sequence

1. Review whether duplicate images or tags were created during testing  
2. Keep only the image set that matches the final intended learning path  
3. Remove abandoned or misleading workload definitions  
4. Keep one clear explanation of the AKS–ACR trust model  
5. Confirm that the retained deployment still points to the intended image  
6. Ensure the environment is ready for Folder 19 without registry-clutter confusion  

## Cost awareness note
Registry resources, stored images, and retained tags can accumulate over time. Even in a learning environment, image clutter can weaken clarity and make later CI/CD automation harder to reason about.

The main cleanup goal here is supply-chain clarity and readiness for pipeline-driven deployment.

## Post-cleanup validation
After cleanup:
- one clean registry-backed workload example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the private image pull flow clearly
- the environment should feel ready for Azure DevOps-to-AKS automation

## Final note
This lab is fully complete only when:
- the ACR workflow has been practiced
- validation is complete
- private-registry trust and image identity are understood clearly
- unnecessary image and deployment clutter has been removed
- the environment is clean enough to support Folder 19
