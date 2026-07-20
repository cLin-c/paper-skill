# Reproducible benchmark

Run the public deterministic safety-gate benchmark:

```bash
python tools/run_benchmark.py
```

The eight synthetic cases cover a ready package, missing identity, unsupported claims, broken evidence links, suspicious DOI metadata, falsely verified references, unresolved author input, and missing reporting-guideline evidence.

Current result: **8/8 classifications correct**. The committed machine-readable result is in [results.json](results.json). This benchmark measures structured package risk classification only. It does not measure prose quality, scientific novelty, or acceptance probability. Future benchmark tracks will add blinded human evaluation for translation fidelity, claim–evidence alignment, and reviewer-response coverage.
