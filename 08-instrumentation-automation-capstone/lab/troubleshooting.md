# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Instrumentation + Automation + Capstone lab.

In this module, the most common failures usually come from cluttered dashboards, weak signal selection, vague automation stories, or incomplete capstone understanding. The goal is to improve operational clarity, not only adjust widgets.

---

## Common issue 1 — Dashboard exists but feels cluttered and not useful

### Symptoms
- too many widgets were added
- the dashboard looks busy but not informative
- the learner cannot explain why each widget is there
- the dashboard feels like a feature showcase instead of a working view

### Likely cause
The learner may be trying to display everything instead of displaying what matters most.

### Fix
- remove low-value widgets
- keep only the views that answer meaningful questions
- group the dashboard around a few themes such as work, build, and delivery status
- optimize for clarity over quantity

### Re-validation
After the fix:
- confirm the learner can explain the purpose of every remaining widget clearly

---

## Common issue 2 — The learner sees dashboards as static reporting only

### Symptoms
- the dashboard is treated like a passive summary page
- the learner does not connect it to operational response
- signals are visible, but no action logic is discussed

### Likely cause
The learner may not yet be thinking from the operator or delivery-owner perspective.

### Fix
Reframe the dashboard like this:
- it should help a team notice changes quickly
- it should support decisions
- it should reduce guesswork
- it should connect to follow-up action when something matters

### Re-validation
After the fix:
- confirm the learner can explain what action a team would take after noticing a key signal change

---

## Common issue 3 — Notification thinking feels weak or noisy

### Symptoms
- the learner chooses too many notification scenarios
- alerts feel random or unnecessary
- the difference between helpful and noisy notification behavior is unclear

### Likely cause
The learner may be focusing on available options instead of signal importance.

### Fix
- choose one or two truly important events
- define why each event deserves attention
- avoid creating awareness patterns that would be ignored quickly
- optimize for timely response, not high alert count

### Re-validation
After the fix:
- confirm the learner can explain why the selected notification is worth a person’s attention

---

## Common issue 4 — Service hooks feel abstract or disconnected

### Symptoms
- the learner understands that they exist but not why they matter
- the service-hook example feels artificial
- the automation story is not connected to a real event

### Likely cause
The learner may still be thinking of Azure DevOps as a closed system instead of an event source for broader automation.

### Fix
Reframe service hooks like this:
- an event happens in Azure DevOps
- that event can be shared with another system
- another system can respond, annotate, or continue automation
- this expands the usefulness of Azure DevOps beyond its own UI

### Re-validation
After the fix:
- confirm the learner can describe one event and one useful external reaction clearly

---

## Common issue 5 — Capstone explanation still feels fragmented

### Symptoms
- the learner can explain individual modules but not the whole flow
- the foundation phase feels like disconnected topics
- the transition into AKS does not feel clear

### Likely cause
The learner may have learned module by module without pausing to connect them into one story.

### Fix
Rebuild the story in this order:
- work starts with planning
- planning becomes implementation through repos
- CI validates changes
- CD promotes validated outputs
- package management supports reuse
- security protects trust boundaries
- instrumentation makes the system visible and manageable

This creates the full foundation-phase narrative.

### Re-validation
After the fix:
- confirm the learner can explain the entire flow without treating each module as isolated

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the dashboard helping, or just displaying more?
- did I choose signals that actually matter?
- does the notification logic support action?
- can I explain one useful event-driven automation story?
- can I describe the full foundation phase as one connected workflow?

## Escalation rule
If the module still feels weak:
1. reduce the dashboard to only a few meaningful views  
2. choose one notification example clearly  
3. choose one service-hook example clearly  
4. rewrite the capstone story from beginning to end  
5. prioritize operational clarity over feature count  
