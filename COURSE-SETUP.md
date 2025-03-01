# Course Setup

This file defines the baseline setup required before starting the modules in this repository.

The goal of this setup is to create a clean, repeatable learning environment that supports all modules from basic Azure DevOps through advanced AKS workflows.

---

## Setup Objective

Before beginning the course, the learner should have:

- a working Azure account
- access to Azure DevOps
- a local development machine prepared
- core CLI tools installed
- Kubernetes tooling ready
- consistent naming conventions for all labs

This reduces confusion and helps maintain consistency across all modules.

---

## Required Accounts

The learner should prepare the following:

### Azure Account
Used for Azure resources such as:
- resource groups
- AKS
- Azure DNS
- Azure Container Registry

### Azure DevOps Account
Used for:
- organization
- projects
- repos
- pipelines
- artifacts
- boards

### GitHub Account
Optional for profile visibility or external reference, but not required for completing the repository.

---

## Local Machine Requirements

Recommended local environment:

- Windows or macOS or Linux
- stable internet connection
- administrative access for installing tools
- VS Code or equivalent editor

---

## Required Tools

Install and verify the following tools before starting advanced modules:

### Core tools
- Git
- Visual Studio Code
- Azure CLI
- kubectl
- Helm
- Docker Desktop or Docker Engine
- Node.js if needed for basic application/pipeline examples

### Recommended supporting tools
- Markdown preview support in VS Code
- YAML extension in VS Code
- Kubernetes extension in VS Code

---

## Tool Verification

Before starting the course, confirm that the following commands work in your terminal:

- `git --version`
- `az --version`
- `kubectl version --client`
- `helm version`
- `docker --version`

If any tool is missing or fails, fix that before starting the labs.

---

## Azure DevOps Preparation

Before starting the modules, ensure that you can:

- sign in to Azure DevOps
- create or access an organization
- create a project
- access Azure Repos, Boards, Pipelines, and Artifacts

---

## Azure Preparation

Before starting AKS-related modules, ensure that you understand the basics of:

- subscription selection
- resource groups
- region choice
- cost awareness
- role/permission boundaries

---

## Naming Convention Recommendation

To keep all labs clean and easy to track, use one consistent naming pattern.

Recommended pattern:

`<project>-<environment>-<purpose>`

Examples:
- `ado-dev-rg`
- `ado-dev-aks`
- `ado-dev-acr`
- `ado-dev-dns`
- `ado-dev-app`

This helps maintain clarity throughout the course.

---

## Folder Progression Dependency

The course is intentionally progressive.

This means:

- do not begin advanced AKS modules before completing at least the main Azure DevOps foundation modules
- follow the roadmap in sequence
- reuse prior learning when later modules depend on earlier setup

---

## Cost Awareness

Some advanced Azure modules may create billable resources.

Before starting advanced labs:

- review pricing implications
- delete unused resources after validation
- follow cleanup instructions carefully
- avoid leaving clusters or public resources running unnecessarily

---

## Recommended Learning Preparation

Before beginning:

- read the root `README.md`
- review `COURSE-ROADMAP.md`
- understand the repository structure
- create a notebook or digital notes file for your learning summaries
- prepare to document validation results for each module

---

## Definition of Ready

You are ready to begin the repository when:

- your local tools are installed
- Azure login works
- Azure DevOps access works
- terminal commands succeed
- you understand the course flow
- you are ready to learn one module at a time without skipping foundational logic

Once this is complete, begin with Module 01.
