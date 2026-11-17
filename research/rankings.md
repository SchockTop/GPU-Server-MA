# Rankings


Important caveats:
- Blender Open Data is user-submitted (uncontrolled systems). Medians with n<10 are noisy.
- llama.cpp tg128 is single-user token generation on a 7B 4-bit model; it mostly measures memory bandwidth and says nothing about whether a larger model fits.
- TFLOPS are spec-sheet peaks (partly derived), not measurements.
- Price/performance for multi-card packages only adds up if the work splits across cards (batch rendering: yes; one big scene or one big model: no).

## 1. Rendering: Blender Open Data 4.5.0 median (higher is better)

| # | Card | Score | n | Note | Price low | EUR per 1,000 pts |
|---|---|---|---|---|---|---|
| 1 | RTX PRO 6000 Blackwell Workstation 96GB | 16,737 | 205 | 5.2.0: 17,306 (n=19) | 17,548 | 1,048 |
| 2 | RTX PRO 6000 Blackwell Server 96GB | 15,519 | 28 | - | 20,599 | 1,327 |
| 3 | GeForce RTX 5090 32GB | 14,966 | 1555 | 5.2.0: 16,101 (n=236) | 7,829 | 523 |
| 4 | RTX PRO 6000 Blackwell Max-Q 96GB | 14,746 | 39 | 5.2.0: 15,505 (n=7) | 16,490 | 1,118 |
| 5 | GeForce RTX 4090 24GB (used) | 11,061 | 527 | - | 2,400 | 217 |
| 6 | RTX PRO 5000 Blackwell 48GB | 10,929 | 7 (!) | small n; 5.2.0: 11,691 (n=4) | 8,119 | 743 |
| 7 | RTX PRO 5000 Blackwell 72GB | 10,849 | 4 (!) | small n | 14,099 | 1,300 |
| 8 | RTX 6000 Ada 48GB | 10,655 | 20 | 5.2.0 value 2,120 (n=6) is an outlier | 9,008 | 845 |
| 9 | GeForce RTX 5080 16GB | 9,138 | 1432 | - | 2,195 | 240 |
| 10 | RTX PRO 4500 Blackwell 32GB | 8,487 | 17 | 5.2.0: 9,186 (n=5) | 4,559 | 537 |
| 11 | GeForce RTX 4080 Super 16GB | 8,419 | 239 | - | - | - |
| 12 | L40S 48GB | 7,848 | 8 (!) | all versions 9,231 (n=52) | 10,403 | 1,326 |
| 13 | GeForce RTX 5070 Ti 16GB | 7,589 | 1416 | - | 1,745 | 230 |
| 14 | RTX PRO 4000 Blackwell 24GB | 6,256 | 40 | 5.2.0: 6,786 (n=19) | 2,775 | 444 |
| 15 | GeForce RTX 5070 12GB | 6,174 | 914 | - | 1,594 | 258 |
| 16 | RTX 5000 Ada 32GB | 5,677 | 9 (!) | unreliable: all-versions median 7,655 (n=31); 5.1.0 7,783 (n=8) | 5,199 | 916 |
| 17 | RTX 4500 Ada 24GB | 5,674 | 5 (!) | small n | 2,786 | 491 |
| 18 | GeForce RTX 3090 24GB (used) | 5,412 | 630 | - | 1,250 | 231 |
| 19 | RTX A6000 48GB (used) | 5,145 | 8 (!) | all versions 5,284 (n=210) | 4,000 | 777 |
| 20 | RTX 4000 Ada 20GB | 4,446 | 16 | - | 1,940 | 436 |
| 21 | RTX A5000 24GB | 4,390 | 24 | - | 4,225 | 962 |
| 22 | GeForce RTX 5060 Ti 16GB | 4,309 | 655 | 16GB and 8GB not separable in Open Data | 909 | 211 |
| 23 | GeForce RTX 5060 Ti 8GB | 4,309 | 655 | shared device name with 16GB | - | - |
| 24 | AMD Radeon PRO W7900 48GB | 3,790 | 2 (!) | tiny n | 3,516 | 928 |
| 25 | Intel Arc Pro B70 32GB | 3,313 | 1 (!) | 4.5.0 n=1; 5.2.0: 3,802 (n=14) | - | - |
| 26 | AMD Radeon RX 9070 XT 16GB | 3,279 | 676 | HIP | 1,052 | 321 |
| 27 | AMD Radeon AI PRO R9700 32GB | 3,209 | 11 | HIP backend; 5.2.0: 3,331 (n=6) | 2,102 | 655 |
| 28 | RTX A4000 16GB | 2,956 | 44 | - | 1,964 | 664 |
| 29 | Intel Arc Pro B60 24GB | 2,133 | 5 (!) | oneAPI, small n | 960 | 450 |

