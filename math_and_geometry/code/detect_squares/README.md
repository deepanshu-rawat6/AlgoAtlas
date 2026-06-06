# LC 2013 — Detect Squares

Design a data structure that adds points from a stream and counts the number of ways to form axis-aligned squares with a given query point as one corner.

## Approaches

### 1. Frequency Map + X-to-Y Index
- **Time:** O(1) add, O(n) count | **Space:** O(n)
- Store `pt_count[(x, y)]` for point frequencies and `x_to_ys[x]` for all y-values at each x.
- For a query `(qx, qy)`: iterate all `y` values at `x = qx`. Each `y ≠ qy` defines a side length `|y - qy|`. The other two corners are `(qx ± side, qy)` and `(qx ± side, y)`. Multiply their counts.

## Key Insight

An axis-aligned square is determined by two points sharing the same x-coordinate (the diagonal). Given the query point `(qx, qy)` and a diagonal point `(qx, y)`, the side length is `|y - qy|`, and the other two corners are fully determined. Multiplying the counts of all three other corners handles duplicate points correctly.

## Edge Cases

- Query point not in the data structure: Still valid — it's the query corner, not a stored point.
- Duplicate points: The frequency map handles them; multiplying counts gives the correct number of distinct squares.
- `y == qy`: Skip (would form a degenerate square with zero area).
- No points at the required corners: Contributes 0 to the count.
