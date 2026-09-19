# SOST Proof Rigor Audit v1.1.0

## Audit questions

The proof is checked against the following failure modes.

### Circular use of the all-order theorem in the finite base

Not present. The order-six theorem is certified directly from the finite move graph.

### Use of the order-seven holdout as a proof premise

Not present. The holdout is absent from the theorem dependency chain.

### Illicit embedding of a six-vertex path into larger order

Not present. Legality of each primitive move depends only on the three edges of its selected triangle. Outside edges are neither read nor toggled.

### Loss of the global invariant during compression

Not present. Every certified compression path lies inside one six-vertex invariant fiber, and every primitive move preserves degree parity and edge count modulo three.

### Nontermination of arbitrary-order compression

Not present. The reduction measure is:

`mu(G,v)=deg_G(v)`.

Whenever `mu>5`, one embedded six-vertex compression removes exactly four incident edges, so:

`mu_new=mu_old-4`.

The process therefore reaches `mu<=5` after finitely many steps.

### Incomplete terminal case analysis

Not present. Once `mu<=5`, the cases are exactly:

- `0,2,4`: even isolation;
- `1,3`: odd anchor compression;
- `5` with anchor present: direct odd anchor compression;
- `5` with anchor absent: the explicit two-stage exceptional branch.

These cases exhaust all possible terminal degrees.

### Degree-five, anchor-absent branch omitted or absorbed into a generic shortcut

Not present. The branch is stated separately and verified by constructive legal-move replay.

### Invalid invariant update after deleting an odd terminal edge

Not present. Deleting the common terminal edge flips the anchor parity in both reduced graphs and subtracts one from the edge residue in both.

### Incomplete realization of invariant labels

Not present. Five-vertex realization covers all `48` admissible local labels, and the recursive representative map realizes every even parity vector and every residue at every order `n>=6`.

### Finite base represented only by a software assertion

Not present. The package includes a standalone spanning-forest certificate over all `32,768` order-six states. An independent verifier checks every parent transition and the one-root-per-invariant-fiber property.

### Confusion between labeled and unlabeled graphs

Avoided. The theorem is a labeled-state theorem. No quotient by vertex permutations is taken.

## Audit conclusion

The proof dependency graph is acyclic. The only computer-assisted theorem premise is the exact finite six-vertex completeness statement, now represented both by exhaustive reconstruction and by a standalone checkable certificate. All extension to arbitrary order is symbolic.
