# LC 1091 - Shortest Path in Binary Matrix

Find the shortest clear path (cells with value `0`) from `(0,0)` to `(n-1,n-1)` moving in 8 directions. Return path length or `-1` if none exists.

## Approach: BFS — O(n²)
Standard BFS guarantees shortest path in unweighted graphs. Start from `(0,0)` with distance 1. Explore all 8 neighbors. First time we reach `(n-1,n-1)` is the answer.

## Key Insight
8-directional movement (including diagonals) means path length ≠ Manhattan distance. BFS still works because all edge weights are 1. Mark cells visited by setting them to `1` in-place to avoid revisiting.

## Edge Cases
- `grid[0][0] == 1` or `grid[n-1][n-1] == 1` → return `-1` immediately
- `n == 1` and `grid[0][0] == 0` → return `1` (already at destination)
- No clear path → return `-1`

## Example
```
grid = [[0,1],[1,0]]
(0,0)→(1,1) diagonally, both are 0
Path length = 2
Output: 2
```
