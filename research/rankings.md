# Rankings

New hardware only; used cards are not listed.

Prices and facts re-checked at the sources on 18 Nov 2026.

Important caveats:
- Blender Open Data is user-submitted (uncontrolled systems). Medians with n<10 are noisy.
- llama.cpp tg128 is single-user token generation on a 7B 4-bit model; it mostly measures memory bandwidth and says nothing about whether a larger model fits.
- TFLOPS are spec-sheet peaks (partly derived), not measurements.
- Price/performance for multi-card packages only adds up if the work splits across cards (batch rendering: yes; one big scene or one big model: no).

## 1. Rendering: Blender Open Data 4.5.0 median (higher is better)

| # | Card | Score | n | Note | Price low | EUR per 1,000 pts |
|---|---|---|---|---|---|---|
| 1 | RTX PRO 6000 Blackwell Workstation 96GB | 16,737 | 205 | 5.2.0: 17,306 (n=19) | 17,548 | 1,048 |
| 2 | RTX PRO 6000 Blackwell Server 96GB | 15,519 | 28 | - | 20,645 | 1,330 |
| 3 | GeForce RTX 5090 32GB | 14,966 | 1555 | 5.2.0: 16,101 (n=236) | 7,829 | 523 |
| 4 | RTX PRO 6000 Blackwell Max-Q 96GB | 14,960 | 33 | 5.2.0: 15,505 (n=7) | 16,199 | 1,083 |
| 5 | RTX PRO 5000 Blackwell 48GB | 10,929 | 7 (!) | small n; 5.2.0: 11,691 (n=4) | 8,119 | 743 |
| 6 | RTX PRO 5000 Blackwell 72GB | 10,849 | 4 (!) | small n | 12,624 | 1,164 |
| 7 | RTX 6000 Ada 48GB | 10,655 | 20 | 5.2.0 value 2,120 (n=6) is an outlier | 9,592 | 900 |
| 8 | GeForce RTX 5080 16GB | 9,138 | 1432 | - | 1,969 | 215 |
| 9 | RTX PRO 4500 Blackwell 32GB | 8,487 | 17 | 5.2.0: 9,186 (n=5) | 4,549 | 536 |
| 10 | GeForce RTX 4080 Super 16GB | 8,419 | 239 | - | 2,708 | 322 |
| 11 | L40S 48GB | 7,848 | 8 (!) | all versions 9,231 (n=52) | 10,403 | 1,326 |
| 12 | GeForce RTX 5070 Ti 16GB | 7,589 | 1416 | - | 1,399 | 184 |
| 13 | RTX PRO 4000 Blackwell 24GB | 6,256 | 40 | 5.2.0: 6,786 (n=19) | 2,819 | 451 |
| 14 | GeForce RTX 5070 12GB | 6,174 | 914 | - | 929 | 150 |
| 15 | RTX 5000 Ada 32GB | 5,677 | 9 (!) | unreliable: all-versions median 7,655 (n=31); 5.1.0 7,783 (n=8) | 4,710 | 830 |
| 16 | RTX 4500 Ada 24GB | 5,674 | 5 (!) | small n | 2,786 | 491 |
| 17 | RTX PRO 4000 Blackwell SFF 24GB | 4,718 | 8 (!) | small sample (n=8) | 3,260 | 691 |
| 18 | RTX 4000 Ada 20GB | 4,446 | 16 | - | 1,940 | 436 |
| 19 | RTX A5000 24GB | 4,390 | 24 | - | 4,225 | 962 |
| 20 | GeForce RTX 5060 Ti 16GB | 4,309 | 655 | 16GB and 8GB not separable in Open Data | 799 | 185 |
| 21 | GeForce RTX 5060 Ti 8GB | 4,309 | 655 | shared device name with 16GB | 520 | 121 |
| 22 | AMD Radeon PRO W7900 48GB | 3,790 | 2 (!) | tiny n | 3,516 | 928 |
| 23 | Intel Arc Pro B70 32GB | 3,313 | 1 (!) | 4.5.0 n=1; 5.2.0: 3,802 (n=14) | 1,599 | 483 |
| 24 | AMD Radeon RX 9070 XT 16GB | 3,279 | 676 | HIP | 949 | 289 |
| 25 | AMD Radeon AI PRO R9700 32GB | 3,209 | 11 | HIP backend; 5.2.0: 3,331 (n=6) | 2,102 | 655 |
| 26 | RTX A4000 16GB | 2,956 | 44 | - | 1,964 | 664 |
| 27 | Intel Arc A770 16GB | 2,448 | 55 | 4.5.0; 5.1.0: 2,609 (n=14); 5.2.0: 2,491 (n=8) | 304 | 124 |
| 28 | Intel Arc B580 12GB | 2,373 | 124 | 4.5.0; 5.2.0: 2,842 (n=24) | 387 | 163 |
| 29 | Intel Arc Pro B60 24GB | 2,133 | 5 (!) | oneAPI, small n | 960 | 450 |
| 30 | Intel Arc B570 10GB | 1,853 | 7 (!) | 4.5.0; 5.2.0: 2,208 (n=6) | 299 | 161 |
| 31 | Intel Arc Pro B50 16GB | 1,546 | 10 | 4.5.0; 5.2.0: 1,834 (n=5) | 569 | 368 |

