# LC 542 - 01 Matrix (Distance of Nearest 0)

For each cell in a binary matrix, find the distance to the nearest `0`.

## Approach: Multi-Source BFS — O(m×n)
Initialize BFS queue with **all** `0` cells at distance 0. Expand outward layer by layer. The first time BFS reaches a `1` cell gives its minimum distance.

## Key Insight
**Don't BFS from each `1` separately** (that's O(m²n²)). Instead, think of all `0`s as a single source. Multi-source BFS is equivalent to adding a virtual super-source connected to all `0`s — the BFS wavefront expands uniformly from all zeros simultaneously.

## Edge Cases
- Cell is already `0` → distance is 0
- Matrix of all `1`s except one `0` → distances radiate from that single cell
- All cells are `0` → all distances are 0

## Example
```
mat = [[0,0,0],[0,1,0],[1,1,1]]
BFS from all 0s:
(2,0)→1, (2,1)→2, (2,2)→1
Output: [[0,0,0],[0,1,0],[1,2,1]]
```
