# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Enterprise Private AKS Landing Zone with Terraform lab.

In this module, the most common failures usually come from underestimating DNS, treating private endpoints as isolated features, or assuming a private AKS cluster behaves like a public one. The goal is to strengthen architecture reasoning, not only fix Terraform execution.

---

## Common issue 1 — The learner treats “private AKS” as a single setting

### Symptoms
- the cluster is marked private
- the learner assumes the architecture is complete
- operational access and supporting dependencies are still unclear

### Likely cause
The learner is thinking in feature terms instead of platform terms.

### Fix
Reframe private AKS like this:
- private cluster is one part of the design
- supporting services also need trust-boundary consideration
- DNS and management access are still part of the problem

### Re-validation
After the fix:
- confirm the learner can explain why private AKS alone does not equal a full private platform

---

## Common issue 2 — Private endpoints exist, but the learner does not understand the DNS model

### Symptoms
- private endpoints are created
- resolution or connectivity still feels confusing
- the learner sees DNS as secondary

### Likely cause
Private endpoint design was treated as networking-only instead of networking plus naming.

### Fix
Reframe the model like this:
- private endpoints change how services are reached
- private DNS is how that private reachability becomes usable
- private networking without private name resolution is incomplete

### Re-validation
After the fix:
- confirm the learner can explain one service’s private endpoint and matching private DNS resolution path clearly

---

## Common issue 3 — The Terraform code exists, but the architecture story is weak

### Symptoms
- resources are created
- the learner still cannot explain the platform clearly
- the module feels like “many Azure resources” rather than one design

### Likely cause
The learner may have focused on provisioning before understanding platform composition.

### Fix
- step back from the code
- redraw the platform boundary
- identify cluster, network, private services, DNS, identity, and monitoring as one architecture
- then reconnect the Terraform structure to that architecture

### Re-validation
After the fix:
- confirm the learner can describe the landing zone without referencing individual resource blocks first

---

## Common issue 4 — The learner does not understand why this module comes after Terraform + Azure DevOps

### Symptoms
- Folder 24 and 25 already felt advanced
- the learner does not yet see why this module is more premium
- the capstone significance feels blurred

### Likely cause
The learner may still be measuring “advanced” by tooling rather than by architecture complexity.

### Fix
Reframe the progression like this:
- Folder 24 taught AKS as code
- Folder 25 taught IaC through pipelines
- Folder 26 teaches what kind of AKS architecture is worth encoding and delivering in serious enterprise scenarios

### Re-validation
After the fix:
- confirm the learner can explain why a private enterprise landing zone is a stronger architecture benchmark than generic AKS provisioning

---

## Common issue 5 — The learner assumes more resources automatically means a better architecture

### Symptoms
- many services are included
- clarity goes down
- the architecture feels bloated rather than premium

### Likely cause
The learner may be optimizing for complexity instead of coherence.

### Fix
Reframe the goal like this:
- premium architecture is not about more services
- it is about stronger boundaries, clearer trust, and cleaner dependency design
- every component should have a reason to exist

### Re-validation
After the fix:
- confirm the learner can explain the architectural purpose of each major component clearly

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the platform boundary clearly defined?
- do I understand private AKS beyond the feature checkbox?
- do I understand how private endpoints and private DNS work together?
- is my Terraform code expressing the architecture clearly?
- can I explain why this architecture is stronger than a normal AKS setup?

## Escalation rule
If the landing-zone story still feels weak:
1. reduce the design to the essential platform components  
2. restate the trust boundary  
3. restate the private control-plane logic  
4. restate one private endpoint + DNS chain  
5. reconnect Terraform to the architecture  
6. prioritize architecture clarity over service count