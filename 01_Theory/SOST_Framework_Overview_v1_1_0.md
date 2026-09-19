# SOST Framework Overview v1.1.0

Shunyaya Orbit Stabilization Theory studies orbit quotients of reversible transformation systems that grow with order, dimension, or branching history.

The framework separates four questions that are often conflated.

## 1. Local quotient transport

Given a growth extension `E` and a projection `P`, four orbit-level gates certify inverse quotient transport:

- `UP`;
- `DOWN`;
- `LOWER`;
- `UPPER`.

When all four hold, `E` and `P` induce inverse bijections between orbit quotients.

## 2. Finite certification

When transformation rules have dependency-complete finite descriptions, local gate obligations can be reduced to finite kernels.

Finite witness search can then either produce a move word or return a finite obstruction.

Future-transport equivalence compresses raw finite observations into a minimal deterministic interface.

## 3. Branching coherence

For branching growth, edgewise transport does not imply path independence.

After choosing root transports, each extra growth edge has a holonomy element. Path independence is equivalent to trivial holonomy on a generating family of cycles.

When growth paths admit a finite convergent grammar, finite cell checks lift local flatness to global path coherence.

## 4. Complete summary interfaces

A complete summary `alpha:X->A` identifies orbit classes exactly when it is invariant, every summary value is realizable, and every state canonicalizes to the representative of its summary.

Summary transport can certify stabilization or expose a frontier obstruction when complete-summary cardinalities differ.

## 5. Discovery and promotion discipline

Finite exact orbit partitions can be used to test and refine finite feature grammars.

The framework distinguishes:

- feature selection;
- witness-driven refinement;
- feature construction from a finite constructor grammar;
- constructor-family selection;
- explicit insufficiency when the supplied grammar cannot classify the orbits.

Finite success is not treated as an all-order theorem. Promotion requires an independent symbolic proof of invariance, realization, and completeness.

## 6. Relation to the principal theorem

The monochromatic-triangle theorem is a consequence family in which the frozen finite feature grammar is insufficient. The complete invariant is instead derived directly from the move law and promoted through a finite six-vertex theorem base plus symbolic induction.

The repository keeps the framework and the graph theorem logically separate so that each claim has a clear proof dependency.
