# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the CD Pipelines lab.

In this module, the most common failures usually come from unclear artifact linkage, weak stage design, confusion between CI and CD logic, approval misunderstandings, or missing rollback thinking. The goal is to strengthen delivery understanding, not only fix configuration issues.

---

## Common issue 1 — The learner cannot clearly connect CI output to CD input

### Symptoms
- the deployment flow exists, but the artifact source feels unclear
- the learner is unsure which build output is being released
- the release process feels disconnected from the CI process

### Likely cause
The artifact from Folder 04 was not reviewed properly, or the learner moved into release design before understanding what the CI pipeline actually produced.

### Fix
- return to the successful CI run
- inspect the artifact carefully
- define in one sentence what the artifact represents
- reconnect the CD flow only after the artifact purpose is clear

### Re-validation
After the fix:
- confirm that the chosen artifact is clearly identifiable
- confirm the learner can explain how it moves from CI into CD

---

## Common issue 2 — Stages exist, but their purpose feels artificial

### Symptoms
- there are one or more stages, but they feel like labels only
- the learner cannot explain why there is a Dev stage or Test stage
- stage order feels arbitrary

### Likely cause
The learner may have created stages to match the concept, but without assigning clear delivery meaning to each stage.

### Fix
- simplify the release story
- define what each stage is intended to represent
- give each stage one clear purpose
- ensure the stage names reflect actual progression, not just technical structure

### Re-validation
After the fix:
- review the stage names
- confirm the learner can explain why the artifact should move in that order

---

## Common issue 3 — Approval logic feels like an obstacle rather than a control

### Symptoms
- the learner sees approval as a delay
- the approval step feels unnecessary in a simple lab
- the workflow loses meaning at the checkpoint

### Likely cause
The learner is focusing only on speed of completion rather than release confidence and risk control.

### Fix
Reframe approvals like this:
- CI checks technical validity
- stage progression introduces deployment risk
- approvals help pause intentionally before increasing that risk
- approvals are about controlled confidence, not bureaucracy alone

### Re-validation
After the fix:
- confirm the learner can explain one real reason an approval checkpoint would exist before promotion

---

## Common issue 4 — Rollback is mentioned, but not truly understood

### Symptoms
- rollback is written down, but the learner cannot explain when or how it would happen
- rollback feels like an afterthought
- the lab feels complete only when deployment succeeds

### Likely cause
The learner is thinking about happy-path automation only and has not yet developed delivery recovery thinking.

### Fix
- define one realistic failure case
- define one realistic “deployment succeeded but should not continue” case
- explain how the last known good artifact or stage state would be used
- connect rollback to operational safety, not only technical error

### Re-validation
After the fix:
- confirm the learner can explain a simple rollback path without hesitation

---

## Common issue 5 — CD still feels like “CI with more steps”

### Symptoms
- the learner treats deployment as just another automation stage
- the difference between build and release remains unclear
- stage progression, approvals, and rollback do not feel distinct

### Likely cause
The learner may be focusing on pipeline mechanics rather than lifecycle purpose.

### Fix
Reframe the workflow like this:
- CI asks: can this change be validated and packaged?
- CD asks: how do we move that package safely into environments?
- CI builds trust in the change
- CD builds trust in the promotion and release process

This distinction is critical.

### Re-validation
After the fix:
- explain the difference between CI and CD in your own words
- if the learner can explain both clearly and separately, the concept is now strong

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the artifact source clear?
- does each stage have a real delivery meaning?
- am I treating approvals as a confidence control?
- have I defined rollback before failure happens?
- can I clearly explain how CD differs from CI?

## Escalation rule
If the delivery flow still feels weak:
1. simplify to one artifact and one stage  
2. add one clear second stage only if needed  
3. define one approval purpose  
4. define one rollback story  
5. explain the lifecycle out loud before adding more complexity  
6. prioritize delivery meaning over pipeline decoration  
