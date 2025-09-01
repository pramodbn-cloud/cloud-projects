# Cleanup

## Purpose of this file
This file defines how to leave the Domain Delegation to Azure DNS lab in a clean and reusable state.

This module can create public DNS zones and real delegation changes. Cleanup should preserve the learning value while avoiding confusing or unintended public naming objects that could interfere with later ExternalDNS and hostname-routing modules.

## What should be removed
Remove or clean up:
- duplicate Azure DNS zones created by mistake
- incorrectly scoped zones that do not match the intended delegation design
- abandoned test delegation patterns that no longer reflect the final model
- notes or records that mix root-domain and subdomain strategies in a confusing way

If something creates DNS authority confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final intended Azure DNS zone
- the chosen delegation model
- the Azure authoritative name server notes
- the final explanation of how registrar or parent-zone delegation connects to Azure
- the naming strategy intended for later ExternalDNS and hostname-based ingress work

These will directly support the next advanced modules.

## Cleanup sequence

1. Review whether multiple Azure DNS zones were created by mistake  
2. Keep only the zone that matches the final delegation strategy  
3. Remove or clearly archive incorrect trial zones  
4. Keep one clean record of the Azure name servers for the retained zone  
5. Confirm that the naming strategy remains readable and intentional  
6. Ensure the environment is ready for Folder 12 without DNS-authority confusion  

## Cost awareness note
Azure DNS zones are not just conceptual objects; retaining unnecessary zones or delegation experiments can create both management clutter and operational confusion. The main cleanup goal here is authority clarity and readiness for automation.

## Post-cleanup validation
After cleanup:
- one clear Azure DNS zone should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh DNS start for the next module
- the learner should still be able to explain the delegation path clearly
- the environment should feel ready for ExternalDNS automation

## Final note
This lab is fully complete only when:
- the DNS delegation workflow has been practiced
- validation is complete
- DNS authority transfer is understood clearly
- unnecessary DNS clutter has been removed
- the environment is clean enough to support Folder 12
