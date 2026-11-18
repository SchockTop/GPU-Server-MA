# GPU master table

Prices and facts re-checked at the sources on 18 Nov 2026.

> Update 2026-11-18: prices, a few specs and a few benchmark values were corrected against the sources. The tables below show all 37 cards of [gpu-master-table.csv](gpu-master-table.csv), which is the source of truth. Notes on the added Intel cards are in [intel-extra.md](intel-extra.md).

Legend: **D** = derived by us (e.g. dense = sparse / 2, or FP16 = FP4-sparse / 8), **U** = unverified (third-party or memory), everything else was seen on a manufacturer page/datasheet (or Wikipedia for GeForce bandwidth/FP32). Tensor figures are **dense**. GeForce FP16 figures are with FP16 accumulate; with FP32 accumulate (typical for training) GeForce runs at half that rate, pro cards do not.

Price evidence: most prices come from hardwaredealz.com (Geizhals data, page time 17.11.2026 08:20, or re-checked on 18.11.2026) because Geizhals, idealo, Mindfactory, Cyberport etc. blocked automated access. The source and date are given per row. AMD/Intel prices come from gpuprix.com (14.11.2026), hardwaredealz.com or search snippets. Used prices are Kleinanzeigen **asking** prices. See SUMMARY.md.

## 1. Price, memory, benchmark headline

