# GPU master table


Legend: **D** = derived by us (e.g. dense = sparse / 2, or FP16 = FP4-sparse / 8), **U** = unverified (third-party or memory), everything else was seen on a manufacturer page/datasheet (or Wikipedia for GeForce bandwidth/FP32). Tensor figures are **dense**. GeForce FP16 figures are with FP16 accumulate; with FP32 accumulate (typical for training) GeForce runs at half that rate, pro cards do not.

Price evidence: most prices come from hardwaredealz.com (Geizhals data, page time 17.11.2026 08:20) because Geizhals, idealo, Mindfactory, Cyberport etc. blocked automated access. AMD/Intel prices come from gpuprix.com (14.11.2026) or search snippets. Used prices are Kleinanzeigen **asking** prices. See SUMMARY.md.

## 1. Price, memory, benchmark headline

| Card | Price low (brutto) | Typical | Net (low) | Price source / date | VRAM GB | Mem | BW GB/s | Blender 4.5 (n) | llama 7B tg t/s |
|---|---|---|---|---|---|---|---|---|---|
| RTX A5000 24GB | 4,225 | - | 3,550 | it-market.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (only offer) (2026-11-17, page) | 24 | GDDR6 | 768 | 4,390 (n=24) | 135.8 |
| RTX 5000 Ada 32GB | 5,199 | 5,500 | 4,369 | Caseking via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (one SKU; 5 shops) (2026-11-17, page) | 32 | GDDR6 | 576 | 5,677 (n=9) | no data |
| RTX A4000 16GB | 1,964 | - | 1,650 | it-market.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (931 offer at PC-KING looks wrong) (2026-11-17, page) | 16 | GDDR6 | 448 | 2,956 (n=44) | 85.2 |
| GeForce RTX 5060 Ti 16GB | 909 | 950 | 764 | Joybuy via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (Gigabyte Aero OC; 10 shops 909-995) (2026-11-17, page) | 16 | GDDR7 | 448 | 4,309 (n=655) | 93.5 |
| GeForce RTX 5060 Ti 8GB | - | - | - | no DE offer found (2026-11-17, -) | 8 | GDDR7 | 448 | 4,309 (n=655) | no data |
| RTX PRO 6000 Blackwell Workstation 96GB | 17,548 | 18,230 | 14,746 | 25now via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Alternate 19,600 (2026-11-17, page) | 96 | GDDR7 ECC | 1,792 | 16,737 (n=205) | 281.1 |
| RTX PRO 6000 Blackwell Max-Q 96GB | 16,490 | 16,800 | 13,857 | BA-Computer / Proshop via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (2026-11-17, page) | 96 | GDDR7 ECC | 1,792 | 14,746 (n=39) | no data |
| RTX PRO 6000 Blackwell Server 96GB | 20,599 | 21,000 | 17,310 | electronis.de etc. via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (PNY Server SKU) (2026-11-17, page) | 96 | GDDR7 ECC | 1,597 | 15,519 (n=28) | no data |
| RTX PRO 5000 Blackwell 72GB | 14,099 | 15,100 | 11,848 | PC-KING / Mindfactory via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (AT shops 11,999) (2026-11-17, page) | 72 | GDDR7 ECC | 1,344 | 10,849 (n=4) | no data |
| RTX PRO 5000 Blackwell 48GB | 8,119 | 8,500 | 6,823 | alza.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Proshop 8,400; Galaxus 8,508 (2026-11-17, page) | 48 | GDDR7 ECC | 1,344 | 10,929 (n=7) | no data |
| RTX PRO 4500 Blackwell 32GB | 4,559 | 4,800 | 3,831 | alza.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Galaxus 4,813; Alternate 5,025 (2026-11-17, page) | 32 | GDDR7 ECC | 896 | 8,487 (n=17) | 168.9 |
| RTX PRO 4000 Blackwell 24GB | 2,775 | 3,050 | 2,332 | esus it via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (retail); bulk 2,950; Alternate 3,189 (2026-11-17, page) | 24 | GDDR7 ECC | 672 | 6,256 (n=40) | 136.4 |
| RTX PRO 4000 Blackwell SFF 24GB | 3,189 | 3,290 | 2,680 | electronis.de / PC-KING via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (2026-11-17, page) | 24 | GDDR7 ECC | 432 | no data | no data |
| RTX 6000 Ada 48GB | 9,008 | 9,600 | 7,570 | electronis.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20); Galaxus 10,049 (2026-11-17, page) | 48 | GDDR6 ECC | 960 | 10,655 (n=20) | 179.5 |
| RTX 4500 Ada 24GB | 2,786 | 2,950 | 2,341 | Galaxus via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (2026-11-17, page) | 24 | GDDR6 ECC | 432 | 5,674 (n=5) | no data |
| RTX 4000 Ada 20GB | 1,940 | - | 1,630 | grafikkarten.com via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (only offer) (2026-11-17, page) | 20 | GDDR6 ECC | 360 | 4,446 (n=16) | no data |
| L40S 48GB | 10,403 | 10,500 | 8,742 | Proshop.de via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (AT 9,555) (2026-11-17, page) | 48 | GDDR6 ECC | 864 | 7,848 (n=8) | no data |
| RTX A6000 48GB (used) | 4,000 | 4,500 | 3,361 | Kleinanzeigen asking prices 4,000-5,000 (VB) (2026-11-17, page (asking prices)) | 48 | GDDR6 ECC | 768 | 5,145 (n=8) | 144.9 |
| A100 80GB PCIe | - | - | - | no offer found (2026-11-17, -) | 80 | HBM2e ECC | 1,935 | no data | 200.9 |
| GeForce RTX 5090 32GB | 7,829 | 9,000 | 6,579 | gpuprix 14.11 (ASUS TUF, in stock); hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20): Jacob 8,999, Galaxus 9,133 (2026-11-14/17, page (aggregators)) | 32 | GDDR7 | 1,792 | 14,966 (n=1555) | 300.4 |
| GeForce RTX 5080 16GB | 2,195 | 2,250 | 1,845 | notebooksbilliger / computeruniverse / Cyberport via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (MSI Gaming Trio OC) (2026-11-17, page) | 16 | GDDR7 | 960 | 9,138 (n=1432) | 184.7 |
| GeForce RTX 5070 Ti 16GB | 1,745 | 1,770 | 1,466 | Galaxus via hardwaredealz.com (Geizhals feed, page 17.11.2026 08:20) (ASUS TUF OC); Alternate 1,795 (2026-11-17, page) | 16 | GDDR7 | 896 | 7,589 (n=1416) | 182.4 |
| GeForce RTX 5070 12GB | 1,594 | - | 1,339 | Geizhals 'ab' via hardwaredealz (undated; looks high, verify) (undated, page (aggregator)) | 12 | GDDR7 | 672 | 6,174 (n=914) | no data |
| GeForce RTX 4090 24GB (used) | 2,400 | 3,000 | 2,017 | Kleinanzeigen asking prices 2,400-3,200 (2026-11-17, page (asking prices)) | 24 | GDDR6X | 1,008 | 11,061 (n=527) | 189.0 |
| GeForce RTX 4080 Super 16GB | - | - | - | no offer found (2026-11-17, -) | 16 | GDDR6X | 736 | 8,419 (n=239) | no data |
| GeForce RTX 3090 24GB (used) | 1,250 | 1,500 | 1,050 | Kleinanzeigen asking prices 1,250-2,000 (2026-11-17, page (asking prices)) | 24 | GDDR6X | 936 | 5,412 (n=630) | 161.9 |
| AMD Radeon AI PRO R9700 32GB | 2,102 | 2,200 | 1,766 | Amazon.de via gpuprix (Gigabyte AI TOP); snippets 1,999-2,316 (2026-11-14, page (aggregator)) | 32 | GDDR6 | 640 | 3,209 (n=11) | 152.7 |
| AMD Radeon PRO W7900 48GB | 3,516 | 3,700 | 2,955 | Jacob.de (search snippet, undated) (undated, snippet) | 48 | GDDR6 ECC | 864 | 3,790 (n=2) | no data |
| AMD Radeon RX 9070 XT 16GB | 1,052 | - | 884 | Geizhals 'ab' via hardwaredealz (undated) (undated, page (aggregator)) | 16 | GDDR6 | 640 | 3,279 (n=676) | no data |
| Intel Arc Pro B60 24GB | 960 | - | 807 | Amazon.de via gpuprix (Maxsun) (2026-11-14, page (aggregator)) | 24 | GDDR6 | 456 | 2,133 (n=5) | 68.1 |
| Intel Arc Pro B70 32GB | - | - | - | no DE offer found (US MSRP 949 USD) (2026-11-17, -) | 32 | GDDR6 | 608 | 3,313 (n=1) | no data |

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
| RTX PRO 4000 Blackwell SFF 24GB | 8960 | 280 (5th) U | 70 (4th) U | 192 | - | n/l | n/l | n/l | V: PNY SFF datasheet |
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
| AMD Radeon RX 9070 XT 16GB | 4096 SP (64 CU) | 128 AI accel. | 64 RA | 256 | 48.7 | ~191 U | ~383 U | n/a | V-wiki |
| Intel Arc Pro B60 24GB | 20 Xe cores | 160 XMX | 20 | 192 | 12.3 | ~98 U (INT8 197 TOPS V) | n/a | n/a | V: intel.com spec page |
| Intel Arc Pro B70 32GB | 32 Xe cores | 256 XMX | U | 256 | - | n/l (INT8 367 TOPS dense) | n/a | n/a | V: Igor's Lab |

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
| RTX PRO 4500 Blackwell 32GB | 200 | 2 | blower (PNY) | yes | no | no (only Server Ed.) | unconfirmed, likely no (Server Ed.: 2) | - |
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
| AMD Radeon AI PRO R9700 32GB | 300 | 2 | blower on most models (conflicting sources) | unclear | no (PCIe, up to 4 cards) | no SR-IOV | n/a | ROCm 7.14 officially supports it on Ubuntu LTS / RHEL |
| AMD Radeon PRO W7900 48GB | 295 | 3 (blower); 2-slot variant exists | blower | yes U | no | no | n/a | ROCm supported |
| AMD Radeon RX 9070 XT 16GB | 304 | 2.5-3 | axial | no | no | no | n/a | ROCm supported |
| Intel Arc Pro B60 24GB | 200 | 2 | blower (typ.) | unclear | no | SR-IOV community only | n/a | IPEX-LLM archived; llm-scaler vLLM is Intel's path |
| Intel Arc Pro B70 32GB | 230 | 2 | varies | n/l | no | SR-IOV community only | n/a | - |

