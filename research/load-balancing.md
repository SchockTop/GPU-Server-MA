# Dynamic load balancing for a small shared GPU server (research notes)

Date of research: 2026-11-17. Scope: 5-20 users, 1-few GPU servers, 8-12 mixed GPUs (16-48 GB), workloads: rendering, NN training, LLM fine-tuning, LLM inference. No paid NVIDIA vGPU.

Legend: **V** = seen on the project page / docs during this research (URL given). **U** = from memory, not verified now. Versions and dates are as seen on 2026-11-17.

---

## 0. Short answer

- Start with **whole-GPU scheduling plus a queue** (single-node k3s or Slurm). Fractions and autoscaling come later.
- For a 1-3 node team the best-value Kubernetes stack is: **k3s + NVIDIA GPU Operator (or plain device plugin) + Kueue** (queues, quotas, preemption, one ResourceFlavor per GPU model) + **Prometheus/DCGM** for metrics.
- Add **vLLM behind a simple router/LiteLLM + KEDA** only when inference is real. Skip llm-d / Gateway API Inference Extension until there are several GPU nodes serving one model.
- Rendering: **Flamenco** (Blender-native) with workers as pods, or Kubernetes Jobs with indexed completion for frame ranges.
- Fractions: **time-slicing** is easy but has no isolation (V). **MIG** only exists on a few data-centre cards. **HAMi** or **KAI Scheduler** are the free options for memory-limited fractions on mixed cards, but both add complexity. Treat them as optional.
- True "dynamic" balancing on a small box is mostly: queue + priorities + preemption + checkpointing + scale-to-zero. Not live migration of running jobs (not available for GPU work in practice).

---

## 1. What "dynamic load balancing" means at each layer

| Layer | Plain-words meaning | Typical question it answers |
|---|---|---|
| (a) Job scheduling / queueing | Jobs wait in a queue and a scheduler places each on a free GPU. Nobody picks "their" GPU by hand. | "Which job runs next, and where?" |
| (b) GPU sharing / fractions | One physical card is split among several jobs (time slices, memory caps, hardware partitions). | "Can two small jobs share a 48 GB card?" |
| (c) Request load balancing | A router spreads incoming inference requests across model replicas, ideally by load or cache hits, not blindly round-robin. | "Which replica answers this prompt?" |
| (d) Autoscaling / scale-to-zero | Number of inference replicas follows demand. At zero demand the service gives its GPU back. | "Can idle chat services free GPUs for a render job at night?" |
| (e) Preemption and priorities | A higher-priority job (interactive, urgent render) evicts or pauses a lower one (batch training). The evicted job must be able to resume. | "Interactive beats batch." |
| (f) Heterogeneous placement | Match job needs (VRAM, speed, architecture) to the right card. Label cards, request by label or by memory. | "A 40 GB fine-tune must not land on a 16 GB card." |

Important distinction: Kubernetes by default counts GPUs as integers (`nvidia.com/gpu: 1`) and does not know VRAM size or speed. Layer (f) therefore needs labels/flavors or Dynamic Resource Allocation (DRA).

---

## 2. Tools per layer

### 2.1 Kubernetes GPU basics

**NVIDIA GPU Operator + device plugin** (layers a, b, f)
- Installs driver, container toolkit, device plugin, GPU Feature Discovery, DCGM exporter via Helm. Latest release seen: **v26.7.2, 14 Oct (2026)**. V: https://github.com/NVIDIA/gpu-operator/releases
- Licence: Apache-2.0 for the operator (U; the release page did not state it). The drivers it deploys keep NVIDIA's own licence.
- Mixed GPU models: yes. GPU Feature Discovery puts labels like `nvidia.com/gpu.product`, `nvidia.com/gpu.memory` on nodes (U for the exact label list). One node with different cards is the weak spot: the stock device plugin exposes all cards of a node as the same resource `nvidia.com/gpu`, so you cannot request "the 48 GB one" on the same node with plain labels. Options: MIG-strategy `mixed`, separate nodes, DRA, or HAMi (see below).
- Sharing docs (time-slicing, MIG): V: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html

**Time-slicing** (b)
- Free, works on any CUDA card including GeForce. V (same page): "there is no memory or fault-isolation between replicas"; a pod requesting 2 slices does not get proportional compute; DCGM exporter cannot attribute metrics per container when time-slicing is on; the operator does not watch the ConfigMap (restart the device plugin after editing). Per-node config via label `nvidia.com/device-plugin.config=<key>` (V), so different card types can get different replica counts.

**MPS** (b): CUDA Multi-Process Service lets processes share a GPU concurrently with optional per-client memory/thread limits. Not covered on the GPU Operator sharing page (V: absent). Support level in the device plugin: U.