Backends: NVIDIA OptiX, AMD HIP, Intel oneAPI. V-Ray, Octane and Redshift: see benchmarks.md (too few comparable absolute values for a ranking; Octane does not run on AMD/Intel).

### Rendering price/performance (EUR per 1,000 Blender points, lower is better)

| # | Card | Price low | Blender | EUR/1k pts (low) | EUR/1k pts (typical) | VRAM |
|---|---|---|---|---|---|---|
| 1 | GeForce RTX 5060 Ti 16GB | 909 | 4,309 | 211 | 220 | 16 |
| 2 | GeForce RTX 4090 24GB (used) *used* | 2,400 | 11,061 | 217 | 271 | 24 |
| 3 | GeForce RTX 5070 Ti 16GB | 1,745 | 7,589 | 230 | 233 | 16 |
| 4 | GeForce RTX 3090 24GB (used) *used* | 1,250 | 5,412 | 231 | 277 | 24 |
| 5 | GeForce RTX 5080 16GB | 2,195 | 9,138 | 240 | 246 | 16 |
| 6 | GeForce RTX 5070 12GB | 1,594 | 6,174 | 258 | - | 12 |
| 7 | AMD Radeon RX 9070 XT 16GB | 1,052 | 3,279 | 321 | - | 16 |
| 8 | RTX 4000 Ada 20GB | 1,940 | 4,446 | 436 | - | 20 |
| 9 | RTX PRO 4000 Blackwell 24GB | 2,775 | 6,256 | 444 | 488 | 24 |
| 10 | Intel Arc Pro B60 24GB | 960 | 2,133 | 450 | - | 24 |
| 11 | RTX 4500 Ada 24GB | 2,786 | 5,674 | 491 | 520 | 24 |
| 12 | GeForce RTX 5090 32GB | 7,829 | 14,966 | 523 | 601 | 32 |
| 13 | RTX PRO 4500 Blackwell 32GB | 4,559 | 8,487 | 537 | 566 | 32 |
| 14 | AMD Radeon AI PRO R9700 32GB | 2,102 | 3,209 | 655 | 686 | 32 |
| 15 | RTX A4000 16GB | 1,964 | 2,956 | 664 | - | 16 |
| 16 | RTX PRO 5000 Blackwell 48GB | 8,119 | 10,929 | 743 | 778 | 48 |
| 17 | RTX A6000 48GB (used) *used* | 4,000 | 5,145 | 777 | 875 | 48 |
| 18 | RTX 6000 Ada 48GB | 9,008 | 10,655 | 845 | 901 | 48 |
| 19 | RTX 5000 Ada 32GB | 5,199 | 5,677 | 916 | 969 | 32 |
| 20 | AMD Radeon PRO W7900 48GB | 3,516 | 3,790 | 928 | 976 | 48 |
| 21 | RTX A5000 24GB | 4,225 | 4,390 | 962 | - | 24 |
| 22 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 16,737 | 1,048 | 1,089 | 96 |
| 23 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,490 | 14,746 | 1,118 | 1,139 | 96 |
| 24 | RTX PRO 5000 Blackwell 72GB | 14,099 | 10,849 | 1,300 | 1,392 | 72 |
| 25 | L40S 48GB | 10,403 | 7,848 | 1,326 | 1,338 | 48 |
| 26 | RTX PRO 6000 Blackwell Server 96GB | 20,599 | 15,519 | 1,327 | 1,353 | 96 |

## 2. LLM inference: llama.cpp Llama-2-7B Q4_0, tg128 tokens/s (single user, higher is better)

