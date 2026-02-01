# Cleanup

## Purpose of this file
This file defines how to leave the AKS Autoscaling lab in a clean and reusable state.

This module can create HPAs, multiple workload replicas, and changed node-pool size over time. Cleanup should preserve the learning value while removing scaling artifacts or resource drift that could interfere with later governance-focused modules.

## What should be removed
Remove or clean up:
- duplicate HPA objects created during testing
- abandoned workload variants used only for scale experiments
- unrealistic min/max settings that no longer reflect the intended lab design
- temporary load-generation tools or test pods that are no longer needed
- notes or manifests that mix different scaling strategies confusingly

If something creates elasticity confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final sample workload
- the final HPA example
- the final Cluster Autoscaler boundary settings used for the lab
- the final explanation of pod-scaling versus node-scaling behavior

These will support later capacity, cost, and governance discussions.

## Cleanup sequence

1. Review whether duplicate HPA or workload variants were created during testing  
2. Keep only the scaling objects that match the final intended learning path  
3. Remove temporary load-generation artifacts if they are no longer needed  
4. Confirm node-pool autoscaler bounds are left in an intentional state  
5. Keep one clear explanation of HPA versus Cluster Autoscaler  
6. Ensure the environment is ready for Folder 23 without elasticity clutter  

## Cost awareness note
Autoscaling experiments can change real node count and therefore real spend. Even in a learning environment, scale-up and delayed scale-down can leave the cluster more expensive than intended if not reviewed afterward. AKS guidance also ties autoscaler behavior directly to cost optimization.

The main cleanup goal here is elasticity clarity and avoiding accidental retained capacity.

## Post-cleanup validation
After cleanup:
- one clean autoscaling example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the elasticity chain clearly
- the environment should feel ready for Azure Policy with AKS

## Final note
This lab is fully complete only when:
- the autoscaling workflow has been practiced
- validation is complete
- HPA and Cluster Autoscaler behavior are understood clearly
- unnecessary scaling clutter has been removed
- the environment is clean enough to support Folder 23
