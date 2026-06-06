# Graph Valid Tree (LC 261)

Given `n` nodes and a list of undirected edges, determine if the edges form a valid tree.
A valid tree is connected and acyclic.

## Approaches

### 1. BFS Connectivity Check
**Complexity:** O(V + E) time, O(V + E) space

First check: a tree with `n` nodes has exactly `n-1` edges. If not, return `false`.
Then BFS from node 0 and verify all `n` nodes are reachable.

**Why it works:** `n-1` edges is necessary for a tree. Combined with full connectivity,
it's sufficient — a connected graph with `n-1` edges has no cycles.

### 2. Union-Find
**Complexity:** O(V · α(V)) time, O(V) space

Check `len(edges) == n-1`. Then process each edge: if both endpoints are already in the
same component, a cycle exists — return `false`. If all edges are processed without
cycles, the graph is a valid tree.

**Why it works:** Union-Find detects cycles in O(α) per edge. Combined with the edge
count check, it validates both tree properties efficiently.

## Key Insight

A valid tree satisfies exactly two conditions: **n-1 edges** and **fully connected**.
Checking edge count first is a cheap O(1) early exit. Either BFS or Union-Find then
verifies connectivity/acyclicity in O(V + E).

## Edge Cases

- `n = 1`, no edges — valid tree (single node).
- Too many edges — immediately `false`.
- Too few edges — immediately `false`.
- Disconnected forest — `false` (not connected).
