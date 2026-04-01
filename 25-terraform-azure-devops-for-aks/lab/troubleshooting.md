# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Terraform + Azure DevOps for AKS lab.

In this module, the most common failures usually come from weak separation of plan and apply, unclear service-connection trust, assuming the pipeline is the problem when the Terraform code is the problem, or underestimating state and execution-context issues. The goal is to strengthen infrastructure-delivery reasoning, not only fix YAML.

---

## Common issue 1 — The learner moves to pipeline execution before Terraform itself is stable

### Symptoms
- the pipeline fails early
- debugging feels chaotic
- the learner blames Azure DevOps first

### Likely cause
The Terraform code from Folder 24 may not yet be stable enough for pipeline execution.

### Fix
- revalidate the Terraform configuration locally or conceptually first
- confirm that the AKS provisioning logic itself is sound
- only then debug Azure DevOps execution flow

### Re-validation
After the fix:
- confirm the learner can distinguish Terraform-code issues from pipeline-orchestration issues

---

## Common issue 2 — Plan and apply are mentally merged together

### Symptoms
- the learner treats both as one step
- reviewability feels weak
- the pipeline is harder to reason about

### Likely cause
The learner may still be thinking in local imperative execution terms.

### Fix
Reframe the lifecycle like this:
- init prepares execution
- plan shows intended change
- apply performs the change
- review value is lost if plan/apply are not separated mentally

### Re-validation
After the fix:
- confirm the learner can explain why pipeline-governed Terraform is stronger when plan remains visible before apply

---

## Common issue 3 — The service connection exists, but the learner does not understand its role

### Symptoms
- the pipeline references a service connection
- access issues appear confusing
- trust-path reasoning is weak

### Likely cause
The learner may still be treating service connections as background settings rather than infrastructure trust boundaries.

### Fix
Reframe the model like this:
- the service connection is what gives Azure DevOps the right to touch Azure resources
- without that trust path, Terraform in the pipeline cannot manage AKS infrastructure
- this is part of the infrastructure architecture, not pipeline decoration

### Re-validation
After the fix:
- confirm the learner can explain which trust boundary the service connection represents

---

## Common issue 4 — The pipeline succeeds partially, but the learner does not know how to judge infrastructure quality

### Symptoms
- commands ran successfully
- Azure resources may exist
- the learner still cannot say whether the infrastructure-delivery model is good

### Likely cause
The learner may be measuring success only by execution outcome rather than by reviewability, repeatability, and clarity.

### Fix
Reframe quality like this:
- successful execution matters
- but stage clarity, review value, trust path, and lifecycle understanding matter too
- infrastructure CI/CD quality is broader than “pipeline green”

### Re-validation
After the fix:
- confirm the learner can explain one way to evaluate infrastructure pipeline quality beyond simple success/failure

---

## Common issue 5 — The learner does not feel why this is the final capstone

### Symptoms
- the module feels like “Terraform plus one more pipeline”
- the end-of-course significance feels weak
- earlier topics feel disconnected from it

### Likely cause
The learner may not yet see that this module ties together runtime platform understanding and infrastructure delivery discipline.

### Fix
Reframe the whole course like this:
- earlier modules taught what AKS is and how it behaves
- middle modules taught governance, security, and runtime design
- Folder 24 codified the cluster
- Folder 25 operationalizes that codified platform through CI/CD

### Re-validation
After the fix:
- confirm the learner can explain why this is the strongest end-state for the course

---

## Troubleshooting mindset
While debugging this module, always ask:
- is Terraform itself valid first?
- is the service connection trust path clear?
- are init, plan, and apply clearly separated?
- is this a pipeline issue or a Terraform issue?
- can I explain why this pipeline is better than local-only execution?

## Escalation rule
If the capstone still feels weak:
1. revalidate Folder 24 Terraform first  
2. simplify the pipeline to one clear init/plan/apply flow  
3. re-check the Azure trust path  
4. validate resulting Azure infrastructure  
5. connect the capstone back to the whole course explicitly  
6. prioritize infrastructure-delivery reasoning over pipeline complexity  
