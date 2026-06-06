# Number of Connected Components in an Undirected Graph (LC 323)

Given `n` nodes and a list of undirected edges, return the number of connected components.

## Approaches

### 1. DFS Component Counting
**Complexity:** O(V + E) time, O(V + E) space

Build adjacency list. For each unvisited node, DFS to mark all reachable nodes as
visited. Each DFS call from an unvisited node = one new component.

**Why it works:** DFS exhaustively visits all nodes in a component. Counting how many
times we start a fresh DFS gives the component count.

### 2. Union-Find (optimal)
**Complexity:** O(V · α(V)) time, O(V) space

Initialize each node as its own component (count = n). For each edge, union the two
endpoints. If they were in different components, decrement count. Return final count.

**Why it works:** Union-Find merges components as edges are processed. Each successful
union reduces the component count by 1. The final count is the answer.

## Key Insight

Connected component counting is one of the most fundamental graph problems. Union-Find
is the canonical solution — it's online (handles dynamic edge additions) and nearly O(1)
per operation with path compression and union by rank.

## Edge Cases

- No edges — each node is its own component, return `n`.
- All nodes connected — return 1.
- Isolated nodes mixed with connected groups — count each isolated node separately.
- Duplicate edges — Union-Find handles gracefully (union of same-component nodes is a no-op).
