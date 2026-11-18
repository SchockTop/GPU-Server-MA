# Imagine case: 10,000 EUR for GPUs

Prices and facts re-checked at the sources on 18 Nov 2026.

A generic worked example for a small team that wants shared GPU compute for **rendering as a service** (Blender/Cycles, V-Ray, Octane, Redshift; on demand and batch), **neural-network training** (UNet, Transformers), **LLM fine-tuning** and **LLM inference**. It assumes a Kubernetes-style setup where jobs get whole GPUs or GPU slices.

This is not a recommendation. It shows what the money buys and what each option gives up.

Prices are German retail as of 2026-11-17/18 (date per card in `gpu-master-table.md`), brutto incl. 19% VAT, from `gpu-master-table.md`. "Low" is the lowest offer found; "typical" is the middle of the top ten shops. GPU prices moved by 2-30% within weeks in autumn 2026, so re-check before buying.

> **Brutto or netto matters a lot.** 10,000 EUR brutto is 8,403 EUR net. 10,000 EUR net is 11,900 EUR brutto, which is close to the 12k options below. The RTX 5090 + 2x RTX 5080 option (11,767 brutto, 9,889 net) now fits under 10,000 EUR net.

Blender figures are Open Data 4.5.0 medians per card, simply added up. The sums only hold if the work splits cleanly across cards (batch rendering: yes; one large scene or one large model: no).

---

## The four main packages

| | A: 2x RTX PRO 4500 Blackwell | B: 1x RTX PRO 5000 Blackwell 48GB | C: 3x RTX PRO 4000 Blackwell | D: 4x GeForce RTX 5080 |
|---|---|---|---|---|
| Price brutto (low / typical) | 9,098 / ~9,600 | 8,119 / ~8,500 | 8,457 / ~9,150 | 7,876 / ~9,000 |
| Net (low) | 7,645 | 6,823 | 7,107 | 6,618 |
| VRAM total (per card) | 64 GB (32) | 48 GB (48) | 72 GB (24) | 64 GB (16) |
| Largest single job | 32 GB | **48 GB** | 24 GB | 16 GB |
| Blender, sum of cards | ~17,000 | ~10,900 | ~18,800 | **~36,600** |
| llama.cpp 7B tg, per card | 169 t/s | no data (similar bandwidth to 6000 Ada: ~180 expected, not measured) | 136 t/s | 185 t/s |
| Power | 2x 200 W | 300 W | 3x 145 W | 4x 360 W |
| Slots / cooling | 2x dual-slot blower | 1x dual-slot blower | 3x **single-slot** blower | 4x 2-3.5-slot axial (partner cards) |
| ECC | yes | yes | yes | no |
| Sharing | whole cards; MIG not confirmed for the Workstation Edition | **MIG 2x 24 GB** | whole cards, many small slots | whole cards or time-slicing |
| vGPU | no | no (only the 72 GB version) | no | no |
| Driver licence | pro driver | pro driver | pro driver | GeForce EULA excludes "datacenter deployment" (needs legal review) |

### What each package is good at

**A: 2x PRO 4500 (32 GB each).** The balanced pro option.
- Two independent 32 GB jobs, or one job spread over two cards.
- Fits 32B LLMs at 4-bit per card and QLoRA of 27-32B models (tight).
- Blower cards stack densely in a server.
- Rendering per euro is mediocre: one 5080 renders slightly faster than one PRO 4500 in Blender.

**B: 1x PRO 5000 48 GB.** The "biggest model on one card" option.
- Runs 70B at 4-bit with short context, and QLoRA of 70B at the minimum (41 GB).
- Splits into two isolated 24 GB MIG slices when idle users need small slices.
- Weak on throughput: one card, so only one large job at a time.
- About 1,500-1,900 EUR stays unspent; that could buy, for example, one 16 GB card for small jobs.

**C: 3x PRO 4000 (24 GB each).** The "many users, low power, few slots" option.
- Single-slot, 145 W, ECC. Three parallel 24 GB jobs.
- Best rendering throughput among the pro packages.
- 24 GB is the weak spot for LLMs: 32B at 4-bit spills to the CPU and becomes about 10x slower (measured).

**D: 4x RTX 5080 (16 GB each).** The rendering-throughput option.
- About twice the render throughput of any pro package. Cycles/OptiX, V-Ray, Octane and Redshift all run.
- 16 GB per card limits LLM work to roughly 14B at 4-bit and QLoRA up to about 14B.
- Large axial-fan cards (2.5-3.5 slots) need airflow and space, so they suit workstations or a roomy chassis better than a dense server.
- No ECC.
- The GeForce driver licence excludes datacenter use. Whether a shared department server counts is a legal question.

---

## Other options worth knowing

