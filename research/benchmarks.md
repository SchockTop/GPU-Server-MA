# GPU benchmarks per use case

Collected 2026-11-17. Only measured values with a source; anything we calculated is marked **DERIVED**. "no data" means we looked and found nothing usable. Most sources are single runs or user-submitted data, so treat small differences (under ~10%) as noise.

Use cases covered: (1) rendering, (2) neural-network training, (3) LLM inference, (4) LLM fine-tuning memory needs.

---

## 1. Rendering

### 1.1 Blender Open Data (Cycles), median score, higher is better

Source: opendata.blender.org, via the site's own JSON query endpoint (`/benchmarks/query/?compute_type=OPTIX&blender_version=4.5.0&group_by=device_name&response_type=datatables`), accessed 2026-11-17. n = number of submitted runs. Backend: NVIDIA OptiX, AMD HIP, Intel oneAPI. 4.5.0 has the best sample sizes; 5.2.0 is the newest version.

| Card | 5.2.0 median (n) | 4.5.0 median (n) | All versions (n) |
|---|---|---|---|
| RTX PRO 6000 Blackwell WS | 17,306 (19) | 16,737 (205) | 16,782 (293) |
| GeForce RTX 5090 | 16,101 (236) | 14,966 (1,555) | 15,089 (3,353) |
| RTX PRO 6000 Server Ed. | 14,103 (10) | 15,519 (28) | 15,620 (52) |
| RTX PRO 6000 Max-Q | 15,505 (7) | 14,746 (39) | 15,121 (78) |
| GeForce RTX 4090 | 11,553 (118) | 11,061 (527) | 11,682 (9,034) |
| RTX PRO 5000 48GB | 11,691 (4) | 10,929 (7) | 11,486 (18) |
| RTX PRO 5000 72GB | 10,956 (5) | 10,849 (4) | 10,861 (9) |
| RTX 6000 Ada | 2,120 (6) outlier | 10,655 (20) | 11,056 (118) |
| RTX PRO 4500 | 9,186 (5) | 8,487 (17) | 8,651 (38) |
| GeForce RTX 5080 | 9,155 (406) | 9,138 (1,432) | 9,150 (3,890) |
| GeForce RTX 4080 Super | 8,218 (52) | 8,419 (239) | 8,419 (2,059) |
| L40S | 8,605 (1) | 7,848 (8) | 9,231 (52) |
| GeForce RTX 5070 Ti | 7,749 (272) | 7,589 (1,416) | 7,628 (3,253) |
| RTX PRO 4000 | 6,786 (19) | 6,256 (40) | 6,624 (89) |
| GeForce RTX 5070 | 5,807 (192) | 6,174 (914) | 6,105 (2,006) |
| RTX 5000 Ada | no data | 5,677 (9) | 7,655 (31) |
| RTX 4500 Ada | no data | 5,674 (5) | 5,577 (23) |
| GeForce RTX 3090 | 5,078 (114) | 5,412 (630) | 5,787 (8,221) |
| RTX A6000 | 4,641 (8) | 5,145 (8) | 5,284 (210) |
| RTX 4000 Ada | 4,439 (10) | 4,446 (16) | 4,448 (76) |
| RTX A5000 | 4,180 (13) | 4,390 (24) | 4,623 (258) |
| GeForce RTX 5060 Ti (8 and 16 GB mixed) | 4,147 (233) | 4,309 (655) | 4,305 (1,504) |
| RTX A4500 | 2,640 (3) | 3,917 (19) | 3,995 (162) |
| Radeon PRO W7900 (HIP) | 4,197 (1) | 3,790 (2) | 3,612 (24) |
| Intel Arc Pro B70 (oneAPI) | 3,802 (14) | 3,313 (1) | 3,742 (37) |
| Radeon RX 9070 XT (HIP) | 3,365 (433) | 3,279 (676) | 3,297 (1,887) |
| Radeon AI PRO R9700 (HIP) | 3,331 (6) | 3,209 (11) | 3,279 (39) |
| RTX A4000 | 2,714 (14) | 2,956 (44) | 3,118 (589) |
| Intel Arc Pro B65 (oneAPI) | 2,742 (24) | no data | 2,760 (27) |
| Intel Arc Pro B60 (oneAPI) | 2,532 (1) | 2,133 (5) | 2,219 (17) |

