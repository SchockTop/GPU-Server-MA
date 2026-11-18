# Training-speed benchmarks beyond the five we already had (research date 2026-11-18)

Question: which public benchmarks measure deep-learning TRAINING (not inference) on single GPUs, and which cover many of the 34 cards on the list with one consistent method?

Evidence labels: RAW = seen in the raw page or raw JSON fetched with curl. IMG = number printed on a chart image that I opened and read (not text). SUM = summary tool. U = search snippet or secondary text only, not verified. Every measured value is in `training-extra.csv` (96 rows). Already-known sources (Exxact, Lambda, Bizon, nikolasent, ROCm/TheRock issue) are not repeated.

The 34 cards of the list, counting each variant separately: A5000, 5000 Ada, A4000, 5060 Ti (16GB, 8GB = 2), PRO 6000 (Workstation, Max-Q, Server = 3), PRO 5000 (48GB, 72GB = 2), PRO 4500, PRO 4000 (24GB, SFF = 2), 6000 Ada, 4500 Ada, 4000 Ada, L40S, A100 80GB PCIe, 5090, 5080, 5070 Ti, 5070, 4080 Super, R9700, AMD Radeon PRO W7900 48GB, RX 9070 XT, Arc Pro B50/B60/B65/B70 (4), Arc Pro B60 Dual 48GB (Maxsun), B580, B570, A770.

## Short answer

Is there one training benchmark that covers most of our cards with one method? No. The best is the AIME "Deep Learning GPU Benchmarks" page (aime.info): one method (PyTorch, BERT Large and ResNet-50, fp32 and fp16 AMP, eager and torch.compile), by one lab, updated November 2025. It has values for 11 of the 34 cards (A5000, 5000 Ada, 6000 Ada, 4500 Ada, L40S, 5090, PRO 6000 x3, PRO 5000 48GB, PRO 4500). It has nothing for all AMD and Intel cards, nothing for the RTX 50-series below the 5090, nothing for 4000/4080 Super/A4000/PRO 4000/PRO 5000 72GB. No other source I found is wider. Everything else is either inference-only, covers 1 to 4 of our cards, or is blocked to automated access.

## 1. AIME Deep Learning GPU Benchmarks (best coverage)

- URL: https://www.aime.info/blog/en/deep-learning-gpu-benchmarks/ ; data files (RAW): https://www.aime.info/data/blog/DL_GPU_Benchmarks/bar_single_gpus_bert_pytorch.json and .../bar_single_gpus_resnet50_pytorch.json (HTTP Last-Modified 2025-11-16). The page text is RAW; the numbers live in these JSON files that the page's chart script loads, so they are not visible in the page HTML.
- Who: AIME GmbH (hardware vendor/seller of the GPU servers and workstations), measured in their own lab. Vendor-run, not crowd-sourced. Scripts public: https://github.com/aime-team/pytorch-benchmarks (not opened).
- What is trained: BERT Large cased (335M params) and ResNet-50 v1.5, PyTorch, synthetic random data (no data-loader effect), 50 steps, average of 3 runs, GPUs started below 50 C.
- Precision: fp32 and fp16 AMP (two tabs). Each with and without torch.compile.
- Batch size: chosen per card to fill VRAM (e.g. BERT fp32 bs 24 on 5090, bs 82 on PRO 6000). So the batch size differs between cards; scores are "best fit" throughput, not equal-batch.
- Software: PyTorch 2.5.1 on Ampere/Ada/Hopper (CUDA 12.4), PyTorch 2.7.0 on Blackwell cards (CUDA 12.8), PyTorch 2.8.0 on PRO 5000. So software version differs by generation, which favours newer cards slightly.
- Unit: BERT Large "processed sequences per second" (sequence length not stated in the text I read); ResNet-50 "processed images per second".
- Platform: EPYC 9354 server (server cards) or Threadripper PRO 7975WX workstation (workstation-only cards), 256 GB DDR5.
- Recency: Nov 2025; includes cards up to PRO 5000 Blackwell and PRO 6000 Blackwell, H200.
- Our cards with values (RAW): RTX A5000 24GB, RTX 5000 Ada 32GB, RTX 6000 Ada 48GB, RTX 4500 Ada 24GB, L40S 48GB, GeForce RTX 5090 32GB, RTX PRO 6000 Blackwell Workstation / Server / Max-Q 96GB, RTX PRO 5000 Blackwell 48GB, RTX PRO 4500 Blackwell 32GB. Total 11 of 34.
- Not covered: A4000, 4000 Ada, PRO 4000 (24GB and SFF), PRO 5000 72GB, 5060 Ti (16GB and 8GB), 5070, 5070 Ti, 5080, 4080 Super, all AMD (page has only MI100), all Intel. The page also lists RTX 4060 Ti 16GB, 4090, 3090, A6000, H100, H200, which are not on our list but useful as bridges, and an A100 whose variant is not in `training-extra.csv`, so the A100 80GB PCIe is not counted.
- Example values (ResNet-50 fp32 compile, images/s): PRO 6000 Server 1494, 5090 1361, PRO 6000 Max-Q 1260, PRO 5000 48GB 1079, 6000 Ada 951, L40S 947, PRO 4500 678, 5000 Ada 612, A5000 604, 4500 Ada 380. BERT Large fp16 compile (sequences/s): PRO 6000 220, 5090 134, PRO 5000 133, 6000 Ada 115, L40S 107, PRO 4500 92, 5000 Ada 79, A5000 50, 4500 Ada 48.
- Strengths: one method for 11 cards, current generations, both precisions, public scripts, raw data in a machine-readable file.
- Weaknesses and warnings: vendor measurement; two models only; batch sizes and PyTorch versions differ by card; PRO 6000 Workstation and Server have identical numbers in every chart (probably one measurement reused, treat as one value); RTX 4500 Ada looks low relative to the 5000 Ada in ResNet fp32 (279 vs 464), which I cannot explain; the RTX 5090 BERT fp32 eager (39) is higher than PRO 4500 and close to PRO 5000, so the BERT fp32 eager column is odd for some cards (cause unknown); no power limit noted. No AMD/Intel coverage. Compare within a column only.
- Trust: medium to good. Transparent method and scripts, but single lab and some irregularities. Good for ranking the 11 cards; do not mix with Exxact numbers (different batch size and software).
- Companion page: https://www.aime.info/blog/en/pytorch-2-gpu-performace-benchmark-comparison/ (older PyTorch-version study, same two models; read as text, no extra cards of ours noted).

