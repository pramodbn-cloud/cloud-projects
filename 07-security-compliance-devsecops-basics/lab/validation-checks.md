# Validation Checks

## Purpose of this file
This file confirms whether the Security + Compliance lab is complete and correct.

The goal is not only to verify that a security-related item was created, but to confirm that the learner understands the main trust boundaries that protect delivery workflows in Azure DevOps.

## Validation approach
For this lab, validation is based on:
- permission and security-model understanding
- service connection understanding
- variable group and secret handling understanding
- least-privilege awareness
- learner explanation ability

## Check 1 — Project security model is understood at a practical level
Confirm that:
- the learner understands that Azure DevOps permissions are shaped by groups, roles, and inheritance
- the learner can explain why not all users should receive equal access
- the learner can identify at least one place where broad access would be risky

This proves that delivery is now being viewed through a governance lens.

## Check 2 — Service connection purpose is clear
Confirm that:
- a service connection exists or was reviewed meaningfully
- the learner understands what external resource it connects to
- the learner can explain why service connections are sensitive trust points

This proves that external delivery access is being treated seriously.

## Check 3 — Least privilege is understood and applied conceptually
Confirm that:
- the learner can explain why automation should not receive more access than necessary
- the service connection or permission scenario was reviewed with scope awareness
- the learner can identify one example of over-permission risk

This proves that the module has moved beyond feature usage into secure design thinking.

## Check 4 — Variable group usage is visible or clearly modeled
Confirm that:
- a variable group exists or is clearly understood
- it includes shared configuration logic
- the learner understands how it can be used across pipelines

This proves that pipeline configuration is being treated as a managed resource.

## Check 5 — Secret handling is improved from naive patterns
Confirm that:
- the learner understands that secrets should not be placed in plain text YAML
- the learner knows that UI secrets, variable groups, or Key Vault-backed variable groups are preferred patterns
- the learner can explain how secrets differ from normal variables

This proves that sensitive data handling is now safer and more intentional.

## Check 6 — Resource restrictions and sharing controls are understood
Confirm that:
- the learner understands that not all pipelines should automatically access all variable groups or secure files
- the learner has basic awareness of restricted pipeline permissions for library resources
- resource sharing is being thought of as controlled, not automatic

This proves that governance is part of the learner’s model.

## Check 7 — Secure files are understood at a high level
Confirm that:
- the learner understands when a sensitive file is different from a sensitive variable
- the learner knows Azure Pipelines offers secure files for this use case
- the learner can explain the difference at a high level

This proves that the learner is seeing multiple secure resource patterns, not only one.

## Check 8 — You can explain the DevSecOps lifecycle in your own words
This is the most important validation for this module.

You should now be able to explain:
- why security belongs inside the delivery workflow
- how permissions and inheritance shape access
- why service connections are trust boundaries
- how secret variables and variable groups improve safety
- why least privilege matters
- why pipeline/resource governance should be intentional

If you can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the learner understands the main Azure DevOps security surfaces
- service connection trust is understood
- secret handling is safer and more intentional
- least-privilege thinking is present
- the learner feels ready to move into operational visibility and automation

## If validation fails
If any validation step fails:
- revisit the security model and permission areas
- simplify the service connection scenario
- review variable group and secret guidance again
- re-check the difference between shared config and sensitive data
- use `troubleshooting.md` for common DevSecOps issues
