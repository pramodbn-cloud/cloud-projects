# Architecture Flow

## Purpose of this file
This file explains the logical source control workflow used in the Source Control Strategy lab before implementation begins.

This module is not mainly about infrastructure architecture. It is about collaboration architecture — how code changes move safely from an individual engineer’s local environment into a shared repository and eventually toward team approval.

## High-level architecture view
The learner works across two connected environments:

- the **local development environment**
- the **remote Azure Repos repository**

The local environment is where changes are created, tested mentally, and prepared through commits.  
The remote repository is where those changes become shared, reviewable, and ultimately mergeable into the main line.

At a high level, the flow looks like this:

- a repository is created or confirmed
- the learner connects the repository to the local machine
- a local working copy is used to make changes
- the learner creates a branch to isolate the work
- commits capture the changes in meaningful history
- the branch is pushed to Azure Repos
- a pull request is opened for controlled merge review

This is the first full implementation workflow in the course.

## Component roles

- **Learner / Engineer** — creates and manages the code change  
- **Local Working Directory** — the place where files are edited and tracked  
- **Git** — the version control mechanism that tracks change history  
- **Azure Repos** — the remote shared repository inside Azure DevOps  
- **Branch** — the isolated line of development for a specific change  
- **Commit** — the unit of recorded change history  
- **Pull Request** — the collaboration and review boundary before merge  

## End-to-end flow

1. A repository is created inside Azure DevOps.  
2. The learner clones or connects to it locally.  
3. Starter content is added or updated in the local copy.  
4. A feature branch is created to isolate the work.  
5. Changes are committed with readable intent.  
6. The branch is pushed to Azure Repos.  
7. A pull request is created to review and merge the change safely.  

## Dependency awareness
This module depends on:
- Folder 01 for Azure DevOps project readiness
- Folder 02 for understanding how planned work connects to execution

This module also prepares for:
- Folder 04, where repository changes will feed into CI pipeline logic

## Operational view
From an engineering workflow perspective, the learner should pay attention to:
- clear repository naming
- disciplined branch usage
- meaningful commits
- safe collaboration boundaries
- merge control
- history clarity

These are the habits that scale from small practice projects to large engineering teams.

## What to keep in mind before implementation
Before starting the steps:
- do not treat the repository as only a file store
- think of the repository as the shared implementation record
- use branches intentionally, not casually
- aim for readable history and clean workflow
- understand that pull requests protect quality and collaboration, not just permissions



