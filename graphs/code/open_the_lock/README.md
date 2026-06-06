# Open the Lock (LC 752)

A 4-wheel lock starts at `'0000'`. Each turn rotates one wheel by 1 (wraps 9↔0).
Given `deadends` (forbidden states) and a `target`, return the minimum turns to reach
the target, or `-1` if impossible.

## Approaches

### 1. Standard BFS
**Complexity:** O(10⁴ · 4) time, O(10⁴) space

BFS from `'0000'`. Each state has 8 neighbors (4 wheels × 2 directions). Skip deadends
and visited states. Return turn count when target is reached.

**Why it works:** BFS explores states level by level, so the first time the target is
reached is via the shortest path (minimum turns).

### 2. Bidirectional BFS (optimal)
**Complexity:** O(10⁴) time, O(10⁴) space

Simultaneously expand from `'0000'` and from `target`. Always expand the smaller
frontier. When a state from one frontier appears in the other, the path is found.

**Why it works:** Bidirectional BFS reduces the search space from O(b^d) to O(b^(d/2))
where b=8 (branching factor) and d=depth. Meeting in the middle is much faster.

## Key Insight

The lock state space is a graph with 10,000 nodes. BFS finds shortest paths in
unweighted graphs. The key optimization is bidirectional BFS — always expand the
smaller frontier to minimize total nodes explored.

## Edge Cases

- `'0000'` is in deadends — return `-1` immediately.
- Target is `'0000'` — return 0 (already there).
- Target is surrounded by deadends — return `-1`.
- Direct path blocked but indirect path exists — BFS finds it.
