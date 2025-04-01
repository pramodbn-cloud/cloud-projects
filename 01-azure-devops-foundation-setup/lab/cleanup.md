# Cleanup

## Purpose of this file
This file defines how to close the Azure DevOps foundation setup lab cleanly without creating unnecessary clutter.

This module does not create many billable cloud resources, but it can still create confusion later if duplicate organizations, duplicate projects, or messy local folders are left behind.

## What should be removed
Remove or avoid keeping:
- duplicate test projects created by mistake
- temporary naming experiments that are no longer needed
- unused local folders created during trial setup
- notes or drafts that may confuse later module execution

## What can be retained
The following should usually be kept because they will be reused in later modules:
- the main Azure DevOps organization
- the main learning project
- the dedicated local root folder for the repository
- the chosen naming convention notes
- any tool installations completed during this module

## Cleanup sequence

1. Review whether you created extra or duplicate projects by mistake  
2. Keep only the main project intended for the course  
3. Delete or archive any accidental setup artifacts that may create confusion later  
4. Confirm that your local machine has one clean root working folder  
5. Confirm that your saved naming decisions are clear and final  

## Cost awareness note
This module does not usually create major billable resources, but poor setup discipline can still create management clutter later.

The real cleanup goal here is not cost reduction alone. It is environment clarity.

## Post-cleanup validation
After cleanup:
- one main Azure DevOps organization should remain in use
- one main project should remain for the course
- the local working folder should be clean and intentional
- the learner should feel confident, not confused, about what will be reused later

## Final note
This lab is fully complete only when:
- the setup is finished
- validation has been completed
- setup confusion has been removed
- the working environment is clean enough to support Module 02
