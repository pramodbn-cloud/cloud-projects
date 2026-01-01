# Cleanup

## Purpose of this file
This file defines how to leave the Azure DevOps with AKS lab in a clean and reusable state.

This module can create pipelines, build artifacts, tags, and multiple deployment attempts. Cleanup should preserve the learning value while removing confusing pipeline states or misleading image/deployment history that could interfere with later modules.

## What should be removed
Remove or clean up:
- duplicate pipeline definitions created during testing
- abandoned pipeline YAML variants that no longer match the intended final flow
- misleading image tags from failed experiments
- deployments that no longer represent the final intended pipeline-driven state
- notes or configurations that mix multiple deployment trust paths confusingly

If something creates delivery-lifecycle confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final working pipeline
- the final image repository and deployment tag pattern
- the final service connection model
- the final AKS deployment manifest set
- the validated explanation of the source-to-ACR-to-AKS lifecycle

These will directly support later rollout, scaling, and production-cluster discussions.

## Cleanup sequence

1. Review whether duplicate pipeline definitions or experiments were created by mistake  
2. Keep only the pipeline that matches the final intended lifecycle  
3. Remove abandoned or misleading deployment attempts  
4. Keep one clear image-tagging strategy for the lab  
5. Confirm that the retained workload in AKS reflects the final intended pipeline state  
6. Ensure the environment is ready for Folder 20 without CI/CD clutter  

## Cost awareness note
Pipelines, retained images, and repeated deployment attempts can create clutter even when they are technically successful. In a learning environment, too many half-valid states make the delivery story harder to reason about.

The main cleanup goal here is lifecycle clarity and readiness for the next AKS runtime-exposure module.

## Post-cleanup validation
After cleanup:
- one clean end-to-end Azure DevOps-to-AKS example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the delivery lifecycle clearly
- the environment should feel ready for Folder 20

## Final note
This lab is fully complete only when:
- the Azure DevOps with AKS workflow has been practiced
- validation is complete
- build-to-registry-to-cluster delivery is understood clearly
- unnecessary CI/CD clutter has been removed
- the environment is clean enough to support Folder 20
