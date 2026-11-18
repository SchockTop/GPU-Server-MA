# GPU-Server-MA

New hardware only; used cards are not listed.

Prices and facts re-checked at the sources on 18 Nov 2026.

Research notes for choosing GPUs for a shared compute setup: rendering as a service (on-demand and batch), neural-network training (UNet, Transformers), LLM training and LLM inference.

**Overview page (charts, sortable table, German): https://schocktop.github.io/GPU-Server-MA/** (source: `index.html`, rebuilt with `python tools/build_site.py`).

Data as of **2026-11-17**. Prices are German retail, brutto incl. 19 % VAT (net = brutto / 1.19). GPU prices move fast, so re-check before buying. Values are marked verified (seen on a cited page), derived or unverified; sources are listed in the files.

| File | Content |
|---|---|
| [research/gpu-master-table.md](research/gpu-master-table.md) / [.csv](research/gpu-master-table.csv) | One row per GPU: prices, shader/CUDA cores, tensor/RT cores, VRAM, bandwidth, TFLOPS, power, slots, cooling, ECC, NVLink, vGPU/MIG |
| [research/benchmarks.md](research/benchmarks.md) | Measured benchmarks: rendering, AI training, LLM inference, VRAM needs |
| [research/rankings.md](research/rankings.md) | The table sorted by benchmark and by price/performance |
| [virtualisierung.html](https://schocktop.github.io/GPU-Server-MA/virtualisierung.html) | One GPU for many VMs (German): Hyper-V explained, NVIDIA vGPU cost, Intel/AMD SR-IOV, hypervisor comparison |
| [research/llm-large.md](research/llm-large.md) | LLM speed for larger models (14B, 32B, 70B) per card, with CSV |
| [research/load-balancing.md](research/load-balancing.md) | Dynamic load balancing: scheduling, GPU sharing, inference routing, autoscaling, render farm, staged integration path |
| [research/training-bench.md](research/training-bench.md) / [.csv](research/training-bench.csv) | Measured deep-learning training numbers per source (Exxact, Lambda, Bizon, community) |
| [research/intel-extra.md](research/intel-extra.md) | Notes on the added Intel cards |
| [research/prices-b2b.md](research/prices-b2b.md) / [.csv](research/prices-b2b.csv) | Business-reseller prices (Bechtle, Senetic, Jacob, Mercateo, Alternate), net and brutto |
| [research/imagine-case-10k.md](research/imagine-case-10k.md) | "Imagine 10,000 EUR": four example packages and trade-offs |
| [research/amd-vs-nvidia.md](research/amd-vs-nvidia.md) | AMD vs NVIDIA (and Intel): software maturity, speed, price |
| [research/virtualization-licensing.md](research/virtualization-licensing.md) | Multi-user costs: NVIDIA vGPU licences, free options (MIG, MPS, time-slicing, passthrough, Run:ai), AMD and Intel equivalents |

Known gaps: no measured training benchmark exists for the newest Blackwell cards (the training ranking uses spec-sheet TFLOPS); several shops blocked automated access; B2B prices are public list prices, not negotiated project prices; some benchmark samples are small.