| # | Card | tg128 t/s | pp512 t/s | VRAM | Source | EUR per t/s |
|---|---|---|---|---|---|---|
| 1 | GeForce RTX 5090 32GB | 300.4 | 14,970 | 32 | llama.cpp #15013 CUDA, FA on | 26 |
| 2 | RTX PRO 6000 Blackwell Workstation 96GB | 281.1 | 16,619 | 96 | llama.cpp #15013 CUDA, FA on | 62 |
| 3 | A100 80GB PCIe | 200.9 | 5,286 | 80 | llama.cpp #15013 CUDA, FA on | - |
| 4 | GeForce RTX 4090 24GB (used) | 189.0 | 14,771 | 24 | llama.cpp #15013 CUDA, FA on | 13 |
| 5 | GeForce RTX 5080 16GB | 184.7 | 9,488 | 16 | llama.cpp #15013 CUDA, FA on | 12 |
| 6 | GeForce RTX 5070 Ti 16GB | 182.4 | 8,420 | 16 | llama.cpp #15013 CUDA, FA on | 10 |
| 7 | RTX 6000 Ada 48GB | 179.5 | 10,577 | 48 | llama.cpp #15013 CUDA, FA on | 50 |
| 8 | RTX PRO 4500 Blackwell 32GB | 168.9 | 7,252 | 32 | llama.cpp #15013 CUDA, FA on | 27 |
| 9 | GeForce RTX 3090 24GB (used) | 161.9 | 5,560 | 24 | llama.cpp #15013 CUDA, FA on | 8 |
| 10 | AMD Radeon AI PRO R9700 32GB | 152.7 | 5,908 | 32 | llama.cpp #10879 Vulkan, FA on | 14 |
| 11 | RTX A6000 48GB (used) | 144.9 | 5,662 | 48 | llama.cpp #15013 CUDA, FA on | 28 |
| 12 | RTX PRO 4000 Blackwell 24GB | 136.4 | 5,674 | 24 | llama.cpp #15013 CUDA, FA on | 20 |
| 13 | RTX A5000 24GB | 135.8 | 4,552 | 24 | llama.cpp #15013 CUDA, FA on | 31 |
| 14 | GeForce RTX 5060 Ti 16GB | 93.5 | 4,196 | 16 | llama.cpp #15013 CUDA, FA on (PCIe x8) | 10 |
| 15 | RTX A4000 16GB | 85.2 | 2,808 | 16 | llama.cpp #15013 CUDA, FA on | 23 |
| 16 | Intel Arc Pro B60 24GB | 68.1 | 727 | 24 | llama.cpp #10879 Vulkan (headers cut, order assumed) | 14 |

Each row is one community submission (n=1 per card), different llama.cpp builds. AMD/Intel rows are Vulkan, NVIDIA rows CUDA with flash attention. For multi-user serving (vLLM batch throughput) and big models see benchmarks.md section 3: there, VRAM and bandwidth decide and the PRO 6000 / 5090 lead by a wide margin.

## 3. AI training

There is **no measured training benchmark that covers most of these cards** (see benchmarks.md section 2). The only consistent measured set (Lambda PyTorch, older software) covers 3090, A6000, 4090, 6000 Ada, A100. As a clearly labelled **proxy**, the table below ranks by spec-sheet dense FP16/BF16 tensor TFLOPS and memory bandwidth. This is not a benchmark.

