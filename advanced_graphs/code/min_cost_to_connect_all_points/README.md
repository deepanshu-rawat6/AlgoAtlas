# Min Cost to Connect All Points (LC 1584)

Given points on a 2D plane, find the minimum cost to connect all points where the cost
between two points is their Manhattan distance. All points must be connected (MST).

## Approaches

### 1. Prim's Algorithm
**Complexity:** O(n²) time, O(n) space

Start from any point. Maintain a min-heap of `(cost, point_index)`. Greedily add the
cheapest edge to an unvisited point. Repeat until all points are in the MST.

**Why it works:** Prim's builds the MST by always adding the cheapest edge connecting
the current tree to an unvisited node. With a dense graph (all pairs connected), Prim's
O(n²) is optimal.

### 2. Kruskal's Algorithm
**Complexity:** O(n² log n) time, O(n²) space

Generate all O(n²) edges with their Manhattan distances. Sort by distance. Use
Union-Find to add edges that connect different components until n-1 edges are added.

**Why it works:** Kruskal's builds the MST by processing edges in sorted order, adding
each edge that doesn't create a cycle. Correct by the cut property of MSTs.

## Key Insight

This is a **Minimum Spanning Tree** problem on a complete graph. Prim's is preferred
here because the graph is dense (O(n²) edges) — Prim's O(n²) beats Kruskal's
O(n² log n) for dense graphs.

## Edge Cases

- Single point — return 0 (no edges needed).
- Two points — return their Manhattan distance.
- All points at the same location — return 0.
- Points with large coordinates — Manhattan distance can be up to 4×10⁶.
