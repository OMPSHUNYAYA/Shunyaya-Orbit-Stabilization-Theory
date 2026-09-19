# SOST Verification Guide v1.1.0

## Requirements

- Python `3.10+`;
- Python standard library only;
- C++17 `g++` compiler for complete verification.

Run commands from the repository root.

## Repository self-test

```bash
python -B verify.py --self-test
```

## Complete verification

```bash
python -B verify.py --verify
```

Complete verification compiles and executes the exact `n=7` C++17 holdout.

If `g++` is installed but not found, ensure its `bin` directory is present in `PATH` and confirm with:

```bash
g++ --version
```

## Standalone K6 theorem-base certificate

```bash
python -B 03_Verification/SOST_K6_Standalone_Certificate_Verifier_v1_1_0.py --verify
```

The verifier reads:

```text
03_Verification/certificates/SOST_K6_Orbit_Certificate_v1_1_0.json
```

and does not import SOST library code.

## Constructive induction replay

```bash
python -B 03_Verification/SOST_Constructive_Induction_Replay_Verifier_v1_1_0.py --verify
```

This executes actual legal moves from the finite certificate inside larger complete graphs.

## Other individual verifiers

```bash
python -B 03_Verification/SOST_Theorem_Core_Verifier_v1_1_0.py --verify
python -B 03_Verification/SOST_Proof_Rigor_Audit_Verifier_v1_1_0.py --verify
python -B 03_Verification/SOST_Independent_Classification_Verifier_v1_1_0.py --verify
```

## Certificate regeneration

The K6 certificate can be regenerated independently:

```bash
python -B 03_Verification/SOST_K6_Certificate_Generator_v1_1_0.py --output 03_Verification/certificates/SOST_K6_Orbit_Certificate_v1_1_0.json
```

The regenerated certificate should then pass the standalone verifier.

## Research utilities

Label a graph:

```bash
python -B 02_Algorithms_and_Software/SOST_Orbit_Label_v1_1_0.py 06_Examples/sample_empty_K6.json
```

Compare two graphs at order at least six:

```bash
python -B 02_Algorithms_and_Software/SOST_Equivalence_Decision_v1_1_0.py 06_Examples/sample_empty_K6.json 06_Examples/sample_triangle_K6.json
```

Using `python -B` prevents bytecode-cache generation.
