# intel-extra notes (2026-11-17)

New hardware only; used cards are not listed.

Rows: B70 (updated), B65 (new), B60 24GB (updated), B60 Dual 48GB Maxsun, B50, B580, B570, A770.

- **B60 32GB does not exist.** The 32 GB card with B60-class silicon is the Arc Pro B65 (20 Xe, 32 GB, 608 GB/s, 200 W, partner boards only, e.g. ASRock Creator). The 32 GB B70 is the bigger die (32 Xe).
- **Prices:** B70 from Geizhals 26.10.2026 via PCGH (1599 / 1689 / 1729 / 1783). Other prices come from gpuprix (tracker, Amazon.de/Alternate, 2026-11-14), B580/B570 from hardwaredealz (Geizhals, undated snippet). **A770:** no orderable new offer (end of life), so it has no price in the CSV; the last seen price (304 EUR) is not used. "Typical" prices (B70, B50) are 3-month medians from a price tracker and can be below the lowest price, which is the cheapest offer on the check date. Direct shop and Geizhals pages were not readable; Galaxus timed out.
- **B60 Dual 48GB:** only a stale GameMachines listing (1499 EUR, Aug 2025, sold out). Price cells empty on purpose. Dual-GPU: two separate 24 GB devices, not one 48 GB pool.
- **Not on sale:** B770 / Big Battlemage consumer (BMG-G31) and Celestial: no launch found (no CES 2026 showing, only leaks). Not included.
- **Blender:** values are Blender Open Data 4.5.0 oneAPI medians (same version as the master). Newer versions are in blender_note; B65 only exists from 5.2.0. API: `...query/?compute_type=ONEAPI&blender_version=4.5.0&group_by=device_name&response_type=datatables`.
- **llama.cpp #10879:** FA-enabled table used (same as existing B60 row), no-FA values in the note. B580/B570 pp512 drops sharply with FA, so pp numbers are unreliable. B70 tg128 (113) is about 1.7x the B60 (112.89 vs 68.06).
- **Computed, not seen:** FP32 of B580 (14.6), B570 (12.7), A770 (19.7) from shaders x2 x boost clock. B50 XMX count derived. B70 RT cores (32) and FP32 (22.9) were added on 18 Nov 2026 from Intel material.
- vGPU/SR-IOV: Intel's support article 000103382 (reviewed 2026-10-01) lists B70 = 4 VFs and B50 = 2 VFs, so B70 and B50 are official; no B60 count from Intel, so B60 stays "community". Read via a summarising tool, re-check in a browser. Other cards not checked.
- Not covered: Flex / Gaudi PCIe cards (no search done), Intel Arc Pro B50 slot count, cooling for most rows.
