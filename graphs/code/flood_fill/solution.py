"""
# LC 733: Flood Fill

Starting from pixel `(sr, sc)`, change all 4-directionally connected pixels
that share the same original color to `color`, and return the image.

## Examples
```text
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
```

## Constraints
- If the starting pixel already has the target color, return as-is (no-op).
- A single-pixel image just changes that pixel.
- Only pixels connected to the start with the original color are repainted.
"""
from typing import List

class Solution:
    # DFS flood fill - change all connected same-color pixels to new color
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image  # edge case: already the target color, avoid infinite loop

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            image[r][c] = color  # paint in-place
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    s = Solution()
    assert s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert s.floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
    print("All tests passed.")
