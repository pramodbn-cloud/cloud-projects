# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the CI Pipelines lab.

In this module, the most common failures usually come from repository linkage issues, pipeline step logic issues, trigger misunderstanding, or artifact configuration problems. The goal is to build not only recovery skill, but confidence in reading pipeline behavior.

---

## Common issue 1 — Pipeline exists but does not run correctly

### Symptoms
- pipeline creation succeeded but execution fails immediately
- the run starts but stops very early
- the learner cannot tell which part failed
- the pipeline feels connected but nonfunctional

### Likely cause
The most common reasons are:
- incomplete or incorrect pipeline definition
- wrong assumptions about the build environment
- a missing file or command in the repository
- step order that does not match the actual repo contents

### Fix
- review the pipeline definition calmly
- confirm that every step references something that actually exists
- simplify the pipeline if needed
- run again after correcting the first visible issue rather than changing many things at once

### Re-validation
After the fix:
- rerun the pipeline
- review the logs step by step
- confirm that the previously failing stage now progresses correctly

---

## Common issue 2 — Repository changes do not trigger the pipeline

### Symptoms
- the pipeline runs manually but not after a repo change
- a push succeeds but no new run appears
- the learner is unsure whether trigger logic is active

### Likely cause
The most common reasons are:
- trigger configuration does not match the branch being updated
- the pipeline is not linked to the expected branch
- the learner tested the wrong repository or wrong branch
- manual-only expectations were not separated from automatic trigger expectations

### Fix
- verify which branch the trigger is watching
- confirm which branch the recent change was pushed to
- review pipeline trigger settings carefully
- make one small controlled change and test again

### Re-validation
After the fix:
- push a new meaningful change to the intended branch
- confirm that a new pipeline run appears
- confirm that the learner now understands the trigger path

---

## Common issue 3 — Build step is present but does not add value

### Symptoms
- the pipeline succeeds, but the build step feels empty
- the learner cannot explain what the build step is doing
- the pipeline looks technical but not meaningful

### Likely cause
The build step may have been added only to complete the flow, without tying it to an actual repository purpose.

### Fix
- redefine the build step in simple, meaningful terms
- ensure it performs a real preparation, packaging, or validation action
- connect the step directly to the chosen sample project or repository scenario

### Re-validation
After the fix:
- review the step again
- confirm the learner can explain what this step is validating or preparing

---

## Common issue 4 — Artifact is not visible after a successful run

### Symptoms
- pipeline succeeds but no artifact appears
- the learner expects output but cannot find it
- logs suggest publication happened, but visibility is unclear

### Likely cause
The most common reasons are:
- artifact publication step is incomplete
- wrong folder or output path was referenced
- the artifact was not actually created before publication
- the learner is checking the wrong area in the run view

### Fix
- review the artifact publish step
- confirm that the intended output exists before publication
- verify the path being published
- reopen the pipeline run and inspect the artifact section carefully

### Re-validation
After the fix:
- rerun the pipeline
- confirm the artifact now appears visibly after success
- confirm the learner can explain what the artifact represents

---

## Common issue 5 — CI still feels procedural instead of meaningful

### Symptoms
- the learner completed the pipeline but still sees it as “just automation”
- build, test, and artifact steps feel disconnected
- the module feels mechanical instead of valuable

### Likely cause
The learner may be focusing on the tool sequence rather than the delivery purpose.

### Fix
Reframe the workflow like this:
- repository change = candidate change entering the system
- build = prepare or verify technical viability
- test = add trust
- artifact = create reusable output
- run history = visible evidence of delivery health

Think in terms of delivery confidence, not only technical steps.

### Re-validation
After the fix:
- explain the pipeline end to end in your own words
- if you can describe how CI reduces delivery risk and prepares for CD, the concept is now clear

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the pipeline connected to the correct repository?
- is the branch or trigger logic correct?
- do the steps match the actual repository content?
- is the artifact path real and valid?
- can I explain why each step exists?

## Escalation rule
If the pipeline still feels broken:
1. simplify the pipeline  
2. test one meaningful step at a time  
3. confirm the repository path and branch assumptions  
4. review logs carefully instead of guessing  
5. fix the first clear failure before changing other parts  
6. keep the CI flow understandable, not overly complicated  
