# Cleanup

## Purpose of this file
This file defines how to leave the CI Pipelines lab in a clean and reusable state.

This module begins to create real automation history and possibly multiple test runs. Cleanup should preserve learning value while removing unnecessary pipeline clutter that could confuse later modules.

## What should be removed
Remove or clean up:
- duplicate pipelines created during trial attempts
- failed experimental pipeline definitions no longer needed
- meaningless test artifacts created by mistake
- outdated trigger experiments that confuse expected behavior
- repository test changes that do not support the intended course flow

If something adds noise without teaching value, it should be removed or renamed clearly.

## What can be retained
The following should usually be kept:
- the main CI pipeline
- the successful pipeline definition
- one or more successful runs for reference
- the artifact output pattern that will support later modules
- the repository structure needed by the pipeline

These will directly support the deployment-focused module that follows.

## Cleanup sequence

1. Review whether multiple pipelines were created by mistake  
2. Keep only the main intended CI pipeline  
3. Remove or ignore failed trial pipelines that no longer have learning value  
4. Confirm that the correct repository and branch remain connected  
5. Keep the successful artifact pattern and pipeline naming clear  
6. Ensure the repository stays in a clean state for the next module  

## Cost awareness note
This module may not create major infrastructure cost by itself, but repeated artifacts, excessive runs, and unnecessary pipeline clutter can reduce clarity and make later debugging harder.

The main cleanup goal here is workflow clarity and reuse readiness.

## Post-cleanup validation
After cleanup:
- one main CI pipeline should remain
- its purpose should be easy to explain
- the repository should still support it cleanly
- the learner should feel ready to use the artifact in Folder 05

## Final note
This lab is fully complete only when:
- the pipeline flow has been practiced
- validation is complete
- CI purpose is understood clearly
- unnecessary automation clutter has been removed
- the project is clean enough to support Folder 05
