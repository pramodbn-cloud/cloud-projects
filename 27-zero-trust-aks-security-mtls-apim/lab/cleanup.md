# Cleanup

## Purpose of this file
This file defines how to leave the Zero-Trust AKS Security with mTLS + Azure API Management lab in a clean and reusable state.

This module can create API Management configuration, certificate references, backend trust relationships, and multiple security design variants. Cleanup should preserve the learning value while removing ambiguity in the trust model or certificate flow.

## What should be removed
Remove or clean up:
- duplicate APIM policy variants created during testing
- superseded certificate paths or temporary trust experiments
- ambiguous notes that mix standard TLS and mTLS behavior
- backend definitions that no longer match the final intended trust model
- temporary client-test artifacts that are no longer useful

If something creates trust-chain confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final APIM-to-AKS architecture description
- the final trust-chain explanation
- the final Key Vault and managed identity integration notes
- the final comparison between standard ingress and zero-trust APIM exposure

These are the final premium reference artifacts of the full course.

## Cleanup sequence

1. Review whether multiple APIM security variants were created during testing  
2. Keep only the trust model that matches the final intended zero-trust design  
3. Remove superseded certificate experiments and ambiguous policy remnants  
4. Keep one clear explanation of client trust and backend trust separately  
5. Confirm the retained architecture is readable and intentional  
6. Leave the course in a clean final-benchmark state  

## Cost awareness note
API Management and related enterprise security architecture can have real cost and operational overhead. The biggest risk here is not only spend, but leaving behind an unclear security model that is hard to reason about later.

The main cleanup goal here is trust clarity and a clean specialty-grade final reference architecture.

## Post-cleanup validation
After cleanup:
- one clean zero-trust AKS API architecture should remain
- the learner should still be able to explain the full trust chain clearly
- the course should now feel complete from DevOps foundations to enterprise architecture benchmark

## Final note
This lab is fully complete only when:
- the APIM + mTLS workflow has been practiced or clearly modeled
- validation is complete
- the trust-chain design is understood clearly
- unnecessary security-configuration clutter has been removed
- the course ends in a clean, premium, benchmark-ready final state