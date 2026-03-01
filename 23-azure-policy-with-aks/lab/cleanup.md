# Cleanup

## Purpose of this file
This file defines how to leave the Azure Policy with AKS lab in a clean and reusable state.

This module can create policy assignments, policy-driven workload outcomes, and multiple governance experiments. Cleanup should preserve the learning value while removing broad or confusing policy state that could interfere with later modules or normal cluster operation.

## What should be removed
Remove or clean up:
- duplicate or overlapping policy assignments created during testing
- broad deny-style policies that were only used experimentally and no longer match the intended final design
- confusing compliant/noncompliant test manifests that are no longer needed
- notes or assignments that mix too many unrelated governance goals in one lab

If something creates policy-governance confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final narrow policy assignment example
- the final compliant/noncompliant manifest pair if useful for later review
- the final explanation of audit versus deny behavior
- the validated explanation of Azure Policy add-on and centralized compliance visibility

These will support later governance and platform-hardening discussions.

## Cleanup sequence

1. Review whether duplicate policy assignments were created during testing  
2. Keep only the policy assignment that matches the final intended learning path  
3. Remove broad or misleading experimental policy state  
4. Keep one clear example of compliant versus noncompliant behavior  
5. Confirm that the retained governance model is readable and intentional  
6. Ensure the environment is ready for Folder 24 without policy clutter  

## Cost awareness note
Azure Policy objects are lightweight technically, but broad or poorly understood policy assignments can create real operational friction. The main cleanup goal here is not cost. It is governance clarity and avoiding accidental cluster disruption later.

## Post-cleanup validation
After cleanup:
- one clean policy-governance example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the policy-enforcement model clearly
- the environment should feel ready for Kubernetes Service Accounts

## Final note
This lab is fully complete only when:
- the Azure Policy with AKS workflow has been practiced
- validation is complete
- audit/enforce governance behavior is understood clearly
- unnecessary policy clutter has been removed
- the environment is clean enough to support Folder 24