Caveats:
- The RTX 6000 Ada 5.2.0 value (2,120) is clearly broken; 5.1.0 shows 12,135 (n=1) and 5.0.0 shows 11,574 (n=2). Use 4.5.0.
- RTX 5000 Ada spreads widely (5,677 on 4.5.0, 7,783 on 5.1.0, 7,655 across all versions). Small n; don't trust a single number.
- Blender Open Data does not separate the RTX 5060 Ti 8 GB and 16 GB versions.
- Older Puget absolute figures (Blender 4.0 OptiX): PRO 6000 16,009, 6000 Ada 10,702, A6000 5,131 ([Puget, 2025-06](https://www.pugetsystems.com/labs/articles/nvidia-rtx-pro-6000-blackwell-workstation-content-creation-review/)). These agree with Open Data.
- AMD: Blender 5.1 turned on HIP-RT (hardware ray tracing) by default. That is reported as a 5-10% gain, which does not close the gap to OptiX.

### 1.2 V-Ray GPU

benchmark.chaos.com is a JavaScript app and returned no data. Substitutes:

| Card | V-Ray RTX | V-Ray CUDA | Setup | Source |
|---|---|---|---|---|
| RTX PRO 6000 Blackwell WS | 15,369 | 11,663 | V-Ray 6.00.01, Puget, Jun 2025 | [Puget](https://www.pugetsystems.com/labs/articles/nvidia-rtx-pro-6000-blackwell-workstation-content-creation-review/) |
| RTX 6000 Ada | 10,206 | 7,500 | same | same |
| RTX A6000 | 4,858 | 3,319 | same | same |
| RTX 5090 | 15,161 | no data | V-Ray 6.0 RTX, n=1 | [hwcooling](https://www.hwcooling.net/wp-content/uploads/2025/11/gigabyte-amd-radeon-rx-9060-xt-gaming-oc-ice-16g-gv-r906xgamingocice-16gd-test-recenze-review-vray-rtx-v1.html) |
| RTX 5080 (7 partner cards) | 9,293-9,592 | no data | same | same |
| RTX 5070 Ti (4 cards) | 7,905-8,113 | no data | same | same |
| RTX 5070 (5 cards) | 6,551-6,573 | no data | same | same |
| RTX 5060 Ti 16GB (4 cards) | 4,388-4,518 | no data | same | same |
| All other cards | no data (absolute) | | | |

Puget, relative results only ([pro roundup, 2025-12](https://www.pugetsystems.com/labs/articles/2025-professional-gpu-content-creation-roundup/)):
- PRO 5000 is about 35% faster than the 5000 Ada and 11% faster than the 6000 Ada.
- PRO 4500 is about 73% faster than the 4500 Ada.
- PRO 4000 is about 83% faster than the 4000 Ada.

AMD: V-Ray GPU on AMD came back via HIP in V-Ray 7 Update 3 for 3ds Max (April 2026). Support in other host apps and on Linux is unconfirmed.

### 1.3 OctaneBench

The OTOY results list sits behind a Cloudflare challenge (HTTP 403). We did not bypass it, so there are **no comparable absolute scores**.

Puget relative results (OctaneBench 2025.2), Blackwell over the matching Ada card: PRO 6000 +49%, PRO 5000 +58%, PRO 4500 +43%, PRO 4000 +34%. 5090 over 4090: +23%.

**Octane on Windows/Linux runs only on NVIDIA (CUDA)**; AMD and Intel are not supported.

### 1.4 Redshift

The only absolute table we found is old: [CGDirector, Redshift 3.5.24](https://www.cgdirector.com/redshift-benchmark-results), published 2024. Render time, lower is better:

| Card | Time |
|---|---|
| RTX 4090 | 1:16 |
| RTX 6000 Ada | 1:28 |
| RTX 4080 Super | 1:39 |
| RTX 3090 / RTX A6000 | 2:42 |
| RTX A5000 | 3:06 |
| Radeon PRO W7900 | 3:21 |
| RTX A4000 | 4:40 |
| 2x RTX 4090 | 0:47 |

There is no Blackwell data. Puget (Redshift 2026.2, relative): Blackwell pro cards render about 23% faster than the next-lower Ada card. Redshift supports AMD on Windows only; on Linux it supports NVIDIA only.

### 1.5 Rendering takeaways (interpretation)
- For each tier, GeForce delivers the same Cycles score for roughly a third to half the price of a pro card. The 5080 and 5070 Ti match or beat the PRO 4500 in Blender.
- The order is consistent across Blender, V-Ray and Octane: PRO 6000 ≈ 5090 > 4090 > PRO 5000 ≈ 6000 Ada > 5080 ≈ PRO 4500 > 5070 Ti > PRO 4000.
- AMD and Intel trail by a factor of 2-3 at similar prices in Blender and lose Octane completely. For a render service they are weak.
- VRAM matters for rendering only once scenes exceed the card. VRAM does not add up across cards in a render, so the largest scene must fit on one card.

---

## 2. Neural-network training (CNN / UNet / Transformer)

**The main gap:** no public measured training benchmark covers the current Blackwell cards (PRO or GeForce), L40S, A5000/A4000 or RTX 4000/5000 Ada. MLPerf Training has no workstation-card entries. Lambda's site renders its tables with JavaScript, but its raw CSVs on GitHub cover older cards only.

### 2.1 Lambda PyTorch training throughput (measured, older software stack)

Source: [lambdal/deeplearning-benchmark, pytorch-train-throughput-fp16.csv](https://raw.githubusercontent.com/lambdal/deeplearning-benchmark/master/pytorch/pytorch-train-throughput-fp16.csv): 1 GPU, mixed-precision FP16, NGC PyTorch containers. Units: images/s or sequences/s; Transformer-XL in tokens/s.

| Card | ResNet-50 | SSD | BERT-base SQuAD | BERT-large SQuAD | Transformer-XL base | Transformer-XL large |
|---|---|---|---|---|---|---|
| RTX 3090 | 905 | 236 | 172 | 52 | 22,863 | 7,821 |
| RTX A6000 | 916 | 260 | 198 | 68 | 26,030 | 11,126 |
| RTX 4090 | 1,301 | 379 | 297 | 93 | 40,427 | 14,509 |
| RTX 6000 Ada | 1,146 | 341 | 255 | 79 | 36,745 | 16,049 |
| A100 40GB PCIe | 1,396 | 395 | 368 | 117 | 35,366 | 16,034 |
| A100 80GB PCIe | 1,527 | 437 | 415 | 140 | 41,602 | 17,082 |

v2 CSV (same units): H100 PCIe ResNet-50 1,976, BERT-large 204.

DERIVED:
- The 4090 beats the 6000 Ada by 14-18% on CNN/BERT.
- The 6000 Ada wins Transformer-XL large by 10%: larger memory, and pro cards run full-rate FP32 accumulate.

### 2.2 Other training data
- [Puget SDXL LoRA training (kohya_ss, 2023)](https://www.pugetsystems.com/labs/articles/stable-diffusion-lora-training-professional-gpu-analysis/):
  - The 6000 Ada was up to 24% faster than the A6000.
  - The W7900 trailed NVIDIA by about 55%.
  - All NVIDIA cards stayed under 20 GB of VRAM; the W7900 needed about 7 GB more.
  - Absolute numbers are only in chart images.
- An unverified blog claims 5090 vs 4090 on ResNet-50 at about 3,800 vs 2,600 img/s, without stated methodology. Not used.

### 2.3 What to use instead (clearly a proxy, not a benchmark)

Training throughput mainly follows dense FP16/BF16 tensor TFLOPS, memory bandwidth and VRAM (for batch size and model size). rankings.md section 3 ranks cards by those spec-sheet values. Two caveats:
- GeForce cards run FP16 with FP32 accumulate at half rate. Pro and datacenter cards do not.
- AMD ROCm and Intel oneAPI deliver less of their peak in practice than CUDA does.

Recommendation for the reader: before buying, run your own short training benchmark, e.g. one epoch of your UNet, on a rented card (cloud GPU rental by the hour).

---

## 3. LLM inference

### 3.1 llama.cpp scoreboard: Llama-2-7B Q4_0, pp512 / tg128 tokens/s

Sources: [llama.cpp discussion #15013 (CUDA)](https://github.com/ggml-org/llama.cpp/discussions/15013) and [#10879 (Vulkan)](https://github.com/ggml-org/llama.cpp/discussions/10879). Each row is one community submission, with different builds. tg = single-user generation speed (driven mostly by memory bandwidth). pp = prompt processing (driven by compute).

| Card | Backend | pp512 | tg128 |
|---|---|---|---|
| RTX 5090 | CUDA, FA | 14,970 | 300.4 |
| RTX PRO 6000 Blackwell | CUDA, FA | 16,619 | 281.1 |
| H100 80GB (reference) | CUDA, FA | 11,263 | 280.7 |
| A100 80GB | CUDA, FA | 5,286 | 200.9 |
| RTX 4090 | CUDA, FA | 14,771 | 189.0 |
| RTX 5080 | CUDA, FA | 9,488 | 184.7 |
| RTX 5070 Ti | CUDA, FA | 8,420 | 182.4 |
| RTX 6000 Ada | CUDA, FA | 10,577 | 179.5 |
| RTX PRO 4500 Blackwell | CUDA, FA | 7,252 | 168.9 |
| RTX 3090 | CUDA, FA | 5,560 | 161.9 |
| L40 (not L40S) | CUDA, FA | 10,098 | 153.8 |
| Radeon AI PRO R9700 | Vulkan, FA | 5,908 | 152.7 |
| RTX A6000 | CUDA, FA | 5,662 | 144.9 |
| RTX PRO 4000 Blackwell | CUDA, FA | 5,674 | 136.4 |
| RTX A5000 | CUDA, FA | 4,552 | 135.8 |
| RTX 5060 Ti 16GB (PCIe x8) | CUDA, FA | 4,196 | 93.5 |
| RTX A4000 | CUDA, FA | 2,808 | 85.2 |
| Intel Arc Pro B60 | Vulkan | 727 | 68.1 |

No row for: RTX PRO 5000, RTX 5000/4000 Ada, L40S, W7900, R9700 on ROCm, B60 on SYCL. For the B60 Vulkan row, the column headers were cut off in the fetch, so the column order is assumed.

### 3.2 Bigger models and multi-user serving (vLLM / Ollama)

| Test | Result | Source |
|---|---|---|
| vLLM aggregate throughput, Qwen3-Coder-30B-A3B AWQ 4-bit, 400 concurrent, 1k in/1k out | 4090 2,259; 5090 4,570; **PRO 6000 8,425** tok/s; 4x 5090 12,744 | [CloudRift](https://www.cloudrift.ai/blog/benchmarking-rtx-gpus-for-llm-inference) |
| same, Llama-3.3-70B AWQ | PRO 6000 1,031; 2x 4090 467; 2x 5090 1,230 tok/s | same |
| vLLM online serving, conc. 32, 512/512 (Server Editions) | Ministral-14B FP8: PRO 4500 1,107, L40S 995, PRO 6000 2,283; Qwen-27B NVFP4: PRO 4500 320, L40S 480, PRO 6000 616 tok/s | [StorageReview, PRO 4500 Server Ed.](https://www.storagereview.com/review/nvidia-rtx-pro-4500-blackwell-server-edition-review) |
| Ollama Q4_K_M single user, PRO 4000 vs PRO 5000 48GB | 8B: 98.9 vs 91.1; 14B: 57.8 vs 54.7; **32B: 5.3 (spills to CPU) vs 27.8**; 72B: does not fit vs 12.1 (8k ctx) tok/s | [ComputingForGeeks](https://computingforgeeks.com/rtx-pro-4000-vs-rtx-pro-5000-blackwell-local-ai-benchmarks/) |
| PRO 6000 context sweep (llama.cpp, Q4_K, 4k ctx tg) | Qwen3-32B 54.9; Llama-3.3-70B 32.0; gpt-oss-120B MXFP4 210; Mistral-123B 19.1 tok/s | [hardware-corner](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-pro-6000-blackwell/) |
| R9700 single, vLLM ROCm FP16, conc. 1/4/8 | Llama-3.1-8B 29.1 / 102 / 153 tok/s; dual R9700 TP=2 Qwen-27B FP8 tuned: 62.8 / 186 / 320 | [Puget R9700](https://www.pugetsystems.com/labs/articles/amd-radeon-ai-pro-r9700-dual-gpu-ai-inference-performance/) |
| R9700 vs 5090 | 5090 "almost four times faster" at peak on a 27B dense model | [ServeTheHome](https://www.servethehome.com/asrock-creator-radeon-ai-pro-r9700-review-workstation-inference-amd-style/2/) |
| PRO 5000 Server Ed. 48GB, vLLM, 50 prompts, 100/600 | Llama-3.1-8B FP16 2,114; Qwen3-14B FP16 1,251 tok/s (vendor data) | [Databasemart](https://www.databasemart.com/blog/vllm-gpu-benchmark-pro5000) |

Takeaways (interpretation):
- **For single-user speed, bandwidth wins:** 5090 ≈ PRO 6000 > 4090 ≈ 5080 ≈ 5070 Ti ≈ 6000 Ada > PRO 4500.
- **Capacity is set by VRAM.** A model that spills to the CPU drops to around a tenth of its speed (the PRO 4000 on 32B). That is why the VRAM pain point matters more than raw speed.
- **Multi-user serving** (batching in vLLM) rewards VRAM, which leaves room for the KV cache, and bandwidth. On a 30B MoE model, one PRO 6000 does about 1.8x one 5090.
- **Splitting across cards:** without NVLink, tensor parallelism across PCIe cards is slow. For inference, several replicas or pipeline parallelism work better. GeForce cards also lack official P2P.

### 3.3 Which model fits in which VRAM (DERIVED rule of thumb)

Weights ≈ parameters × bytes per parameter: FP16 = 2.0, Q8 ≈ 1.06, Q4_K_M ≈ 0.6. On top of that comes the KV cache:
- Llama-3-8B: about 1 GB per 8k tokens.
- Llama-3-70B: about 2.5 GB per 8k tokens.

Add 1-2 GB of runtime overhead.

| VRAM | FP16 | 8-bit | 4-bit | Measured anchors |
|---|---|---|---|---|
| 8 GB | ~3B | ~7B (tight) | 7-8B | |
| 16 GB | ~7B | 13-14B | 20-24B (14B at long context) | |
| 24 GB | 8B with long ctx, ~11B max | ~20B | 32B only with short context | 32B Q4 at 32k ctx spilled on a 24 GB card |
| 32 GB | ~14B | 27-30B | 32-40B comfortable | |
| 48 GB | ~20B | ~40B | 70B at ~8k context | 72B Q4: 1 layer spilled at 8k, 12 of 81 layers at 32k |
| 72 GB | ~32B | 60-65B | 70B at 32k+, MoE up to ~100B | |
| 96 GB | ~40B | 80-90B | 70B at 128k; 106-123B | Llama-70B Q4 at 128k and Mistral-123B Q4 at 64k ran on a 96 GB card |

MoE models (e.g. gpt-oss-120B, Qwen3-30B-A3B) need the full weights in memory but generate much faster than dense models of the same size.

---

## 4. LLM training and fine-tuning: VRAM needs

### 4.1 QLoRA / LoRA minimums

Source: [Unsloth requirements](https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements). Unsloth calls these the absolute minimum at batch 1-3 and short sequences. Add 20-50% for realistic sequence lengths.

| Model | QLoRA 4-bit | LoRA 16-bit |
|---|---|---|
| 7-8B | 5-6 GB | 19-22 GB |
| 14B | 8.5 GB | 33 GB |
| 27B | 22 GB | 64 GB |
| 32B | 26 GB | 76 GB |
| 70B | 41 GB | 164 GB |

### 4.2 Full fine-tune

Source: [Hugging Face, model memory anatomy](https://huggingface.co/docs/transformers/model_memory_anatomy). Mixed-precision AdamW needs about **18 bytes per parameter**, plus activations: 6 for weights, 8 for optimizer states, 4 for gradients. 8-bit Adam brings that to about 12 bytes per parameter.

DERIVED:

| Model | Memory (excl. activations) | Fits on one card? |
|---|---|---|
| 1B | ~18 GB | yes (24-32 GB card) |
| 3B | ~54 GB | only on a 72-96 GB card |
| 7-8B | ~126-144 GB | no single card here: needs FSDP/ZeRO sharding over several cards, CPU offload, or 8-bit Adam plus 96 GB |

### 4.3 Which cards are realistic
| Goal | Minimum card class |
|---|---|
| QLoRA of 7-14B models | 16-24 GB cards |
| QLoRA of 32B | 32 GB (tight) or 48 GB |
| QLoRA of 70B | 48 GB minimum; 72-96 GB comfortable |
| LoRA 16-bit of 8B | 24-32 GB |
| LoRA 16-bit of 14B | 48 GB |
| Full fine-tuning above ~1-3B | multiple large cards or rented datacenter GPUs |
| UNet/CNN and small-to-mid Transformer training | 16-32 GB is usually enough; more VRAM allows larger batches and resolutions |

---

## 5. Sources that failed or were not usable
- OctaneBench results (Cloudflare 403, not bypassed).
- benchmark.chaos.com (V-Ray): JavaScript app with no data.
- Lambda benchmark page: JavaScript-rendered; we used its GitHub CSVs instead.
- LocalScore (404 on the URL tried).
- Puget absolute numbers: chart images only, not readable as text.
- MLPerf Training: no workstation cards.
- TechPowerUp: 403.
- No measured training numbers for any Blackwell card.
- No llama.cpp rows for PRO 5000, L40S, 4000/5000 Ada, ROCm or SYCL.
