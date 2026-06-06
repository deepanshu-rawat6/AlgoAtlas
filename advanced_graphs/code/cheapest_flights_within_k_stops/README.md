# Cheapest Flights Within K Stops (LC 787)

Given `n` cities, flight prices, source `src`, destination `dst`, and max stops `k`,
find the cheapest price from `src` to `dst` with at most `k` stops. Return `-1` if
no such route exists.

## Approaches

### 1. Bellman-Ford with K+1 Rounds
**Complexity:** O(k · E) time, O(V) space

Run Bellman-Ford for exactly `k+1` rounds (k stops = k+1 edges). Use a **copy** of
the price array each round to prevent using more than one edge per round.

**Why it works:** Each round of Bellman-Ford relaxes one more edge. After `k+1` rounds,
`prices[v]` = minimum cost to reach `v` using at most `k+1` edges (k stops). The copy
prevents "chaining" multiple edges in a single round.

### 2. Modified Dijkstra with Stop Tracking
**Complexity:** O(V · E) time, O(V · k) space

Heap entry: `(cost, node, stops_used)`. Expand cheapest options; skip if stops > k.
Track `dist[node][stops]` to avoid revisiting the same state.

**Why it works:** Standard Dijkstra doesn't account for the stop constraint. Tracking
stops as part of the state ensures we don't exceed `k` stops while still finding the
cheapest path.

## Key Insight

The stop constraint makes standard Dijkstra incorrect (a cheaper path might use more
stops). Bellman-Ford naturally handles this by limiting relaxation rounds. The critical
trick: use a **copy** of distances each round to prevent multi-hop updates within one round.

## Edge Cases

- `k = 0` — only direct flights from `src` to `dst` are valid.
- No path within `k` stops — return `-1`.
- Multiple paths with same cost but different stops — return the cost.
- `src == dst` — return 0 (problem guarantees they differ).
