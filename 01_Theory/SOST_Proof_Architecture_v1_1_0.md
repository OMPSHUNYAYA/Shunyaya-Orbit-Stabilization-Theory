# SOST Proof Architecture v1.1.0

The principal theorem has three verification-visible layers and one proof dependency chain.

## Finite exact theorem layer

- exhaustive five-vertex invariant realization;
- exhaustive six-vertex move partition;
- exact six-vertex invariant completeness;
- exhaustive six-vertex compression targets;
- standalone K6 spanning-forest certificate covering all `32,768` states.

## Universal symbolic layer

- direct move invariance;
- locality of embedded six-vertex move paths;
- degree reduction by exactly four while degree exceeds five;
- explicit decreasing measure `mu(G,v)=deg_G(v)`;
- exhaustive terminal cases `0,1,2,3,4,5`;
- vertex-elimination induction;
- invariant realization at every order;
- exact quotient counting and binary growth.

## Independent verification layer

- separate small-order flood-fill implementation;
- exact C++17 order-seven holdout;
- constructive legal-move replay at larger sampled orders;
- proof dependency and terminal-case audit.

## Dependency chain

`direct invariants`

`five-vertex realization + exact six-vertex completeness`

`-> six-vertex compression`

`-> embedded arbitrary-order compression`

`-> terminating degree reduction + exhaustive terminal cases`

`-> vertex elimination`

`-> complete classification`

`-> orbit count and quotient growth`.

The exact seven-vertex computation is outside this dependency chain and serves only as an independent falsification test.
