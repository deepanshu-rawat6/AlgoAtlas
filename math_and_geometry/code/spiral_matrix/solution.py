"""
# 54. Spiral Matrix

Given an `m x n` matrix, return all elements of the matrix in spiral order.

## Examples

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiralOrder_layers(self, matrix: List[List[int]]) -> List[int]:
        # O(m*n) time — peel off outer layer iteratively
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            result += matrix[top][left:right+1]
            for r in range(top + 1, bottom + 1):
                result.append(matrix[r][right])
            if top < bottom:
                result += matrix[bottom][left:right][::-1]
            if left < right:
                for r in range(bottom - 1, top, -1):
                    result.append(matrix[r][left])
            top += 1; bottom -= 1; left += 1; right -= 1
        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Shrink boundaries (top, bottom, left, right) after traversing each side
        # Traverse: left-to-right, top-to-bottom, right-to-left, bottom-to-top
        # O(m*n) time — direction simulation with visited marking
        m, n = len(matrix), len(matrix[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        d = r = c = 0
        result = []
        for _ in range(m * n):
            result.append(matrix[r][c])
            matrix[r][c] = None
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] is not None):
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            r, c = nr, nc
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.spiralOrder_layers([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert s.spiralOrder_layers([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("All tests passed.")
