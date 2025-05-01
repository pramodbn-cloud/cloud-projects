# Validation Checks

## Purpose of this file
This file confirms whether the Source Control Strategy lab is complete and correct.

The goal is not only to verify that a repository exists, but to confirm that the learner understands and has practiced the safe workflow of repository-based collaboration.

## Validation approach
For this lab, validation is based on:
- repository existence verification
- local-to-remote connectivity verification
- branch workflow verification
- commit and push verification
- pull request understanding verification

## Check 1 — Repository exists and is usable
Confirm that:
- the repository is visible in Azure Repos
- the learner can open it successfully
- the repository contains the intended starter content

This proves that the shared source control container is ready.

## Check 2 — Local working copy is connected properly
Confirm that:
- the repository is cloned locally
- the working folder is correct
- the learner can view and edit the tracked files locally

This proves that the local and remote workflow connection is working.

## Check 3 — Branch-based workflow was used
Confirm that:
- a feature branch was created
- the change was made on that branch
- the learner did not rely only on direct main-branch editing

This proves that the learner understands isolated development flow.

## Check 4 — Commit history is meaningful
Review the commit created during the lab.

Confirm that:
- the commit exists
- the message is readable
- the change is understandable from the history

This proves that the learner is practicing clear version history discipline.

## Check 5 — Push to Azure Repos worked
Confirm that:
- the feature branch appears remotely
- the pushed commit is visible in Azure Repos
- the learner can see the updated branch history

This proves that the remote collaboration side of the workflow is functioning correctly.

## Check 6 — Pull request exists and makes sense
Confirm that:
- a pull request was created
- the branch source and target are correct
- the title and summary reflect the actual change
- the pull request is understandable from a reviewer’s perspective

This proves that the learner understands the merge boundary and team review concept.

## Check 7 — Main branch reflects the merged change if merge was completed
If the pull request was completed, confirm that:
- the main branch now contains the change
- the learner can identify the merged result
- the history reflects a completed workflow

If the merge was not completed intentionally, the learner should still be able to explain the merge step clearly.

## Check 8 — You can explain the full source control lifecycle in your own words
This is the most important validation for this module.

You should now be able to explain:
- why the repository exists
- why local cloning is needed
- why branches are used
- why commits matter
- why pushing to remote is necessary
- why pull requests improve collaboration safety

If you can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the repository exists and is clean
- the local workflow is connected properly
- branch isolation was used intentionally
- the pull request flow is visible and understandable
- the learner feels ready to connect source control to CI in the next module

## If validation fails
If any validation step fails:
- revisit the implementation sequence
- verify the correct repository and branch were used
- confirm Git connectivity and remote linkage
- re-check the pull request details
- use `troubleshooting.md` for common issues
