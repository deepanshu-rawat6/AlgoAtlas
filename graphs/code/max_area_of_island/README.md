# Max Area of Island (LC 695)

Given a binary grid where `1` = land and `0` = water, return the maximum area of any
island (connected group of `1`s). Return 0 if no island exists.

## Approaches

### 1. DFS Flood Fill
**Complexity:** O(m·n) time, O(m·n) space (recursion stack)

For each unvisited `1`, DFS to count all connected land cells, marking them `0` to
avoid revisiting. Track the maximum count seen.

**Why it works:** DFS explores the entire island from a starting cell, returning the
total cell count. Marking cells as visited prevents double-counting.

### 2. BFS Flood Fill
**Complexity:** O(m·n) time, O(m·n) space (queue)

Same as DFS but uses a queue. Avoids recursion depth issues on large grids.

**Why it works:** BFS also explores all connected cells. Area is accumulated as cells
are dequeued.

## Key Insight

Both approaches are flood fill — the same algorithm used for "paint bucket" in image
editors. The key is marking cells as visited (setting to 0) during traversal to avoid
counting the same cell twice.

## Edge Cases

- All water — return 0.
- All land — return m × n.
- Single land cell — return 1.
- Multiple islands of equal size — return that size.
