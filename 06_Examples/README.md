# SOST Examples

The examples use the JSON format:

```json
{
  "n": 6,
  "edges": [[0,1],[1,2]]
}
```

`sample_empty_K6.json` and `sample_triangle_K6.json` are theorem-equivalent: the triangle is obtained from the empty graph by one legal move, and both have zero degree parity and edge count `0 mod 3`.

`sample_single_edge_K6.json` is inequivalent to the empty graph because its degree-parity vector and edge residue differ.

These examples are intended for the labeling and equivalence utilities under `02_Algorithms_and_Software/`.
