# SOST Verification Scope v1.1.0

The repository distinguishes mathematical proof from computational verification.

## EXHAUSTIVE-FINITE

A declared finite case space is checked completely.

Examples:

- all five-vertex graph states for invariant realization;
- all `32,768` six-vertex graph states;
- all six-vertex compression targets;
- every parent transition in the standalone K6 spanning-forest certificate.

## EXHAUSTIVE-AT-ORDER

All states are checked at one fixed order.

The `n=7` holdout checks all `2,097,152` edge-colorings and audits all legal triangle transitions encountered by the flood-fill engine.

## CONSTRUCTIVE-REPLAY

A finite deterministic corpus is reduced using only actual legal moves generated from the certified K6 paths.

This layer tests the executable content of the symbolic compression and induction, including the exceptional degree-five, anchor-absent branch.

It is verification evidence, not a replacement for the universal proof.

## UNIVERSAL-WRITTEN

The claim is proved symbolically for arbitrary order.

The locality lemma, decreasing degree measure, exhaustive terminal case split, vertex-elimination induction, orbit-count formula, and binary quotient-growth theorem are universal written arguments.

## Independence

The exact `n=7` holdout is not a premise of the universal proof.

The standalone K6 certificate verifier and the independent partition verifier do not import the SOST core library.
