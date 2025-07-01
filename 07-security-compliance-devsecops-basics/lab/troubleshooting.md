# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Security + Compliance lab.

In this module, the most common failures usually come from treating security as abstract policy instead of practical workflow design, or from misunderstanding where trust boundaries actually exist. The goal is to strengthen security reasoning, not only fix a setting.

---

## Common issue 1 — Security feels theoretical and disconnected from delivery

### Symptoms
- the learner understands the words but not the workflow impact
- security settings feel administrative rather than practical
- the module feels less real than CI/CD modules

### Likely cause
The learner may still be thinking of security as something separate from normal engineering work.

### Fix
Reframe the workflow like this:
- repository changes trigger pipelines
- pipelines use identities and external connections
- deployments use access into environments
- secrets support that access
- permissions and governance determine what is possible

This makes security directly tied to every earlier module.

### Re-validation
After the fix:
- confirm the learner can point to at least three earlier modules that depend on security controls

---

## Common issue 2 — Service connection is seen as only a convenience object

### Symptoms
- the learner understands how to create it but not why it is sensitive
- scope and access questions feel secondary
- the service connection feels like just another setup item

### Likely cause
The learner may not be thinking about what a pipeline can actually do once a connection exists.

### Fix
Reframe service connections like this:
- they are trust bridges to external systems
- they can allow deployment, modification, or access actions
- over-permissioned connections expand delivery risk
- naming, ownership, and restricted usage all matter

### Re-validation
After the fix:
- confirm the learner can explain one misuse or risk that could happen with an over-permissioned service connection

---

## Common issue 3 — Secret variables and normal variables feel the same

### Symptoms
- the learner stores sensitive values casually
- secret handling does not feel meaningfully different
- the reason for variable groups or UI-managed secrets feels weak

### Likely cause
The learner may not yet appreciate the exposure risk of plain text values in pipelines or source files.

### Fix
Reframe the difference like this:
- normal variables are for regular configuration
- secret variables are for sensitive data that must be masked and controlled
- Azure DevOps recommends avoiding plain text secrets in pipeline YAML
- shared secret patterns improve both control and reuse

### Re-validation
After the fix:
- confirm the learner can explain why putting a secret directly in `azure-pipelines.yml` is not the preferred approach.

---

## Common issue 4 — Least privilege is understood in theory but not applied

### Symptoms
- the learner agrees with least privilege but still grants broad access casually
- there is no clear difference between admin, contributor, and consumer thinking
- pipeline resource access is left wide open

### Likely cause
The learner may be optimizing for convenience instead of control.

### Fix
- identify one user or pipeline role
- ask what exact actions are needed
- remove the assumption that wider access is always easier
- think in terms of minimum necessary capability

### Re-validation
After the fix:
- confirm the learner can give one concrete example of narrowing access without blocking legitimate work

---

## Common issue 5 — Governance feels like friction rather than safety

### Symptoms
- approvals, restricted pipeline access, or controlled sharing feel unnecessary
- the learner sees governance as slowing down delivery
- the security model feels too heavy for a learning repo

### Likely cause
The learner is focusing on fastest-path execution rather than sustainable and safe execution.

### Fix
Reframe governance like this:
- security controls are there to reduce avoidable mistakes
- not every pipeline needs every secret or every connection
- controlled sharing improves clarity as well as safety
- good governance helps teams trust automation more, not less

### Re-validation
After the fix:
- confirm the learner can explain one way controlled sharing improves both safety and clarity

---

## Troubleshooting mindset
While debugging this module, always ask:
- am I connecting security to real workflow actions?
- do I understand what the service connection can actually do?
- am I treating secrets differently from normal variables?
- have I thought about least privilege instead of convenience?
- is this control improving delivery trust?

## Escalation rule
If the security model still feels weak:
1. simplify to one project, one pipeline, one service connection, and one variable group  
2. identify one sensitive value and one non-sensitive value clearly  
3. identify one over-permission risk clearly  
4. explain one controlled-sharing example clearly  
5. prioritize trust-boundary understanding over tool detail  
