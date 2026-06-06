# Number of Islands (LC 200)

Given an `m x n` binary grid of `'1'`s (land) and `'0'`s (water), return the number of
islands. An island is formed by connecting adjacent land cells horizontally or vertically.

## Approaches

### 1. DFS Flood Fill
**Complexity:** O(m·n) time, O(m·n) space (recursion stack)

For each unvisited `'1'`, increment count and DFS to mark all connected land as `'0'`.
Each DFS call sinks an entire island.

**Why it works:** Marking visited cells as `'0'` prevents revisiting. Each top-level DFS
call from an unvisited `'1'` corresponds to exactly one new island.

### 2. BFS Flood Fill
**Complexity:** O(m·n) time, O(min(m, n)) space (queue width)

Same idea as DFS but uses a queue. Better for very large grids where recursion depth
could cause stack overflow.

### 3. Union-Find
**Complexity:** O(m·n) time, O(m·n) space

Initialize each land cell as its own component. Union adjacent land cells. Count
distinct roots among land cells.

**Why it works:** Union-Find efficiently merges connected components. The final count
of distinct roots equals the number of islands.

## Key Insight

All three approaches reduce to the same idea: **connected component counting**. DFS/BFS
flood fill is simplest; Union-Find is useful when the grid is dynamic (cells added over time).

## Edge Cases

- All water — return 0.
- All land — return 1 (one giant island).
- Single cell grid — return 1 if land, 0 if water.
- Diagonal land cells — not connected (only 4-directional adjacency).
