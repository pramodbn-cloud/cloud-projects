# Troubleshooting

## Purpose of this file
This file helps the learner understand common setup issues that may appear during the Azure DevOps foundation setup lab.

The goal is not only to fix problems. The goal is also to understand why these problems happen, so later labs feel easier and more controlled.

---

## Common issue 1 — Unable to sign in to Azure DevOps

### Symptoms
- sign-in page does not complete successfully
- account loops back to login
- access error appears after login
- the portal opens but project access is missing

### Likely cause
The most common reasons are:
- incorrect account was used
- enterprise access restrictions exist
- browser session is stale
- the learner is signed into a different Microsoft account than intended

### Fix
- confirm which Microsoft or work account should be used
- sign out and sign in again carefully
- try a private browser window
- confirm whether the organization is tied to a specific work account
- if in an enterprise environment, confirm access with the administrator

### Re-validation
After the fix:
- open Azure DevOps again
- confirm successful sign-in
- confirm the correct organization and project are visible

---

## Common issue 2 — Unable to create or access an organization

### Symptoms
- the portal opens but no organization is available
- organization creation fails
- existing organization is visible but inaccessible
- permission-related messages appear

### Likely cause
The most common causes are:
- insufficient permissions
- organization was created under another account
- naming conflict during creation
- enterprise controls restrict self-service creation

### Fix
- confirm whether you should create a new organization or reuse an existing one
- verify that the correct account is signed in
- retry with a simpler organization name
- if working under company controls, confirm your access model before continuing

### Re-validation
After the fix:
- ensure the organization appears in the portal
- confirm that it opens successfully
- verify that you can navigate inside it

---

## Common issue 3 — Project creation fails or project is not visible

### Symptoms
- project creation does not complete
- project appears to create but is not visible later
- permission or visibility settings cause confusion
- the learner is unsure whether the project exists properly

### Likely cause
The likely reasons are:
- project creation did not fully finish
- the learner is in the wrong organization
- visibility or naming caused confusion
- browser state is stale

### Fix
- refresh the portal and confirm the current organization
- search for the project name carefully
- create the project again only if it truly does not exist
- use a clean and distinct project name

### Re-validation
After the fix:
- confirm the project appears in the correct organization
- open it directly
- check that Boards, Repos, Pipelines, and other sections are visible

---

## Common issue 4 — Git or Azure CLI does not work locally

### Symptoms
- terminal says command not found
- version commands fail
- tools are installed but not recognized
- the learner is unsure whether installation completed correctly

### Likely cause
The common reasons are:
- tool was not installed fully
- PATH was not refreshed
- terminal session needs restart
- installation was performed for another user context

### Fix
- verify installation properly
- restart terminal
- reopen the machine if needed
- check whether the tool is available in system PATH
- reinstall only if truly necessary

### Re-validation
After the fix:
- run version commands again
- confirm the terminal recognizes the tools successfully

---

## Common issue 5 — Learner feels setup is done but still feels unclear

### Symptoms
- all access works, but the learner still feels lost
- the interface looks unfamiliar
- uncertainty exists about what Boards, Repos, Pipelines, and Artifacts are for
- the learner is worried about later modules

### Likely cause
This is usually not a technical problem. It is a familiarity problem.

The learner may have completed the setup but not yet translated the platform into a mental workflow.

### Fix
- revisit the main module `README.md`
- revisit `architecture-flow.md`
- manually open each Azure DevOps service area once more
- focus on understanding purpose, not details
- remind yourself that deep usage comes in later modules

### Re-validation
After the fix:
- try explaining Azure DevOps in your own words
- if you can describe the role of the organization, project, and major services at a high level, you are ready

---

## Troubleshooting mindset
While debugging, always ask:
- am I using the correct account?
- am I inside the correct organization?
- did I actually create the project successfully?
- are my tools installed and available in the terminal?
- is this a real technical issue or just unfamiliarity with the interface?

## Escalation rule
If repeated attempts fail:
1. return to prerequisites  
2. verify access assumptions one by one  
3. simplify the naming and setup choices  
4. restart from the smallest failing point  
5. avoid creating multiple duplicate projects unless necessary  
