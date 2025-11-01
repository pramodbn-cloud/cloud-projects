# Cleanup

## Purpose of this file
This file defines how to leave the Kubernetes Requests + Limits lab in a clean and reusable state.

This module can leave behind multiple workload versions, comparison manifests, or confusing experimental resource values. Cleanup should preserve the learning value while removing resource settings that no longer match the intended final governance model.

## What should be removed
Remove or clean up:
- duplicate sample workloads created during testing
- unrealistic or extreme request/limit experiments that are no longer part of the final learning path
- abandoned manifests that mix multiple conflicting resource strategies
- temporary notes that make the final scheduler/runtime story harder to follow

If something creates confusion in workload resource behavior without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean workload with explicit requests and limits
- the before/after reasoning notes if they help later review
- one readable manifest pattern that demonstrates the intended resource contract
- the final explanation of scheduler versus runtime behavior

These will support the next module, especially when namespace-level policy controls are introduced.

## Cleanup sequence

1. Review whether multiple workload variants were created by mistake  
2. Keep only the workload version that matches the final intended resource-governance pattern  
3. Remove conflicting or unrealistic trial manifests  
4. Keep one clear record of the request and limit strategy used  
5. Confirm that the retained workload is healthy and readable  
6. Ensure the cluster is ready for Folder 16 without resource-definition clutter  

## Cost awareness note
Resource-governance labs can lead learners to create oversized or unrealistic requests during experimentation. Even in a lab environment, that can waste cluster capacity or create scheduling confusion.

The main cleanup goal here is workload clarity and readiness for namespace-level governance.

## Post-cleanup validation
After cleanup:
- one clean workload resource example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the request/limit contract clearly
- the cluster should feel ready for namespace and policy work

## Final note
This lab is fully complete only when:
- the requests-and-limits workflow has been practiced
- validation is complete
- scheduler and runtime behavior are understood clearly
- unnecessary resource-definition clutter has been removed
- the environment is clean enough to support Folder 16
