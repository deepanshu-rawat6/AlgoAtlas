# LC 329 — Longest Increasing Path in a Matrix

Given an `m × n` integer matrix, return the length of the longest strictly increasing path. You can move in 4 directions (up, down, left, right), not diagonally.

## Approaches

### 1. DFS with Memoization
- **Time:** O(m × n) | **Space:** O(m × n)
- `dfs(r, c)` = longest increasing path starting at `(r, c)`. Recurse to all 4 neighbors with strictly larger values. Memoize results to avoid recomputation.

### 2. Topological Sort (BFS / Kahn's Algorithm)
- **Time:** O(m × n) | **Space:** O(m × n)
- Build a DAG where edges go from smaller to larger values. Compute in-degrees. Process nodes with in-degree 0 (local minima) first via BFS. Each BFS level adds 1 to the path length.

## Key Insight

The strictly increasing constraint means the graph is a DAG (no cycles possible). This enables memoization without cycle detection. The topological sort approach counts BFS levels, where each level represents one step in the longest path. Both approaches achieve O(m × n) because each cell is processed exactly once.

## Edge Cases

- Single cell: Return 1.
- All cells equal: No valid moves (not strictly increasing), each cell is its own path of length 1.
- Monotonically increasing row/column: The entire row/column forms one path.
- Matrix with one row or column: Reduces to a 1D longest increasing subsequence.
