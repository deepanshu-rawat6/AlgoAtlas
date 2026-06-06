# LC 48 — Rotate Image

Rotate an `n × n` matrix 90 degrees clockwise **in-place**.

## Approaches

### 1. Transpose + Reverse Rows
- **Time:** O(n²) | **Space:** O(1)
- Transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]`), then reverse each row. The composition of these two operations equals a 90° clockwise rotation.

### 2. Four-Way Cyclic Swap (Layer by Layer)
- **Time:** O(n²) | **Space:** O(1)
- Process the matrix layer by layer (outer to inner). For each position in a layer, perform a 4-way cyclic swap: top → right → bottom → left → top.

## Key Insight

A 90° clockwise rotation maps `(i, j)` to `(j, n-1-i)`. The transpose + reverse approach decomposes this into two simpler operations: transpose maps `(i, j)` to `(j, i)`, and reversing each row maps `(j, i)` to `(j, n-1-i)`. The cyclic swap approach directly implements the rotation by moving four elements at once, requiring only one temporary variable.

## Edge Cases

- `1 × 1` matrix: No change needed.
- `2 × 2` matrix: One layer, four elements swap cyclically.
- Even vs odd `n`: Both approaches handle both cases uniformly.
