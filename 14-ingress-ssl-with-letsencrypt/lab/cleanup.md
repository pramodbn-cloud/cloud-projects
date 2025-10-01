# Cleanup

## Purpose of this file
This file defines how to leave the Ingress SSL with Let’s Encrypt lab in a clean and reusable state.

This module creates certificate resources, issuer objects, TLS secrets, and secure ingress configuration. Cleanup should preserve the learning value while removing duplicate or confusing trust objects that could interfere with later AKS modules or repeated certificate experiments.

## What should be removed
Remove or clean up:
- duplicate Issuer or ClusterIssuer resources created during testing
- abandoned certificate requests or challenge objects from failed experiments
- duplicate TLS secrets that no longer match the intended final ingress design
- hostnames or ingress rules that were only temporary for testing and no longer fit the final scenario
- mixed staging/production trial configurations that make the final trust model unclear

If something creates certificate-lifecycle confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final hostname-based ingress route
- the final working Issuer or ClusterIssuer model
- the final TLS secret used by the ingress
- the validated HTTPS hostname
- the final explanation of the certificate lifecycle from DNS to ingress trust

These will support future reference and keep the platform state understandable.

## Cleanup sequence

1. Review whether multiple certificate or issuer experiments were created by mistake  
2. Keep only the issuer model that matches the final design  
3. Remove duplicate or misleading certificate resources  
4. Keep one clean ingress TLS pattern with one clear hostname  
5. Confirm that the retained TLS secret matches the intended ingress route  
6. Ensure the environment is ready for the next module without certificate-lifecycle clutter  

## Cost awareness note
TLS automation is more about trust state and operational cleanliness than direct infrastructure cost, but duplicate certificate resources, incorrect hostnames, or mixed CA environments can create real confusion and make later testing less trustworthy.

The main cleanup goal here is trust clarity and lifecycle readability.

## Post-cleanup validation
After cleanup:
- one clean secure ingress example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for later modules
- the learner should still be able to explain the certificate lifecycle clearly
- the environment should feel ready for the next production-readiness topic

## Final note
This lab is fully complete only when:
- the TLS workflow has been practiced
- validation is complete
- certificate lifecycle and ingress trust are understood clearly
- unnecessary certificate and ingress clutter has been removed
- the environment is clean enough to support Folder 15
