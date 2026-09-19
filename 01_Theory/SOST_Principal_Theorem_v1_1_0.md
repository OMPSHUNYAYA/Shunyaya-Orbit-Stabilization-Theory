# SOST Principal Theorem v1.1.0

## Monochromatic-triangle toggle system

Let `X_n` be the set of simple labeled graphs on vertex set `{0,...,n-1}`.

A move chooses a triple `{a,b,c}` whose three induced edge bits are either:

`000`

or:

`111`.

The move complements all three bits:

`000 <-> 111`.

The move is involutive.

Define the degree-parity vector:

`P(G)=(deg_G(0),...,deg_G(n-1)) mod 2`

and the edge residue:

`R(G)=|E(G)| mod 3`.

## Principal classification theorem

For every `n>=6` and every `G,H in X_n`:

`G ~ H  iff  P(G)=P(H) and R(G)=R(H)`.

Thus:

`Q_n ~= {p in F_2^n : wt(p) is even} x Z_3`.

Consequently:

`|Q_n|=3*2^(n-1)`.

## Exact quotient growth

For every `n>=6`:

`Q_(n+1) ~= Q_n x {0,1}`,

and therefore:

`|Q_(n+1)|=2|Q_n|`.

## Sharp boundary

Exact enumeration gives:

`n=3 : 7 orbits`

`n=4 : 32 orbits`

`n=5 : 59 orbits`

`n=6 : 96 orbits`.

The invariant pair `(P,R)` is complete at `n=3`, incomplete at `n=4,5`, and complete for every `n>=6`.

Thus `n=6` is the sharp permanent completeness threshold.

## Proof type

The proof is computer-assisted through one exhaustive finite theorem base at order six and symbolic for all larger orders.

The finite base is accompanied by a standalone spanning-forest certificate covering all `32,768` order-six states.

The exact order-seven computation is an independent verification holdout and is not a proof premise.
