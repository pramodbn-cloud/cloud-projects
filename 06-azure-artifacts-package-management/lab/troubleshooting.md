# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Azure Artifacts lab.

In this module, the most common failures usually come from unclear package strategy, feed confusion, publish-versus-artifact confusion, weak versioning discipline, or misunderstanding of upstream sources. The goal is to strengthen package lifecycle understanding, not only fix a publish step.

---

## Common issue 1 — The learner confuses pipeline artifacts with Azure Artifacts packages

### Symptoms
- the learner treats feed publishing like normal pipeline artifact storage
- package strategy feels unnecessary
- the value of a feed is unclear

### Likely cause
The learner is still thinking in terms of one pipeline run and not yet in terms of reusable, versioned outputs across workflows.

### Fix
Reframe the difference like this:
- pipeline artifacts are usually tied to a specific run and handoff flow
- packages in Azure Artifacts are managed, versioned, reusable components stored in feeds
- package management is for repeated consumption and controlled reuse

### Re-validation
After the fix:
- confirm the learner can explain why a feed exists even when pipeline artifacts already exist

---

## Common issue 2 — Feed exists, but its purpose feels artificial

### Symptoms
- the feed was created, but the learner cannot explain why it is needed
- the package scenario feels weak or forced
- the lab feels like storage setup rather than package strategy

### Likely cause
The chosen scenario may not represent something truly reusable.

### Fix
- choose a simpler but clearly reusable example
- think in terms of shared utility, internal library, common template, or reusable bundle
- ensure the learner can explain who would consume this package and why

### Re-validation
After the fix:
- confirm the learner can explain one real reuse story for the feed

---

## Common issue 3 — Versioning is present, but not meaningful

### Symptoms
- the package has a version, but the learner sees it as a label only
- version changes do not feel connected to delivery quality
- package identity feels weak

### Likely cause
The learner may not yet understand that consumption decisions depend on package version clarity.

### Fix
Reframe versioning like this:
- version identifies exactly what consumers are using
- version changes signal evolution or update
- package reuse becomes reliable only when identity is precise

### Re-validation
After the fix:
- confirm the learner can explain why consuming “the package” is not enough without knowing which version

---

## Common issue 4 — Upstream sources feel confusing or unnecessary

### Symptoms
- the learner does not understand why public packages would route through the feed
- upstream feels like extra complexity
- internal and external package strategy feel disconnected

### Likely cause
The learner is thinking only at small-project scale and not at dependency governance scale.

### Fix
Reframe upstream sources like this:
- teams often want one trusted place to resolve dependencies
- upstream sources let public dependencies be accessed through the feed
- consumed packages can be saved in the feed, improving continuity and centralization
- this supports simpler dependency management and better package integrity controls

### Re-validation
After the fix:
- confirm the learner can explain one organizational reason to enable upstream sources.

---

## Common issue 5 — Consumption flow still feels incomplete

### Symptoms
- the learner understands publishing but not retrieval
- package lifecycle feels one-sided
- feed connection steps feel unclear

### Likely cause
The learner focused on creating the feed and package but did not spend enough time on the consumer perspective.

### Fix
- reopen the feed connection guidance
- review how the selected package type is consumed
- explain the publish-consume loop end to end
- connect this idea back to how pipelines or projects would use the feed later

### Re-validation
After the fix:
- confirm the learner can describe the full lifecycle from publish to consume

---

## Troubleshooting mindset
While debugging this module, always ask:
- am I thinking in reusable packages or only in stored files?
- does the feed have a clear purpose?
- does the package scenario feel genuinely reusable?
- is version identity being treated seriously?
- do I understand how upstream sources improve dependency centralization?

## Escalation rule
If the package flow still feels weak:
1. simplify to one feed and one clear package story  
2. define one version clearly  
3. define one consumer clearly  
4. explain one upstream use case clearly  
5. focus on package lifecycle meaning before adding more complexity  
6. prioritize reuse logic over tool detail  
