# Training benchmark scores per GPU (collected 2026-11-17)

New hardware only; used cards are not listed.

RTX 3090, RTX 4090 and RTX A6000 are listed as reference values only; they are practically only available used and are not purchase candidates.


Data: `training-bench.csv` (93 rows). Only values read on the source page. Nothing derived. Evidence V = seen in fetched page text (pages were read through a summarising fetcher, so spot-check before publishing). Rows with a `relative_value` are the source's own ratios.

## Which benchmark as "the training score"?

No single benchmark in this file covers the 34 cards. No MLPerf Training, Geekbench AI, UL Procyon or MLPerf Client result is usable (data-center only, or inference only).

Coverage by benchmark:
- **Bizon ResNet50 FP16/FP32** covers the most cards (7: A4000, A5000, A6000, A100 80GB, 3090, 4090, 6000 Ada). Weaknesses: no units, no batch size, no date ("2026 [Updated]"). Its Blackwell, 5000 Ada, 4500 Ada and 50-series cells are "n/a".
- **Lambda PyTorch (GitHub CSV)** covers 5 cards (A100 80GB PCIe, A6000, 3090, 4090, 6000 Ada) with ResNet50, BERT Base and BERT Large. All run FP16 AMP in one method. The stack is old (2023, PyTorch 1.13).
- **Exxact deep-learning benchmark (Apr 2026)** covers 4 cards: PRO 6000 Server, PRO 6000 Max-Q, 6000 Ada, L40S. It runs 10 workloads in one method (PyTorch 2.5, FP32 only) and publishes ratios against L40S. This is the only current measured data for Blackwell PRO. 
- **Exxact LoRA fine-tune (Jun 2026)**: Llama 3.1 8B, tokens/s on PRO 4500, PRO 5000 48GB and PRO 6000 Server.
- **nikolasent (Feb 2025, community)**: 3090, 4090, 5090 across 5 CNNs in FP32 and FP16. It is the only 5090 data point.

Recommendation: use **Exxact ResNet50 + BERT Large (FP32)** as the training score for the Blackwell PRO, 6000 Ada and L40S group. Use **Lambda FP16** for the older Ampere/Ada group. RTX 6000 Ada appears in both, so it can bridge the two scales, but the stacks and precisions differ, so any merged ranking must be labelled as spliced. We did not compute one.

## Coverage per card (master-table names)

Measured number exists:
- RTX PRO 6000 Blackwell Server 96GB: Exxact (10 workloads, LoRA)
- RTX PRO 6000 Blackwell Max-Q 96GB: Exxact
- RTX PRO 6000 Blackwell Workstation 96GB: one community ResNet50 number (naveen.ing, variant inferred from 600 W)
- RTX PRO 5000 Blackwell 48GB: Exxact LoRA only
- RTX PRO 4500 Blackwell 32GB: Exxact LoRA only
- GeForce RTX 5090 32GB: nikolasent (community)
- GeForce RTX 5070 Ti 16GB, GeForce RTX 5070 12GB: one small-model run on a GitHub issue (community, a 10-epoch total time)
- GeForce RTX 4090 24GB: Lambda, Bizon, nikolasent, GitHub issue
- GeForce RTX 3090 24GB: Lambda, Bizon, nikolasent
- RTX 6000 Ada 48GB: Lambda, Bizon, Exxact
- L40S 48GB: Exxact
- RTX A6000 48GB: Lambda, Bizon
- A100 80GB PCIe: Lambda, Bizon
- RTX A5000 24GB, RTX A4000 16GB: Bizon only
- AMD Radeon RX 9070 XT 16GB: GitHub issue (community, ROCm Windows, several runs)