Backends: NVIDIA OptiX, AMD HIP, Intel oneAPI. V-Ray, Octane and Redshift: see benchmarks.md (too few comparable absolute values for a ranking; Octane does not run on AMD/Intel).

### Rendering price/performance (EUR per 1,000 Blender points, lower is better)

| # | Card | Price low | Blender | EUR/1k pts (low) | EUR/1k pts (typical) | VRAM |
|---|---|---|---|---|---|---|
| 1 | GeForce RTX 5060 Ti 8GB | 520 | 4,309 | 121 | - | 8 |
| 2 | Intel Arc A770 16GB | 304 | 2,448 | 124 | - | 16 |
| 3 | GeForce RTX 5070 12GB | 929 | 6,174 | 150 | - | 12 |
| 4 | Intel Arc B570 10GB | 299 | 1,853 | 161 | - | 10 |
| 5 | Intel Arc B580 12GB | 387 | 2,373 | 163 | - | 12 |
| 6 | GeForce RTX 5070 Ti 16GB | 1,399 | 7,589 | 184 | - | 16 |
| 7 | GeForce RTX 5060 Ti 16GB | 799 | 4,309 | 185 | - | 16 |
| 8 | GeForce RTX 5080 16GB | 1,969 | 9,138 | 215 | 246 | 16 |
| 9 | AMD Radeon RX 9070 XT 16GB | 949 | 3,279 | 289 | - | 16 |
| 10 | GeForce RTX 4080 Super 16GB | 2,708 | 8,419 | 322 | - | 16 |
| 11 | Intel Arc Pro B50 16GB | 569 | 1,546 | 368 | 349 | 16 |
| 12 | RTX 4000 Ada 20GB | 1,940 | 4,446 | 436 | - | 20 |
| 13 | Intel Arc Pro B60 24GB | 960 | 2,133 | 450 | - | 24 |
| 14 | RTX PRO 4000 Blackwell 24GB | 2,819 | 6,256 | 451 | 488 | 24 |
| 15 | Intel Arc Pro B70 32GB | 1,599 | 3,313 | 483 | 477 | 32 |
| 16 | RTX 4500 Ada 24GB | 2,786 | 5,674 | 491 | 520 | 24 |
| 17 | GeForce RTX 5090 32GB | 7,829 | 14,966 | 523 | 601 | 32 |
| 18 | RTX PRO 4500 Blackwell 32GB | 4,549 | 8,487 | 536 | 566 | 32 |
| 19 | AMD Radeon AI PRO R9700 32GB | 2,102 | 3,209 | 655 | 505 | 32 |
| 20 | RTX A4000 16GB | 1,964 | 2,956 | 664 | - | 16 |
| 21 | RTX PRO 4000 Blackwell SFF 24GB | 3,260 | 4,718 | 691 | 697 | 24 |
| 22 | RTX PRO 5000 Blackwell 48GB | 8,119 | 10,929 | 743 | 778 | 48 |
| 23 | RTX 5000 Ada 32GB | 4,710 | 5,677 | 830 | - | 32 |
| 24 | RTX 6000 Ada 48GB | 9,592 | 10,655 | 900 | 901 | 48 |
| 25 | AMD Radeon PRO W7900 48GB | 3,516 | 3,790 | 928 | 976 | 48 |
| 26 | RTX A5000 24GB | 4,225 | 4,390 | 962 | - | 24 |
| 27 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 16,737 | 1,048 | 1,089 | 96 |
| 28 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,199 | 14,960 | 1,083 | 1,123 | 96 |
| 29 | RTX PRO 5000 Blackwell 72GB | 12,624 | 10,849 | 1,164 | 1,392 | 72 |
| 30 | L40S 48GB | 10,403 | 7,848 | 1,326 | 1,338 | 48 |
| 31 | RTX PRO 6000 Blackwell Server 96GB | 20,645 | 15,519 | 1,330 | 1,353 | 96 |

