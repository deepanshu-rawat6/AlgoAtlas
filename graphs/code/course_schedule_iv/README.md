# Course Schedule IV (LC 1462)

Given `numCourses`, `prerequisites` (direct dependencies), and `queries` of the form
`[u, v]`, answer whether course `u` is a (direct or indirect) prerequisite of course `v`.

## Approaches

### 1. BFS per Query
**Complexity:** O(V · (V + E)) time, O(V²) space

For each query `(u, v)`, BFS from `u` to check if `v` is reachable.

**Why it works:** Correct but redundant — recomputes reachability for every query.

### 2. Floyd-Warshall Transitive Closure (optimal)
**Complexity:** O(V³) time, O(V²) space

Build a boolean reachability matrix. Initialize with direct prerequisites. Apply
Floyd-Warshall: `reach[i][j] |= reach[i][k] & reach[k][j]` for all `k`.
Answer each query in O(1).

**Why it works:** Floyd-Warshall computes all-pairs reachability. After the O(V³)
preprocessing, each query is answered in O(1) — ideal when queries >> V.

## Key Insight

With up to 10,000 queries but only 100 courses, precomputing all-pairs reachability
via Floyd-Warshall (O(V³) = O(10⁶)) is far better than O(Q · (V + E)) per-query BFS.
Trade preprocessing time for O(1) query answering.

## Edge Cases

- No prerequisites — all queries return `false`.
- `u == v` — problem guarantees `u != v` in queries.
- Transitive chain `1→2→3`: query `[1,3]` should return `true`.
- Disconnected graph — nodes in different components return `false`.
