# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS with Terraform lab.

In this module, the most common failures usually come from weak provider/state understanding, mixing too much Terraform complexity into the first AKS example, using unclear variables, or assuming that successful apply automatically means good infrastructure design. The goal is to strengthen IaC reasoning, not only fix `.tf` files.

---

## Common issue 1 — The learner treats Terraform as a scripting tool instead of an infrastructure lifecycle tool

### Symptoms
- the learner focuses only on getting apply to succeed
- plan, state, and review feel secondary
- Terraform feels like a CLI wrapper rather than a platform model

### Likely cause
The learner may still be thinking in ad hoc execution terms instead of declarative infrastructure terms.

### Fix
Reframe Terraform like this:
- configuration defines desired infrastructure state
- plan previews change
- apply creates or changes the platform
- state tracks what Terraform manages

### Re-validation
After the fix:
- confirm the learner can explain why plan and state matter even when apply succeeds

---

## Common issue 2 — The first Terraform design is too complex

### Symptoms
- many files, variables, and resources appear at once
- the learner loses the AKS story inside Terraform structure
- troubleshooting becomes harder than necessary

### Likely cause
Too much abstraction was added before the learner understood the core AKS lifecycle.

### Fix
- reduce to a small, readable AKS Terraform pattern
- keep the first example intentionally limited
- focus on one cluster and a small supporting resource set

### Re-validation
After the fix:
- confirm the learner can explain the Terraform structure without confusion

---

## Common issue 3 — The learner understands apply, but not state

### Symptoms
- Terraform created the cluster
- the learner still does not understand why state matters
- future team or pipeline use feels vague

### Likely cause
State is often invisible until the learner thinks beyond one local apply.

### Fix
Reframe state like this:
- state is how Terraform remembers managed infrastructure
- safe updates and destroys depend on accurate state
- team workflows and pipelines become risky if state is misunderstood

### Re-validation
After the fix:
- confirm the learner can explain one risk of ignoring Terraform state

---

## Common issue 4 — The learner thinks this module repeats earlier AKS creation topics

### Symptoms
- the learner says “we already know how to create a cluster”
- the value of Terraform feels incremental
- the endgame importance feels weak

### Likely cause
The learner may still be comparing “cluster exists” versus “cluster exists” instead of comparing manual creation versus codified platform provisioning.

### Fix
Reframe the module like this:
- earlier modules taught how AKS behaves and is operated
- this module teaches how AKS itself becomes an IaC-managed platform artifact
- the point is not cluster existence; the point is provisioning maturity

### Re-validation
After the fix:
- confirm the learner can explain one clear advantage of codified provisioning over manual provisioning

---

## Common issue 5 — The learner sees Terraform success as proof of production readiness

### Symptoms
- apply succeeds
- the learner assumes the design is production-ready
- there is little reflection on naming, variables, change safety, or lifecycle structure

### Likely cause
The learner may still be optimizing for resource creation rather than long-term platform manageability.

### Fix
Reframe success like this:
- successful apply is only the first signal
- readable structure, safe changes, and reproducibility matter just as much
- production-readiness comes from lifecycle quality, not only creation success

### Re-validation
After the fix:
- confirm the learner can explain one way to judge Terraform quality beyond “apply worked”

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the Terraform structure too complex for the first learning goal?
- do I understand provider, plan, apply, and state separately?
- are the AKS resources defined clearly?
- am I optimizing for readability and repeatability, not just creation?
- can I explain why this is better than manual provisioning?

## Escalation rule
If the IaC story still feels weak:
1. simplify to one AKS cluster example  
2. reduce unnecessary variables  
3. re-explain plan and state  
4. validate the created resources clearly  
5. compare manual and Terraform provisioning again  
6. prioritize infrastructure lifecycle reasoning over file count  
