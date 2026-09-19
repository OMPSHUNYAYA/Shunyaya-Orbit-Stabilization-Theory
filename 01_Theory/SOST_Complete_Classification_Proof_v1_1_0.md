# SOST Complete Classification Proof v1.1.0

## 1. Primitive move

A state is a simple labeled graph on `K_n`.

For a triple `T={a,b,c}`, the move on `T` is legal when the induced edge set on `T` is either empty or complete. The three edge bits are then complemented.

The move is involutive.

## 2. Direct invariants

### Degree parity

A legal triangle toggle changes the degree of each of `a,b,c` by `+2` or `-2` and does not change the parity of any other degree.

Therefore:

`P(G)=(deg_G(v) mod 2)_v`

is invariant.

### Edge count modulo three

A legal move adds or removes exactly three edges.

Therefore:

`R(G)=|E(G)| mod 3`

is invariant.

## 3. Five-vertex realization lemma

Let `p in F_2^5` have even Hamming weight and let `r in Z_3`.

There exists a simple graph on five labeled vertices with degree-parity vector `p` and edge-count residue `r`.

Only parity weights `0`, `2`, and `4` occur.

### Weight zero

For residues `0,1,2`, use respectively:

- the empty graph;
- a 4-cycle;
- a 5-cycle.

### Weight two

Let the odd vertices be `a,b`.

For residues `0,1,2`, use respectively:

- a 3-edge path from `a` to `b`;
- the edge `ab`;
- a 2-edge path from `a` to `b`.

### Weight four

Let the odd vertices be `a,b,c,d` and let `e` be the remaining vertex.

For residues `0,1,2`, use respectively:

- one edge joining two odd vertices together with a 2-edge path joining the other two through `e`;
- the four-edge star centered at `e`;
- two disjoint edges pairing the four odd vertices.

This realizes all:

`3*2^4=48`

admissible labels on five vertices.

The role of five vertices is structural: these realizations supply every admissible local target needed to control a sixth designated vertex.

## 4. Exact six-vertex theorem base

There are `15` edges in `K_6` and therefore:

`2^15=32768`

states.

The exact move graph has exactly `96` connected components.

Every component has one invariant pair `(P,R)`, every admissible pair occurs, and no admissible pair occurs in two components.

Hence, on six vertices:

`G ~ H  iff  (P(G),R(G))=(P(H),R(H))`.

This finite theorem premise is supplied in two forms:

1. independent exact partition reconstruction;
2. a standalone spanning-forest certificate over all `32,768` states.

The certificate records one legal parent move for every non-root state and has exactly `96` roots, one for each admissible invariant label.

## 5. Six-vertex compression

Fix a designated vertex `v` in a six-vertex graph.

### Even local parity

Suppose `P_v=0`.

On the other five vertices, retain the required parity coordinates and edge-count residue. The five-vertex realization lemma produces a graph with those data.

Adding isolated `v` gives a six-vertex graph with the same global `(P,R)` as the original graph.

By six-vertex completeness, the original graph can be transformed to a representative in which `v` is isolated.

### Odd local parity

Suppose `P_v=1` and fix any anchor `a!=v`.

Require the final representative to contain exactly one incident edge at `v`, namely `va`.

Removing that desired edge flips the required parity at `a` and subtracts one from the required edge residue modulo `3`.

The remaining five-vertex parity vector has even weight and is realizable by the five-vertex lemma.

Adding `va` gives a six-vertex graph with the original global label.

By six-vertex completeness, the original graph can be transformed to a representative in which `v` has exactly the single incident edge `va`.

The exhaustive verification checks all `288` even-parity isolation targets and all `1440` odd-parity anchored targets.

## 6. Local paths embed in larger complete graphs

A triangle move reads and toggles only the three edges of its selected triangle.

If a legal move sequence is supported on a chosen six-vertex subset of a larger complete graph, edges outside that subset do not affect legality of any move in the sequence.

Therefore every certified six-vertex compression path embeds unchanged into arbitrary order while all outside edges remain fixed.

## 7. Arbitrary-order degree compression

Let `n>6`, choose a designated vertex `v`, and fix an anchor `a!=v`.

We construct a legal sequence that leaves:

- `v` isolated when `P_v=0`;
- `v` incident only with `a` when `P_v=1`.

### 7.1 Nonterminal reduction

If `deg(v)>5`, select any five current neighbors of `v`.

