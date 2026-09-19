# SOST Claim Boundary v1.1.0

## Exact theorem domain

The complete classification theorem applies to simple **labeled** graphs on `n>=6` vertices under the conditional move `000 <-> 111` on monochromatic vertex triples.

The theorem does not quotient by graph isomorphism or vertex relabeling.

## Finite theorem base

The exact six-vertex move partition is a theorem premise. Its role is finite and explicit.

The package provides both exhaustive reconstruction and a standalone spanning-forest certificate over all `32,768` six-vertex states.

The exact seven-vertex computation is independent verification only and is not used in the proof.

## Small orders

The invariant pair `(degree parity, edge count mod 3)` is complete at order three, incomplete at orders four and five, and complete for every order at least six.

## All-order proof boundary

The arbitrary-order theorem depends on symbolic locality, a strictly decreasing degree-compression measure, exhaustive terminal cases, and vertex-elimination induction.

Finite replay at larger orders supports those arguments but does not replace them.

## Framework boundary

The general SOST framework supplies finite-certificate concepts for reversible orbit systems. The principal graph theorem is one consequence and should not be read as proving that every reversible transformation family stabilizes or admits the same invariant form.

## Research comparison

Comparison material is category-level and separate from the proof chain. The focused audit supplies a novelty signal but does not assert absolute historical priority.

## Assurance boundary

The repository contains a complete written computer-assisted proof, a standalone finite theorem-base certificate, independent exact implementations, and an order-seven exhaustive holdout.

Proof-assistant formalization is not claimed.
