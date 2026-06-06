# Path With Minimum Effort (LC 1631)

Given a height matrix, find the path from top-left to bottom-right that minimizes the
**maximum absolute height difference** between consecutive cells (the "effort").

## Approaches

### 1. Binary Search + BFS
**Complexity:** O(m·n·log(10⁶)) time, O(m·n) space

Binary search on the effort value. For each candidate effort, BFS to check if a path
exists where all consecutive height differences ≤ effort.

**Why it works:** The answer is monotone — if effort `e` allows a valid path, so does
`e+1`. Binary search finds the minimum valid effort in O(log(max_height)) BFS calls.

### 2. Dijkstra (min-heap on max effort)
**Complexity:** O(m·n·log(m·n)) time, O(m·n) space

Min-heap stores `(max_effort_so_far, row, col)`. Expand the cell with the lowest
current effort. Update a cell only if the new path has lower effort. Return when
`(rows-1, cols-1)` is reached.

**Why it works:** This is a **minimax path** problem on a grid. Dijkstra with cost =
max absolute difference seen so far finds the optimal path directly.

## Key Insight

Effort = maximum edge weight on the path. This is a **minimax path** problem, not a
shortest path problem. Dijkstra works because the cost function (max) is still
monotonically non-decreasing as we extend the path.

## Edge Cases

- Single cell — return 0 (no movement needed).
- Flat grid (all same height) — return 0.
- Only one path exists — return its maximum difference.
- Heights differ by up to 10⁶ — binary search range must cover this.
