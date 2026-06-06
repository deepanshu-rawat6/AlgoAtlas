# N-Queens II (LC 52)

Place `n` queens on an `n×n` chessboard so no two queens attack each other. Return the
**count** of distinct solutions (not the boards themselves).

## Approaches

### 1. Backtracking with Set-Based Conflict Tracking
**Complexity:** O(n!) time, O(n) space

Place one queen per row. Track occupied columns (`cols`), left diagonals (`row - col`),
and right diagonals (`row + col`) using sets. For each row, try each column; skip if
any conflict exists. Increment count when all `n` rows are filled.

**Why it works:** Queens attack along rows, columns, and diagonals. Placing one per row
eliminates row conflicts. The diagonal invariants (`row - col` constant for left diagonals,
`row + col` constant for right diagonals) allow O(1) conflict checking.

## Key Insight

The diagonal encoding is elegant: all cells on the same left diagonal share the same
`row - col` value; all cells on the same right diagonal share the same `row + col` value.
Three sets replace an O(n²) board scan, making conflict checking O(1).

## Edge Cases

- `n = 1` — one solution (single queen on the only cell).
- `n = 2` or `n = 3` — no solutions exist.
- `n = 8` — 92 solutions (classic problem).
