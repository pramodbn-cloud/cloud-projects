# Lab Guide — ACR with AKS

## Lab objective
The objective of this lab is to help the learner understand and implement a secure AKS-to-ACR image pull workflow so that workloads are sourced from a private Azure registry under controlled access.

This lab focuses on registry integration, image push flow, cluster authentication, role assignment, and runtime image pull behavior. The goal is not to build a large image-factory platform yet, but to make the learner comfortable with the core trusted-registry model used in AKS environments.

## What you will build or configure
In this lab, you will create or review an ACR instance, push a sample image into it, integrate or confirm integration between AKS and ACR, deploy a workload that references the private image, and validate that AKS pulls and runs the image successfully.

This creates the first true private-image supply workflow in the course.

## Why this lab matters
Workloads cannot run unless their images can be retrieved reliably. In AKS, that means the cluster needs both a trusted registry and a secure authentication path to it.

Microsoft documents `--attach-acr` as the standard AKS integration mechanism and explains that it assigns AcrPull on the registry to the AKS managed identity. Azure guidance also emphasizes that this avoids the need for ad hoc image pull secrets in the standard AKS–ACR model.

## Estimated time
50 to 65 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a private image stored in ACR
- AKS integrated with that registry
- a workload running from the private image
- confidence in explaining the identity and registry-pull lifecycle

## Skills gained
- Understanding ACR as the trusted image source for AKS
- Connecting registry push and cluster pull flows
- Thinking in terms of registry permissions and managed identity
- Preparing for CI/CD-based image promotion and deployment later

## Real-world relevance
In real AKS platforms, ACR is often the default private registry because it integrates cleanly with AKS identities and Azure RBAC. Microsoft’s documentation centers the attach-acr pattern and AcrPull assignment as the supported integration path, and ACR best-practice guidance emphasizes disciplined image/version management.

## Completion standard
A learner should not mark this lab complete until:
- the registry integration model is clear
- the image exists in ACR
- AKS can pull it successfully
- validation confirms the registry-to-cluster lifecycle end to end
