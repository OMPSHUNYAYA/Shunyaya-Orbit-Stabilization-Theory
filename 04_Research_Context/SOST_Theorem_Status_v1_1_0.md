# SOST Theorem Status v1.1.0

## Principal classification

Status: **complete written computer-assisted proof**.

The theorem for all `n>=6` is proved from:

- direct invariant laws;
- constructive five-vertex realization;
- exact six-vertex completeness;
- six-vertex compression;
- locality of embedded six-vertex paths;
- a strictly decreasing arbitrary-order degree measure;
- exhaustive terminal cases;
- vertex-elimination induction.

## Exact finite theorem certificate

The order-six base is represented by a standalone spanning forest covering every one of the `32,768` states and containing exactly `96` roots, one for each admissible invariant label.

Every parent transition is independently checked as a legal monochromatic-triangle toggle.

## Independent exact verification

A separate Python flood-fill implementation reconstructs the small-order boundary.

A separate C++17 flood-fill engine exhaustively checks all `2,097,152` order-seven states and obtains exactly `192` components with zero invariant-classification mismatch.

## Constructive replay

A separate verifier executes the written compression algorithm using certified legal moves, including the degree-five, anchor-absent exceptional branch, and checks deterministic larger-order corpora.

## Historical comparison

No absolute historical-priority claim is made. Category-level comparison is maintained separately from the proof.

## Formalization

Proof-assistant formalization is not included in this version.
