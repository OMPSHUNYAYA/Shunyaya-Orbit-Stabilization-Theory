# Shunyaya Orbit Stabilization Theory (SOST)

## Exact orbit classification for the monochromatic-triangle toggle on labeled complete graphs

**Shunyaya Orbit Stabilization Theory (SOST) v1.1.0** proves an exact all-order orbit classification for a reversible, state-dependent graph dynamic.

For a simple graph `G` on `n` labeled vertices, a primitive move selects a vertex triple whose three induced edge bits are monochromatic and toggles all three:

`000 <-> 111`.

For every `n>=6`, the only orbit invariants are:

`P(G) = vertex degree-parity vector in F_2^n`

and

`R(G) = |E(G)| mod 3`.

Equivalently:

`G ~ H  iff  P(G)=P(H) and R(G)=R(H)`.

[![Version](https://img.shields.io/badge/Version-1.1.0-blue)](./VERSION)
[![Theorem](https://img.shields.io/badge/Theorem-All%20n%3E%3D6-brightgreen)](./01_Theory/SOST_Principal_Theorem_v1_1_0.md)
[![Proof](https://img.shields.io/badge/Proof-Computer--assisted-blue)](./04_Research_Context/SOST_Theorem_Status_v1_1_0.md)
[![K6 certificate](https://img.shields.io/badge/K6-32%2C768%20states%20%7C%2096%20fibers-brightgreen)](./03_Verification/SOST_K6_Standalone_Certificate_Verifier_v1_1_0.py)
[![K7 holdout](https://img.shields.io/badge/K7-2%2C097%2C152%20states%20%7C%20192%20orbits-brightgreen)](./03_Verification/SOST_Independent_Holdout_n7_v1_1_0.cpp)
[![Verification](https://img.shields.io/badge/Verification-Reproducible-brightgreen)](./05_Reproduction_and_Verification/SOST_Verification_Scope_v1_1_0.md)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](./05_Reproduction_and_Verification/SOST_Verification_Guide_v1_1_0.md)
[![C++](https://img.shields.io/badge/C%2B%2B-17-blue)](./05_Reproduction_and_Verification/SOST_Verification_Guide_v1_1_0.md)

[![Verify](https://github.com/OMPSHUNYAYA/Shunyaya-Orbit-Stabilization-Theory/actions/workflows/verify.yml/badge.svg)](https://github.com/OMPSHUNYAYA/Shunyaya-Orbit-Stabilization-Theory/actions/workflows/verify.yml)

---

## Repository summary

This repository establishes an exact stabilization theorem for monochromatic-triangle toggle dynamics on labeled complete graphs. The central result proves that for every `n>=6`, orbit equivalence is completely determined by the degree-parity vector and edge-count residue modulo `3`. The proof combines an exact `K_6` theorem-base certificate with constructive symbolic compression and induction, while an exhaustive `K_7` computation is retained as an independent holdout rather than a proof premise.

The resulting quotient has the exact form

`Q_n ~= {even parity vectors in F_2^n} x Z_3`,

with

`|Q_n| = 3*2^(n-1)`

and exact binary growth

`Q_(n+1) ~= Q_n x {0,1}`.

The repository includes the theorem and complete proof, finite certificates, constructive replay, independent exhaustive checks, machine-readable evidence, reproducible verification commands, and explicit claim/provenance boundaries.

---

## Principal theorem

Let `X_n` be the set of simple labeled graphs on `{0,...,n-1}`. A move on a vertex triple is legal exactly when its three induced edge bits are all `0` or all `1`; the move complements those three bits.

For every `n>=6`:

`G ~ H  iff  P(G)=P(H) and R(G)=R(H)`.

Thus:

`Q_n ~= {even parity vectors in F_2^n} x Z_3`,

so

`|Q_n| = 3*2^(n-1)`.

The quotient grows by one exact binary factor:

`Q_(n+1) ~= Q_n x {0,1}`.

The threshold is sharp and non-monotone:

`n=3 -> 7 orbits; (P,R) complete on realized labels`

`n=4 -> 32 orbits; (P,R) incomplete`

`n=5 -> 59 orbits; (P,R) incomplete`

`n=6 -> 96 orbits; (P,R) complete`

`n>=6 -> completeness persists for every larger order`.

[Principal theorem](./01_Theory/SOST_Principal_Theorem_v1_1_0.md) · [Complete proof](./01_Theory/SOST_Complete_Classification_Proof_v1_1_0.md) · [Exact quotient growth](./01_Theory/SOST_Exact_Quotient_Growth_v1_1_0.md)

---

## Why the threshold is six

The proof separates one finite exact kernel from a symbolic induction.

Five vertices are exactly sufficient to realize every admissible local pair consisting of an even degree-parity vector and an edge-count residue modulo `3`. This gives the local target grammar needed to control a sixth designated vertex.

At six vertices, the complete move graph has:

`32,768 states`

and exactly:

`96 = 3*2^5 orbits`.

Every admissible `(P,R)` label occurs in exactly one orbit. From that finite statement, the proof obtains two local compression operations:

- even local parity -> isolate a designated vertex;
- odd local parity -> retain exactly one incident edge to any selected anchor.

Triangle legality depends only on the three edges of the selected triangle, so a certified six-vertex move path embeds unchanged in every larger complete graph. The all-order induction then eliminates one vertex at a time.

The terminal degree analysis is exhaustive. After repeated reductions by four, the designated degree is at most five. The remaining cases are:

`0,2,4 -> even terminal isolation`

`1,3 -> odd terminal anchor compression`

`5 with anchor present -> direct odd anchor compression`

`5 with anchor absent -> two-stage exceptional compression`.

The reduction measure is the designated degree. Every nonterminal reduction decreases it by exactly four, so the compression process terminates.

[Proof architecture](./01_Theory/SOST_Proof_Architecture_v1_1_0.md) · [Proof rigor audit](./01_Theory/SOST_Proof_Rigor_Audit_v1_1_0.md)

---

## Finite theorem-base certificate

The order-six theorem base is shipped as a standalone finite certificate rather than only as a computation receipt.

The certificate contains a rooted spanning forest over all `32,768` six-vertex states. Each non-root state records:

- a parent state;
- the triangle used for the legal parent transition.

There are exactly `96` roots, one for every admissible `(P,R)` label.

The standalone verifier uses no SOST library code. It checks:

- every parent transition is a legal monochromatic-triangle toggle;
- every parent transition preserves `(P,R)`;
- every state reaches exactly one root;
- the `96` roots have distinct admissible invariant labels;
- every admissible label is represented;
- every six-vertex compression target required by the proof occurs in the corresponding certified fiber.

This converts the finite theorem premise into a compact, independently checkable witness structure.

[K6 certificate scope](./03_Verification/SOST_K6_Certificate_Scope_v1_1_0.md) · [Standalone verifier](./03_Verification/SOST_K6_Standalone_Certificate_Verifier_v1_1_0.py)

---

## Constructive all-order replay

A separate constructive verifier uses only legal triangle moves plus the certified six-vertex paths to execute the written compression algorithm.

It directly exercises:

- repeated degree reduction;
- even terminal isolation;
- odd terminal anchor compression;
- the degree-five, anchor-absent exceptional branch;
- recursive vertex elimination;
- canonical reduction at orders `8`, `9`, and `10` on deterministic test corpora.

The replay is verification evidence for the constructive induction. The all-order theorem remains the written proof.

[Constructive induction replay](./03_Verification/SOST_Constructive_Induction_Replay_Verifier_v1_1_0.py)

---

## Independent exact holdout

The exact order-seven computation remains outside the proof dependency chain.

A separate C++17 flood-fill engine checks all:

`2,097,152`

edge-colorings of `K_7` and obtains exactly:

`192 = 3*2^6`

components, with zero invariant-classification mismatches.

It also audits:

`18,350,080`

legal state/triangle transitions.

The `K_7` result is an independent falsification test, not a theorem premise.

---

## SOST framework boundary

SOST also records finite-certificate concepts for reversible orbit systems: quotient transport, branching coherence, complete summaries, finite obstruction interfaces, and theorem promotion from finite discovery to symbolic proof.

The graph theorem above is the complete all-order theorem established in this repository. The framework should not be read as claiming that arbitrary reversible systems admit the same invariant structure or stabilization law.

[Framework overview](./01_Theory/SOST_Framework_Overview_v1_1_0.md) · [Claim boundary](./04_Research_Context/SOST_Claim_Boundary_v1_1_0.md)

---

## Research lineage

SOST is mathematically self-contained. Its proof does not depend on SSDC or SSDD theorems. The projects form a research-method lineage:

`SSDC: representation discovery -> theorem discovery`

`SSDD: structural dynamics -> invariant geometry -> exact classification`

`SOST: reversible local dynamics -> invariant completeness -> stabilized orbit quotient`.

SSDC: https://github.com/OMPSHUNYAYA/Shunyaya-Structural-Discovery-Compiler

SSDD: https://github.com/OMPSHUNYAYA/Shunyaya-Structural-Discovery-Demonstration

---

## Research positioning

The mathematical development is independent of literature comparison.

A focused comparison audit across adjacent categories did not identify a direct match for the complete combination of:

`conditional monochromatic-triangle toggle`

`complete invariant (degree parity, edge count mod 3)`

`sharp permanent threshold n=6`

`|Q_n|=3*2^(n-1)`

`Q_(n+1) ~= Q_n x {0,1}`.

This is a strong novelty signal, not an assertion of absolute historical priority. The repository therefore uses category-level positioning and contains no bibliography of comparison literature.

[Research positioning](./04_Research_Context/SOST_Research_Positioning_v1_1_0.md)

---

## Verification

From the repository root:

```bash
python -B verify.py --self-test
python -B verify.py --verify
```

Complete verification combines:

- theorem-core finite enumeration;
- standalone `K_6` certificate verification;
- constructive induction replay;
- proof-rigor checks;
- independent small-order flood fill;
- exhaustive C++17 `K_7` holdout.

The Python paths use only the standard library. Complete verification additionally requires a C++17 `g++` compiler on `PATH`.

[Verification guide](./05_Reproduction_and_Verification/SOST_Verification_Guide_v1_1_0.md) · [Verification scope](./05_Reproduction_and_Verification/SOST_Verification_Scope_v1_1_0.md)

---

## Repository map

| Area | Contents |
|---|---|
| [`01_Theory/`](./01_Theory/) | theorem, complete proof, quotient growth, framework, proof architecture, rigor audit, research summary |
| [`02_Algorithms_and_Software/`](./02_Algorithms_and_Software/) | core move/invariant utilities, equivalence tool, recursive representatives |
| [`03_Verification/`](./03_Verification/) | theorem-core verifier, standalone K6 certificate, constructive induction replay, independent classification verifier, exact K7 holdout |
| [`04_Research_Context/`](./04_Research_Context/) | claim boundary, theorem status, dependency/evidence maps, category-level positioning |
| [`05_Reproduction_and_Verification/`](./05_Reproduction_and_Verification/) | verification guide/scope, computational integrity, package binding, receipts |
| [`06_Examples/`](./06_Examples/) | machine-readable sample states |

---

## Integrity, provenance, and rights

The SHA-256 integrity record binds computational and machine-readable scientific artifacts. Editable explanatory documents are intentionally not hash-bound.

The repository contains project-authored mathematical exposition and implementation. It does not redistribute third-party research text, figures, tables, datasets, or software source. Category-level research comparison is independently written and non-bibliographic.

Software, verification code, workflows, and machine-readable scientific artifacts are provided under Apache License 2.0. Project-authored theorem exposition and research documentation are provided under CC BY-NC 4.0, subject to the repository notices.

Copyright and license terms govern project-authored expression and implementation; they do not assert ownership of mathematical facts, abstract theorem statements, equations, or independently developed proofs.

[Copyright notice](./COPYRIGHT_NOTICE.txt) · [License map](./LICENSE) · [Third-party and provenance notices](./THIRD_PARTY_NOTICES.txt)
