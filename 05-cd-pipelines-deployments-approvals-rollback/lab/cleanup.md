# Cleanup

## Purpose of this file
This file defines how to leave the CD Pipelines lab in a clean and reusable state.

This module begins to create release history, deployment-stage structure, and possibly test approval logic. Cleanup should preserve the learning value while removing confusing duplicates or unnecessary release clutter.

## What should be removed
Remove or clean up:
- duplicate or abandoned deployment pipelines
- trial stage definitions that no longer match the chosen release flow
- unclear or incorrectly named environments
- release runs created only for failed experiments and no longer useful
- placeholder approval configurations that confuse the intended workflow

If something creates confusion without strengthening learning, it should be removed or renamed clearly.

## What can be retained
The following should usually be kept:
- the main CD or deployment pipeline
- the clean release stage structure
- the artifact linkage from CI
- one understandable approval model
- the documented rollback approach

These will support future modules and strengthen the learner’s delivery understanding.

## Cleanup sequence

1. Review whether multiple release pipelines were created by mistake  
2. Keep only the main intended deployment flow  
3. Remove or ignore abandoned stage experiments with no learning value  
4. Confirm that the correct CI artifact remains linked  
5. Keep stage names clean and consistent  
6. Ensure the project is ready for the next module without release clutter  

## Cost awareness note
This module may begin interacting with deployment-like targets or environment concepts. Even if the lab is simplified, repeated delivery experiments can still create confusion and operational clutter.

The main cleanup goal here is not only cost awareness. It is stage clarity and reuse readiness.

## Post-cleanup validation
After cleanup:
- one main deployment flow should remain
- its stages should be easy to explain
- the artifact linkage should still be correct
- the rollback story should remain documented clearly
- the learner should feel ready to move into package management strategy

## Final note
This lab is fully complete only when:
- the CD workflow has been practiced
- validation is complete
- approval and rollback logic are understood
- unnecessary release clutter has been removed
- the project is clean enough to support Folder 06
