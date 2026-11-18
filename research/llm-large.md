# Larger-LLM generation speed per GPU (research notes, 2026-11-18)

New hardware only; used cards are not listed.

RTX 3090, RTX 4090 and RTX A6000 are listed as reference values only; they are practically only available used and are not purchase candidates.


## Most consistent source
Hardware Corner per-GPU pages (https://www.hardware-corner.net/gpu-llm-benchmarks/<gpu>/, "Updated Benchmarks: March 2026"). Same author and method for every card: llama.cpp llama-bench, CUDA, Q4_K quant, token generation at 4k/16k/32k... context. Rows in the CSV use the 4k column (the other contexts are on the same pages). Models and counts:
- Qwen3 14B Q4_K: 11 cards (5090, PRO 6000, PRO 5000 48GB, 4090, 6000 Ada, 5080, 5070 Ti, 3090, 5070, A6000, 5060 Ti 16GB)
- Qwen3 32B dense Q4_K: 7 cards (5090, PRO 6000, PRO 5000 48GB, 4090, 6000 Ada, 3090, A6000)
- Qwen3.5 27B and Gemma4 31B: 3 cards each (PRO 6000, 5090, 3090)
- Llama 3.3 70B Q4_K: 4 cards (PRO 6000, PRO 5000 48GB, 6000 Ada, A6000). Only 48GB+ cards fit 70B, so no row for 24/32 GB cards.

Recommendation: Qwen3 32B Q4_K at 4k context from Hardware Corner (7 cards) as the "larger LLM" column; Llama 3.3 70B (4 cards) as the optional "70B" column; Qwen3 14B (11 cards) if wider coverage matters.

## Other sources used
- LocalScore leaderboard (localscore.ai): Qwen2.5 14B Q4_K_M generation for 4 of our cards (6000 Ada, 4090, PRO 6000, 5090). The 5090 value (45.5) looks anomalously low and the 4090 appears twice (68.8 and 50.0); crowd-sourced, mixed setups. No 32B/70B model on the leaderboard.
- PMZFX Arc Pro B70 community repo (GitHub): B70 on llama.cpp SYCL: Qwen3.5 27B Q4_K_M 20.4, Gemma4 31B 21.7, Phi-4 14B 43.7 t/s (tg128). Not vendor data; different method (tg128, SYCL) than Hardware Corner, so only roughly comparable. Its 70B result needs 2 GPUs, so no row.
- llama.cpp discussion #19890: R9700 (Vulkan) and 5090 (CUDA) on MoE models (Qwen3.5-35B-A3B, Qwen3-30B-A3B). MoE, so NOT comparable to dense 27-32B; included for completeness only.

## Method caveats
- Pages were read through a fetch tool that summarises HTML; numbers were transcribed from its table output. "V" means the number appeared in that output, but spot-check key rows before publishing.
- Hardware Corner uses Q4_K / Q4_K_XL, not exactly Q4_K_M. Context length changes speeds a lot (RTX A6000 Qwen3 32B: 24.6 at 4k, 18.3 at 16k). An older Hardware Corner ranking page (https://www.hardware-corner.net/gpu-ranking-local-llm/, Dec 2025) gives 16K numbers with the same pattern; not duplicated in the CSV.
- The Hardware Corner "RTX PRO 5000 Blackwell" page says 48GB; the 72GB variant is not covered.
- Some oddities: 4090 (Qwen3 32B 39.6) vs 3090 (35.1) is a small gap; 6000 Ada (37.4) is near the 4090 as expected.

## Gaps (no usable measured number found)
RTX A5000, RTX 5000 Ada, RTX A4000, RTX PRO 5000 72GB, RTX PRO 4500, RTX PRO 4000, RTX 4500 Ada, RTX 4000 Ada, L40S, RX 9070 XT, W7900, Arc Pro B60, Arc Pro B50, Arc B580, Arc A770: only estimator/aggregator sites (willitrunai, llmrun, specpicks etc.) or blogs without a clear measurement method turned up; these were rejected as not measured. R9700 and B70 only have MoE or single-source community numbers. B60 has no dense measurement found. Puget's R9700 article (dual-GPU, Qwen3.6-27B Q4_K_M, 23.4 t/s on 2 cards, GenAI-Perf) is not a single-card llama-bench number, so excluded. ServeTheHome R9700 review covers concurrency, not single-stream. Not checked: localscore.ai per-accelerator pages (the /accelerators URL returned 404), Puget professional-GPU article (page body not retrieved), Ollama community tables, Exxact/Bizon.