The RTX 5060 Ti 8GB row uses the Blender score shared with the 16GB card (Open Data does not separate them).

## 2. LLM inference: llama.cpp Llama-2-7B Q4_0, tg128 tokens/s (single user, higher is better)

| # | Card | tg128 t/s | pp512 t/s | VRAM | Source | EUR per t/s |
|---|---|---|---|---|---|---|
| 1 | GeForce RTX 5090 32GB | 300.4 | 14,970 | 32 | llama.cpp #15013 CUDA, FA on | 26 |
| 2 | RTX PRO 6000 Blackwell Workstation 96GB | 281.1 | 16,619 | 96 | llama.cpp #15013 CUDA, FA on | 62 |
| 3 | A100 80GB PCIe | 200.9 | 5,286 | 80 | llama.cpp #15013 CUDA, FA on | - |
| 4 | GeForce RTX 5080 16GB | 184.7 | 9,488 | 16 | llama.cpp #15013 CUDA, FA on | 11 |
| 5 | GeForce RTX 5070 Ti 16GB | 182.4 | 8,420 | 16 | llama.cpp #15013 CUDA, FA on | 8 |
| 6 | RTX 6000 Ada 48GB | 179.5 | 10,577 | 48 | llama.cpp #15013 CUDA, FA on | 53 |
| 7 | RTX PRO 4500 Blackwell 32GB | 168.9 | 7,252 | 32 | llama.cpp #15013 CUDA, FA on | 27 |
| 8 | AMD Radeon AI PRO R9700 32GB | 152.7 | 5,908 | 32 | llama.cpp #10879 Vulkan, FA on | 14 |
| 9 | GeForce RTX 4080 Super 16GB | 147.5 | 9,439 | 16 | llama.cpp #15013 CUDA | 18 |
| 10 | AMD Radeon RX 9070 XT 16GB | 142.0 | 5,604 | 16 | llama.cpp #10879 Vulkan | 7 |
| 11 | RTX PRO 4000 Blackwell 24GB | 136.4 | 5,674 | 24 | llama.cpp #15013 CUDA, FA on | 21 |
| 12 | RTX A5000 24GB | 135.8 | 4,552 | 24 | llama.cpp #15013 CUDA, FA on | 31 |
| 13 | GeForce RTX 5070 12GB | 128.2 | 5,783 | 12 | llama.cpp #15013 CUDA | 7 |
| 14 | Intel Arc Pro B70 32GB | 112.9 | 4,570 | 32 | llama.cpp #10879 Vulkan, FA on | 14 |
| 15 | GeForce RTX 5060 Ti 16GB | 93.5 | 4,196 | 16 | llama.cpp #15013 CUDA, FA on (PCIe x8) | 9 |
| 16 | RTX A4000 16GB | 85.2 | 2,808 | 16 | llama.cpp #15013 CUDA, FA on | 23 |
| 17 | Intel Arc B580 12GB | 72.0 | 419 | 12 | llama.cpp #10879 Vulkan, FA on | 5 |
| 18 | Intel Arc Pro B60 24GB | 68.1 | 727 | 24 | llama.cpp #10879 Vulkan, FA on | 14 |
| 19 | Intel Arc A770 16GB | 53.1 | 1,120 | 16 | llama.cpp #10879 Vulkan, FA on | 6 |
| 20 | Intel Arc B570 10GB | 50.5 | 289 | 10 | llama.cpp #10879 Vulkan, FA on | 6 |
| 21 | Intel Arc Pro B50 16GB | 47.7 | 1,123 | 16 | llama.cpp #10879 Vulkan, FA on | 12 |

