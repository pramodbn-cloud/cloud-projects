# Cleanup

## Purpose of this file
This file defines how to leave the AKS Ingress Basics lab in a clean and reusable state.

This module creates real cluster resources that can affect later labs if left messy. Cleanup should preserve the learning value while removing accidental or duplicate traffic objects that could interfere with later advanced ingress modules.

## What should be removed
Remove or clean up:
- duplicate ingress resources created during testing
- incorrect or abandoned Service definitions
- extra sample workloads that no longer support the chosen lab path
- unused or experimental ingress-controller resources if they were created only for failed trials
- namespace clutter that makes later routing modules harder to understand

If something creates confusion in the traffic path without strengthening learning, it should be removed or renamed clearly.

## What can be retained
The following should usually be kept:
- the main sample backend workload
- the correct internal Service
- the clean ingress resource that demonstrates the basic path
- notes on the ingress-controller strategy used
- the validated explanation of the end-to-end request flow

These will support the next advanced modules, especially context-path routing and later DNS-based routing.

## Cleanup sequence

1. Review whether multiple ingress resources were created by mistake  
2. Keep only the main intended ingress example  
3. Remove incorrect or duplicate Service and workload objects  
4. Confirm that the retained ingress resource is clean and simple  
5. Ensure the namespace and resource naming remain readable  
6. Confirm that the cluster is ready for Folder 10 without traffic-path clutter  

## Cost awareness note
Ingress-related resources can involve real infrastructure behavior such as external load balancer exposure, depending on the controller model. Even in a learning environment, unnecessary retained resources can create both cost and operational confusion.

The main cleanup goal here is traffic clarity and cluster readiness.

## Post-cleanup validation
After cleanup:
- one clean ingress example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the ingress path clearly
- the cluster should feel ready for advanced routing work

## Final note
This lab is fully complete only when:
- the ingress workflow has been practiced
- validation is complete
- the traffic path is understood clearly
- unnecessary ingress and service clutter has been removed
- the cluster is clean enough to support Folder 10