No measured training number found in this file (20 cards; three of them, RTX 5000 Ada, RTX 4500 Ada and Radeon PRO W7900, have values in `training-extra.csv`, see the next section):
RTX PRO 5000 Blackwell 72GB, RTX PRO 4000 Blackwell 24GB, RTX PRO 4000 Blackwell SFF 24GB, GeForce RTX 5080 16GB, GeForce RTX 5060 Ti 16GB, GeForce RTX 5060 Ti 8GB, GeForce RTX 4080 Super 16GB, RTX 5000 Ada 32GB, RTX 4500 Ada 24GB, RTX 4000 Ada 20GB, AMD Radeon AI PRO R9700 32GB, AMD Radeon PRO W7900 48GB, Intel Arc Pro B60 24GB, Intel Arc Pro B65 32GB, Intel Arc Pro B60 Dual 48GB (Maxsun), Intel Arc Pro B70 32GB, Intel Arc Pro B50 16GB, Intel Arc B580 12GB, Intel Arc B570 10GB, Intel Arc A770 16GB.
## Wider sources found later: `training-extra.csv`

`training-sources.md` lists the further training sources checked on 2026-11-18, and `training-extra.csv` (96 rows) holds their values.
- The **AIME series** (BERT Large and ResNet-50, fp32 and fp16 AMP, eager and torch.compile; 11 cards; November 2025) is the widest single-method training source found. The overview page shows it as a table column and a chart box. It is not part of the weighted score, because it covers only 11 of 34 cards.
- A second source, Puget Systems SDXL LoRA training, adds 4 cards (RTX A5000, RTX 5000 Ada, RTX 6000 Ada, AMD Radeon PRO W7900 48GB).
- Together with `training-bench.csv`, 17 of the 34 cards have at least one measured training value. The other 17 have none: GeForce RTX 5060 Ti 16GB and 8GB, RTX PRO 5000 Blackwell 72GB, RTX PRO 4000 Blackwell 24GB and SFF, RTX 4000 Ada, GeForce RTX 5080, GeForce RTX 4080 Super, Radeon AI PRO R9700, and all Intel cards.
- The values of the two files come from different methods. Compare only within one benchmark.

## Checked, nothing usable
- AI-Benchmark ranking: stale. The only matching rows are Radeon VII/RX 480/470; the page has no modern NVIDIA, AMD or Intel entries.
- AIME blog: the chart values are loaded from JSON files; they were read later and are in `training-extra.csv` (see the next section). Lambda web page: JavaScript table, not readable, so the GitHub CSV was used.
- Puget 2025-26: RTX 5090/5080 AI review is inference only. No Blackwell training article found.
- Phoronix: R9700 reviews are vLLM/OpenCL. The Phoronix PRO Blackwell review returned 403. A news.lavx.hu mirror lists non-existent GPUs ("Radeon AI PRO X3", "Arc Pro B-Series 800"), so it was ignored.
- MLPerf Training v5.1: data-center systems only. Intel B60 MLPerf: inference only. Geekbench AI, UL Procyon, MLPerf Client: inference only.
- trooper.ai, gigagpu.com, vrlatech, dev.to pages: inference or unverified/generated content. Not used.
- MatrixSP/pytorch-gpu-benchmark (5090 and A100, ResNet etc.): chart images only.
- Not reached: TechPowerUp, Tom's Hardware, STH, Chips and Cheese, c't/heise, Thomas-Krenn, Level1Techs R9700 thread (had no training numbers in the snippets seen).

## Caveats
- Exxact page has typos in some cells (e.g. 8x Transformer-XL values); only the 1x rows were taken. Its "Server" and "Max-Q" PRO 6000 are not the Workstation edition. The page is FP32 only. Exxact's own FP32/FP16 tabs may hide FP16 data that was not in the page text.
- Bizon: units, batch, date unknown; the 6000 Ada FP16 (1800) is higher than the Lambda 4090-class ordering would suggest, so treat the numbers as indicative.
- Lambda vs Exxact vs Bizon ResNet50 numbers for the same card differ strongly (e.g. 6000 Ada: 1146 FP16 Lambda, 1800 FP16 Bizon, 1185 FP32 Exxact). The cause is different precision, software and batch size. Do not mix sources in one ranking.
- The GitHub-issue numbers are one user, one unspecified small model. The 5070 Ti beat the 4090 there, which is an oddity. Warm-up and ROCm Windows effects are included. The R9700 32GB result in that issue was image-only.
- Phoronix, Puget and Tom's all lack public training scores for the Blackwell consumer cards other than the 5090. The cleanest option for the public table is a "measured subset" column plus "n/a" for the rest, not a derived score.