| Card | Price low (brutto) | Typical | Net (low) | Price source / date | VRAM GB | Mem | BW GB/s | Blender 4.5 (n) | llama 7B tg t/s |
|---|---|---|---|---|---|---|---|---|---|
| RTX A5000 24GB | 4,225 | - | 3,550 | it-market.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (only offer) (2026-11-17, page) | 24 | GDDR6 | 768 | 4,390 (n=24) | 135.8 |
| RTX 5000 Ada 32GB | 4,710 | - | 3,958 | grafikkarten.com, PNY; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 32 | GDDR6 | 576 | 5,677 (n=9) | no data |
| RTX A4000 16GB | 1,964 | - | 1,650 | it-market.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (931 offer at PC-KING looks wrong) (2026-11-17, page) | 16 | GDDR6 | 448 | 2,956 (n=44) | 85.2 |
| GeForce RTX 5060 Ti 16GB | 799 | - | 671 | Caseking, ASUS Prime OC; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 16 | GDDR7 | 448 | 4,309 (n=655) | 93.5 |
| GeForce RTX 5060 Ti 8GB | 520 | - | 437 | amazon.de (in stock); Alternate from 535; re-checked 18.11.2026 (2026-11-18, -) | 8 | GDDR7 | 448 | 4,309 (n=655) | no data |
| RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 18,230 | 14,746 | 25now via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Alternate 19,600 (2026-11-17, page) | 96 | GDDR7 ECC | 1,792 | 16,737 (n=205) | 281.1 |
| RTX PRO 6000 Blackwell Max-Q 96GB | 16,199 | 16,800 | 13,613 | computeruniverse, PNY; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 96 | GDDR7 ECC | 1,792 | 14,960 (n=33) | no data |
| RTX PRO 6000 Blackwell Server 96GB | 20,645 | 21,000 | 17,349 | Jacob; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 96 | GDDR7 ECC | 1,597 | 15,519 (n=28) | no data |
| RTX PRO 5000 Blackwell 72GB | 12,624 | 15,100 | 10,608 | PNY; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 72 | GDDR7 ECC | 1,344 | 10,849 (n=4) | no data |
| RTX PRO 5000 Blackwell 48GB | 8,119 | 8,500 | 6,823 | alza.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Proshop 8,400; Galaxus 8,508 (2026-11-17, page) | 48 | GDDR7 ECC | 1,344 | 10,929 (n=7) | no data |
| RTX PRO 4500 Blackwell 32GB | 4,549 | 4,800 | 3,823 | alza.de; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 32 | GDDR7 ECC | 896 | 8,487 (n=17) | 168.9 |
| RTX PRO 4000 Blackwell 24GB | 2,819 | 3,050 | 2,369 | alza.de; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 24 | GDDR7 ECC | 672 | 6,256 (n=40) | 136.4 |
| RTX PRO 4000 Blackwell SFF 24GB | 3,260 | 3,290 | 2,739 | Jacob; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 24 | GDDR7 ECC | 432 | 4,718 (n=8) | no data |
| RTX 6000 Ada 48GB | 9,592 | 9,600 | 8,061 | Proshop, PNY; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 48 | GDDR6 ECC | 960 | 10,655 (n=20) | 179.5 |
| RTX 4500 Ada 24GB | 2,786 | 2,950 | 2,341 | Galaxus via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (2026-11-17, page) | 24 | GDDR6 ECC | 432 | 5,674 (n=5) | no data |
| RTX 4000 Ada 20GB | 1,940 | - | 1,630 | grafikkarten.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (only offer) (2026-11-17, page) | 20 | GDDR6 ECC | 360 | 4,446 (n=16) | no data |
| L40S 48GB | 10,403 | 10,500 | 8,742 | Proshop.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (AT 9,555) (2026-11-17, page) | 48 | GDDR6 ECC | 864 | 7,848 (n=8) | no data |
| RTX A6000 48GB (used) | 4,000 | 4,500 | 3,361 | Kleinanzeigen asking prices 4,000-5,000 (VB) (2026-11-17, page (asking prices)) | 48 | GDDR6 ECC | 768 | 5,145 (n=8) | 144.9 |
| A100 80GB PCIe | - | - | - | no offer found (2026-11-17, -) | 80 | HBM2e ECC | 1,935 | no data | 200.9 |
| GeForce RTX 5090 32GB | 7,829 | 9,000 | 6,579 | gpuprix 14.11 (ASUS TUF, in stock); hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20): Jacob 8,999, Galaxus 9,133 (2026-11-14/17, page (aggregators)) | 32 | GDDR7 | 1,792 | 14,966 (n=1555) | 300.4 |
| GeForce RTX 5080 16GB | 1,969 | 2,250 | 1,655 | Joybuy, Gigabyte Windforce SFF; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 16 | GDDR7 | 960 | 9,138 (n=1432) | 184.7 |
| GeForce RTX 5070 Ti 16GB | 1,399 | - | 1,176 | Joybuy; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page) | 16 | GDDR7 | 896 | 7,589 (n=1416) | 182.4 |
| GeForce RTX 5070 12GB | 929 | - | 781 | MSI Ventus 2X OC; hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page (aggregator)) | 12 | GDDR7 | 672 | 6,174 (n=914) | 128.2 |
| GeForce RTX 4090 24GB (used) | 2,650 | 3,000 | 2,227 | Kleinanzeigen asking price, re-checked 18.11.2026; new from about 4,790 (2026-11-18, page (asking prices)) | 24 | GDDR6X | 1,008 | 11,061 (n=527) | 189.0 |
| GeForce RTX 4080 Super 16GB | 2,708 | - | 2,276 | amazon.de via gpuprix, new; used about 1,000-1,800 (Kleinanzeigen); re-checked 18.11.2026 (2026-11-18, -) | 16 | GDDR6X | 736 | 8,419 (n=239) | 147.5 |
| GeForce RTX 3090 24GB (used) | 1,250 | 1,500 | 1,050 | Kleinanzeigen asking prices 1,250-2,000 (2026-11-17, page (asking prices)) | 24 | GDDR6X | 936 | 5,412 (n=630) | 161.9 |
| AMD Radeon AI PRO R9700 32GB | 2,102 | 1,622 | 1,766 | Amazon.de via gpuprix (Gigabyte AI TOP); snippets 1,999-2,316 (2026-11-14, page (aggregator)) | 32 | GDDR6 | 640 | 3,209 (n=11) | 152.7 |
| AMD Radeon PRO W7900 48GB | 3,516 | 3,700 | 2,955 | Jacob.de (search snippet, undated) (undated, snippet) | 48 | GDDR6 ECC | 864 | 3,790 (n=2) | no data |
| AMD Radeon RX 9070 XT 16GB | 949 | - | 797 | hardwaredealz.com price comparison, re-checked 18.11.2026 (2026-11-18, page (aggregator)) | 16 | GDDR6 | 640 | 3,279 (n=676) | 142.0 |
| Intel Arc Pro B60 24GB | 960 | - | 807 | Amazon.de via gpuprix (Maxsun Milestone 24G) (2026-11-14, page (aggregator); 3-month median 893, 12-month low 683 per same page; undated Geizhals snippets 669-685 EUR not verified) | 24 | GDDR6 | 456 | 2,133 (n=5) | 68.1 |
| Intel Arc Pro B70 32GB | 1,599 | 1,581 | 1,344 | Geizhals via PCGH (ASRock Arc Pro B70 Creator lowest; Intel reference 1689; Asus UGen 1729, UVP 1799); Amazon.de via gpuprix 1679 (Asus UGen) (2026-10-26, page (PCGH article 27.10.2026 quoting Geizhals); gpuprix 2026-11-14) | 32 | GDDR6 | 608 | 3,313 (n=1) | 112.9 |
| Intel Arc Pro B65 32GB | 1,687 | - | 1,418 | Amazon.de via gpuprix (ASRock Arc Pro B65 Creator) (2026-11-14, page (aggregator); 3-month median 1401 per same page) | 32 | GDDR6 | 608 | no data | no data |
| Intel Arc Pro B60 Dual 48GB (Maxsun) | - | - | - | GameMachines.de list price 1499 EUR brutto (1259.66 net), first listing then delisted/sold out; US 1200 USD at Maxsun (2025-08-23, stale news (PCGH 23.08.2025); no current German offer found, price cells left empty) | 48 (2x24) | GDDR6 | 2x456 | no data | no data |
| Intel Arc Pro B50 16GB | 569 | 539 | 478 | Amazon.de via gpuprix (Gunnir B50 LP); typical = tracker 3-month median (2026-11-14, page (aggregator)) | 16 | GDDR6 | 224 | 1,546 (n=10) | 47.7 |
| Intel Arc B580 12GB | 387 | - | 325 | Geizhals via hardwaredealz.com (ASRock B580 Challenger OC); gpuprix: ASRock 321 and Intel LE used 407, both out of stock (2026-11-17, page, undated snippet (fetched today); gpuprix 3-month median 317 (2026-11-14) suggests cheaper offers when in stock) | 12 | GDDR6 | 456 | 2,373 (n=124) | 72.0 |
| Intel Arc B570 10GB | 299 | - | 251 | Geizhals via hardwaredealz.com; gpuprix Amazon.de ASRock Challenger OC 300 in stock (2026-11-17, page, undated snippet (fetched today); gpuprix 2026-11-14 (300)) | 10 | GDDR6 | 380 | 1,853 (n=7) | 50.5 |
| Intel Arc A770 16GB | 304 | - | 255 | Alternate via gpuprix (ASRock A770 Challenger SE OC), out of stock (2026-11-14, page (aggregator); EOL card, no in-stock offer seen) | 16 | GDDR6 | 560 | 2,448 (n=55) | 53.1 |

