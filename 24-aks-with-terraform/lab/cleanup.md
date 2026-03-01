# Cleanup

## Purpose of this file
This file defines how to leave the AKS with Terraform lab in a clean and reusable state.

This module can create real Azure infrastructure, Terraform state files, and multiple configuration experiments. Cleanup should preserve the learning value while removing confusion in state, duplicated resources, or leftover AKS clusters that no longer match the final intended Terraform model.

## What should be removed
Remove or clean up:
- duplicate Terraform experiments that no longer reflect the intended final design
- abandoned AKS clusters or resource groups from failed or superseded test runs
- misleading variable sets or file variants that make the final IaC story harder to follow
- local artifacts that should not be treated as the final intended configuration

If something creates IaC confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean Terraform configuration
- the final validated AKS cluster design
- the final explanation of provider, plan, apply, and state
- the final notes that connect Terraform provisioning to the pipeline-driven capstone

These will directly support Folder 25.

## Cleanup sequence

1. Review whether multiple Terraform variants were created during testing  
2. Keep only the configuration that matches the final intended AKS design  
3. Remove duplicated or superseded infrastructure if no longer needed  
4. Keep one clear explanation of the state and lifecycle model  
5. Confirm that the retained configuration is readable and intentional  
6. Ensure the environment is ready for Folder 25 without IaC clutter  

## Cost awareness note
AKS clusters and supporting Azure resources can incur real cost. Terraform labs make it easy to create full infrastructure quickly, so forgotten clusters or duplicate environments can become an expensive form of clutter.

The main cleanup goal here is IaC clarity and avoiding unnecessary retained Azure infrastructure.

## Post-cleanup validation
After cleanup:
- one clean AKS Terraform example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the Terraform provisioning lifecycle clearly
- the environment should feel ready for the Terraform + Azure DevOps capstone

## Final note
This lab is fully complete only when:
- the AKS-with-Terraform workflow has been practiced
- validation is complete
- the IaC lifecycle is understood clearly
- unnecessary infrastructure and config clutter has been removed
- the environment is clean enough to support Folder 25
