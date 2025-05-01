# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Source Control Strategy lab.

In this module, the most common failures usually come from repository confusion, branch confusion, or local-to-remote Git workflow mistakes. The purpose here is not only to fix errors, but to help the learner develop source control confidence.

---

## Common issue 1 — Repository exists remotely but is not usable locally

### Symptoms
- the repository is visible in Azure DevOps but not present locally
- local folder exists but is not connected properly
- learner is unsure whether the clone actually worked
- files are missing or the wrong folder is open

### Likely cause
The most common reasons are:
- the repository was not cloned successfully
- the learner opened the wrong local folder
- the clone happened in an unexpected location
- the remote URL or clone flow was not followed carefully

### Fix
- confirm the clone destination clearly
- verify that the intended repository folder exists locally
- reopen the correct folder in the editor
- if needed, reclone into a clean and obvious location

### Re-validation
After the fix:
- confirm the local folder contains the repo files
- confirm the editor is opened at the correct path
- confirm the learner can inspect and edit the tracked content

---

## Common issue 2 — Learner accidentally works on the main branch

### Symptoms
- changes were made directly on the main branch
- no feature branch exists
- learner realizes branch isolation was skipped
- the workflow feels too direct and unsafe

### Likely cause
The learner focused on making the change quickly and forgot the purpose of branch-based development.

### Fix
- stop and identify whether the change should be isolated
- create the intended branch if possible before continuing further
- if the change is already committed, decide whether to keep it for learning or recreate the flow properly in a clean practice cycle
- review why feature branches protect stability and review quality

### Re-validation
After the fix:
- confirm that the meaningful practice flow now includes a feature branch
- confirm the learner can explain why direct main-branch editing is not the preferred practice

---

## Common issue 3 — Commit works locally but push fails

### Symptoms
- commit exists locally
- push command fails or remote does not update
- Azure Repos does not show the new branch or commit
- learner feels stuck between local and remote states

### Likely cause
The most common reasons are:
- authentication issue
- remote configuration issue
- branch upstream was not established properly
- the wrong repository or account is being targeted

### Fix
- verify that the correct Azure DevOps account is being used
- confirm the correct remote repository is configured
- confirm the current branch name
- retry push carefully after checking authentication and branch target

### Re-validation
After the fix:
- confirm the branch appears in Azure Repos
- confirm the commit is visible remotely
- confirm local and remote history now align

---

## Common issue 4 — Pull request is confusing or incorrect

### Symptoms
- wrong source or target branch is selected
- pull request title does not explain the change
- the diff looks unexpected
- the learner is unsure whether the pull request is valid

### Likely cause
The learner may have rushed into PR creation without checking the branch context carefully, or the branch may contain extra unintended changes.

### Fix
- verify source and target branches explicitly
- review the branch content before submitting the PR
- update the title and description so the PR explains the real intent
- ensure the change set is small and understandable

### Re-validation
After the fix:
- confirm the pull request clearly represents the intended change
- confirm a reviewer could understand it without guessing

---

## Common issue 5 — Source control feels mechanical instead of meaningful

### Symptoms
- the learner completed the steps but still does not understand why the workflow matters
- branch, commit, and PR actions feel like tool clicks only
- the module feels procedural rather than collaborative

### Likely cause
The learner may be focusing on commands and UI actions without connecting them to team engineering behavior.

### Fix
Reframe the workflow like this:
- repository = shared implementation history
- branch = safe isolated work area
- commit = recorded unit of intent
- push = move local work into shared visibility
- pull request = controlled collaboration and merge review

Think in terms of team safety and traceability, not just tool navigation.

### Re-validation
After the fix:
- explain the full lifecycle in your own words
- if you can describe why each stage protects the team and the codebase, the concept is now clear

---

## Troubleshooting mindset
While debugging this module, always ask:
- am I in the correct repository?
- am I on the correct branch?
- is my local folder the actual cloned repository?
- did my commit stay local only, or reach the remote?
- is my pull request showing the intended change and nothing extra?

## Escalation rule
If the workflow still feels broken:
1. verify the repository path  
2. confirm the current branch  
3. inspect local changes carefully  
4. verify remote branch visibility  
5. recreate one clean and simple branch flow if needed  
6. prioritize clarity over trying to repair a messy practice state  
