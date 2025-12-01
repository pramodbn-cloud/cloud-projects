# Folder 17 — AKS Virtual Nodes
![Week-17 Plan](../Posts/17.png)

## Overview
This module expands the AKS execution model by introducing virtual nodes as a way to run Kubernetes pods on Azure Container Instances (ACI) without waiting for traditional VM-based worker node scale-out.

This is where the course moves from cluster organization and workload governance into execution-model flexibility. The learner is no longer thinking only in terms of “which namespace should this workload live in?” but also “what kind of compute backing should this workload use, and when is serverless pod execution operationally useful?”

## Why this module matters
Not every workload needs to run on a traditional AKS VM node pool all the time. Some workloads benefit from fast burst capacity, event-driven execution, or avoiding the delay of waiting for node-scale events. Virtual nodes provide a way to extend the cluster with ACI-backed compute for those cases.

Microsoft’s AKS documentation explains that virtual nodes let you deploy pods in AKS that run as container groups in ACI, allowing fast scale-up without waiting for cluster autoscaler-driven VM provisioning. Microsoft also states that virtual nodes require AKS clusters using advanced networking (Azure CNI). The StackSimplify AKS course likewise places virtual nodes in the advanced execution section and explicitly notes the Azure CNI requirement.

## What you will learn
- What AKS virtual nodes are in practical platform terms
- How virtual nodes differ from standard AKS VM-backed node pools
- Why virtual nodes are useful for burst, transient, or fast-scale workloads
- Why networking prerequisites and workload-fit decisions matter before using them

## Workflow position
This module builds directly on Folder 16, where the learner organized workloads logically with namespaces. Now the learner moves into execution placement strategy and starts thinking about different compute backends inside one Kubernetes control plane.

This module also prepares the learner for:
- ACR-integrated workload delivery
- autoscaling strategy later in the course
- production-cluster design trade-off thinking

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain AKS virtual nodes clearly
- understand the role of ACI-backed pod execution
- compare virtual-node-backed workloads with standard node-pool workloads
- explain when virtual nodes are a good fit and when they are not

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the execution-model behavior carefully  
5. Do not move ahead until virtual nodes feel clear as a capacity and execution design pattern, not only an AKS feature toggle  

## Next module
The next module is **ACR with AKS**.

That module builds directly on this by focusing on secure image supply and registry-backed workload delivery, which is a core dependency no matter whether the workload lands on standard node pools or virtual nodes.