**MIG** (b): hardware-isolated partitions (V, same page). Only on specific data-centre cards (A30/A100/H100 class and some newer RTX PRO workstation cards, U). Not on typical RTX A-series or GeForce. For a mixed workstation fleet, MIG is mostly irrelevant.

**Dynamic Resource Allocation (DRA)** (a, b, f)
- V: **stable (GA) since Kubernetes v1.35**, feature gate locked on; objects: ResourceSlice, DeviceClass, ResourceClaim, ResourceClaimTemplate. https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- V limitation on that page: "the scheduler doesn't support preemption for DRA resources". A high-priority pod needing a DRA device stays Pending until the device is freed. This matters for layer (e).
- DRA lets a pod ask for devices by attribute (e.g. memory >= 40Gi, product name) via CEL selectors (U). NVIDIA ships a DRA driver for GPUs (U; the GPU Operator page did not confirm it). Maturity of the NVIDIA DRA driver, partitioning and consumable-capacity features: not verified.
- Practical view: DRA is the "right" long-term answer for heterogeneous placement, but for 1-3 nodes node labels + Kueue flavors are simpler today.

**Node Feature Discovery (NFD) / GPU Feature Discovery** (f): NFD labels nodes with hardware features; GFD (part of the GPU Operator) adds GPU model/VRAM/driver labels. Licence Apache-2.0 (U). Fine for choosing nodes, not for choosing one card among several on the same node.

### 2.2 Batch scheduling, queues, priorities (a, e, f)

**Kueue** (kubernetes-sigs)
- Job queueing layer: ClusterQueues, LocalQueues, quotas, borrowing, preemption, fair sharing, ResourceFlavors, Topology-Aware Scheduling, MultiKueue. Latest release seen: **v0.20.6 (12 Nov 2026)**, notes mention preemption, fair sharing, TAS, MultiKueue fixes. V: https://github.com/kubernetes-sigs/kueue/releases
- Licence Apache-2.0 (U). Works with the default kube-scheduler, so low operational weight. Handles Kubernetes Job, JobSet, RayJob/RayCluster, Kubeflow trainers (U for the exact list).
- Mixed GPUs: yes via **one ResourceFlavor per GPU model** (nodeLabels selecting `nvidia.com/gpu.product`). Users or admins state which flavors a job accepts and in what order (e.g. "prefer 24 GB, fall back to 48 GB").
- Recommended core of this setting.

