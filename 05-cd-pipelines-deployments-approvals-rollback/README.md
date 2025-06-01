# Folder 05 — CD Pipelines: Deployments + Approvals + Rollback
![Week-5 Plan](../Posts/5.png)

## Overview
This module introduces Continuous Delivery as the workflow that takes validated build outputs and moves them forward through controlled deployment stages. It helps the learner understand that delivery is not only about creating artifacts, but about promoting them safely, visibly, and responsibly into environments.

This is where the course moves from automated validation into controlled release execution. The learner begins to see how deployment stages, environment awareness, approval logic, and rollback thinking work together to create trust in delivery systems.

## Why this module matters
A successful CI pipeline proves that code can be built, checked, and packaged. But that is only half of the delivery story. Teams also need a disciplined way to move those outputs into runtime environments without creating unnecessary risk.

Without CD discipline, releases become unpredictable, approvals become informal, and recovery from bad deployments becomes slow and stressful. Controlled deployment workflows reduce that risk by introducing stage boundaries, human or policy checkpoints, and recovery thinking before production-like releases happen.

This module builds that delivery maturity.

## What you will learn
- What Continuous Delivery means in a practical DevOps workflow
- How deployment stages differ from build stages
- Why approvals and environment boundaries matter in release flow
- Why rollback thinking is part of delivery design, not only incident response

## Workflow position
This module builds directly on Folder 04, where the learner created a CI pipeline that produces validated artifacts. Now the learner moves from “Can we build and verify this?” to “How do we deliver it safely?”

This module also prepares the learner for package strategy, security, and later AKS-based delivery patterns by building stage-based release thinking early.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain the difference between CI and CD clearly
- understand how artifacts move into environments
- design a simple stage-based deployment flow
- describe the role of approvals and rollback planning in modern delivery

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the deployment stage flow carefully  
5. Do not move ahead until the release lifecycle feels understandable end to end  

## Next module
The next module is **Azure Artifacts: Package Management Strategy**.

That module will deepen the learner’s understanding of reusable outputs by showing how internal package management supports consistency, reuse, and scalable delivery across teams and pipelines.
