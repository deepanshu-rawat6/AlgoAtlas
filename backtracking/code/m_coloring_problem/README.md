# M Coloring Problem (Classic Backtracking)

Given an undirected graph and `m` colors, determine if the graph can be colored with at
most `m` colors such that no two adjacent vertices share the same color.

## Approaches

### 1. Backtracking with Adjacency Check
**Complexity:** O(m^n) time, O(n) space (n = vertices)

Assign colors to vertices one by one. For each vertex, try colors 1 to m. Check if the
color conflicts with any already-colored neighbor. If valid, assign and recurse to the
next vertex. Backtrack (reset to 0) if no color works.

**Why it works:** Backtracking explores all valid colorings. The `is_safe` check ensures
the graph coloring constraint is maintained at every step. If all vertices are colored
successfully, the graph is m-colorable.

## Key Insight

Graph coloring is NP-complete in general, but backtracking with constraint checking is
practical for small graphs. The key is checking only **already-colored** neighbors —
uncolored neighbors don't constrain the current choice.

## Edge Cases

- `m >= n` — always colorable (assign each vertex a unique color).
- Complete graph (all pairs connected) — requires exactly `n` colors; return `false` if `m < n`.
- Triangle (3-cycle) — requires 3 colors; `m=2` returns `false`.
- Bipartite graph — always 2-colorable; `m >= 2` returns `true`.
