# Cleanup

## Purpose of this file
This file defines how to leave the Source Control Strategy lab in a clean and reusable state.

This module creates important repository history, so cleanup should be thoughtful. The goal is not to delete learning value, but to remove confusion and preserve one clean source control workflow that later modules can build on.

## What should be removed
Remove or clean up:
- accidental duplicate repositories created during testing
- unnecessary branches with unclear names
- abandoned trial commits that do not support the learning flow
- pull requests created by mistake and no longer needed
- local folders that were cloned into the wrong place

If something creates confusion without adding learning value, it should be removed or archived.

## What can be retained
The following should usually be kept:
- the main course repository
- the clean merged history from the lab
- the local cloned working copy in the correct folder
- one readable branch naming pattern
- the updated root README or starter content created during the lab

These items will directly support later modules, especially the CI pipeline module.

## Cleanup sequence

1. Review whether multiple repositories were created by mistake  
2. Keep only the main intended repository  
3. Remove unnecessary or poorly named temporary branches  
4. Confirm that the desired merged content is present in the main branch  
5. Ensure the local repository folder is the correct one to keep using  
6. Remove duplicate local folders if accidental clones were created  

## Cost awareness note
This module does not mainly affect cloud infrastructure cost, but it does affect workflow clarity.

Poor cleanup here can cause confusion in later modules, especially when CI pipelines are connected to the wrong repository or when old branches clutter the collaboration flow.

## Post-cleanup validation
After cleanup:
- one main repository should remain
- the local clone should be correct and usable
- the main branch should reflect the intended starter content
- no confusing extra branches or duplicate repos should distract future work

## Final note
This lab is fully complete only when:
- the repository workflow has been practiced
- validation is complete
- the learner understands the purpose of branch-based collaboration
- the repository is clean enough to support Folder 04
