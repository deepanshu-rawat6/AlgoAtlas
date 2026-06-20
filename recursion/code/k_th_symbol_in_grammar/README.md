# LC 779 — K-th Symbol in Grammar

Build a table where row 1 is `"0"` and each subsequent row replaces `0→01` and `1→10`. Return the k-th symbol (1-indexed) in row `n`.

## Approaches

### 1. Recursive Parent Lookup
- **Time:** O(n) | **Space:** O(n) call stack
- Each row is double the previous. The k-th symbol in row `n` comes from the `ceil(k/2)`-th symbol in row `n-1`. If `k <= mid` (first half), it's the same as the parent. If `k > mid` (second half), it's the parent XOR 1 (flipped).

## Key Insight

Row `n` is formed by expanding each symbol of row `n-1`: `0` becomes `01` and `1` becomes `10`. So the first half of row `n` is identical to row `n-1`, and the second half is the bitwise complement. This gives the recurrence: if `k <= 2^(n-2)`, recurse with `(n-1, k)`; otherwise recurse with `(n-1, k - 2^(n-2))` and flip the result (XOR 1).

## Edge Cases

- `n = 1, k = 1`: Base case, return 0.
- `k` in the first half: Same as parent symbol.
- `k` in the second half: Parent symbol XOR 1.
- `n = 30` (max): Recursion depth is 30, well within limits.