## 2. Compute units and throughput

| Card | CUDA cores / shaders | Tensor | RT | Bus bit | FP32 TFLOPS | FP16/BF16 dense | FP8 dense | FP4 dense | Spec verification |
|---|---|---|---|---|---|---|---|---|---|
| RTX A5000 24GB | 8192 | 256 (3rd) | 64 (2nd) | 384 | 27.8 | 111 | n/a | n/a | V: datasheet; FP16 dense D (sparse/2) |
| RTX 5000 Ada 32GB | 12800 | 400 (4th) | 100 (3rd) | 256 | 65.3 | 261 | 522 | n/a | V: datasheet; tensor dense D |
| RTX A4000 16GB | 6144 | 192 (3rd) | 48 (2nd) | 256 | 19.2 | 77 | n/a | n/a | V: datasheet; bus U; FP16 dense D |
| GeForce RTX 5060 Ti 16GB | 4608 | 144 (5th) U | 36 (4th) U | 128 | 23.7 | 95 (FP16 acc) | 190 D | 380 D | V: nvidia.com cores/VRAM/TGP; bandwidth U; TFLOPS from Wikipedia |
| GeForce RTX 5060 Ti 8GB | 4608 | 144 (5th) U | 36 (4th) U | 128 | 23.7 | 95 (FP16 acc) | 190 D | 380 D | as 16GB |
| RTX PRO 6000 Blackwell Workstation 96GB | 24064 U | 752 (5th) U | 188 (4th) U | 512 | 125 | ~500 D | ~1000 D | 2000 D (4000 sparse V) | V: product page (VRAM, BW, FP32, TDP); core counts third-party |
| RTX PRO 6000 Blackwell Max-Q 96GB | 24064 | 752 (5th) U | 188 (4th) U | 512 | 110 | ~439 D | ~878 D | 1756 D (3511 sparse V) | V: NVIDIA Max-Q datasheet |
| RTX PRO 6000 Blackwell Server 96GB | 24064 | 752 (5th) U | 188 (4th) | 512 | 120 | ~500 D | ~1000 D | ~2000 D | V: NVIDIA server page |
| RTX PRO 5000 Blackwell 72GB | 14080 | 440 (5th) U | 110 (4th) U | 384 | 65 | ~258 D | ~516 D | 1032 D (2064 sparse V) | V: NVIDIA datasheet + product page |
| RTX PRO 5000 Blackwell 48GB | 14080 | 440 (5th) U | 110 (4th) U | 384 | 65 | ~258 D | ~516 D | 1032 D (2064 sparse V) | V: NVIDIA datasheet + product page |
| RTX PRO 4500 Blackwell 32GB | 10496 | 328 (5th) | 82 (4th) | 256 | 51 | ~202 D | ~404 D | 808 D (1617 sparse V) | V: NVIDIA WE datasheet, Lenovo guide |
| RTX PRO 4000 Blackwell 24GB | 8960 | 280 (5th) U | 70 (4th) U | 192 | 40 | ~161 D | ~323 D | 645 D (1290 sparse V) | V: NVIDIA page/datasheet (140 W PNY vs 145 W NVIDIA) |
| RTX PRO 4000 Blackwell SFF 24GB | 8960 | 280 (5th) U | 70 (4th) U | 192 | 24 | ~96 D (770 AI TOPS / 8) | n/l | n/l | V: PNY SFF datasheet |
| RTX 6000 Ada 48GB | 18176 | 568 (4th) | 142 (3rd) | 384 | 91.1 | ~364 D | ~728 D | n/a | V: datasheet; bandwidth U |
| RTX 4500 Ada 24GB | 7680 | 240 (4th) | 60 (3rd) | 192 | 39.6 | ~158 D | ~317 D | n/a | V: datasheet |
| RTX 4000 Ada 20GB | 6144 | 192 (4th) | 48 (3rd) | 160 | 26.7 | ~82 D | ~164 D | n/a | V: datasheet |
| L40S 48GB | 18176 | 568 (4th) | 142 (3rd) | 384 | 91.6 | 362 | 733 | n/a | V: NVIDIA L40S page |
| RTX A6000 48GB (used) | 10752 | 336 (3rd) | 84 (2nd) | 384 | 38.7 | ~155 D | n/a | n/a | V: datasheet |
| A100 80GB PCIe | 6912 | 432 (3rd) U | none | 5120 | 19.5 | 312 | n/a | n/a | V: A100 datasheet |
| GeForce RTX 5090 32GB | 21760 | 680 (5th) U | 170 (4th) U | 512 | 104.8 | 419 (FP16 acc; ~210 FP32 acc) | 838 D | 1676 D | V: nvidia.com; BW/FP32 Wikipedia |
| GeForce RTX 5080 16GB | 10752 | 336 (5th) U | 84 (4th) U | 256 | 56.3 | 225 (FP16 acc) | 450 D | 900 D | V: nvidia.com; BW/FP32 Wikipedia |
| GeForce RTX 5070 Ti 16GB | 8960 | 280 (5th) U | 70 (4th) U | 256 | 43.9 | 177 (FP16 acc) | 352 D | 703 D | V: nvidia.com; BW/FP32 Wikipedia |
| GeForce RTX 5070 12GB | 6144 | 192 (5th) U | 48 (4th) U | 192 | 30.9 | 124 (FP16 acc) | 247 D | 494 D | V: nvidia.com; BW/FP32 Wikipedia |
| GeForce RTX 4090 24GB (used) | 16384 | 512 (4th) | 128 (3rd) | 384 | 82.6 | 330 (FP16 acc; ~165 FP32 acc) | 660 D | n/a | V: nvidia.com; others Wikipedia |
| GeForce RTX 4080 Super 16GB | 10240 | 320 (4th) | 80 (3rd) | 256 | 51.3 | n/l | 418 D | n/a | V: nvidia.com; others Wikipedia |
| GeForce RTX 3090 24GB (used) | 10496 | 328 (3rd) | 82 (2nd) | 384 | 35.6 | 142 (FP16 acc) | n/a | n/a | V: nvidia.com; others Wikipedia |
| AMD Radeon AI PRO R9700 32GB | 4096 SP (64 CU) | 128 AI accel. | 64 RA | 256 | 47.8 | ~191 U | ~383 U | n/a | V: ServeTheHome, Wikipedia; FP8/FP16 matrix U |
| AMD Radeon PRO W7900 48GB | 6144 SP (96 CU) | 192 AI accel. | 96 RA | 384 | 61 | ~122 U | n/a | n/a | U: snippets only (AMD pages timed out) |
| AMD Radeon RX 9070 XT 16GB | 4096 SP (64 CU) | 128 AI accel. | 64 RA | 256 | 48.7 | 195 | 389 | n/a | V-wiki |
| Intel Arc Pro B60 24GB | 2560 shaders / 20 Xe cores | 160 XMX | 20 | 192 | 12.3 | ~98 U (INT8 197 TOPS V) | n/a | n/a | V: intel.com spec page; gpuprix page (ECC supported, 200 W) |
| Intel Arc Pro B70 32GB | 4096 shaders / 32 Xe cores | 256 XMX | 32 | 256 | 22.9 | n/l (INT8 367 TOPS dense) | n/a | n/a | V: PCGH + gpuprix (shaders, bus, bw, TDP, ECC, 2 slots); RT cores and FP32 not verified, empty |
| Intel Arc Pro B65 32GB | 2560 shaders / 20 Xe cores | 160 XMX | 20 | 256 | 12.3 | n/l (INT8 197 TOPS peak) | n/a | n/a | V: gpuprix page (cores, VRAM, bw, TFLOPS, TDP, ECC); cooling and vGPU not checked |
| Intel Arc Pro B60 Dual 48GB (Maxsun) | 5120 shaders / 40 Xe cores (2x BMG-G21) | 320 XMX (2x160) | 40 D (2x20) | 2x192 | 24.6 (2x12.3) | - | n/a | n/a | V: PCGH article (shaders, Xe, VRAM, bus, bw, TDP range); FP32 and XMX doubled from single B60, not seen on page |
| Intel Arc Pro B50 16GB | 2048 shaders / 16 Xe cores | 128 XMX | 16 | 128 | 10.65 | - | n/a | n/a | V: gpuprix page (shaders, Xe, bw, TFLOPS, TDP); XMX derived at 8 per Xe core, not seen |
| Intel Arc B580 12GB | 2560 shaders / 20 Xe cores | 160 XMX | 20 | 192 | 14.6 | - | n/a | n/a | V: gpuprix page (shaders, bus, bw, TDP, boost 2850 MHz); FP32 computed 2560x2x2.85 GHz |
| Intel Arc B570 10GB | 2304 shaders / 18 Xe cores | 144 XMX | 18 | 160 | 12.7 | - | n/a | n/a | V: gpuprix page (shaders, bus, bw, TDP; page text also says 140 W); FP32 computed 2304x2x2.75 GHz |
| Intel Arc A770 16GB | 4096 shaders / 32 Xe cores | 512 XMX | 32 | 256 | 19.7 | - | n/a | n/a | V: gpuprix page; FP32 computed 4096x2x2.4 GHz |

