# Cleanup

## Purpose of this file
This file defines how to leave the Terraform + Azure DevOps for AKS lab in a clean and reusable state.

This module can create infrastructure pipelines, repeated plan/apply history, and multiple infrastructure variants. Cleanup should preserve the learning value while removing pipeline or infrastructure confusion that weakens the final capstone story.

## What should be removed
Remove or clean up:
- duplicate infrastructure pipelines created during testing
- abandoned pipeline YAML variants that no longer match the final intended capstone design
- superseded Terraform execution experiments that confuse the final lifecycle story
- notes or definitions that mix multiple trust-path models without clear intent

If something creates infrastructure-delivery confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final Terraform pipeline
- the final Terraform AKS codebase
- the final service-connection model
- the final explanation of init, plan, and apply lifecycle through Azure DevOps
- the final end-to-end course-capstone explanation

These are the final reference artifacts of the course.

## Cleanup sequence

1. Review whether duplicate infrastructure pipelines were created during testing  
2. Keep only the pipeline that matches the final intended capstone flow  
3. Remove superseded or misleading variants  
4. Keep one clear explanation of the trust path and lifecycle stages  
5. Confirm the retained Terraform code and pipeline match each other intentionally  
6. Leave the course in a clean, final-capstone state  

## Cost awareness note
Infrastructure pipelines can create real AKS and Azure resource changes. The biggest risk here is not just clutter — it is leaving unintended infrastructure active or leaving an unclear final delivery model that makes later reuse unsafe.

The main cleanup goal here is capstone clarity and avoiding unintended retained infrastructure.

## Post-cleanup validation
After cleanup:
- one clean Terraform + Azure DevOps capstone example should remain
- the learner should still be able to explain the full infrastructure-delivery lifecycle clearly
- the course should now feel complete from runtime through governance through provisioning and delivery

## Final note
This lab is fully complete only when:
- the Terraform + Azure DevOps workflow has been practiced
- validation is complete
- infrastructure-delivery governance is understood clearly
- unnecessary pipeline and infrastructure clutter has been removed
- the course ends in a clean and reusable final state