**Volcano**
- CNCF incubating batch scheduler, Apache-2.0 (V: https://github.com/volcano-sh/volcano). Gang scheduling, queues, fair-share. Replaces the scheduler, so heavier to adopt. GPU sharing details not verified. Fine if you want an all-in-one batch system, but Kueue is lighter for a small team.

**NVIDIA KAI Scheduler (open-sourced Run:ai scheduler)**
- V: NVIDIA open-sourced the **Run:ai scheduler as KAI Scheduler on 1 April 2025, Apache-2.0**. Features named: gang scheduling (PodGroups), hierarchical queues with priority and fairness, GPU sharing. Still packaged as part of the commercial NVIDIA Run:ai platform. https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/
- V: repo is a **CNCF Sandbox** project; v0.10.0 highlighted (Oct 2025); native Ray/KubeRay integration; prerequisites: Kubernetes, Helm, GPU Operator. https://github.com/NVIDIA/KAI-Scheduler (the page did not show the newest version; check releases).
- Not verified: fraction request syntax in current release (from memory, pods use annotations like `gpu-fraction: "0.5"` and optionally `gpu-memory`; U). Not open-sourced (as far as seen): the Run:ai control plane, UI, and the commercial platform (the blog does not list them; U).
- KAI fractions are time-slicing-like (no hard memory isolation, U). Mixed models: it can place by node labels; per-card VRAM awareness within one node is not verified.
- Maybe, for stage 2 if fractions and fairness between users are needed. Overlaps with Kueue; running both needs care (U).

**HAMi** (CNCF incubating)
- V: Apache-2.0; "Kubernetes GPU virtualization and heterogeneous accelerator scheduling", isolates device memory and compute; topics list NVIDIA plus several Chinese accelerator vendors; AMD not mentioned on the page. https://github.com/Project-HAMi/HAMi
- U: lets a pod request e.g. `nvidia.com/gpumem: 8000` and `nvidia.com/gpucores: 30`, enforced by an in-container interception library (software limit, not hardware isolation); can select GPU by type/UUID via annotations; sees each physical card separately, so it handles mixed cards on one node better than the stock plugin.
- Risk: intercepting CUDA calls can break with new driver/CUDA versions and some frameworks. Test per workload.

**Slurm (non-Kubernetes alternative)**
- V: current release listed as **Slurm 26.05**; recent GRES AutoDetect and Prometheus GPU allocation stats. https://slurm.schedmd.com/news.html Licence GPLv2 (U; page silent).
- Strengths: simple for batch training/fine-tuning, fair-share, QoS preemption, GRES types per GPU model (`Gres=gpu:a6000:1`, `--gres=gpu:rtx4090:1`), accounting. Handles mixed models on one node very naturally (U).
- Weak: no native inference serving, autoscaling or scale-to-zero; rendering and desktops need extra glue. Great for 1-2 nodes of batch work.

**Ray / KubeRay**
- V: KubeRay Apache-2.0; CRDs RayCluster, RayJob, RayService (Ray Serve with zero-downtime upgrades); integrates with Volcano, YuniKorn, Kueue. https://github.com/ray-project/kuberay
- Layers a, c, d. Useful if teams already write Ray code (distributed training, Ray Serve). Extra moving part otherwise.

### 2.3 Inference serving (c, d)

| Tool | Facts |
|---|---|
| **vLLM production stack** | V: Apache-2.0; router with round-robin and session-ID routing (prefix-aware in progress), LMCache KV offload tutorial, Prometheus/Grafana dashboard. Autoscaling listed as roadmap, page does not mention KEDA. No release numbers visible (first announced Jan 2025). https://github.com/vllm-project/production-stack |
| **llm-d** | V: Apache-2.0, CNCF sandbox (joined March 2026), founded by Red Hat, Google Cloud, IBM Research, CoreWeave, NVIDIA; sits above vLLM/SGLang; **v1.0 in Oct 2026** (stable v1 config API, multi-tenant QoS); validated on NVIDIA, AMD, Intel GPUs and TPUs; SLO-aware autoscaling listed. https://github.com/llm-d/llm-d Aimed at multi-node clusters; heavy for 1 node. |
| **Gateway API Inference Extension (GAIE)** | V: official Kubernetes project; extends Gateway API gateways with an Endpoint Picker (EPP) choosing replicas from model-server metrics; InferencePool CRD; works with Envoy Gateway, kgateway, GKE Gateway; both v1 and v1alpha1 API refs exist. https://gateway-api-inference-extension.sigs.k8s.io/ Needs a Gateway implementation. Gains appear with several replicas of the same model. |
| **LiteLLM proxy** | U: open-source (MIT core, some enterprise features paid) OpenAI-compatible proxy; routing/fallback across backends, per-user keys, budgets. Page named as a gateway option on the GAIE page (V). Good for a small team: one URL and keys for all models. |
| **Triton Inference Server** | U: Apache/BSD-style, NVIDIA; multi-framework, dynamic batching. Best for classic NN serving; for LLMs most small teams use vLLM directly. |
| **KServe** | U: CNCF, Apache-2.0; InferenceService CRD. V (outline only): supports scale-to-zero via Knative or raw-deployment mode with KEDA. https://kserve.github.io/website/latest/modelserving/autoscaling/autoscaling/ Heavy (needs Knative or KEDA, Istio/Gateway). Probably too much for 1-3 nodes. |
| **Knative Serving** | U: scale-to-zero for HTTP services with request buffering (activator), cold start depends on model load. |
| **KEDA** | V: Prometheus scaler with `query`, `threshold`, `activationThreshold`; examples use `minReplicaCount: 0`; docs advise verifying scale-to-zero against concepts docs. https://keda.sh/docs/latest/scalers/prometheus/ KEDA's HTTP add-on (U) is needed to hold requests while a pod starts from zero; plain Prometheus scaler cannot buffer requests. |
| **Ollama** | U: very easy, but limited: single-host process, queues requests per model with `OLLAMA_NUM_PARALLEL`, loads/unloads models on a keep-alive timer (a poor-man's scale-to-zero of VRAM), no cluster-level routing, no per-user quotas, weak multi-GPU placement control. Fine for personal desktops, not as the shared service. |
| **GPUStack** | V: Apache-2.0 GPU cluster manager for model serving and GPU instance provisioning; supports NVIDIA, AMD, Ascend and several other vendors; backends vLLM, SGLang, TensorRT-LLM; quick start uses Docker, no Kubernetes needed. Whether it mixes vendors in one cluster: not stated. https://github.com/gpustack/gpustack Attractive for a tiny team that mainly wants LLM serving across mixed GPUs (U for its scheduling quality). |

### 2.4 Rendering

| Tool | Facts |
|---|---|
| **Blender Flamenco** | V: all components GPLv3, free; core in Go + SQLite; job types written in JavaScript; "in active development at Blender Studio" (no version number seen). https://flamenco.blender.org/ U: Manager + Workers (each worker runs Blender headless) + shared storage; per-worker tags; Cycles GPU supported through Blender settings. Best fit for Blender/Cycles. |
| **Kubernetes Jobs, indexed completion** | U: `completionMode: Indexed` gives each pod `JOB_COMPLETION_INDEX`, which maps to a frame or frame chunk. Works with Kueue for quotas/priorities. No render-specific UI; needs shared storage for scenes/output. |
| **OpenCue** | V: Apache-2.0 (Academy Software Foundation), Python 3.6+ badge, no GPU/Blender info on page. https://github.com/AcademySoftwareFoundation/OpenCue U: designed for studio pipelines; heavier than Flamenco. |
| **AWS Thinkbox Deadline 10** | V: Deadline 10 is free downloadable software; **License-Free Mode allows up to ten workers without a licence** (since 10.1); usage-based licensing for third-party apps moved to **AWS Deadline Cloud UBL** (pay-as-you-go via AWS bill); **legacy Thinkbox UBL ended 30 Sep 2025**. https://docs.thinkboxsoftware.com/products/deadline/10.4/1_User%20Manual/manual/licensing-usage-based.html and https://aws.amazon.com/thinkbox-deadline/ . No 2026 announcement found; the 10-worker limit is relevant for a farm of this size. |
| **CGRU / Afanasy** | U: open-source (LGPL-style) farm manager with Blender support; smaller community. Not verified. |
| **V-Ray / Octane** | U: both need their own licences (V-Ray render nodes via licence server, Octane via OTOY account/licence). Check licence terms for containerised or multi-user use before planning. |

Cycles/Blender needs no special scheduler support: a render job is just "one GPU for N minutes".

### 2.5 Lightweight non-Kubernetes or "Kubernetes-light" options

| Tool | Facts |
|---|---|
| **k3s** | U: CNCF-certified lightweight Kubernetes, single binary, Apache-2.0; works with the GPU Operator/device plugin (NVIDIA containerd runtime config needed). Right size for 1-3 nodes. |
| **Nomad + NVIDIA device plugin** | V (partial): plugin fingerprints memory, power, bar1, driver version, clocks, etc. and example job uses `affinity` on `${device.model}`; excluding GPUs by UUID possible; licence not stated on page. https://developer.hashicorp.com/nomad/plugins/devices/nvidia Nomad's licence is BSL since 2023 (U). Per-model constraints are natural here, with no sharing/fractions. |
| **dstack** | V: MPL-2.0; control plane for GPU provisioning and orchestration; on-prem via **SSH fleets** (no backend config), Kubernetes backend, job queuing, autoscaling; accelerators NVIDIA/AMD/TPU/Tenstorrent; version 0.21.0 seen (news, 2026/08). Mixed fleet and fractions not stated. https://github.com/dstackai/dstack |
| **SkyPilot** | V: Apache-2.0; supports Kubernetes, Slurm, VMware vSphere, 20+ clouds; queue, run and auto-recover jobs; "Autostop". No version seen. https://github.com/skypilot-org/skypilot Good "submit and forget" interface for researchers on top of k3s or Slurm. |
| **ClearML (agent)** | U: open-source server + agents pull tasks from queues, one queue per GPU type is a common pattern; experiment tracking included. Free self-hosted tier. Licence of server: SSPL/other, check (U). |
| **GPUStack** | see 2.3 |

---

## 3. Integration path in stages

### Stage 0: measure (1-2 days, no user impact)
- Install on each server: **DCGM exporter** (container or package), node exporter, Prometheus, Grafana (U: all free/open-source). Fallback: a cron `nvidia-smi --query-gpu=... --format=csv` logger.
- Record per GPU: utilisation %, memory used, power, per user/process (nvidia-smi pmon), peak VRAM per job type.
- Output: who uses which card when, how much VRAM jobs really need, idle share (usually 50-80% for desktop-style use, U). This decides how many "reserved" GPUs you need later.
- Users notice: nothing.

### Stage 1: whole-GPU scheduling with a queue (2-5 days)
- Option A: **k3s + NVIDIA driver + container toolkit + GPU Operator (or plain device plugin) + Kueue**. Label nodes/GPUs by model. Users submit with `kubectl`/a thin CLI/Helm chart, or via SkyPilot/dstack on top.
- Option B: **Slurm** (slurmctld/slurmd on the server, `gres.conf` per GPU model, accounting). Faster if users are comfortable with SSH + `sbatch`.
- Keep a **reserved pool** of 2-4 GPUs for remote-desktop users (cordon those cards via a separate node label/taint, or `NVIDIA_VISIBLE_DEVICES` split; U for exact mechanism). Everything else is queue-managed.
- Users notice: submitting jobs instead of grabbing a card; shorter waits when the queue is fair; need to learn one submit command.

### Stage 2: priorities, quotas, preemption, fractions (3-7 days)
- Kueue: `ClusterQueue` per team/role with nominal quota, `cohort` borrowing, `WorkloadPriorityClass` (interactive > render-urgent > training > backfill), preemption policy `LowerPriority`.
- Make training **preemption-safe** (checkpoint every N minutes, resume from latest, `restartPolicy` / `backoffLimit`). Without this, preemption wastes work.
- Fractions: start with **time-slicing on small-card nodes** (2-4 replicas) for notebooks/dev only; for memory-limited sharing evaluate **HAMi** or **KAI Scheduler**. Keep production training on whole GPUs.
- Users notice: urgent jobs start fast; batch jobs may be paused/restarted; quotas visible.

### Stage 3: inference serving with autoscaling and router (3-7 days)
- Deploy **vLLM** as Deployments (one per model, pinned to GPU flavor by label/memory). Put **LiteLLM** (or the vLLM router) in front for one URL, keys and fallbacks.
- Scale: **KEDA** with a Prometheus trigger on vLLM metrics (e.g. waiting requests) from min 1 to max N; scale-to-zero only for rarely used models, accepting cold start (see pitfalls).
- Run inference Deployments at **lower priority than interactive but with a floor** (e.g. min 1 replica for the main model during working hours, scheduled via KEDA cron scaler U).
- Only if several replicas of one model run across nodes: add GAIE/llm-d for prefix-cache-aware routing.
- Users notice: a stable OpenAI-compatible endpoint; first request after idle may be slow.

### Stage 4: render farm on the same pool (2-4 days)
- Flamenco Manager as a pod (or on a non-GPU host) with shared storage (NFS/SMB, U). Workers as Deployments requesting 1 GPU each, scaled by KEDA or by hand; Kueue gives them a low-priority/backfill class so training and inference can reclaim cards.
- Alternative: a render CLI submits a Kubernetes Indexed Job (one frame range per index) into a Kueue LocalQueue.
- Licence servers (V-Ray, Octane) must be reachable from the cluster network.
- Users notice: "Submit to farm" from Blender instead of rendering on their desktop session; renders fill idle GPUs.

### Keeping remote-desktop users working during migration
1. **Reserve first, shrink later**: start with most cards still "desktop"; move 1-2 cards per month into the pool as usage data (Stage 0) shows idle time.
2. **Per-card split on the same host**: desktop sessions use only the reserved GPUs; the queue cannot see them (taint/label or device exclusion).
3. **Desktop as a pod**: U: possible with a container desktop (KasmVNC/Xpra/Selkies style) requesting a GPU through the queue with highest priority. Works for CUDA/OpenGL on NVIDIA; verify per application.
4. **Desktop as a VM with passthrough**: possible (VFIO) but binds a card exclusively to the VM and complicates the host driver; GeForce passthrough has historic quirks (U). Use only if hard isolation is required.
5. Tell users a card in the pool may be needed: an "interactive" priority class that preempts batch within a few minutes is the practical compromise.

---

## 4. Reference architectures

All snippets are **illustrative** (not copied from docs unless stated). Check field names against the version you install.

### 4.1 Minimal: one server, Slurm or k3s, whole GPUs

```
 users --ssh/CLI--> [ queue: Slurm  OR  k3s + Kueue ]
                          |
        +-----------------+------------------+
        | single GPU server                    |
        |  reserved: GPU0-GPU3  (remote desktop)
        |  pool:     GPU4-GPU9  (jobs)         |
        |  DCGM exporter -> Prometheus -> Grafana
        +--------------------------------------+
```

Slurm illustrative `gres.conf` / `slurm.conf` lines:
```
# gres.conf
NodeName=gpu01 Name=gpu Type=a6000   File=/dev/nvidia4,/dev/nvidia5
NodeName=gpu01 Name=gpu Type=rtx4090 File=/dev/nvidia6,/dev/nvidia7
# slurm.conf
GresTypes=gpu
NodeName=gpu01 Gres=gpu:a6000:2,gpu:rtx4090:2 ...
PreemptType=preempt/qos
PreemptMode=REQUEUE
```
Submit: `sbatch --gres=gpu:a6000:1 --qos=batch train.sh`.
Fits: 1 node yes. No inference autoscaling; run vLLM as long-lived Slurm jobs or systemd.

### 4.2 Recommended: k3s + GPU Operator + Kueue + KEDA + LiteLLM + Flamenco

```
 users --kubectl/CLI/Helm--> k3s API
                                |
   +----------------+-----------+------------------+
   | Kueue          | KEDA      | Prometheus/DCGM  |
   | ClusterQueues  | scalers   | Grafana          |
   +-------+--------+-----+-----+------------------+
           |              |
    LocalQueue per team   |
           v              v
   [train/finetune Jobs] [vLLM Deployments] <- [LiteLLM / router] <- users, apps
   [Flamenco workers  ]  (1 per model)
           |
   GPU nodes (label: gpu.product=A6000 / RTX4090 / L4 ...)
   reserved desktop GPUs excluded
```

Kueue illustrative (one flavor per GPU model):
```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata: { name: a6000-48g }
spec:
  nodeLabels: { nvidia.com/gpu.product: NVIDIA-RTX-A6000 }
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata: { name: shared-gpu }
spec:
  namespaceSelector: {}
  preemption:
    withinClusterQueue: LowerPriority
  resourceGroups:
  - coveredResources: ["nvidia.com/gpu"]
    flavors:
    - name: a6000-48g
      resources: [{ name: nvidia.com/gpu, nominalQuota: 2 }]
    - name: rtx4090-24g
      resources: [{ name: nvidia.com/gpu, nominalQuota: 4 }]
```
Caveat: label values and API version (`v1beta1` vs newer) depend on installed versions. Also, if two card models sit in one node, the stock plugin cannot tell them apart; use one node per model, MIG-`mixed`, or HAMi/DRA.

Flamenco worker as a Deployment (illustrative):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: flamenco-worker }
spec:
  replicas: 2
  selector: { matchLabels: { app: flamenco-worker } }
  template:
    metadata:
      labels:
        app: flamenco-worker
        kueue.x-k8s.io/queue-name: render   # note: plain Deployments need Kueue's pod-integration enabled (U)
    spec:
      priorityClassName: render-backfill
      containers:
      - name: worker
        image: registry.example/flamenco-worker:blender-4.x   # self-built
        resources: { limits: { nvidia.com/gpu: 1 } }
        volumeMounts: [{ name: shared, mountPath: /shared }]
      volumes: [{ name: shared, persistentVolumeClaim: { claimName: render-share } }]
```

KEDA for vLLM (illustrative; metric name `vllm:num_requests_waiting` is U):
```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata: { name: vllm-chat }
spec:
  scaleTargetRef: { name: vllm-chat }
  minReplicaCount: 0        # 1 during office hours, via cron scaler (U)
  maxReplicaCount: 3
  cooldownPeriod: 900
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring:9090
      query: sum(vllm:num_requests_waiting{app="vllm-chat"})
      threshold: "2"
      activationThreshold: "1"
```
(`serverAddress`, `query`, `threshold`, `activationThreshold` are V fields on the KEDA page.) With min 0 you need something that wakes the service on first request (KEDA HTTP add-on or Knative, U).

Fits: 1 node yes (control plane + GPU on same host), though a single host is a single point of failure.

### 4.3 Advanced: multi-node, fractions, fair share, cache-aware routing

```
                        Gateway (Envoy/kgateway) + GAIE Endpoint Picker / llm-d
                                       |
  users --> LiteLLM (keys, budgets) ---+--> InferencePool: vLLM replicas (node A, B)
       \
        +--> KAI Scheduler (hierarchical queues, gang, fractions)  [or Kueue + HAMi]
                 |         |
     training / RayJob     fractional notebooks (0.25-0.5 GPU)
                 |
   DRA (v1.35 GA) ResourceClaims: "gpu with memory >= 40Gi"
   NFD + GFD labels; DCGM + Prometheus; MultiKueue / second cluster optional
   Flamenco / Indexed Jobs as lowest-priority backfill
```

KAI fraction request (illustrative; annotation name from memory, U, check the KAI docs):
```yaml
metadata:
  labels:    { kai.scheduler/queue: team-a }
  annotations: { gpu-fraction: "0.5" }
spec:
  schedulerName: kai-scheduler
```

DRA claim (illustrative; API group version and CEL attribute names must be checked, U):
```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata: { name: big-gpu }
spec:
  spec:
    devices:
      requests:
      - name: gpu
        exactly:
          deviceClassName: gpu.nvidia.com
          selectors:
          - cel: { expression: 'device.capacity["gpu.nvidia.com"].memory.compareTo(quantity("40Gi")) >= 0' }
```
Fits: 1 node no (overkill). Remember V: the scheduler does not preempt for DRA resources, so combine carefully with priority policies.

---

## 5. Pitfalls

1. **Mixed GPU models and VRAM fragmentation.** Integer GPU counts hide VRAM. A 16 GB job on a 48 GB card wastes 32 GB; a 40 GB job pends while small cards idle. Use flavors with an ordered preference (small job -> smallest fitting card), or request `gpu.memory` via labels/DRA/HAMi. Different architectures (e.g. Turing vs Ada) also need matching CUDA/driver versions and different FP8/bf16 support (U).
2. **Model load time vs scale-to-zero.** Loading a 7-70 B model from disk to VRAM takes tens of seconds to minutes (U), plus container start. Scale-to-zero suits batch-like or rarely used models; keep min replicas 1 for interactive chat. Use a node-local cache (hostPath/PVC on NVMe) for weights, and a request buffer so the first call waits instead of failing.
3. **GeForce driver licence in shared servers.** V: NVIDIA GeForce licence section 2.8 says GeForce/Titan software "is not licensed for datacenter deployment" and limits use to hardware you own. https://www.nvidia.com/en-us/drivers/geforce-license/ (only the quoted part was seen; a blockchain exception exists in the real text, U). A multi-user server cluster may count as datacenter use; check with NVIDIA/legal. Workstation (RTX A-series/RTX PRO) cards use the professional driver licence (U), preferable here.
4. **Noisy neighbours with time-slicing and no memory isolation.** V: no memory or fault isolation between time-sliced replicas; one process OOM-ing the card can kill others; equal time shares regardless of need. Do not use it for production services; use MIG (hardware cards only), HAMi limits, or whole GPUs.
5. **Preempted training must resume.** Save checkpoints (model, optimizer, data-loader position, RNG) to shared storage every 10-30 min; use `torchrun` elastic/`--resume`; set SIGTERM grace period long enough for a final save; for LLM fine-tuning libraries confirm resume-from-checkpoint works.
6. **Render jobs need licence servers.** V-Ray and Octane (U) require reachable licence servers or accounts; Deadline's free mode is capped at 10 workers (V). Blender itself has no licence issue. Limit concurrent licensed workers with Kueue quotas.
7. **Single point of failure with one node.** One k3s node: if it dies, control plane and workloads die. Mitigate: backups of etcd/SQLite, configs in Git, documented restore, keep the queue state disposable. Second small node for control plane is an optional upgrade.
8. **DRA preemption gap (V).** High-priority pods needing DRA devices do not preempt; avoid mixing DRA-claimed devices with strict interactive-priority guarantees until this changes.
9. **Scheduler overlap.** Running Kueue with KAI or Volcano needs a clear split of responsibility (U); pick one admission/queue system.
10. **Operations burden.** GPU Operator upgrades, driver pins, container toolkit config on k3s, and time-slicing ConfigMap restarts (V) all need a documented routine. Budget ongoing time, not just install time.
11. **Interactive desktops and CUDA on the same card.** Display/desktop sessions consume VRAM and may conflict with compute-mode settings; keep desktop cards outside the pool.

---

## 6. Comparison table

| Tool | Layer | Licence / cost | Mixed-GPU support | Complexity | Fits 1 node | Recommended |
|---|---|---|---|---|---|---|
| GPU Operator + device plugin | a, f | Apache-2.0 (U), free | Labels per model; same-node mix limited | Medium | yes | **yes** (base layer) |
| Time-slicing | b | free, in plugin | any CUDA card | Low | yes | maybe (dev/notebooks only; no isolation V) |
| MPS | b | free, in driver | NVIDIA only | Medium | yes | maybe (small jobs, same user) |
| MIG | b | free, hardware-bound | data-centre cards only | Medium | yes | no (cards not supported, U) |
| DRA | a, b, f | Kubernetes, GA in v1.35 (V) | attribute-based (U) | High | yes | maybe (watch it; no preemption V) |
| NFD / GFD labels | f | Apache-2.0 (U) | node-level labels | Low | yes | yes (comes with operator) |
| Kueue | a, e, f | Apache-2.0 (U), free | flavor per GPU model | Medium | yes | **yes** (queues, quotas, preemption) |
| Volcano | a, e | Apache-2.0 (V) | via labels | High | yes | no (Kueue is lighter) |
| KAI Scheduler | a, b, e | Apache-2.0 (V), CNCF Sandbox | via labels; per-card VRAM not verified | High | yes | maybe (if fractions + fair share needed) |
| HAMi | b, f | Apache-2.0 (V), CNCF incubating | per-card, vendor-mixed (partly V) | Medium-high | yes | maybe (memory-capped fractions) |
| Slurm | a, e, f | GPLv2 (U), free | strong (GRES types) | Medium | yes | **yes** (if batch-only / SSH culture) |
| k3s | platform | Apache-2.0 (U) | n/a | Low-medium | yes | **yes** |
| Nomad + GPU plugin | a, f | BSL (U) | model attribute/affinity (V) | Medium | yes | no (smaller GPU ecosystem) |
| Ray / KubeRay | a, c, d | Apache-2.0 (V) | via labels | Medium-high | yes | maybe (only if Ray is used) |
| vLLM (single deployment) | c | Apache-2.0 (U) | per replica | Low | yes | **yes** |
| vLLM production stack router | c | Apache-2.0 (V) | per replica | Medium | yes | maybe (needs >1 replica) |
| llm-d | c, d | Apache-2.0 (V), v1.0 Oct 2026 | NVIDIA/AMD/Intel (V) | High | no | no (multi-node scale) |
| Gateway API Inference Extension | c | Apache-2.0 (U) | n/a | High | no | no (later) |
| LiteLLM proxy | c | MIT core (U) | n/a | Low | yes | **yes** (single URL, keys) |
| Triton | c | open source (U) | per replica | Medium | yes | maybe (classic NN serving) |
| KServe | c, d | Apache-2.0 (U) | per replica | High | yes | no (heavy) |
| Knative / KEDA | d | Apache-2.0 (U) | n/a | Medium | yes | KEDA yes, Knative maybe |
| Ollama | c | MIT (U), free | weak placement control | Low | yes | no for shared service; ok on desktops |
| GPUStack | c, a | Apache-2.0 (V) | multi-vendor listed (V) | Low-medium | yes | maybe (LLM-only quick start) |
| Flamenco | render | GPLv3 (V), free | any Blender-capable GPU | Low | yes | **yes** (Blender) |
| OpenCue | render | Apache-2.0 (V) | n/a | High | yes | no |
| Deadline 10 | render | free, 10 workers licence-free (V) | n/a | Medium | yes | maybe (if V-Ray/Octane pipeline needs it) |
| CGRU / Afanasy | render | open source (U) | n/a | Medium | yes | maybe/no (unverified) |
| K8s Indexed Jobs | render | free | via Kueue flavors | Low-medium | yes | yes (alt. to Flamenco) |
| dstack | a, c | MPL-2.0 (V) | not stated | Medium | yes | maybe (submit UX) |
| SkyPilot | a | Apache-2.0 (V) | not stated | Medium | yes | maybe (UX layer) |
| ClearML agent | a | free self-hosted (U) | queue per GPU type | Medium | yes | maybe (if tracking wanted) |

---

## 7. Not verified in this pass

- Exact current versions of KAI Scheduler, HAMi, Volcano, KubeRay, vLLM production stack, SkyPilot (pages showed no release number).
- KAI fraction syntax, HAMi resource names, NVIDIA DRA driver maturity, MPS support in the device plugin, DRA partitioning/consumable capacity.
- Licences marked U (GPU Operator, Kueue, k3s, LiteLLM, Triton, KServe, Ollama, ClearML, Afanasy, Nomad BSL).
- Deadline 2026 licensing changes (none found; latest docs seen are 10.4).
- Behaviour of Flamenco with multiple GPUs per worker, V-Ray/Octane containerised licensing.

## 8. Sources (pages fetched 2026-11-17)

- https://github.com/NVIDIA/KAI-Scheduler
- https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/
- https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- https://github.com/kubernetes-sigs/kueue/releases
- https://github.com/NVIDIA/gpu-operator/releases
- https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html
- https://github.com/Project-HAMi/HAMi
- https://github.com/volcano-sh/volcano
- https://github.com/ray-project/kuberay
- https://github.com/llm-d/llm-d
- https://github.com/vllm-project/production-stack
- https://gateway-api-inference-extension.sigs.k8s.io/
- https://keda.sh/docs/latest/scalers/prometheus/
- https://kserve.github.io/website/latest/modelserving/autoscaling/autoscaling/
- https://flamenco.blender.org/
- https://github.com/AcademySoftwareFoundation/OpenCue
- https://docs.thinkboxsoftware.com/products/deadline/10.4/1_User%20Manual/manual/licensing-usage-based.html
- https://slurm.schedmd.com/news.html
- https://developer.hashicorp.com/nomad/plugins/devices/nvidia
- https://github.com/dstackai/dstack
- https://github.com/skypilot-org/skypilot
- https://github.com/gpustack/gpustack
- https://www.nvidia.com/en-us/drivers/geforce-license/
