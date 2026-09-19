# SOST Exact Quotient Growth v1.1.0

For every `n>=6`, the complete orbit label is

`(P,R)`

with `P` an even-weight vector in `F_2^n` and `R in Z_3`.

Therefore:

`|Q_n|=3*2^(n-1)`.

Fix anchor vertex `0`.

For an order-`n+1` label, let `b` be the parity of the new vertex.

- If `b=0`, the new vertex can be isolated and removed.
- If `b=1`, it can be compressed to the sole anchor edge; removal flips the anchor parity and subtracts one from the residue modulo `3`.

This yields an explicit bijection:

`Q_(n+1) ~= Q_n x {0,1}`.

Hence:

`|Q_(n+1)|=2|Q_n|`.

The quotient sequence is therefore neither eventually constant nor eventually periodic. Its cardinality grows exactly by a factor of two at each step from order six onward.