| # | Card | FP16/BF16 dense TFLOPS (spec, partly D/U) | BW GB/s | VRAM | EUR per TFLOPS (low) |
|---|---|---|---|---|---|
| 1 | RTX PRO 6000 Blackwell Workstation 96GB | ~500 D | 1,792 | 96 | 35 |
| 2 | RTX PRO 6000 Blackwell Server 96GB | ~500 D | 1,597 | 96 | 41 |
| 3 | RTX PRO 6000 Blackwell Max-Q 96GB | ~439 D | 1,792 | 96 | 38 |
| 4 | GeForce RTX 5090 32GB | 419 (FP16 acc; ~210 FP32 acc) | 1,792 | 32 | 19 |
| 5 | RTX 6000 Ada 48GB | ~364 D | 960 | 48 | 25 |
| 6 | L40S 48GB | 362 | 864 | 48 | 29 |
| 7 | GeForce RTX 4090 24GB (used) | 330 (FP16 acc; ~165 FP32 acc) | 1,008 | 24 | 7 |
| 8 | A100 80GB PCIe | 312 | 1,935 | 80 | - |
| 9 | RTX 5000 Ada 32GB | 261 | 576 | 32 | 20 |
| 10 | RTX PRO 5000 Blackwell 72GB | ~258 D | 1,344 | 72 | 55 |
| 11 | RTX PRO 5000 Blackwell 48GB | ~258 D | 1,344 | 48 | 31 |
| 12 | GeForce RTX 5080 16GB | 225 (FP16 acc) | 960 | 16 | 10 |
| 13 | RTX PRO 4500 Blackwell 32GB | ~202 D | 896 | 32 | 23 |
| 14 | AMD Radeon AI PRO R9700 32GB | ~191 U | 640 | 32 | 11 |
| 15 | AMD Radeon RX 9070 XT 16GB | ~191 U | 640 | 16 | 6 |
| 16 | GeForce RTX 5070 Ti 16GB | 177 (FP16 acc) | 896 | 16 | 10 |
| 17 | RTX PRO 4000 Blackwell 24GB | ~161 D | 672 | 24 | 17 |
| 18 | RTX 4500 Ada 24GB | ~158 D | 432 | 24 | 18 |
| 19 | RTX A6000 48GB (used) | ~155 D | 768 | 48 | 26 |
| 20 | GeForce RTX 3090 24GB (used) | 142 (FP16 acc) | 936 | 24 | 9 |
| 21 | GeForce RTX 5070 12GB | 124 (FP16 acc) | 672 | 12 | 13 |
| 22 | AMD Radeon PRO W7900 48GB | ~122 U | 864 | 48 | 29 |
| 23 | RTX A5000 24GB | 111 | 768 | 24 | 38 |
| 24 | Intel Arc Pro B60 24GB | ~98 U (INT8 197 TOPS V) | 456 | 24 | 10 |
| 25 | GeForce RTX 5060 Ti 16GB | 95 (FP16 acc) | 448 | 16 | 10 |
| 26 | GeForce RTX 5060 Ti 8GB | 95 (FP16 acc) | 448 | 8 | - |
| 27 | RTX 4000 Ada 20GB | ~82 D | 360 | 20 | 24 |
| 28 | RTX A4000 16GB | 77 | 448 | 16 | 26 |

Caveat: GeForce figures are FP16-accumulate; with FP32 accumulate they halve, so for mixed-precision training a 5090 is closer to ~210 than 419. AMD/Intel values are unverified. Real training speed also depends on software (CUDA vs ROCm vs oneAPI).

## 4. EUR per GB VRAM (lower is better)

| # | Card | Price low | VRAM GB | EUR/GB (low) | EUR/GB (typical) | Memory |
|---|---|---|---|---|---|---|
| 1 | Intel Arc Pro B60 24GB | 960 | 24 | 40 | - | GDDR6 |
| 2 | GeForce RTX 3090 24GB (used) *used* | 1,250 | 24 | 52 | 62 | GDDR6X |
| 3 | GeForce RTX 5060 Ti 16GB | 909 | 16 | 57 | 59 | GDDR7 |
| 4 | AMD Radeon AI PRO R9700 32GB | 2,102 | 32 | 66 | 69 | GDDR6 |
| 5 | AMD Radeon RX 9070 XT 16GB | 1,052 | 16 | 66 | - | GDDR6 |
| 6 | AMD Radeon PRO W7900 48GB | 3,516 | 48 | 73 | 77 | GDDR6 ECC |
| 7 | RTX A6000 48GB (used) *used* | 4,000 | 48 | 83 | 94 | GDDR6 ECC |
| 8 | RTX 4000 Ada 20GB | 1,940 | 20 | 97 | - | GDDR6 ECC |
| 9 | GeForce RTX 4090 24GB (used) *used* | 2,400 | 24 | 100 | 125 | GDDR6X |
| 10 | GeForce RTX 5070 Ti 16GB | 1,745 | 16 | 109 | 111 | GDDR7 |
| 11 | RTX PRO 4000 Blackwell 24GB | 2,775 | 24 | 116 | 127 | GDDR7 ECC |
| 12 | RTX 4500 Ada 24GB | 2,786 | 24 | 116 | 123 | GDDR6 ECC |
| 13 | RTX A4000 16GB | 1,964 | 16 | 123 | - | GDDR6 |
| 14 | GeForce RTX 5070 12GB | 1,594 | 12 | 133 | - | GDDR7 |
| 15 | RTX PRO 4000 Blackwell SFF 24GB | 3,189 | 24 | 133 | 137 | GDDR7 ECC |
| 16 | GeForce RTX 5080 16GB | 2,195 | 16 | 137 | 141 | GDDR7 |
| 17 | RTX PRO 4500 Blackwell 32GB | 4,559 | 32 | 142 | 150 | GDDR7 ECC |
| 18 | RTX 5000 Ada 32GB | 5,199 | 32 | 162 | 172 | GDDR6 |
| 19 | RTX PRO 5000 Blackwell 48GB | 8,119 | 48 | 169 | 177 | GDDR7 ECC |
| 20 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,490 | 96 | 172 | 175 | GDDR7 ECC |
| 21 | RTX A5000 24GB | 4,225 | 24 | 176 | - | GDDR6 |
| 22 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 96 | 183 | 190 | GDDR7 ECC |
| 23 | RTX 6000 Ada 48GB | 9,008 | 48 | 188 | 200 | GDDR6 ECC |
| 24 | RTX PRO 5000 Blackwell 72GB | 14,099 | 72 | 196 | 210 | GDDR7 ECC |
| 25 | RTX PRO 6000 Blackwell Server 96GB | 20,599 | 96 | 215 | 219 | GDDR7 ECC |
| 26 | L40S 48GB | 10,403 | 48 | 217 | 219 | GDDR6 ECC |
| 27 | GeForce RTX 5090 32GB | 7,829 | 32 | 245 | 281 | GDDR7 |

