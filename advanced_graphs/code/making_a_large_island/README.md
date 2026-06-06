# LC 827 - Making A Large Island

Flip at most one `0` to `1` in a binary grid. Return the size of the largest island after the flip.

## Approach: Label + Lookup — O(n²)
1. DFS to label each island with a unique id (starting from 2) and record its size.
2. For each `0` cell, look at its 4 neighbors, sum sizes of **distinct** neighboring islands + 1 (the flipped cell).
3. Answer = max over all `0` cells (and also consider the case of no `0` cells).

## Key Insight
Label islands first so neighbor lookups are O(1). Use a `seen` set per `0` cell to avoid double-counting when two neighbors belong to the same island. Start island IDs from 2 since 0 and 1 are already used in the grid.

## Edge Cases
- Grid is all `1`s → no `0` to flip, answer = n²
- Grid is all `0`s → flip any one → answer = 1
- Single `0` surrounded by 4 different islands → sum all 4 + 1

## Example
```
grid = [[1,0],[0,1]]
Island 1 at (0,0), Island 2 at (1,1)
Flip (0,1): connects island at (0,0) + itself = 2
Flip (1,0): connects island at (1,1) + itself = 2
But flipping (0,1) or (1,0) can bridge both → size 3
Output: 3
```
