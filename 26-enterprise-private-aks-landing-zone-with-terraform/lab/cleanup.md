# Cleanup

## Purpose of this file
This file defines how to leave the Enterprise Private AKS Landing Zone with Terraform lab in a clean and reusable state.

This module can create real enterprise-style Azure infrastructure, including AKS, networking, private endpoints, private DNS zones, and supporting services. Cleanup should preserve the learning value while removing infrastructure sprawl or design variants that weaken the final architecture story.

## What should be removed
Remove or clean up:
- duplicate Terraform variants that no longer match the final architecture
- abandoned private-endpoint experiments
- extra DNS zone variations that are no longer needed
- superseded AKS clusters or resource groups
- trial designs that blur the final landing-zone intent

If something creates architecture confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean Terraform configuration
- the final landing-zone diagram and explanation
- the final private dependency and DNS model
- the final explanation of why this architecture is enterprise-grade

These will directly support the next specialty module.

## Cleanup sequence

1. Review whether multiple architecture variants were created during testing  
2. Keep only the Terraform configuration that matches the final intended landing-zone design  
3. Remove duplicate private endpoint or DNS experiments  
4. Confirm that retained infrastructure still reflects one clear private platform model  
5. Keep one clear explanation of the trust boundary and dependency design  
6. Ensure the environment is ready for Folder 27 without landing-zone clutter  

## Cost awareness note
This is a real cost-sensitive module. Private AKS, private endpoints, DNS zones, and supporting platform services can create significant retained Azure spend if left running unnecessarily. Cost awareness here is part of platform maturity.

## Post-cleanup validation
After cleanup:
- one clean enterprise AKS landing-zone example should remain, if intentionally reused
- or the lab should be fully cleaned if a fresh start is preferred
- the learner should still be able to explain the architecture clearly
- the environment should feel ready for the zero-trust API security module

## Final note
This lab is fully complete only when:
- the architecture has been practiced or clearly modeled
- validation is complete
- the private enterprise platform story is understood clearly
- unnecessary infrastructure clutter has been removed
- the environment is clean enough to support Folder 27