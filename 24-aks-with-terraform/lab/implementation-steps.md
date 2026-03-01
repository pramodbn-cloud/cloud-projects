# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS with Terraform lab.

The goal is to create one clear IaC path where AKS infrastructure is defined in Terraform, reviewed, applied, and validated as a reproducible platform foundation.

---

## Step 1 — Understand the IaC goal
Before writing any Terraform, understand what this module is trying to teach.

This lab is not only about replacing portal clicks with Terraform commands. It is about creating an infrastructure lifecycle that is:

- declarative
- repeatable
- reviewable
- easier to evolve safely over time

At the end of this lab, you should have:
- one Terraform-based AKS foundation
- one clear plan/apply/validate lifecycle
- one clear explanation of why AKS belongs in infrastructure as code

## Step 2 — Reconfirm Azure authentication and Terraform readiness
Before defining AKS resources, verify that:
- Azure CLI authentication is working
- Terraform is installed and usable
- the Azure subscription context is correct

This step matters because Terraform success depends as much on environment readiness as on configuration correctness.

## Step 3 — Structure the Terraform files
Now define a simple and readable Terraform file structure.

Recommended baseline structure:
- provider configuration
- variables
- core AKS resource definition
- outputs

The learner should understand that readability matters because Terraform becomes a team artifact, not just a one-time script.

## Step 4 — Configure the Azure provider
Now define the AzureRM provider and any required provider constraints.

HashiCorp’s provider documentation recommends staying current because AKS evolves quickly. The learner should understand:
- provider version choice affects resource behavior
- Terraform infrastructure quality includes provider/version discipline

This is the first major IaC maturity checkpoint.

## Step 5 — Define the basic Azure resources
Now define the minimum Azure resource structure needed for the AKS cluster.

At a basic level, this often includes:
- a resource group
- the AKS cluster resource itself
- core node-pool settings
- identity/network-related settings according to the lab design

Keep the first scenario simple. The goal is to understand provisioning flow, not to model every advanced option immediately.

## Step 6 — Add variables and keep them intentional
Now introduce variables for values that are likely to differ by environment or purpose.

The learner should understand:
- variables help reusability
- too many variables too early reduce clarity
- the first lab should focus on meaningful inputs, not maximum abstraction

This is where the Terraform design becomes reusable instead of static.

## Step 7 — Add outputs for useful cluster information
Now define outputs for the values that help validate the environment later.

Examples include:
- cluster name
- resource group name
- other readable outputs that improve validation and reuse

Outputs help connect Terraform provisioning to the next operational steps.

## Step 8 — Initialize Terraform
Now run Terraform initialization.

At this stage, the learner should understand:
- providers are being prepared
- state context is being established
- the working directory becomes a Terraform execution context

This is the official start of the Terraform lifecycle.

## Step 9 — Run Terraform plan
Now run the plan phase.

The learner should inspect:
- what Terraform intends to create
- whether the cluster shape and dependent resources look correct
- whether the configuration expresses the intended platform foundation

This is one of the most important learning moments in the module because it reinforces review before change.

## Step 10 — Apply the configuration
Now run the apply phase.

At this stage, observe:
- resource creation progress
- AKS provisioning timing
- whether the infrastructure is created successfully

The learner should understand that Terraform is now turning declarative intent into actual Azure state.

## Step 11 — Validate the provisioned cluster
Once apply succeeds, validate that:
- the AKS cluster exists
- the expected Azure resources exist
- the cluster can be reached or credentials can be obtained if included in the lab flow

This confirms that the IaC path produced a usable platform, not only a successful command result.

## Step 12 — Review Terraform state thinking
Now pause and reflect on state.

The learner should understand:
- Terraform state tracks what the tool manages
- safe lifecycle control depends on state being accurate
- this becomes even more important when teams collaborate or pipelines run Terraform later

This is the core state-awareness moment of the module.

## Step 13 — Compare Terraform provisioning to manual provisioning
Now reflect on the difference between:
- manually creating AKS resources
- provisioning AKS through Terraform

Ask:
- why is Terraform easier to review?
- why is Terraform easier to repeat?
- why is Terraform more suitable for multi-environment platform engineering?

This is the main platform reasoning moment of the module.

## Step 14 — Explain the IaC lifecycle end to end
Now explain the flow in plain language:

- infrastructure is defined in Terraform
- Terraform initializes providers and state
- Terraform plans the intended Azure changes
- Terraform applies those changes
- AKS and related resources are created consistently as code

If the learner can explain this clearly, the module is doing its real job.

## Step 15 — Reflect on Terraform as platform-foundation engineering
Pause and think beyond the `.tf` files.

In this module, Terraform for AKS means:
- cluster foundations become reproducible
- platform changes become reviewable
- environments become easier to clone and evolve
- the platform becomes less dependent on manual provisioning habits

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the Terraform structure is clear
- AKS and supporting resources are defined declaratively
- Terraform init/plan/apply flow is understood
- the provisioned cluster is validated or clearly modeled
- the learner understands why state and reproducibility matter

## Step 16 — Prepare for the final capstone
Before moving to the next module, understand what changes next.

The next module is **Terraform + Azure DevOps for AKS**. That means the learner will now take this IaC model and run it through a governed CI/CD pipeline, which is the final capstone of the course.

This is the bridge from Terraform-based provisioning into pipeline-driven infrastructure delivery.

---

## Implementation notes
- keep the first Terraform AKS scenario simple and readable
- focus on lifecycle understanding before advanced abstraction
- treat state as a core concept, not a background detail
- prefer clarity over maximum modularity in the first pass
- focus on reproducibility, not only resource creation

## End-of-implementation summary
In this lab, you:
- prepared Terraform and Azure authentication
- structured Terraform files for AKS provisioning
- defined AKS infrastructure declaratively
- ran init, plan, and apply
- validated the resulting cluster
- reflected on state, reviewability, and repeatability
- practiced the first true IaC foundation pattern for AKS in the course

You are now ready to validate whether the AKS-with-Terraform lifecycle is clean, correct, and explainable.
