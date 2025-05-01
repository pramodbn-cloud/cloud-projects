# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Source Control Strategy lab.

The goal is to create a complete basic repository workflow from remote repository creation through local editing, branch usage, push flow, and pull request creation.

---

## Step 1 — Understand the source control goal
Before creating the repository, understand what this module is trying to teach.

This lab is not about storing files in a remote tool. It is about learning how modern engineering teams manage changes safely using repositories, branches, commits, and pull requests.

At the end of this lab, you should have:
- one usable repository
- a local clone or connected working copy
- one isolated branch change flow
- one pull request workflow completed or reviewed

## Step 2 — Open Azure Repos in your project
Go to your Azure DevOps project and open the Repos area.

Spend a few minutes observing:
- the repository interface
- file browsing area
- branch-related options
- commit/history sections
- pull request area

Do not rush ahead. First understand that this is the shared code collaboration space for the project.

## Step 3 — Create the repository
If your project does not already contain the intended repository, create a new one.

Choose a professional and reusable name that fits the course direction.

Recommended example:
- `azure-devops-aks-job-ready`

The purpose of this step is to establish the shared implementation container that future modules will build on.

## Step 4 — Initialize the repository with simple starter content
You can initialize the repository in a simple way, either through the Azure DevOps interface or from your local machine after cloning.

Keep the content minimal and clear.

Examples:
- a root `README.md`
- a short project description
- one placeholder folder or file showing the repo purpose

This step matters because it turns the repository into a working code location instead of an empty concept.

## Step 5 — Clone the repository to the local machine
Copy the clone URL and connect the repository to your local machine.

Clone it into the dedicated course working folder you created earlier.

Once cloned, verify that:
- the folder exists locally
- the repository contents are visible
- the local working copy is now connected to Azure Repos

This is the bridge between local engineering work and shared team history.

## Step 6 — Open the repository in your editor
Open the cloned repository in your code editor.

Review the file structure and make sure the local environment feels ready for real changes.

At this stage, the learner should feel comfortable that editing locally and syncing with the remote repo is now possible.

## Step 7 — Create a feature branch
Before making a change, create a new branch.

Use a clear and readable name that explains the purpose of the work.

Examples:
- `feature/repo-setup`
- `feature/readme-enhancement`

This step is one of the most important in the module because it teaches isolated development instead of editing directly on the main branch.

## Step 8 — Make a simple, meaningful change
Inside the new branch, make one clean update.

Examples:
- improve the root README
- add a course-structure note
- create one starter file describing the module flow

Do not make a random change. Make a change that feels meaningful and easy to review.

## Step 9 — Review the local change
Before committing, inspect what changed.

Ask:
- Is the change clear?
- Is it small enough to understand easily?
- Would a teammate understand why this was changed?

This step helps build good commit discipline.

## Step 10 — Commit the change
Create a commit that records the change with a readable message.

The message should clearly express what was done.

Examples:
- `Add initial repository overview`
- `Update root README with course structure`

Avoid vague messages. Commit messages are part of team communication.

## Step 11 — Push the branch to Azure Repos
Push the feature branch to the remote repository.

Once pushed, verify that:
- the branch appears in Azure Repos
- the change history is visible
- the remote platform now reflects the isolated work

This is where the branch becomes part of the shared workflow.

## Step 12 — Create a pull request
Open a pull request from the feature branch into the main branch.

At this stage, review:
- the branch being merged from and into
- the title of the pull request
- the summary of the change
- the visible diff if available

This step is critical because it teaches that merge should happen through a review boundary, not by careless direct change.

## Step 13 — Review the pull request like a collaborator
Even if this is a solo practice repo, review the pull request from a team mindset.

Ask:
- Is the title clear?
- Is the change size reasonable?
- Would this be easy for a reviewer to approve?
- Is the branch purpose obvious?

This helps the learner understand that pull requests are collaboration tools, not just merge buttons.

## Step 14 — Complete the merge if appropriate
If your practice setup allows it and the flow is clear, complete the pull request and merge the change into the main branch.

After merge, confirm that:
- the main branch contains the change
- the history reflects the completed workflow
- the learner can now describe the full path from local edit to shared merge

## Step 15 — Reflect on source control strategy
Pause and think beyond the mechanics.

In this module, source control strategy means:
- code lives in a shared history
- changes should be isolated before merge
- branches protect stability
- commits preserve intent
- pull requests improve review and confidence

This mindset is more important than any single button click.

---

## Checkpoint
At this point, the following should already be true:

- the repository exists in Azure DevOps
- the local machine is connected to it
- a branch was created intentionally
- a meaningful change was committed
- the branch was pushed successfully
- a pull request was created and understood

## Step 16 — Prepare for CI thinking
Before moving to the next module, recognize the next workflow step.

The next module introduces CI pipelines. Once code changes exist in a repository and move through branch workflows, the next logical step is to automate validation of those changes.

This is the bridge from source control into build automation.

---

## Implementation notes
- keep the repository content simple in this module
- focus on workflow, not application complexity
- use readable names for repositories, branches, and commits
- avoid direct edits on the main branch for practice
- treat the pull request as a review boundary, not a formality

## End-of-implementation summary
In this lab, you:
- opened Azure Repos
- created or confirmed a repository
- connected it to your local machine
- created a feature branch
- made a meaningful change
- committed and pushed that change
- created and reviewed a pull request
- completed the first full source control collaboration cycle

You are now ready to validate whether the repository workflow is clean, correct, and explainable.