## 3. Physical, sharing, licence

| Card | TDP W | Slots | Cooling | ECC | NVLink | vGPU (release) | MIG | Licence / software note |
|---|---|---|---|---|---|---|---|---|
| RTX A5000 24GB | 230 | 2 | blower (active) | yes | yes (2-way bridge) | yes (12.2, displayless) | no | - |
| RTX 5000 Ada 32GB | 250 | 2 | blower (active) | yes | no | yes (16.1) | no | - |
| RTX A4000 16GB | 140 | 1 | blower (active) | yes | no | no | no | - |
| GeForce RTX 5060 Ti 16GB | 180 | 2-2.5 (partner) | axial (open air) | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| GeForce RTX 5060 Ti 8GB | 180 | 2 (partner) | axial (open air) | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| RTX PRO 6000 Blackwell Workstation 96GB | 600 | 2 (137x305 mm, oversize) | double flow-through | yes | no | no (not listed) | yes, up to 4 | - |
| RTX PRO 6000 Blackwell Max-Q 96GB | 300 | 2 | blower (PNY) | yes | no | no (not listed) | yes, up to 4 | - |
| RTX PRO 6000 Blackwell Server 96GB | 600 | 2 (FHFL) | passive (server airflow) | yes | no | yes (19.0) | yes, up to 4 | - |
| RTX PRO 5000 Blackwell 72GB | 300 | 2 | blower (PNY) | yes | no | yes (20.2) | yes, up to 2 (2x36 GB) | - |
| RTX PRO 5000 Blackwell 48GB | 300 | 2 | blower (PNY) | yes | no | no (not listed) | yes, up to 2 (2x24 GB) | - |
| RTX PRO 4500 Blackwell 32GB | 200 | 2 | blower (PNY) | yes | no | no (only Server Ed.) | yes, up to 2 | - |
| RTX PRO 4000 Blackwell 24GB | 145 | 1 | blower (PNY) | yes | no | no | no | - |
| RTX PRO 4000 Blackwell SFF 24GB | 70 | 2 (half height) | active | yes | no | no | no | - |
| RTX 6000 Ada 48GB | 300 | 2 | blower (active) | yes | no | yes (15.2) | no | - |
| RTX 4500 Ada 24GB | 210 | 2 | blower (active) | yes | no | no | no | - |
| RTX 4000 Ada 20GB | 130 | 1 | blower (active) | yes | no | no | no | - |
| L40S 48GB | 350 | 2 | passive (server airflow) | yes | no | yes (16.1) | no | - |
| RTX A6000 48GB (used) | 300 | 2 | blower (active) | yes | yes (2-way, 112.5 GB/s) | yes (12.0) | no | - |
| A100 80GB PCIe | 300 | 2 | passive | yes | yes (bridge) | no (not listed) | yes, up to 7 | - |
| GeForce RTX 5090 32GB | 575 | 2 (FE) / 3-4 (partner) | axial / flow-through | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed); 12V-2x6 600 W connector |
| GeForce RTX 5080 16GB | 360 | 2 (FE) / 3+ (partner) | axial | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| GeForce RTX 5070 Ti 16GB | 300 | 2.5-3 (partner) | axial | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| GeForce RTX 5070 12GB | 250 | 2-2.5 | axial | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| GeForce RTX 4090 24GB (used) | 450 | 3-3.5 | axial | no (driver toggle on some) | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed); 12VHPWR connector |
| GeForce RTX 4080 Super 16GB | 320 | 3 | axial | no | no | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| GeForce RTX 3090 24GB (used) | 350 | 3 | axial | no | yes (2-way) | no | no | GeForce EULA s.2.8: 'not licensed for datacenter deployment' (term undefined; legal review needed) |
| AMD Radeon AI PRO R9700 32GB | 300 | 2 | blower on most models (conflicting sources) | yes (Linux only) | no (PCIe, up to 4 cards) | no SR-IOV | n/a | ROCm 7.14 officially supports it on Ubuntu LTS / RHEL |
| AMD Radeon PRO W7900 48GB | 295 | 3 (blower); 2-slot variant exists | blower | yes U | no | no | n/a | ROCm supported |
| AMD Radeon RX 9070 XT 16GB | 304 | 2.5-3 | axial | no | no | no | n/a | ROCm supported |
| Intel Arc Pro B60 24GB | 200 | 2 | blower (typ.) | yes | no | SR-IOV announced by Intel (phased); community reports | n/a | IPEX-LLM archived; llm-scaler vLLM is the Intel path |
| Intel Arc Pro B70 32GB | 230 (Intel ref; Asus 310, Sparkle up to 330) | 2 | blower | yes | no | SR-IOV official (Intel), 4 VFs | n/a | - |
| Intel Arc Pro B65 32GB | 200 | 2 | - | yes | no | - | - | - |
| Intel Arc Pro B60 Dual 48GB (Maxsun) | 250-400 configurable | 2 (Turbo blower); Liquid variant single-slot | - | - | no (two GPUs on one PCIe 5.0 x16 board) | - | - | - |
| Intel Arc Pro B50 16GB | 70 | 2 (low profile) | - | yes | no | SR-IOV official (Intel), 2 VFs | - | - |
| Intel Arc B580 12GB | 190 | 2 (varies) | - | - | no | - | - | - |
| Intel Arc B570 10GB | 150 | 2 (varies) | - | - | no | - | - | - |
| Intel Arc A770 16GB | 225 | 2 (varies) | - | - | no | - | - | - |

