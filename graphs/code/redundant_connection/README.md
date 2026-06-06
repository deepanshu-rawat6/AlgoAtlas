# Redundant Connection (LC 684)

A tree of `n` nodes had one extra edge added. Given the resulting graph's edges, return
the edge that can be removed to restore the tree. If multiple answers exist, return the
one that appears **last** in the input.

## Approaches

### 1. DFS Cycle Detection
**Complexity:** O(V · E) time, O(V + E) space

For each edge `(a, b)`, check if a path already exists from `a` to `b` in the graph
built so far. If yes, this edge creates a cycle — return it. Otherwise, add it.

**Why it works:** The first edge that connects two already-connected nodes is the
redundant one. DFS path check confirms connectivity before adding each edge.

### 2. Union-Find (optimal)
**Complexity:** O(V · α(V)) ≈ O(V) time, O(V) space

Process edges in order. Use Union-Find with path compression and union by rank.
The first edge where both endpoints share the same root is the redundant edge.

**Why it works:** Union-Find efficiently tracks connected components. When `find(a) == find(b)`
before unioning, the edge `(a, b)` would create a cycle — it's the answer.

## Key Insight

A tree with `n` nodes has exactly `n-1` edges. The redundant edge is the **first** one
(in input order) that connects two nodes already in the same component.

## Edge Cases

- The redundant edge is the last edge in the input — guaranteed by the problem to exist.
- Multiple edges could form a cycle — return the last one in input order.
- Minimum graph: 3 nodes, 3 edges (triangle).