## 4. Notes

- **vGPU list** from docs.nvidia.com/vgpu/gpus-supported-by-vgpu.html (17.11.2026). Not listed: RTX PRO 6000 Workstation/Max-Q, PRO 5000 48 GB, PRO 4500 Workstation, PRO 4000, RTX 4500/4000 Ada, A4500, A4000, A100, all GeForce.
- **MIG** from NVIDIA MIG user guide. PRO 4500 Workstation: the guide lists 'RTX PRO 4500 Blackwell 32GB: 2' without an edition, but NVIDIA's WE datasheet does not mention MIG and Lenovo's product guide says 'No support'. Treat as unsupported until confirmed.
- **Blower** for PRO 5000/4500/4000 and 6000 Max-Q: PNY spec tables say 'Blower Active Fan'; NVIDIA only says 'Active'.
- **RTX 5060 Ti 8 GB vs 16 GB**: identical compute; Blender Open Data does not separate them. 8 GB limits LLM use to ~7B at 4-bit.
- **RTX 5070 price** (1,594) is an undated Geizhals 'ab' value and looks implausibly close to the 5070 Ti; verify.
- Cards without a usable price (A100, 4080 Super, B70, 5060 Ti 8GB) stay in the table for specs and are skipped in price rankings.
- Full source list per row: CSV column `spec_sources`; raw research notes in `raw/`.
