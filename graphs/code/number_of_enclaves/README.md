# LC 1020 - Number of Enclaves

Count land cells (`1`s) from which you **cannot** walk off the boundary of the grid.

## Approach: Boundary BFS/DFS — O(m×n)
1. Seed a BFS/DFS with all land cells on the 4 borders.
2. Flood-fill (sink to 0) all land reachable from the boundary.
3. Count remaining `1`s — these are enclaves.

## Key Insight
Instead of checking each land cell for boundary reachability (expensive), **invert the problem**: mark everything reachable from the boundary, then count what's left. Modifying the grid in-place avoids a separate visited array.

## Edge Cases
- No land on boundary → all land cells are enclaves
- All land connected to boundary → answer is 0
- Grid with no land → answer is 0

## Example
```
grid = [[0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]]
(1,0) is on boundary → sunk
(1,2),(2,1),(2,2) are interior → enclaves
Output: 3
```
