# Cleanup

## Purpose of this file
This file defines how to leave the AKS Virtual Nodes lab in a clean and reusable state.

This module can create additional execution paths, workloads targeted to ACI-backed runtime, and extra configuration tied to virtual-node experiments. Cleanup should preserve the learning value while removing duplicate or confusing execution artifacts that could interfere with later modules.

## What should be removed
Remove or clean up:
- duplicate test workloads created only for placement experiments
- abandoned manifests with conflicting placement intent
- notes or configuration fragments that mix standard-node and virtual-node designs confusingly
- unused virtual-node test patterns that no longer match the final lab design

If something creates execution-model confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean workload example targeted to the virtual-node path
- the final notes explaining the chosen execution model
- the comparison notes between standard and virtual-node execution
- the validated explanation of how AKS and ACI work together here

These will support later scaling and cluster-design discussions.

## Cleanup sequence

1. Review whether multiple workload variants were created by mistake  
2. Keep only the workload example that matches the final intended virtual-node pattern  
3. Remove conflicting or abandoned placement manifests  
4. Keep one clear explanation of the ACI-backed execution model  
5. Confirm that the retained resources remain readable and intentional  
6. Ensure the environment is ready for Folder 18 without execution-model clutter  

## Cost awareness note
Virtual-node experiments can affect real runtime backing and associated Azure services. Even in a learning environment, unnecessary retained workloads can create operational confusion and potentially unnecessary spend.

The main cleanup goal here is execution clarity and readiness for secure image delivery and later scaling topics.

## Post-cleanup validation
After cleanup:
- one clean virtual-node example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the execution model clearly
- the environment should feel ready for ACR and secure image supply work

## Final note
This lab is fully complete only when:
- the virtual-node workflow has been practiced
- validation is complete
- the execution-model difference is understood clearly
- unnecessary virtual-node clutter has been removed
- the environment is clean enough to support Folder 18
