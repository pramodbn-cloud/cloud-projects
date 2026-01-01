# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Azure DevOps with AKS lab.

In this module, the most common failures usually come from build and deploy stages being mentally mixed together, service connections being misconfigured, the wrong image tag being deployed, or assuming that pipeline success always means rollout success. The goal is to strengthen end-to-end delivery reasoning, not only fix pipeline YAML.

---

## Common issue 1 — The image builds, but the deployment does not update correctly

### Symptoms
- the build stage succeeds
- the image appears in ACR
- the deployment stage runs, but the workload does not reflect the expected image
- the learner assumes AKS is broken

### Likely cause
The deployment stage may still be referencing an old image tag or the manifest update path may not be aligned to the newly built image.

### Fix
- inspect the image tag used during build
- inspect the image reference used during deployment
- make sure the deployment path receives the exact image identity that was just pushed
- avoid ambiguous or reused tags while validating the first flow

### Re-validation
After the fix:
- rerun the pipeline
- confirm that the expected image now reaches AKS

---

## Common issue 2 — The pipeline can push to ACR but cannot deploy to AKS

### Symptoms
- the image reaches ACR successfully
- the deployment stage fails
- the learner is unsure whether the problem is AKS, Azure DevOps, or manifests

### Likely cause
The service connection or deployment trust path to AKS may be incorrect or incomplete.

### Fix
- inspect the AKS deployment connection model
- verify the intended Azure DevOps service connection
- verify permissions and target-cluster access
- separate registry access troubleshooting from cluster deployment troubleshooting

### Re-validation
After the fix:
- rerun only the deployment reasoning path mentally and then in the pipeline
- confirm manifests now reach the cluster successfully

---

## Common issue 3 — The pipeline is green, but the application is not healthy

### Symptoms
- the pipeline reports success
- the deployment exists in AKS
- the application does not behave correctly at runtime
- the learner assumes the pipeline lied

### Likely cause
Pipeline success and application health are related but not identical. The deployment task may have completed while the application itself still has runtime issues unrelated to pipeline mechanics.

### Fix
- inspect pod status and application logs separately
- distinguish rollout success from application-process success
- avoid blaming the CI/CD path for container runtime failures inside the app

Microsoft documentation and related troubleshooting patterns make this distinction important: successful image pull and deployment do not guarantee application process health.

### Re-validation
After the fix:
- confirm whether the issue was deployment-path-related or application-runtime-related
- retest after correcting the right layer

---

## Common issue 4 — The learner does not understand why Azure DevOps with AKS matters after ACR

### Symptoms
- the learner sees this as “just automate what we already did manually”
- the platform value feels incremental rather than major
- the sequence between Folder 18 and Folder 19 feels weak

### Likely cause
The learner may still be thinking in isolated feature terms rather than lifecycle terms.

### Fix
Reframe the progression like this:
- Folder 18 created trusted private image supply
- Folder 19 turns that supply into a repeatable delivery lifecycle
- ACR solved trusted image sourcing
- Azure DevOps with AKS solves repeatable rollout and traceability

### Re-validation
After the fix:
- confirm the learner can explain why trusted image supply had to exist before full deployment automation

---

## Common issue 5 — The learner treats service connections as setup details rather than trust boundaries

### Symptoms
- the learner knows the pipeline needs service connections
- the security and architectural importance of them feels weak
- troubleshooting around deployment access feels random

### Likely cause
The learner may be treating service connections as hidden plumbing instead of as the trust path between Azure DevOps and Azure resources.

### Fix
Reframe service connections like this:
- they define what the pipeline is allowed to access
- they are the trust bridge between Azure DevOps and AKS/ACR
- they are part of the delivery architecture, not just background configuration

### Re-validation
After the fix:
- confirm the learner can explain which connection enables which stage of the pipeline and why that matters

---

## Troubleshooting mindset
While debugging this module, always ask:
- did the image build correctly?
- did the image push to ACR correctly?
- did the deployment stage reference the right image?
- does Azure DevOps actually have the right trust path to AKS?
- is this a pipeline problem or an application runtime problem?

## Escalation rule
If the delivery lifecycle still feels broken:
1. validate build success  
2. validate ACR push success  
3. validate image identity  
4. validate AKS deployment trust path  
5. validate rollout health in the cluster  
6. separate deployment-path failures from app-runtime failures  
7. prioritize lifecycle reasoning over repeated YAML edits  
