# Network Delay Time (LC 743)

Given a directed weighted graph and a source node `k`, find the minimum time for a
signal to reach all `n` nodes. Return `-1` if any node is unreachable.

## Approaches

### 1. Dijkstra's Algorithm
**Complexity:** O((V + E) log V) time, O(V + E) space

Single-source shortest path from `k`. The answer is the maximum shortest-path distance
across all nodes. Return `-1` if any node remains at infinity.

**Why it works:** Dijkstra greedily processes nodes in order of increasing distance,
guaranteeing shortest paths in graphs with non-negative weights. The last node to
receive the signal determines the total delay.

### 2. Bellman-Ford
**Complexity:** O(V · E) time, O(V) space

Relax all edges `V-1` times. The maximum finite distance is the answer.

**Why it works:** Bellman-Ford handles any graph without negative cycles. After `V-1`
relaxations, all shortest paths are found. Slower than Dijkstra but works with
negative weights (not needed here).

## Key Insight

"Minimum time for all nodes to receive the signal" = **maximum of all single-source
shortest paths** from `k`. Dijkstra computes all shortest paths in one pass; the
bottleneck (slowest node) is the answer.

## Edge Cases

- Some node unreachable from `k` — return `-1`.
- `k` is the only node — return 0.
- Multiple edges between same pair — use the minimum weight one.
- Self-loops — ignored (distance to self is 0).
