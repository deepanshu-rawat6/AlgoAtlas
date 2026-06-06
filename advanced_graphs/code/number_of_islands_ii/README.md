# LC 305 - Number of Islands II

Given an m×n grid, add land cells one by one from `positions`. After each addition, return the current number of islands.

## Approach: Online Union-Find — O(k·α(mn))
Use a Union-Find with lazy initialization (only add cells as they're placed). For each new land cell:
1. Create a new component (island count +1)
2. Check 4 neighbors — union with any existing land neighbors (island count -1 per merge)

## Key Insight
Union-Find handles dynamic connectivity perfectly. Using a dictionary for `parent` avoids pre-allocating the full m×n grid. Encode cell `(r,c)` as `r*n + c` for the key. Handle duplicate positions by checking if cell already exists in `parent`.

## Edge Cases
- Duplicate positions → island count unchanged for that step
- Adding land surrounded by existing land → merges multiple islands
- Single cell additions with no neighbors → each adds 1 island

## Example
```
m=3, n=3, positions=[[0,0],[0,1],[1,2],[2,1]]
Add (0,0): 1 island
Add (0,1): merges with (0,0) → 1 island
Add (1,2): isolated → 2 islands
Add (2,1): isolated → 3 islands
Output: [1,1,2,3]
```
