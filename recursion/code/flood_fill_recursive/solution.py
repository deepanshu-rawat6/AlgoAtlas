"""
# 733: Flood Fill (Recursive)

Given a 2D `image` grid, a starting cell `(sr, sc)`, and a new `color`, perform
a flood fill: change the starting cell and all 4-directionally connected cells
of the same original color to `color`.

## Examples
```text
Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

## Constraints
- Connectivity is 4-directional (up, down, left, right).
- If the starting cell already has the target color, return the image unchanged.
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS recursive O(m*n).
        # Capture the original color at the starting cell before any changes.
        # Base case: out of bounds, different original color, or already filled.
        original = image[sr][sc]
        if original == color:  # already the target color — avoid infinite loop
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return  # out of bounds
            if image[r][c] != original:
                return  # different color — stop spreading
            image[r][c] = color  # fill current cell
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    sol = Solution()
    img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = sol.floodFill(img, 1, 1, 2)
    assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    # Already target color — no change
    img2 = [[0, 0, 0], [0, 0, 0]]
    assert sol.floodFill(img2, 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]

    # Single cell
    assert sol.floodFill([[1]], 0, 0, 5) == [[5]]
    print("All tests passed.")
