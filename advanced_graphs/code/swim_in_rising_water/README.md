# Swim in Rising Water (LC 778)

Given an `n×n` grid of elevations, find the minimum time `t` such that you can swim
from `(0,0)` to `(n-1,n-1)`. At time `t`, you can only be in cells with elevation ≤ `t`.

## Approaches

### 1. Binary Search + BFS
**Complexity:** O(n² log n) time, O(n²) space

Binary search on the answer `t` in range `[grid[0][0], n²-1]`. For each candidate `t`,
BFS to check if `(n-1,n-1)` is reachable using only cells with elevation ≤ `t`.

**Why it works:** The answer is monotone — if time `t` works, so does `t+1`. Binary
search finds the minimum valid `t` in O(log n) BFS calls.

### 2. Dijkstra (min-heap on max elevation)
**Complexity:** O(n² log n) time, O(n²) space

Min-heap stores `(max_elevation_on_path, row, col)`. Greedily expand the cell with the
lowest bottleneck elevation. Return the bottleneck when `(n-1,n-1)` is reached.

**Why it works:** This is a **minimax path** problem. Dijkstra with cost = max elevation
seen so far finds the path minimizing the maximum elevation (= minimum time needed).

## Key Insight

The problem asks for the **minimax path** — minimize the maximum elevation on any path
from top-left to bottom-right. Dijkstra with a modified cost function (max instead of
sum) solves this directly. Binary search + BFS is an alternative with the same complexity.

## Edge Cases

- `n = 1` — return `grid[0][0]` (already at destination).
- Grid where the only path goes through a high-elevation cell — that elevation is the answer.
- All cells have the same elevation — return that elevation.