## 5. EUR per FP32 TFLOPS (lower is better)

| # | Card | Price low | FP32 TFLOPS | EUR/TFLOPS |
|---|---|---|---|---|
| 1 | AMD Radeon RX 9070 XT 16GB | 1,052 | 48.7 | 22 |
| 2 | GeForce RTX 4090 24GB (used) *used* | 2,400 | 82.6 | 29 |
| 3 | GeForce RTX 3090 24GB (used) *used* | 1,250 | 35.6 | 35 |
| 4 | GeForce RTX 5060 Ti 16GB | 909 | 23.7 | 38 |
| 5 | GeForce RTX 5080 16GB | 2,195 | 56.3 | 39 |
| 6 | GeForce RTX 5070 Ti 16GB | 1,745 | 43.9 | 40 |
| 7 | AMD Radeon AI PRO R9700 32GB | 2,102 | 47.8 | 44 |
| 8 | GeForce RTX 5070 12GB | 1,594 | 30.9 | 52 |
| 9 | AMD Radeon PRO W7900 48GB | 3,516 | 61 | 58 |
| 10 | RTX PRO 4000 Blackwell 24GB | 2,775 | 40 | 69 |
| 11 | RTX 4500 Ada 24GB | 2,786 | 39.6 | 70 |
| 12 | RTX 4000 Ada 20GB | 1,940 | 26.7 | 73 |
| 13 | GeForce RTX 5090 32GB | 7,829 | 104.8 | 75 |
| 14 | Intel Arc Pro B60 24GB | 960 | 12.3 | 78 |
| 15 | RTX 5000 Ada 32GB | 5,199 | 65.3 | 80 |
| 16 | RTX PRO 4500 Blackwell 32GB | 4,559 | 51 | 89 |
| 17 | RTX 6000 Ada 48GB | 9,008 | 91.1 | 99 |
| 18 | RTX A4000 16GB | 1,964 | 19.2 | 102 |
| 19 | RTX A6000 48GB (used) *used* | 4,000 | 38.7 | 103 |
| 20 | L40S 48GB | 10,403 | 91.6 | 114 |
| 21 | RTX PRO 5000 Blackwell 48GB | 8,119 | 65 | 125 |
| 22 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 125 | 140 |
| 23 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,490 | 110 | 150 |
| 24 | RTX A5000 24GB | 4,225 | 27.8 | 152 |
| 25 | RTX PRO 6000 Blackwell Server 96GB | 20,599 | 120 | 172 |
| 26 | RTX PRO 5000 Blackwell 72GB | 14,099 | 65 | 217 |

FP32 TFLOPS on GeForce/AMD count dual-issue lanes; real shader throughput differs by architecture. Use this column only within one vendor generation.
