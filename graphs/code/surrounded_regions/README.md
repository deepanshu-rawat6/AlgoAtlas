# Surrounded Regions (LC 130)

Given an `m x n` matrix of `'X'` and `'O'`, capture all regions that are 4-directionally
surrounded by `'X'` by flipping those `'O'`s to `'X'`. An `'O'` is **not** captured if it
is on the border or connected to a border `'O'`.

## Approaches

### 1. DFS from Borders
**Complexity:** O(m·n) time, O(m·n) space (recursion stack)

Start DFS from every `'O'` on the border and mark reachable cells as `'S'` (safe).
Then flip all remaining `'O'` → `'X'` and restore `'S'` → `'O'`.

**Why it works:** Any `'O'` connected to the border cannot be surrounded. By marking
border-connected cells first, the remaining `'O'`s are guaranteed to be fully enclosed.

### 2. BFS from Borders (optimal)
**Complexity:** O(m·n) time, O(m·n) space (queue)

Same logic as DFS but uses a queue. Avoids recursion stack overflow on large grids.

## Key Insight

Invert the problem: instead of finding surrounded regions, find **unsurrounded** ones
(border-connected `'O'`s). Everything else is surrounded by definition.

## Edge Cases

- Single-cell board — no `'O'` can be surrounded.
- All border cells are `'O'` — nothing gets flipped.
- No `'O'` in the grid — board unchanged.
- `'O'` on the corner — always safe, never captured.