Each row is one community submission (n=1 per card), different llama.cpp builds. Rows without a price show "-" in the last column. AMD/Intel rows are Vulkan, NVIDIA rows CUDA with flash attention. For multi-user serving (vLLM batch throughput) and big models see benchmarks.md section 3: there, VRAM and bandwidth decide and the PRO 6000 / 5090 lead by a wide margin.

## 3. AI training

There is **no measured training benchmark that covers most of these cards** (see benchmarks.md section 2). The only consistent measured set (Lambda PyTorch, older software) covers 6000 Ada and A100 from our list, plus the RTX 3090, RTX 4090 and RTX A6000, which are not purchase candidates. As a clearly labelled **proxy**, the table below ranks by spec-sheet dense FP16/BF16 tensor TFLOPS and memory bandwidth. This is not a benchmark.

| # | Card | FP16/BF16 dense TFLOPS (spec, partly D/U) | BW GB/s | VRAM | EUR per TFLOPS (low) |
|---|---|---|---|---|---|
| 1 | RTX PRO 6000 Blackwell Workstation 96GB | ~500 D | 1,792 | 96 | 35 |
| 2 | RTX PRO 6000 Blackwell Server 96GB | ~500 D | 1,597 | 96 | 41 |
| 3 | RTX PRO 6000 Blackwell Max-Q 96GB | ~439 D | 1,792 | 96 | 37 |
| 4 | GeForce RTX 5090 32GB | 419 (FP16 acc; ~210 FP32 acc) | 1,792 | 32 | 19 |
| 5 | RTX 6000 Ada 48GB | ~364 D | 960 | 48 | 26 |
| 6 | L40S 48GB | 362 | 864 | 48 | 29 |
| 7 | A100 80GB PCIe | 312 | 1,935 | 80 | - |
| 8 | RTX 5000 Ada 32GB | 261 | 576 | 32 | 18 |
| 9 | RTX PRO 5000 Blackwell 72GB | ~258 D | 1,344 | 72 | 49 |
| 10 | RTX PRO 5000 Blackwell 48GB | ~258 D | 1,344 | 48 | 31 |
| 11 | GeForce RTX 5080 16GB | 225 (FP16 acc) | 960 | 16 | 9 |
| 12 | RTX PRO 4500 Blackwell 32GB | ~202 D | 896 | 32 | 23 |
| 13 | AMD Radeon RX 9070 XT 16GB | 195 | 640 | 16 | 5 |
| 14 | AMD Radeon AI PRO R9700 32GB | ~191 U | 640 | 32 | 11 |
| 15 | GeForce RTX 5070 Ti 16GB | 177 (FP16 acc) | 896 | 16 | 8 |
| 16 | RTX PRO 4000 Blackwell 24GB | ~161 D | 672 | 24 | 18 |
| 17 | RTX 4500 Ada 24GB | ~158 D | 432 | 24 | 18 |
| 18 | GeForce RTX 5070 12GB | 124 (FP16 acc) | 672 | 12 | 7 |
| 19 | AMD Radeon PRO W7900 48GB | ~122 U | 864 | 48 | 29 |
| 20 | RTX A5000 24GB | 111 | 768 | 24 | 38 |
| 21 | Intel Arc Pro B60 24GB | ~98 U (INT8 197 TOPS V) | 456 | 24 | 10 |
| 22 | RTX PRO 4000 Blackwell SFF 24GB | ~96 D (770 AI TOPS / 8) | 432 | 24 | 34 |
| 23 | GeForce RTX 5060 Ti 16GB | 95 (FP16 acc) | 448 | 16 | 8 |
| 24 | GeForce RTX 5060 Ti 8GB | 95 (FP16 acc) | 448 | 8 | 5 |
| 25 | RTX 4000 Ada 20GB | ~82 D | 360 | 20 | 24 |
| 26 | RTX A4000 16GB | 77 | 448 | 16 | 26 |