## 4. Notes

- **vGPU list** from docs.nvidia.com/vgpu/gpus-supported-by-vgpu.html (17.11.2026). Not listed: RTX PRO 6000 Workstation/Max-Q, PRO 5000 48 GB, PRO 4500 Workstation, PRO 4000, RTX 4500/4000 Ada, A4500, A4000, A100, all GeForce.
- **MIG** from NVIDIA MIG user guide. PRO 4500 Workstation: the guide lists 'RTX PRO 4500 Blackwell 32GB: max 2' without naming an edition, so the table says 'yes, up to 2'. NVIDIA's WE datasheet does not mention MIG and Lenovo's product guide says 'No support', so check before relying on it.
- **Blower** for PRO 5000/4500/4000 and 6000 Max-Q: PNY spec tables say 'Blower Active Fan'; NVIDIA only says 'Active'.
- **RTX 5060 Ti 8 GB vs 16 GB**: identical compute; Blender Open Data does not separate them. 8 GB limits LLM use to ~7B at 4-bit.
- **RTX 5070 price** (929) is the MSI Ventus 2X OC seen on hardwaredealz.com (page re-checked 18.11.2026). The CSV has no typical price for it.
- Cards without a usable price (A100 80GB PCIe, Arc Pro B60 Dual 48GB) stay in the table for specs and are skipped in price rankings.
- **Typical price below lowest price:** for the R9700 (2,102 low, 1,622 typical), Arc Pro B70 (1,599 / 1,581) and Arc Pro B50 (569 / 539) the CSV typical price is lower than the lowest price. The CSV does not say why; treat both with care.
- Full source list per row: CSV column `spec_sources`; raw research notes in `raw/`.
