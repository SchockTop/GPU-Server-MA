# Multi-user GPU sharing: virtualisation options and licence costs

As of 2026-11-17. [V] = checked on the cited page (some pages were read through a summarising fetch tool, so re-check key figures against the page before relying on them). [U] = secondary, community or unverified. Prices are NVIDIA list prices in USD; partner quotes differ.

Context: a small team moving from remote desktops to Kubernetes-style shared compute for rendering, training and LLM inference.

## 1. NVIDIA vGPU (paid)

vGPU splits one physical GPU into fixed-memory slices for VMs on a hypervisor. It needs licensed guest drivers and a licence server.

### 1.1 Editions and list prices

Source: [NVIDIA vGPU Packaging, Pricing and Licensing Guide](https://docs.nvidia.com/vgpu/packaging-pricing-licensing-guide/latest) [V]

| Edition | Subscription per concurrent user (CCU) / year | Perpetual per CCU | CUDA in the VM? |
|---|---|---|---|
| vApps | 10 USD | 20 USD + 5 USD/yr support | no |
| vPC | 50 USD | 100 USD + 25 USD/yr | no |
| **RTX vWS** | **250 USD** (4-yr 206.25, 5-yr 180 per year) | **450 USD + 100 USD/yr** (5 years of support must be bought) | **yes** |
| vWS Education | 50 USD | 99 USD + 25 USD/yr | yes (qualified education institutions only) |

- Only RTX vWS includes CUDA/OpenCL, so rendering and AI inside VMs need vWS [V].
- **Example (DERIVED):** 8 concurrent users on vWS subscription cost 8 × 250 = 2,000 USD per year. Perpetual costs 8 × (450 + 5 × 100) = 7,600 USD for 5 years.

### 1.2 NVIDIA AI Enterprise (NVAIE)

Source: [NVAIE pricing, updated 2 Sep 2026](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/pricing.html) [V]

- **4,500 USD per GPU per year**; perpetual with 5 years of support costs 22,500 USD.
- Education institutions and NVIDIA Inception/Connect members pay 25% of list: 1,125 USD per GPU per year [V].
- In the cloud it costs 1 USD per GPU-hour; development use is free with community support [V].
- NVAIE covers "vGPU for Compute" (C-series vGPU, i.e. Kubernetes nodes inside VMs with CUDA slices) [U, from NVAIE docs summary].

### 1.3 Without a licence
- From the vGPU 16 licensing guide [V]: full speed for 20 minutes after VM boot, then 15 fps with reduced CUDA performance. After 24 hours: 3 fps, and **CUDA calls fail**.
- We could not check the same schedule for the current release (v20/21) [U].
- A one-time **90-day evaluation licence** exists; it needs a corporate e-mail address [V NVIDIA blog / U details].

### 1.4 Which cards support vGPU

Source: [docs.nvidia.com/vgpu/gpus-supported-by-vgpu.html](https://docs.nvidia.com/vgpu/gpus-supported-by-vgpu.html), fetched 2026-11-17 [V]

| Listed (first vGPU release) | Not listed |
|---|---|
| RTX PRO 6000 Blackwell **Server Ed.** (19.0) | RTX PRO 6000 Workstation and Max-Q |
| RTX PRO 5000 Blackwell **72 GB** (20.2) | RTX PRO 5000 **48 GB** |
| RTX PRO 4500 Blackwell **Server Ed.** (20.0) | RTX PRO 4500 Workstation, RTX PRO 4000 |
| RTX 6000 Ada (15.2), RTX 5000 Ada (16.1), RTX 5880 Ada | RTX 4500 Ada, RTX 4000 Ada |
| L40S (16.1), L40 (15.2), L4, L20, L2 | A100, H100 PCIe (vGPU list) |
| RTX A6000 (12.0), RTX A5000 (12.2), A5500, A40, A16, A10 | RTX A4500, RTX A4000 |
| | **all GeForce** |

- On Linux KVM, the A6000, A5500, A5000 and A40 run in displayless mode only [V].
- The per-hypervisor validated lists differ. For example, the PRO 5000 72 GB is missing from the KVM release notes [V].
- Hypervisors: VMware vSphere, RHEL KVM, Ubuntu, Nutanix AHV, Citrix XenServer and Azure Local per the support matrix. **Proxmox VE** has been a validated KVM platform since vGPU 18, with support provided by Proxmox. XCP-ng: no evidence of support [V/U].

Assessment: of the new cards that fit a ~10k budget, none is vGPU-capable. The cheapest vGPU-capable new card is the RTX 5000 Ada (~5,200 EUR). Among Blackwell cards, the cheapest is the PRO 5000 72 GB (~14,100 EUR).

## 2. Free NVIDIA options

| Option | What it does | Isolation | Cards |
|---|---|---|---|
| **Whole-GPU scheduling** (Kubernetes device plugin, Slurm) | Each job/pod gets whole GPUs | Full (one job per card) | all |
| **PCI passthrough** to VMs (Proxmox/KVM) | One whole GPU per VM with the normal driver | Full | all pro cards. GeForce works technically; licence caveat below. "No licence needed" is common practice; we found no NVIDIA page stating it explicitly [U] |
| **MIG** (Multi-Instance GPU) | Hardware partitions with their own memory, cache and SMs | **Hardware memory + fault isolation** [V] | RTX PRO 6000 Blackwell (WS, Max-Q, Server): up to 4. RTX PRO 5000 48 GB: 2 (2x24); PRO 5000 72 GB: 2 (2x36, per datasheet). PRO 4500: Server Ed. 2; Workstation Ed. **unconfirmed** (Lenovo says no). A100/H100: up to 7. [V] |
| **Time-slicing** (GPU Operator ConfigMap) | Several pods share a GPU in turns | **None**: no memory or fault isolation [V] | all NVIDIA |
| **MPS** (Multi-Process Service) | Concurrent kernels from several processes; MPS v3 adds SM/memory limits | Separate address spaces, but one fatal fault hits all clients; same-user by default [V] | all CUDA GPUs |
| **GPU Operator** | Installs driver, device plugin, MIG manager, monitoring on Kubernetes | n/a | all NVIDIA |
| **KAI Scheduler** (Apache 2.0, CNCF Sandbox) | GPU-aware queues, quotas, fractional sharing | scheduler-level | NVIDIA |
| **Run:ai open source** (since 13 Oct 2026) | Full Run:ai platform as a "Community Product": KAI Scheduler, GPU Fractioning Operator (CUDA-native fractions), resource management, workload map. No subscription needed, no NVIDIA support [V](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/) | software fractions | NVIDIA |
| **HAMi** (CNCF Incubating, Apache 2.0) | Kubernetes GPU "virtualisation" with memory/compute limits per pod | software-enforced | NVIDIA + others [V] |
| **Kubernetes DRA** | Dynamic Resource Allocation, GA in Kubernetes 1.35; NVIDIA DRA driver exists | depends on driver | NVIDIA, Intel [V/U] |

Notes:
- MIG gives compute slices only: no graphics/OptiX viewport rendering in MIG mode.
- MIG needs display outputs off (compute mode), Linux, and partly a VBIOS update. For a render service, MIG suits inference and fine-tuning slices, while render jobs take whole cards.
- **GeForce in a shared server:** the GeForce driver licence, section 2.8, says the software "is not licensed for datacenter deployment" ([nvidia.com/en-us/drivers/geforce-license](https://www.nvidia.com/en-us/drivers/geforce-license/), version 25 Feb 2025) [V]. "Datacenter" is not defined, so whether a department server counts is a question for your legal team.

## 3. AMD
- **MxGPU (SR-IOV):** supported on Instinct MI210X, MI300X, MI325X, MI350X/MI355X and the **Radeon PRO V710** only, on QEMU/KVM [V]. The documentation names no licence fee; we found none [U].
- **Not** on the Radeon AI PRO R9700 or W7900 [V, by absence].
- **Partitioning:** MI300-series CPX/NPS modes, managed by the AMD GPU Operator's Device Config Manager [U]. Instinct only.
- **Kubernetes:** the ROCm k8s-device-plugin assigns whole GPUs [V]. Sharing on Radeon cards needs generic means (e.g. HAMi lists other vendors; AMD support not confirmed [U]).
- Assessment: on workstation Radeon cards, AMD sharing means whole-card scheduling or passthrough, with no paid tier and no hardware partitioning.

## 4. Intel
- **Data Center GPU Flex:** SR-IOV with a licence-free Intel stack [U, not re-verified].
- **Arc Pro B60/B70:** SR-IOV works in community Proxmox setups (kernel ≥ 6.17, firmware-defined VF count) [U]. Upstream vGPU profile provisioning is planned for Linux 7.5 [U]. We found no official Intel support statement.
- **Kubernetes:** the Intel GPU device plugin offers `shared-dev-num` (several containers per GPU, no isolation) and hands out SR-IOV VFs once configured [V].

## 5. Practical comparison

| Option | Cost | Isolation | Fits Kubernetes plan | Which cards | Comment |
|---|---|---|---|---|---|
| Whole-GPU scheduling (device plugin / Slurm) | free | full per card | **yes** | all | Simplest; GPUs idle when jobs are small |
| PCI passthrough to VMs | free (hypervisor may cost) | full per card | partly (Kubernetes nodes as VMs) | all pro cards; GeForce: licence caveat | Good bridge from remote desktop to cluster |
| Time-slicing | free | none | **yes** | all NVIDIA | Fine for trusted, light interactive use; noisy neighbours |
| MPS | free | weak (shared fault domain) | yes | all NVIDIA | Many small inference processes from one team |
| MIG | free | **hardware** | **yes** (GPU Operator, DRA) | RTX PRO 6000 (4), PRO 5000 48/72 (2), PRO 4500 Server (2), A100/H100 | Best free isolation; compute only |
| KAI / Run:ai OSS / HAMi | free (no vendor support) | scheduler / software | **yes** | NVIDIA (HAMi broader) | Quotas, queues, fair share, fractions |
| NVIDIA vGPU RTX vWS | 250 USD/CCU/yr, or 450 + 100/yr perpetual | strong (VM, fixed slices) | partly (VDI, or Kubernetes inside VMs) | see 1.4 (none of the new <10k cards) | Only option for shared graphics desktops on one GPU |
| NVIDIA AI Enterprise (vGPU for Compute) | 4,500 USD/GPU/yr (EDU/Inception 1,125) | strong (VM) | yes | datacenter / qualified cards | Expensive for a small team |
| AMD MxGPU SR-IOV | no fee found | strong (VF) | partly | Instinct MI2xx/MI3xx, Radeon PRO V710 | Not available on workstation Radeon |
| AMD CPX/NPS partitioning | free | hardware-like | yes (AMD GPU Operator) | Instinct MI300 series | Datacenter only |
| Intel SR-IOV | free | VF | partly | Flex; Arc Pro B60/B70 (community) | Maturity uncertain |

Assessment for a render + AI service: free tools cover the Kubernetes goal well. Use whole-GPU scheduling for render jobs and training, MIG or time-slicing for small inference and notebook slices, and KAI/Run:ai for queues and quotas. Paid vGPU matters mainly if several users need **graphical remote desktops sharing one physical GPU**. Even then, licence costs per concurrent user add up, and only a few cards qualify.
