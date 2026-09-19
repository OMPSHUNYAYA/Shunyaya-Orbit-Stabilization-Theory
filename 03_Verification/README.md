# Verification

The verification layer contains independent finite reconstruction, a standalone theorem-base certificate, constructive replay, and an exact order-seven holdout.

- `SOST_Theorem_Core_Verifier_v1_1_0.py` — union-find reconstruction of the finite theorem base and compression targets.
- `SOST_K6_Certificate_Generator_v1_1_0.py` — regenerates the complete six-vertex spanning-forest certificate.
- `SOST_K6_Standalone_Certificate_Verifier_v1_1_0.py` — checks the certificate without importing SOST library code.
- `SOST_Constructive_Induction_Replay_Verifier_v1_1_0.py` — executes the written compression/elimination algorithm using actual certified legal moves.
- `SOST_Independent_Classification_Verifier_v1_1_0.py` — separate small-order flood fill and C++17 holdout launcher.
- `SOST_Proof_Rigor_Audit_Verifier_v1_1_0.py` — checks dependency acyclicity, locality, termination measure, and terminal-case exhaustiveness.
- `SOST_Independent_Holdout_n7_v1_1_0.cpp` — exhaustive order-seven flood fill over all `2,097,152` states.

The order-seven holdout is verification evidence and is not used in the written proof.
