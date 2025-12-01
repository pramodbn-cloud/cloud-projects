# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the ACR with AKS lab.

In this module, the most common failures usually come from incorrect image paths, assuming AKS is already authorized to pull, misunderstanding which identity performs the registry pull, or treating image tags casually. The goal is to strengthen supply-chain reasoning, not only fix deployment YAML.

---

## Common issue 1 — The workload is deployed, but the image cannot be pulled

### Symptoms
- the deployment exists
- the pod does not start successfully
- image pull errors appear in pod status or events
- the learner assumes AKS is broken

### Likely cause
The most common cause is one of these:
- the image path is wrong
- the tag is wrong
- the image was never pushed correctly
- AKS does not have authorization to pull from ACR

### Fix
- verify the image exists in ACR
- verify the image reference exactly
- verify the AKS–ACR trust path and AcrPull assignment
- inspect pod events instead of guessing

### Re-validation
After the fix:
- redeploy or restart the pod
- confirm that image pull now succeeds

---

## Common issue 2 — The learner does not know which identity is actually pulling from ACR

### Symptoms
- the learner knows the cluster can pull or cannot pull
- the identity model feels vague
- troubleshooting feels random

### Likely cause
The learner may not yet distinguish the cluster control plane from the node/kubelet identity used for registry pulls.

### Fix
Reframe the pull flow like this:
- AKS uses its managed identity model for registry integration
- attach-acr grants AcrPull to the managed identity used for pulls
- the registry trusts that identity for read access

Microsoft’s docs explicitly say attach-acr configures AcrPull for the managed identity.

### Re-validation
After the fix:
- confirm the learner can explain the pull trust path clearly

---

## Common issue 3 — The image exists in ACR, but the wrong repository/tag is used in the deployment

### Symptoms
- the registry is healthy
- the learner can see the image in ACR
- the pod still cannot pull
- the problem looks like authentication but may not be

### Likely cause
The deployment may reference:
- the wrong login server
- the wrong repository path
- the wrong tag

### Fix
- compare the deployment image string against the actual image stored in ACR
- keep the first lab image path simple and explicit
- avoid ambiguous or reused tags during validation

### Re-validation
After the fix:
- confirm the deployment points at the exact pushed image path
- retest the workload

---

## Common issue 4 — The learner treats ACR as only a storage location

### Symptoms
- the image push works
- the learner still does not see why this module matters
- the operational value of ACR feels low

### Likely cause
The learner may still be thinking at single-image demo scale instead of platform supply-chain scale.

### Fix
Reframe ACR like this:
- it is the trusted image source for the platform
- AKS workloads depend on it at runtime
- tags and repositories affect release reliability
- governance, retention, and consistency start here

### Re-validation
After the fix:
- confirm the learner can explain one strong production advantage of ACR over unmanaged public image sourcing

---

## Common issue 5 — The learner thinks image pull secrets are the normal default here

### Symptoms
- the learner keeps reaching for image pull secrets first
- the AKS–ACR integrated model feels secondary
- the trust path feels more manual than it should

### Likely cause
The learner may be bringing in generic Kubernetes habits without considering the Azure-native integration model.

### Fix
Reframe the standard model like this:
- in AKS with ACR, the normal clean path is identity-based integration
- attach-acr plus managed identity and AcrPull is the supported mainstream pattern
- image pull secrets are not the first-choice pattern for the standard same-tenant AKS–ACR scenario

### Re-validation
After the fix:
- confirm the learner can explain why managed-identity-based pull is cleaner in this Azure-native design

---

## Troubleshooting mindset
While debugging this module, always ask:
- does the image actually exist in ACR?
- is the image reference exact?
- which AKS identity is supposed to pull it?
- does that identity have AcrPull?
- am I debugging auth, path, or tag confusion?

## Escalation rule
If the image-supply story still feels broken:
1. confirm the image exists in ACR  
2. confirm the exact image path and tag  
3. confirm AKS–ACR integration  
4. confirm AcrPull on the right identity  
5. inspect pod events again  
6. retest one simple workload only  
7. prioritize trust-path reasoning over repeated deployment edits  