Caveat: GeForce figures are FP16-accumulate; with FP32 accumulate they halve, so for mixed-precision training a 5090 is closer to ~210 than 419. AMD/Intel values are unverified. Real training speed also depends on software (CUDA vs ROCm vs oneAPI).

## 4. EUR per GB VRAM (lower is better)

| # | Card | Price low | VRAM GB | EUR/GB (low) | EUR/GB (typical) | Memory |
|---|---|---|---|---|---|---|
| 1 | Intel Arc A770 16GB | 304 | 16 | 19 | - | GDDR6 |
| 2 | Intel Arc B570 10GB | 299 | 10 | 30 | - | GDDR6 |
| 3 | Intel Arc B580 12GB | 387 | 12 | 32 | - | GDDR6 |
| 4 | Intel Arc Pro B50 16GB | 569 | 16 | 36 | 34 | GDDR6 |
| 5 | Intel Arc Pro B60 24GB | 960 | 24 | 40 | - | GDDR6 |
| 6 | GeForce RTX 5060 Ti 16GB | 799 | 16 | 50 | - | GDDR7 |
| 7 | Intel Arc Pro B70 32GB | 1,599 | 32 | 50 | 49 | GDDR6 |
| 8 | Intel Arc Pro B65 32GB | 1,687 | 32 | 53 | - | GDDR6 |
| 9 | AMD Radeon RX 9070 XT 16GB | 949 | 16 | 59 | - | GDDR6 |
| 10 | GeForce RTX 5060 Ti 8GB | 520 | 8 | 65 | - | GDDR7 |
| 11 | AMD Radeon AI PRO R9700 32GB | 2,102 | 32 | 66 | 51 | GDDR6 |
| 12 | AMD Radeon PRO W7900 48GB | 3,516 | 48 | 73 | 77 | GDDR6 ECC |
| 13 | GeForce RTX 5070 12GB | 929 | 12 | 77 | - | GDDR7 |
| 14 | GeForce RTX 5070 Ti 16GB | 1,399 | 16 | 87 | - | GDDR7 |
| 15 | RTX 4000 Ada 20GB | 1,940 | 20 | 97 | - | GDDR6 ECC |
| 16 | RTX 4500 Ada 24GB | 2,786 | 24 | 116 | 123 | GDDR6 ECC |
| 17 | RTX PRO 4000 Blackwell 24GB | 2,819 | 24 | 117 | 127 | GDDR7 ECC |
| 18 | RTX A4000 16GB | 1,964 | 16 | 123 | - | GDDR6 |
| 19 | GeForce RTX 5080 16GB | 1,969 | 16 | 123 | 141 | GDDR7 |
| 20 | RTX PRO 4000 Blackwell SFF 24GB | 3,260 | 24 | 136 | 137 | GDDR7 ECC |
| 21 | RTX PRO 4500 Blackwell 32GB | 4,549 | 32 | 142 | 150 | GDDR7 ECC |
| 22 | RTX 5000 Ada 32GB | 4,710 | 32 | 147 | - | GDDR6 |
| 23 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,199 | 96 | 169 | 175 | GDDR7 ECC |
| 24 | RTX PRO 5000 Blackwell 48GB | 8,119 | 48 | 169 | 177 | GDDR7 ECC |
| 25 | GeForce RTX 4080 Super 16GB | 2,708 | 16 | 169 | - | GDDR6X |
| 26 | RTX PRO 5000 Blackwell 72GB | 12,624 | 72 | 175 | 210 | GDDR7 ECC |
| 27 | RTX A5000 24GB | 4,225 | 24 | 176 | - | GDDR6 |
| 28 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 96 | 183 | 190 | GDDR7 ECC |
| 29 | RTX 6000 Ada 48GB | 9,592 | 48 | 200 | 200 | GDDR6 ECC |
| 30 | RTX PRO 6000 Blackwell Server 96GB | 20,645 | 96 | 215 | 219 | GDDR7 ECC |
| 31 | L40S 48GB | 10,403 | 48 | 217 | 219 | GDDR6 ECC |
| 32 | GeForce RTX 5090 32GB | 7,829 | 32 | 245 | 281 | GDDR7 |

