# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Source Control Strategy lab.

This module is practical and depends on both the Azure DevOps platform side and the local machine side being ready to work together.

## Required account access
You should have working access to:
- Azure DevOps
- the organization created or confirmed in Folder 01
- the project used for the learning repository
- Azure Repos inside that project

## Required tools
The following tools should be available on your machine:

- Git
- a code editor such as Visual Studio Code
- terminal access such as PowerShell, Command Prompt, or Bash
- a web browser for Azure DevOps access

Optional but recommended:
- Git integration inside the editor
- a markdown preview extension if you plan to edit README files

## Required permissions
You should be able to:
- create or access repositories inside the project
- clone a repository
- push branches to the remote repository
- create a pull request

If working in a controlled enterprise environment, verify that repository creation and push permissions are available.

## Required prior modules
You should complete:
- Folder 01 — Azure DevOps Foundation Setup
- Folder 02 — Agile Planning + Traceability

These earlier modules created the project structure and delivery context that this repository workflow now supports.

## Required environment state
Before starting:
- Azure DevOps project access should work
- the learner should be able to open Repos in the project
- Git should work from the terminal
- a local working folder should already exist from earlier setup
- the learner should understand the basic purpose of planned work from Folder 02

## Repository content recommendation
For this lab, keep the starter content simple.

Recommended options:
- a root `README.md`
- a sample text file describing the project
- a small starter folder structure for the course repo

The goal is to practice workflow, not build application complexity yet.

## Naming convention to follow
Use clear and consistent naming.

Recommended examples:
- repository name: `azure-devops-aks-job-ready`
- branch name: `feature/repo-setup`
- branch name: `feature/readme-update`
- commit message: short, action-based, readable

Avoid vague names like:
- `test`
- `new`
- `changes`
- `final-final`

## Definition of ready
The learner is ready to begin this lab when:
- Azure Repos is accessible
- Git works locally
- the local working folder is ready
- repository naming has been thought through
- the learner is ready to practice isolated, reviewable code changes
