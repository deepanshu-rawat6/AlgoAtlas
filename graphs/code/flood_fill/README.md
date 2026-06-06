# LC 733 - Flood Fill

Starting from pixel `(sr, sc)`, change all 4-directionally connected pixels of the same original color to `color`.

## Approach: DFS — O(m×n)
Record the original color. DFS from the starting pixel: if current pixel matches original color, repaint it and recurse in 4 directions.

## Key Insight
**Early exit**: if `image[sr][sc] == color` already, return immediately. Without this check, DFS would infinitely revisit already-painted cells since they still match the "original" color.

## Edge Cases
- Starting pixel already has the target color → return as-is (no-op)
- Single pixel image → just change that pixel
- Starting pixel surrounded by different colors → only that pixel changes

## Example
```
image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
Original color at (1,1) = 1
All 4-connected 1s get painted 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```
