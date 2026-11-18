# AMD vs NVIDIA (and a note on Intel) for rendering, NN/LLM training and LLM inference

New hardware only; used cards are not listed.

Prices and facts re-checked at the sources on 18 Nov 2026.

As of 2026-11-17. Prices are German brutto (see `gpu-master-table.md`); benchmark sources are in `benchmarks.md`. [V] = checked on a cited page, [U] = secondary or unverified. Sentences marked "Assessment" are our interpretation.

## 1. Short version
- **Rendering:** NVIDIA leads clearly. In Blender, AMD's best cards (R9700, W7900) score about a third of a similarly priced NVIDIA card. Octane does not run on AMD, and Redshift supports AMD on Windows only.
- **LLM inference:** AMD has the cheapest VRAM per euro among AMD and NVIDIA pro cards: 32 GB for about 2,100 EUR (66 EUR per GB, RTX 4000 Ada: 97). Small-model token speed is decent (R9700 about 153 t/s vs 185 t/s on an RTX 5080 in llama.cpp), but under load NVIDIA pulls far ahead (5090 "almost four times faster" on a 27B model [U, ServeTheHome]).
- **Training and fine-tuning:** possible on ROCm, but there are no measured comparisons for current cards. FlashAttention, bitsandbytes and Unsloth support on RDNA4 is recent and partly community-maintained.
- **Operations:** NVIDIA's Kubernetes stack is mature: GPU Operator, MIG, time-slicing, open-source Run:ai. AMD's is solid on Instinct datacenter cards and thinner for Radeon PRO cards.

## 2. Software maturity

| Area | NVIDIA (CUDA) | AMD (ROCm / HIP) | Intel (oneAPI / XPU) |
|---|---|---|---|
| Driver / platform support | Broad Linux and Windows support, long-lived branches | The AMD docs "latest" page shows ROCm Core SDK 10.1.0 (Oct 2026), while the install page still says 7.14.0 (7.14 Jul 2026, 7.14.1 Sep 2026); which is current is to be confirmed [V]. It supports the **R9700, RX 9070 XT and W7900 on Linux** (Ubuntu 22.04.5/24.04.5/26.04.1, RHEL 9.8/10.2) and on Windows 11 25H2 [V]. | xe kernel driver; Battlemage support is still settling |
| PyTorch | First-class | ROCm wheels; the ROCm 10.1.0 docs list PyTorch 2.14.0 on Linux and Windows, the older ROCm 7.14 line PyTorch 2.10-2.12 (to be confirmed with the ROCm version) [V] | PyTorch XPU backend; IPEX-LLM archived Jan 2026 [U] |
| vLLM | First-class | RDNA4 (gfx1200/1201) listed as supported; official ROCm image [V]. A user saw about a 50% regression on one model after a vLLM/ROCm update on 4x R9700 [U]. Puget ran dual R9700 with TP=2 reliably [U]. | Intel's own llm-scaler vLLM fork [U] |
| llama.cpp | CUDA backend, fastest | HIP backend and Vulkan; both work [V build docs] | SYCL and Vulkan; prompt processing on the B60 is very slow on Vulkan (727 vs 3,900 t/s on a 5060 Ti) |
| bitsandbytes / FlashAttention / Unsloth (fine-tuning) | Mature | RDNA4 4-bit in bitsandbytes since 0.49 [U]. FlashAttention via Triton/AOTriton/AITER kernels, partly community [U]. Unsloth officially supports RDNA 3/4 since mid-2026 [U]. | Limited |
| Blender Cycles | OptiX (RT cores) + CUDA | HIP; HIP-RT on by default since Blender 5.1 [U] | oneAPI (Arc A/B) |
| V-Ray GPU | Full | Returned via HIP in V-Ray 7 Update 3 for 3ds Max (Apr 2026) [V digitalproduction]. V-Ray for Blender and V-Ray 7.4 for Maya (Jul 2026) also have it [U, Chaos announcements]; Linux unclear | No |
| Octane | Full | **Not supported** on Windows/Linux [U] | No |
| Redshift | Full (Windows and Linux) | **Windows only** (RDNA2+) [U] | No |
| Kubernetes | GPU Operator v26.x: device plugin, time-slicing, MIG, DRA driver; KAI Scheduler; Run:ai open source since 13 Oct 2026 [V] | ROCm k8s-device-plugin + AMD GPU Operator; partitioning only on Instinct (MI300 CPX/NPS) [V/U]. No sharing feature for Radeon PRO described. | Intel GPU device plugin with `shared-dev-num` sharing; hands out SR-IOV VFs [V] |
| Virtualisation | vGPU (paid licences) on selected pro/datacenter cards; MIG on RTX PRO 6000/5000/4500 | MxGPU/SR-IOV only on Instinct and Radeon PRO V710, not on R9700/W7900 [V] | SR-IOV: B70 (4 VFs) and B50 (2 VFs) official per Intel; B60 works in community setups (kernel ≥ 6.17), no official count [U] |

