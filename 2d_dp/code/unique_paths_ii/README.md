# LC 63 — Unique Paths II

Same as Unique Paths but the grid contains obstacles (`1` = obstacle, `0` = free). Return the number of unique paths from top-left to bottom-right avoiding obstacles.

## Approaches

### 1. 2D DP
- **Time:** O(m × n) | **Space:** O(m × n)
- Same as Unique Paths but set `dp[i][j] = 0` if `obstacleGrid[i][j] == 1`. Initialize first row/column carefully — stop propagating 1s once an obstacle is hit.

### 2. 1D DP (Space-Optimized)
- **Time:** O(m × n) | **Space:** O(n)
- Process row by row. If current cell is an obstacle, set `dp[j] = 0`. Otherwise `dp[j] += dp[j-1]` (add paths from the left).

## Key Insight

Obstacles simply zero out the path count at that cell. The key subtlety is in initializing the first row and column: once an obstacle is encountered, all cells beyond it in that row/column are unreachable (set to 0), even if the obstacle is not at the start. The 1D DP handles this naturally by zeroing obstacle cells.

## Edge Cases

- Start cell `[0][0]` is an obstacle: Return 0 immediately.
- End cell is an obstacle: Return 0.
- Obstacle in the middle of the only path: Return 0.
- No obstacles: Same as Unique Paths (LC 62).
- `[[1]]`: Start is an obstacle, return 0.
