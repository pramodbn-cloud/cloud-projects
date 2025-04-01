# Prerequisites

## Purpose of this file
This file defines everything that must be ready before starting the Azure DevOps foundation setup lab.

This lab is simple compared to later modules, but it still depends on clean access and a prepared machine. The better the preparation here, the easier the full course becomes.

## Required account access

### Azure DevOps access
You should be able to sign in to Azure DevOps using your Microsoft account or work account.

### Azure account
An Azure account is recommended because later modules in this repository will depend on Azure services such as AKS, Azure DNS, and Azure Container Registry.

For this specific module, full Azure resource creation is not the main focus, but the account should still be available for continuity.

## Required tools

Install or verify the following tools on your machine:

- Git
- Visual Studio Code or another code editor
- Azure CLI
- A modern web browser
- Terminal access such as PowerShell, Command Prompt, or Bash

Optional but recommended for later modules:
- kubectl
- Helm
- Docker

## Required permissions
For this module, the learner should have:
- permission to sign in to Azure DevOps
- permission to create or access an Azure DevOps organization
- permission to create or access a project inside that organization

If working in a restricted enterprise environment, ensure these permissions are available before beginning.

## Required prior modules
There are no prior modules for this lab because this is the first module in the course.

## Required environment state
Before starting:
- the learner should have internet access
- the local machine should allow tool installation or already have the tools installed
- Azure DevOps sign-in should work
- terminal commands should be executable on the machine

## Naming convention to follow
To keep the repository professional and consistent, use simple and readable naming.

Recommended pattern:

`ado-foundation-<purpose>`

Examples:
- `ado-foundation-project`
- `ado-foundation-demo`
- `ado-foundation-lab`

For personal learning, choose one naming style and use it consistently.

## Definition of ready
The learner is ready to begin this lab when:
- Azure DevOps sign-in works
- the browser can access the Azure DevOps portal
- Git is installed
- the code editor is ready
- terminal access is working
- the learner is ready to create the initial organization and project structure
