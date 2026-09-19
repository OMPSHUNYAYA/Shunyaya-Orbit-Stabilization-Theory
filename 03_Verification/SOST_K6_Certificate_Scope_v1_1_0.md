# SOST K6 Finite Theorem-Base Certificate v1.1.0

## Purpose

The six-vertex completeness statement is the only exhaustive finite theorem premise in the all-order classification proof.

This package represents that premise by a standalone certificate covering the entire `K_6` state space.

## Certificate structure

The file:

`certificates/SOST_K6_Orbit_Certificate_v1_1_0.json`

contains:

- the canonical edge order of `K_6`;
- the canonical triangle order;
- a parent state for every non-root graph state;
- the legal triangle index connecting each non-root state to its parent;
- `96` fiber records containing invariant label, root, size, and maximum certificate depth.

The parent relation is a spanning forest of the complete legal-move graph.

## What the standalone verifier proves

The standalone verifier checks from first principles that:

1. the certificate covers all `2^15=32,768` states exactly once;
2. every non-root parent transition is a legal `000 <-> 111` triangle toggle;
3. every parent transition preserves degree parity and edge count modulo `3`;
4. every parent chain terminates at one of exactly `96` roots;
5. the `96` roots have distinct admissible `(P,R)` labels;
6. every admissible label occurs;
7. each certified fiber agrees with its declared size;
8. all even-parity isolation targets and odd-parity anchored targets required by the proof occur in the appropriate fibers.

Because direct invariance prevents transitions between distinct labels, one connected certified tree per admissible label establishes exact six-vertex completeness.

## Independence

The standalone verifier does not import the SOST core library or theorem-core verifier.

The certificate generator and verifier are both included so that the finite witness can be regenerated and checked independently.