Assessment: for a mixed render + AI service run by a small group, the software risk on AMD falls on whoever runs it (debugging, version pinning). On NVIDIA it largely does not.

## 3. Performance and price per benchmark

Lowest German brutto price; Blender Open Data 4.5.0; llama.cpp Llama-2-7B Q4_0 tg128.

| Card | Price | VRAM | EUR/GB | Blender | EUR per 1k Blender | llama tg t/s | EUR per t/s |
|---|---|---|---|---|---|---|---|
| AMD Radeon AI PRO R9700 32GB | 2,102 | 32 | **66** | 3,209 (n=11) | 655 | 152.7 (Vulkan) | 13.8 |
| AMD Radeon PRO W7900 48GB | ~3,516 (snippet) | 48 | 73 | 3,790 (n=2) | 928 | no data | - |
| AMD RX 9070 XT 16GB | 949 | 16 | 59 | 3,279 | 289 | no data | - |
| NVIDIA RTX PRO 4000 Blackwell 24GB | 2,819 | 24 | 117 | 6,256 | 451 | 136.4 | 20.7 |
| NVIDIA RTX PRO 4500 Blackwell 32GB | 4,549 | 32 | 142 | 8,487 | 536 | 168.9 | 26.9 |
| NVIDIA RTX PRO 5000 Blackwell 48GB | 8,119 | 48 | 169 | 10,929 (n=7) | 743 | no data | - |
| NVIDIA RTX 5080 16GB | 1,969 | 16 | 123 | 9,138 | **215** | 184.7 | **10.7** |
| NVIDIA RTX 5090 32GB | 7,829 | 32 | 245 | 14,966 | 523 | 300.4 | 26.1 |
| Intel Arc Pro B60 24GB | 960 | 24 | **40** | 2,133 (n=5) | 450 | 68.1 (Vulkan) | 14.1 |

Reading the table:
- **Price per GB of VRAM:** the R9700 costs about half as much per GB as the cheapest NVIDIA pro card. The Intel B60 is cheaper still, but slow.
- **Render price/performance:** NVIDIA GeForce wins. Among pro cards, the R9700 (655 EUR per 1k points) is only on par with the PRO 5000 and worse than the PRO 4000.
- **LLM single-user speed per euro:** a 5080 ≈ R9700 ≈ B60. The R9700 doubles the VRAM, though.
- **Multi-user LLM serving:** AMD falls further behind (5090 about 3-4x the R9700 under load [U]).

Price evidence: the R9700 price comes from Amazon.de via the gpuprix aggregator (14 Nov 2026); the W7900 price comes only from a search snippet.

## 4. Driver and support risks

| Risk | NVIDIA | AMD |
|---|---|---|
| OS and kernel restrictions | Few | Radeon ROCm support limited to specific Ubuntu LTS / RHEL versions and kernels [V] |
| Breaking updates | Rare in production branches | Community reports of RDNA4 regressions after ROCm 7.x / vLLM updates [U]; version pinning recommended |
| New-hardware lag | Day-one CUDA support (Blackwell needed CUDA 12.8+) | RDNA4 compute support arrived months after launch (ROCm 6.4.1) [U] |
| Renderer coverage | All major renderers | Octane missing; Redshift Windows-only; V-Ray HIP new |
| Licence | GeForce EULA excludes "datacenter deployment"; pro cards: unverified, NVIDIA's pro-driver licence terms for datacenter use were not checked | No equivalent restriction found on Radeon/ROCm (ROCm is open source) [U: we did not review AMD's driver EULA in detail] |
| Sharing / isolation | MIG on RTX PRO 6000/5000/4500; paid vGPU on selected cards | No SR-IOV on Radeon AI PRO / W-series; time-slicing only via generic k8s means |

## 5. When AMD makes sense
- The main pain is **LLM VRAM**, and the people running it are comfortable on Linux with pinned ROCm/vLLM versions. For example, 4x R9700 give 128 GB for about 8,400 EUR, enough for 70B models with long context or several 32B replicas.
- Rendering is mostly Blender, where AMD works at lower speed, or runs on separate NVIDIA cards.
- A mixed fleet is acceptable: NVIDIA for rendering and training, AMD for inference capacity. The cost is two software stacks and two Kubernetes device plugins.

## 6. When it does not
- Octane or Linux Redshift is part of the render service.
- Fine-tuning workflows depend on CUDA-only tools or on fast bring-up of new research code.
- MIG-style isolated slices or vGPU are needed.

## 7. Intel in one paragraph
The Arc Pro B60 (24 GB, about 960 EUR) and B70 (32 GB, 949 USD MSRP, from about 1,600 EUR incl. VAT in Nov 2026) are the cheapest VRAM available. But rendering is roughly 1/4 of comparable NVIDIA cards, LLM prompt processing on Vulkan is very slow, and Intel retired IPEX-LLM in favour of its own vLLM fork. Intel officially lists SR-IOV for the B70 (4 VFs) and B50 (2 VFs); on the B60 it works in community setups only. Assessment: interesting for cheap, isolated inference experiments, not as the backbone of a render + AI service in 2026.