| Package | Price brutto (low) | VRAM | Blender sum | Why consider | Why not |
|---|---|---|---|---|---|
| 4x Radeon AI PRO R9700 32GB | ~8,400 | **128 GB** | ~12,800 (HIP) | Most VRAM per euro. vLLM with TP=4 runs 70B. ROCm officially supports the card. | Rendering at 1/3 of NVIDIA per card. Octane unsupported. Redshift AMD is Windows-only. ROCm on Linux is limited to Ubuntu LTS/RHEL, and updates have caused regressions. |
| 2x RTX A6000 48GB (used) | ~8,000-9,000 (asking) | 96 GB | ~10,300 | 48 GB per card plus an **NVLink** pair. Listed for vGPU. | Used, no warranty. Ampere: no FP8/FP4. Slower than a PRO 4500 per card in rendering. |
| 1x RTX 6000 Ada 48GB | ~9,600 | 48 GB | ~10,700 | 48 GB **with vGPU support**, for teams that need VDI-style virtual workstations. | Costs more than a PRO 5000 48GB for similar speed. No MIG, no FP4. |
| 1x PRO 4500 + 2x RTX 5080 | ~8,500 | 64 GB (32+16+16) | ~26,800 | Mixed: one 32 GB pro card for LLM and big scenes, two GeForce cards for render throughput. | Two driver/licence classes to manage. Same GeForce caveats. |
| 5x RTX 5070 Ti 16GB | ~7,000 | 80 GB | ~38,000 | Best render throughput per euro among new 16 GB cards (about 184 EUR per 1,000 Blender points). The 12 GB RTX 5070 is cheaper per point (about 150). | Same as D, with five cards to house and power (5x 300 W). |
| 1x RTX 5090 32GB | ~7,800-9,000 | 32 GB | ~15,000 | Fastest single card in this budget for rendering and LLM speed. | Price doubled in a few months. 575 W, 12V-2x6 connector, large cooler. GeForce licence. |

## What does NOT fit 10,000 EUR
- **RTX PRO 6000 Blackwell (96 GB)**: from 16,199 (Max-Q) or 17,548 (Workstation).
- **RTX PRO 5000 72 GB**: from 12,624 in German shops.
- **L40S**: from 10,403. It is also passive and needs server airflow.
- **Two RTX 5090s**: 15,600+.
- **Full fine-tuning of 7B+ LLMs**: about 130-150 GB of memory plus activations. No package reaches that on one card. It needs sharding across cards, or renting datacenter GPUs.
- **Hardware-isolated sharing plus graphics VDI on new cards**: only the PRO 5000 72 GB and the Server Editions are on NVIDIA's vGPU list.

## What changes at 12,000-15,000 EUR brutto

| Option | Price brutto (low) | What it adds |
|---|---|---|
| 1x RTX PRO 5000 72GB | 12,624 | 72 GB on one card: 70B at 32k+ context, QLoRA of 70B with headroom. **vGPU-listed and MIG 2x36 GB**. One card only. |
| PRO 5000 48GB + PRO 4500 | ~12,670 | One 48 GB card for big models plus one 32 GB card for parallel work, 80 GB total. |
| 3x PRO 4500 | ~13,650 | 96 GB over three 32 GB cards, ~25,500 Blender sum. Good for many parallel users. |
| 6x R9700 | ~12,600 | 192 GB of VRAM. The same AMD software caveats apply. |
| RTX 5090 + 2x RTX 5080 | ~11,770 | ~33,000 Blender sum plus one 32 GB card. GeForce caveats. At this price it no longer reaches the 12,000 EUR brutto band: it sits just below it. |
| RTX PRO 6000 Max-Q | 16,199 | Still out of reach at 15k. It is the one card that removes the VRAM problem (96 GB, MIG 4x24 GB) and matches the 5090 in speed. |

## How to choose (questions, not answers)
1. **What is the largest single job?** Largest scene, model or batch, in GB. That sets the minimum VRAM per card, because VRAM does not add up across cards for one render.
2. **How many jobs run at the same time?** Many parallel users favour several mid cards (A, C, D). Few large jobs favour one big card (B, 72 GB).
3. **Which renderers?** Octane rules out AMD and Intel. Redshift on Linux rules out AMD.
4. **Server or workstations?** Dense servers need blower or passive cards (pro line). GeForce partner cards are large and axial.
5. **Is GeForce in a shared server acceptable** under the driver licence for your organisation?
6. **Do you need isolation** (MIG or vGPU) or is a scheduler enough? See `virtualization-licensing.md`.
7. **Measure before buying.** Log GPU use and VRAM for 1-2 weeks:
   `nvidia-smi --query-gpu=timestamp,index,name,utilization.gpu,memory.used,memory.total --format=csv -l 60`
   Then rent the candidate card for an hour and run one real job.
