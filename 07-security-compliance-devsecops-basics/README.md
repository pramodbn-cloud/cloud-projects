# Folder 07 — Security + Compliance: DevSecOps Basics
![Week-7 Plan](../Posts/7.png)

## Overview
This module introduces DevSecOps as the discipline of building security and compliance thinking directly into delivery workflows instead of treating them as separate, late-stage activities. It helps the learner understand that secure delivery depends on more than code quality — it also depends on permissions, identity boundaries, secret handling, service connection governance, and safe dependency practices.

This is where the course begins to mature from pure workflow automation into controlled and trustworthy delivery design. The learner starts to see that every pipeline and every deployment action operates inside a security model.

## Why this module matters
A working pipeline is not automatically a safe pipeline. In real projects, delivery risk often comes from excessive permissions, exposed secrets, poorly controlled service connections, weak approval paths, or unsafe dependency behavior.

Azure DevOps provides multiple security control surfaces, including permissions and inheritance, service connections, variable groups, secret variables, secure files, and pipeline security guidance. Secret values should not be stored directly in pipeline YAML, and shared secrets are commonly managed through variable groups or Azure Key Vault-backed variable groups.

This module builds the mindset that secure delivery is part of the delivery design itself.

## What you will learn
- How Azure DevOps security is shaped by permissions, roles, groups, and inheritance
- Why service connections are critical trust boundaries in pipeline workflows
- How secret variables, variable groups, and secure files support safer delivery
- Why DevSecOps is about reducing delivery risk early, not only reacting later

## Workflow position
This module builds on the earlier CI, CD, and package-management modules. Now that the learner understands how code moves, builds, packages, and gets delivered, the next step is to understand how all of that must be governed safely.

This module also prepares the learner for monitoring, AKS, RBAC, registry access, and later production-style platform delivery.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain why DevSecOps matters in Azure DevOps workflows
- understand the role of permissions and inheritance
- create or review a service connection safely
- explain how secrets and shared variables should be handled in pipelines

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the security surfaces and control points carefully  
5. Do not move ahead until the security model feels practical and explainable  

## Next module
The next module is **Instrumentation + Automation + Capstone**.

That module will build on security-aware delivery by showing how monitoring, notifications, automation hooks, and lifecycle visibility come together into a more complete operational workflow.