## 2. Puget Systems SDXL LoRA training (professional GPUs)

- URL: https://www.pugetsystems.com/labs/articles/stable-diffusion-lora-training-professional-gpu-analysis/ ; chart (IMG): https://wp-cdn.pugetsystems.com/2022/08/SDXL-LoRA-Training-Performance-SDPA.png
- Who: Puget Systems (workstation vendor), own lab, Threadripper PRO 5995WX, Ubuntu 22.04.3.
- What: SDXL LoRA with kohya_ss v22.2.1, 13 images at 1024x1024, Adafactor, unet only, batch size 1, 520 steps, SDPA attention (also an xFormers chart for NVIDIA), network dimension 1/8/64/128/256. PyTorch 2.1.0 + CUDA 12.1 (NVIDIA) and PyTorch 2.1.1 + ROCm 5.6 (AMD). Precision not stated. Unit: iterations per second.
- Date: 12 Dec 2023, updated 19 Dec 2023. Page itself warns it is probably out of date.
- Our cards (IMG, values printed on the bars): RTX 6000 Ada 48GB (1.80 it/s at dim 8, 1.73 at dim 128), RTX 5000 Ada 32GB (1.81, 1.70), RTX A5000 24GB (1.37, 1.30), Radeon PRO W7900 48GB (1.16, 1.10; poor 0.807 at dim 1). 4 of 30. Also has RTX A6000 (not ours).
- Strengths: the only independent-looking AMD vs NVIDIA training number for the W7900; a real fine-tuning workload; VRAM usage chart (NVIDIA under 20 GB, W7900 about 7 GB more).
- Weaknesses: 2023 software, none of the Blackwell cards, only 4 of ours. A separate consumer-GPU article exists (https://www.pugetsystems.com/labs/articles/stable-diffusion-lora-training-consumer-gpu-analysis/, U: 2023, no card of ours expected) but I did not open it. Puget's newer RTX 5090/5080 AI review (https://pugetsystems.com/labs/articles/nvidia-geforce-rtx-5090-amp-5080-ai-review) returned HTTP 403 to curl, so it is a gap; the search snippet suggests it is SD.Next image generation, i.e. inference (U). Puget's 2025 engineering roundup (https://www.pugetsystems.com/labs/articles/2025-professional-gpu-engineering-roundup/, RAW) lists the PRO Blackwell cards but its text has no training or PyTorch tests.
- Trust: good method, old.

## 3. MLPerf Training (MLCommons)

- URLs: https://mlcommons.org/benchmarks/training/ (403 to curl, gap); coverage via https://nebius.com/blog/posts/mlperf-training-v6-0-results, https://www.spheron.network/blog/mlperf-training-v6-0-results-what-they-mean-for-gpu-buyers-2/ (RAW text, secondary), search results (U).
- Who: MLCommons, vendor-submitted and peer-reviewed (strongest governance of all sources).
- Latest: v6.0 published 16 June 2026 (24 submitters, 13 accelerators). v5.1 Nov 2025. Workloads: Llama 3.1 8B/405B, DeepSeek-V3 (new in v6.0), GPT-OSS-20B (single node), Flux/Stable Diffusion-class and others; unit time-to-train in minutes.
- Our cards: none found (U). Submissions are NVIDIA GB200/GB300/B200/B300/H100/H200 and AMD MI325X/MI355X, run at node or rack scale. RTX PRO 6000 Blackwell Server appears in MLPerf INFERENCE (v5.1, HPE), not training. 0 of 30. I could not read the official result table (blocked), so "none" is based on secondary coverage.
- Verdict: useful for credibility, useless for choosing our cards.

## 4. AI Benchmark (ETH Zurich), desktop GPU ranking

- URLs (RAW): https://ai-benchmark.com/ranking_deeplearning.html and .../ranking_deeplearning_detailed.html
- Who: A. Ignatov, crowd-submitted results of the AI Benchmark pip package (TensorFlow). Separate "Inference score", "Training score", and combined AI-Score. Detailed page lists per-network train ms (MobileNet-V2, Inception, ResNet, VGG, U-Net, LSTM, GNMT etc.).
- Recency: table is frozen at the TensorFlow 2.1/CUDA 10.1 era. Newest GPUs are Turing (RTX 2080 Ti, Titan RTX, Quadro RTX 8000) and Radeon VII, Tesla V100. Page footer says copyright 2018-2026 but there are no Ampere, Ada or Blackwell entries.
- Our cards: 0 of 34.
- Verdict: dead for our purpose; only valid as historical context.

## 5. Phoronix Test Suite / OpenBenchmarking.org (PyTorch, TensorFlow profiles)

- URLs: https://openbenchmarking.org/test/pts/pytorch and /pts/tensorflow (403 to curl, gap). Phoronix's R9700 review (https://www.phoronix.com/review/amd-radeon-ai-pro-r9700) also 403.
- From search results only (U): PTS has a TensorFlow profile (tf_cnn_benchmarks.py) and a PyTorch profile (ResNet-50, batch sizes, CUDA GPU device). To my knowledge the PyTorch profile measures inference and the TensorFlow one is mostly used for inference/CNN throughput on CPU; I could not confirm training. Phoronix's R9700 coverage (vLLM, OpenCL) is inference/compute.
- Crowd-sourced uploads exist (anyone can upload), but GPU coverage per card is thin and method varies by uploader.
- Our cards: unverified, effectively 0 verified training values.

## 6. Inference-only benchmarks (state clearly: NOT training)

- Geekbench AI (Primate Labs): inference only (accuracy and throughput for single-precision, half, quantized). Page returned 403 to curl, classification from product definition (U).
- UL Procyon AI Computer Vision / AI Image Generation / AI Text Generation: inference only; the Computer Vision page says "measures both inference performance and output quality" (RAW, https://benchmarks.ul.com/procyon/ai-inference-benchmark, the Android/NNAPI page). Tom's Hardware and ComputerBase AI pages use Procyon, Stable Diffusion and LLM generation: inference.
- PassMark: GPU compute tests, not DL training.
- MLPerf Client / MLPerf Inference: inference.
- Trooper.AI fleet benchmarks (https://www.trooper.ai/benchmarks-compare-RTX-Pro-4000-Blackwell-with-RTX-Pro-5000-Blackwell, RAW): 28 automatic tests from a rental fleet (vLLM, Ollama, image generation, vision). All inference. Wide Blackwell pro coverage (PRO 4000, 5000, 6000, 5090) but no training.
- CloudRift, RunPod, VRLA Tech, Level1Techs R9700 thread: inference or opinion; the Level1Techs R9700 thread (RAW) contains no training numbers (one user asks for YOLO epoch times).
- Intel Arc Pro B50/B60/B70: Intel's relative-performance sheet, StorageReview, IgorsLab report inference and vendor claims only; no training throughput found (U).

## 7. Other training-adjacent sources (single card or relative only)

- Kaitchup, RTX PRO 6000 vs H100 vs A100 (https://kaitchup.substack.com/p/faster-and-cheaper-than-the-h100, RAW): Qwen3-8B full, LoRA and QLoRA fine-tuning, same batch size, gradient checkpointing, PyTorch 2.8 nightly, RunPod cloud, Aug 2025. Only relative result in text: RTX PRO 6000 about 10% faster than H100 PCIe/NVL and nearly 50% faster than A100. No absolute number in the text, so no CSV row. Covers 1 of our cards (PRO 6000, edition not stated). Earlier Kaitchup RTX 5090 article (Mar 2025) is paywalled (U).
- Spheron RTX PRO 6000 training case study (https://www.spheron.network/blog/h100-vs-rtx-pro-6000-blackwell-fine-tuning-benchmark-2026/, RAW): explicitly says it has no own timed RTX PRO 6000 run; relies on Exxact and Kaitchup. Not an independent source.
- Vast.ai DLPerf: a proprietary score "predicting iterations/s for typical deep learning tasks such as training ResNet-50", measured on marketplace hosts (https://docs.vast.ai/guides/reference/faq/rental-types, U via search). Wide GPU coverage in principle, but I found no public per-card table (offers are behind the platform), and the score mixes in host quality. Not usable as a source here.
- NVIDIA DeepLearningExamples performance tables, AMD ROCm performance results (https://amd.com/en/developer/resources/rocm-hub/ai-cloud-development/performance-results.html), Intel launch material: vendor numbers, datacenter cards (A100/H100/MI300-class) only; not opened in depth (U). Mark any use as vendor.
- gigagpu.com GPU-hosting blog pages claim fine-tune throughput for many cards (e.g. RTX 5060 Ti 16GB); page blocked (403) and a hosting-vendor blog with unknown method; not used (U).
- Bizon, SabrePC, Lambda: Lambda and Bizon already in the CSV. Bizon's newer comparison pages for RTX PRO 6000 vs PRO 5000 72GB showed "n/a" for ResNet-50 in the search snippet (U). SabrePC: nothing found in search.
- Academic comparisons of these 2025 cards: none found in my searches.

## Coverage matrix (our cards with at least one measured training value in these new sources)

| Card | AIME | Puget SDXL LoRA | Other |
|---|---|---|---|
| RTX A5000 24GB | yes | yes | - |
| RTX 5000 Ada 32GB | yes | yes | - |
| RTX A4000 16GB | no | no | - |
| RTX 5060 Ti 16GB and 8GB | no | no | - |
| RTX PRO 6000 Blackwell Workstation | yes | no | Kaitchup relative only (edition unclear) |
| RTX PRO 6000 Blackwell Max-Q | yes | no | - |
| RTX PRO 6000 Blackwell Server | yes (identical to WS) | no | - |
| RTX PRO 5000 Blackwell 48GB | yes | no | - |
| RTX PRO 5000 Blackwell 72GB | no | no | - |
| RTX PRO 4500 Blackwell 32GB | yes | no | - |
| RTX PRO 4000 Blackwell 24GB and SFF | no | no | - |
| RTX 6000 Ada 48GB | yes | yes | - |
| RTX 4500 Ada 24GB | yes | no | - |
| RTX 4000 Ada 20GB | no | no | - |
| A100 80GB PCIe | no | no | - |
| L40S 48GB | yes | no | - |
| GeForce RTX 5090 32GB | yes | no | - |
| RTX 5080, 5070 Ti, 5070, 4080 Super | no | no | - |
| AMD Radeon PRO W7900 48GB | no | yes | - |
| Radeon AI PRO R9700, RX 9070 XT | no | no | - |
| Intel Arc Pro B50/B60/B65/B70, B60 Dual 48GB, B580, B570, A770 | no | no | - |

Counts (from `training-extra.csv` and the master CSV): AIME 11 of 34 cards; Puget 4 of 34; union 12 of 34 (W7900 is the only addition from Puget). No new training value for 22 cards: A4000, 5060 Ti 16GB and 8GB, PRO 5000 72GB, PRO 4000 and SFF, 4000 Ada, A100 80GB PCIe, 5080, 5070 Ti, 5070, 4080 Super, R9700, RX 9070 XT, B50, B60, B60 Dual, B65, B70, B580, B570, A770. (`training-bench.csv` already has partial values for a few of these, e.g. A4000 and A100 via Bizon and Lambda, 5070/5070 Ti/9070 XT via the TheRock issue. Counting both CSVs, 17 of the 34 cards have no training value at all.)

## Gaps and blocked sites

- Blocked to automated access (HTTP 403 with curl, not bypassed): mlcommons.org training results, openbenchmarking.org profile pages, phoronix.com, geekbench.com, pugetsystems.com 5090/5080 review, gigagpu.com. Their content is unverified.
- No benchmark found at all with training numbers for: Intel Arc (any), Radeon AI PRO R9700, RX 9070 XT (besides the TheRock issue), RTX 5080, RTX 5060 Ti, PRO 4000 Blackwell, RTX 4000 Ada, PRO 5000 72GB.
- Practical consequence: for the 22 cards without a new value the only consistent route is our own run of one fixed script (for example the AIME scripts, ResNet-50 and BERT Large, fp16 AMP and fp32, same PyTorch version, equal batch size) on each card, or scaling estimates from memory bandwidth and tensor throughput clearly marked as estimates.
