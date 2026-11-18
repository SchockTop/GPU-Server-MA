# GPU-Server-MA

New hardware only; used cards are not listed.

Prices and facts re-checked at the sources on 18 Nov 2026.

Research notes for choosing GPUs for a shared compute setup: rendering as a service (on-demand and batch), neural-network training (UNet, Transformers), LLM training and LLM inference.

**Overview page (charts, sortable table, German): https://schocktop.github.io/GPU-Server-MA/** (source: `index.html`, rebuilt with `python tools/build_site.py`). It covers 34 cards (new hardware only) and has an adjustable weighted score (sliders and presets), pin and hide for single cards, and collapsible sections.

Data as of **2026-11-17**. Prices are German retail, brutto incl. 19 % VAT (net = brutto / 1.19). GPU prices move fast, so re-check before buying. Values are marked verified (seen on a cited page), derived or unverified; sources are listed in the files. Cards without an orderable new offer (for example the Intel Arc A770, end of life) have no price.

| File | Content |
|---|---|
| [index.html](https://schocktop.github.io/GPU-Server-MA/) | Overview page (German): charts, sortable table, weighted score, 10,000 EUR example packages, B2B prices, sharing and licences, load balancing |
| [virtualisierung.html](https://schocktop.github.io/GPU-Server-MA/virtualisierung.html) | One GPU for many VMs (German): Hyper-V explained, NVIDIA vGPU cost, Intel/AMD SR-IOV, hypervisor comparison |
| [research/gpu-master-table.md](research/gpu-master-table.md) | One row per GPU (34 cards): prices, shader/CUDA cores, tensor/RT cores, VRAM, bandwidth, TFLOPS, power, slots, cooling, ECC, NVLink, vGPU/MIG |
| [research/gpu-master-table.csv](research/gpu-master-table.csv) | Source of truth for the master table and all prices |
| [research/benchmarks.md](research/benchmarks.md) | Measured benchmarks: rendering, AI training, LLM inference, VRAM needs |
| [research/rankings.md](research/rankings.md) | The table sorted by benchmark and by price/performance |
| [research/llm-large.md](research/llm-large.md) | LLM speed for larger models (14B, 32B, 70B) per card |
| [research/llm-large.csv](research/llm-large.csv) | Data behind `llm-large.md` |
| [research/training-bench.md](research/training-bench.md) | Measured deep-learning training numbers per source (Exxact, Lambda, Bizon, community) and a pointer to the wider AIME series |
| [research/training-bench.csv](research/training-bench.csv) | Data behind `training-bench.md` |
| [research/training-sources.md](research/training-sources.md) | Further training benchmarks checked (AIME, Puget and others), with coverage per card |
| [research/training-extra.csv](research/training-extra.csv) | Data behind `training-sources.md` (AIME series: BERT Large and ResNet-50 on 11 cards; Puget SDXL LoRA) |
| [research/intel-extra.md](research/intel-extra.md) | Notes on the added Intel cards |
| [research/prices-b2b.md](research/prices-b2b.md) | Business-reseller prices (Bechtle, Senetic, Jacob, Mercateo, Alternate), net and brutto |
| [research/prices-b2b.csv](research/prices-b2b.csv) | Data behind `prices-b2b.md` |
| [research/imagine-case-10k.md](research/imagine-case-10k.md) | "Imagine 10,000 EUR": five example packages (A to E, E = one strong card plus one card for VM sharing) and trade-offs |
| [research/amd-vs-nvidia.md](research/amd-vs-nvidia.md) | AMD vs NVIDIA (and Intel): software maturity, speed, price |
| [research/virtualization-licensing.md](research/virtualization-licensing.md) | Multi-user costs: NVIDIA vGPU licences, free options (MIG, MPS, time-slicing, passthrough, Run:ai), AMD and Intel equivalents |
| [research/load-balancing.md](research/load-balancing.md) | Dynamic load balancing: scheduling, GPU sharing, inference routing, autoscaling, render farm, staged integration path |

Known gaps: measured training values exist for 17 of the 34 cards (the widest source is the AIME series, 11 cards); the other 17 (for example the RTX 5080 and all Intel cards) have none, and the training ranking falls back to spec-sheet TFLOPS for them; several shops blocked automated access; B2B prices are public list prices, not negotiated project prices; some benchmark samples are small.