Note: for the R9700, Arc Pro B70 and Arc Pro B50 the typical price in the CSV is lower than the lowest price (different dates and sources), so their typical column is lower than the low column.

## 5. EUR per FP32 TFLOPS (lower is better)

| # | Card | Price low | FP32 TFLOPS | EUR/TFLOPS |
|---|---|---|---|---|
| 1 | Intel Arc A770 16GB | 304 | 19.7 | 15 |
| 2 | AMD Radeon RX 9070 XT 16GB | 949 | 48.7 | 19 |
| 3 | GeForce RTX 5060 Ti 8GB | 520 | 23.7 | 22 |
| 4 | Intel Arc B570 10GB | 299 | 12.7 | 24 |
| 5 | Intel Arc B580 12GB | 387 | 14.6 | 27 |
| 6 | GeForce RTX 5070 12GB | 929 | 30.9 | 30 |
| 7 | GeForce RTX 5070 Ti 16GB | 1,399 | 43.9 | 32 |
| 8 | GeForce RTX 5060 Ti 16GB | 799 | 23.7 | 34 |
| 9 | GeForce RTX 5080 16GB | 1,969 | 56.3 | 35 |
| 10 | AMD Radeon AI PRO R9700 32GB | 2,102 | 47.8 | 44 |
| 11 | GeForce RTX 4080 Super 16GB | 2,708 | 51.3 | 53 |
| 12 | Intel Arc Pro B50 16GB | 569 | 10.65 | 53 |
| 13 | AMD Radeon PRO W7900 48GB | 3,516 | 61 | 58 |
| 14 | Intel Arc Pro B70 32GB | 1,599 | 22.9 | 70 |
| 15 | RTX 4500 Ada 24GB | 2,786 | 39.6 | 70 |
| 16 | RTX PRO 4000 Blackwell 24GB | 2,819 | 40 | 70 |
| 17 | RTX 5000 Ada 32GB | 4,710 | 65.3 | 72 |
| 18 | RTX 4000 Ada 20GB | 1,940 | 26.7 | 73 |
| 19 | GeForce RTX 5090 32GB | 7,829 | 104.8 | 75 |
| 20 | Intel Arc Pro B60 24GB | 960 | 12.3 | 78 |
| 21 | RTX PRO 4500 Blackwell 32GB | 4,549 | 51 | 89 |
| 22 | RTX A4000 16GB | 1,964 | 19.2 | 102 |
| 23 | RTX 6000 Ada 48GB | 9,592 | 91.1 | 105 |
| 24 | L40S 48GB | 10,403 | 91.6 | 114 |
| 25 | RTX PRO 5000 Blackwell 48GB | 8,119 | 65 | 125 |
| 26 | RTX PRO 4000 Blackwell SFF 24GB | 3,260 | 24 | 136 |
| 27 | Intel Arc Pro B65 32GB | 1,687 | 12.3 | 137 |
| 28 | RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 125 | 140 |
| 29 | RTX PRO 6000 Blackwell Max-Q 96GB | 16,199 | 110 | 147 |
| 30 | RTX A5000 24GB | 4,225 | 27.8 | 152 |
| 31 | RTX PRO 6000 Blackwell Server 96GB | 20,645 | 120 | 172 |
| 32 | RTX PRO 5000 Blackwell 72GB | 12,624 | 65 | 194 |

FP32 TFLOPS on GeForce/AMD count dual-issue lanes; real shader throughput differs by architecture. Use this column only within one vendor generation.