Inside the six-vertex subset formed by `v` and those five neighbors, the local degree of `v` is five and therefore odd.

Use six-vertex odd compression to retain only one of those five incident edges.

Exactly four selected incident edges disappear. All incident edges outside the chosen six-set remain unchanged.

Hence:

`deg_new(v)=deg_old(v)-4`.

### 7.2 Termination measure

Define:

`mu(G,v)=deg_G(v)`.

Every nonterminal reduction strictly decreases `mu` by exactly four.

Therefore after at most:

`ceil(max(deg_G(v)-5,0)/4)`

nonterminal reductions, the degree is at most five.

No cycle of nonterminal reductions is possible.

### 7.3 Exhaustive terminal cases

Once `deg(v)<=5`, the terminal cases are exactly the following.

#### Even terminal degree: `0,2,4`

Choose a six-vertex subset containing `v`, every remaining neighbor of `v`, and enough filler vertices to reach six vertices.

The local parity of `v` is even, so six-vertex compression isolates `v`.

#### Odd terminal degree below five: `1,3`

Choose a six-vertex subset containing `v`, every remaining neighbor, the fixed anchor `a` if it is not already present, and enough fillers.

The local parity of `v` is odd, so six-vertex compression leaves exactly the edge `va`.

#### Terminal degree five with anchor present

The six-set consisting of `v` and its five current neighbors already contains `a`.

Odd six-vertex compression leaves exactly the edge `va`.

#### Terminal degree five with anchor absent

Choose four of the five current neighbors together with `a`.

In this six-set, the local degree of `v` is four and therefore even. Compress those four selected incident edges away.

Exactly one old incident edge remains outside the first six-set.

Choose a second six-set containing `v`, that remaining neighbor, the fixed anchor `a`, and three fillers.

The local degree of `v` is now one, so odd six-vertex compression moves the sole incident edge to `va`.

The cases `0,1,2,3,4,5` are therefore exhaustive, and every case reaches the required terminal form.

## 8. Vertex-elimination induction

We prove the classification for every `n>=6`.

### Base

The order-six classification is the exact finite theorem base.

### Induction step

Assume completeness at order `n-1`.

Let `G,H` be order-`n` graphs with equal `(P,R)`.

Choose the same vertex `v` and the same fixed anchor `a` in both graphs.

If `P_v=0`, compress `v` to an isolated vertex in both graphs and delete it. The reduced graphs have identical parity vectors and identical edge residues.

If `P_v=1`, compress `v` to the sole edge `va` in both graphs. Delete `v` and the common edge. In both reduced graphs the anchor parity flips and the edge residue decreases by one modulo `3`.

Thus the two reduced order-`n-1` graphs have equal invariant labels.

By the induction hypothesis they are connected by legal triangle moves on the remaining vertices.

Those moves avoid `v`, so they remain legal in the original order-`n` graphs.

Concatenating the first compression path, the lifted induction path, and the reverse of the second compression path gives `G~H`.

The converse follows from direct invariance.

Therefore, for every `n>=6`:

`G~H iff (P(G),R(G))=(P(H),R(H))`.

## 9. Orbit count

A graph degree-parity vector has even Hamming weight by the handshake identity.

Exactly `2^(n-1)` binary vectors of length `n` have even weight.

The recursive representative construction realizes all three residues for every even parity vector at every `n>=6`.

Hence:

`|Q_n|=3*2^(n-1)`.

## 10. Exact binary quotient growth

Fix anchor vertex `0`.

For an order-`n+1` invariant label, let `b` be the parity bit of the new vertex.

If `b=0`, isolate and delete the new vertex. The order-`n` label is unchanged.

If `b=1`, compress the new vertex to the sole edge joining anchor `0`. Delete that edge and the new vertex. The reduced label flips the anchor parity and subtracts one from the edge residue modulo `3`.

This gives a bijection:

`Q_(n+1) -> Q_n x {0,1}`.

The inverse adds either an isolated new vertex or a new vertex joined only to the fixed anchor.

Therefore:

`Q_(n+1) ~= Q_n x {0,1}`.

## 11. Constructive replay and independent holdout

The package includes a constructive replay verifier that executes the degree-compression and elimination algorithm using only certified legal six-vertex move paths.

The exact order-seven flood fill is separate from Sections 1-10. It checks all `2^21=2097152` states and obtains exactly `192` orbit components.

Neither the constructive finite replay nor the order-seven holdout replaces the symbolic induction; both are independent verification layers around it.
