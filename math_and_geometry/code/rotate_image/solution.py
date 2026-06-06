"""
# 48. Rotate Image

You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees clockwise **in-place**.

You must modify the input matrix directly. Do not allocate another 2D matrix.

## Examples

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate_transpose(self, matrix: List[List[int]]) -> None:
        # O(n^2) time, O(1) space — transpose then reverse each row
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        # Then reverse each row to achieve 90-degree clockwise rotation
        # O(n^2) time, O(1) space — four-way cyclic swap layer by layer
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp


if __name__ == '__main__':
    import copy
    s = Solution()
    for method in (s.rotate_transpose, s.rotate):
        m = [[1,2,3],[4,5,6],[7,8,9]]
        method(m)
        assert m == [[7,4,1],[8,5,2],[9,6,3]], f"Failed: {m}"
    print("All tests passed.")
