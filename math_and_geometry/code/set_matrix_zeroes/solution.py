"""
# 73. Set Matrix Zeroes

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`s.

You must do it **in place**.

## Examples

```text
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List


class Solution:
    def setZeroes_extra_space(self, matrix: List[List[int]]) -> None:
        # O(m*n) time, O(m+n) space — record zero rows/cols then zero them out
        rows, cols = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r); cols.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Use first row and first column as markers to avoid O(m+n) extra space
        # First pass: mark rows/cols that need zeroing using first row/col
        # Second pass: zero cells based on markers; then zero first row/col if needed
        # O(m*n) time, O(1) space — use first row/col as markers
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row_zero:
            for c in range(n): matrix[0][c] = 0
        if first_col_zero:
            for r in range(m): matrix[r][0] = 0


if __name__ == '__main__':
    import copy
    s = Solution()
    for method in (s.setZeroes_extra_space, s.setZeroes):
        m = [[1,1,1],[1,0,1],[1,1,1]]
        method(m)
        assert m == [[1,0,1],[0,0,0],[1,0,1]], f"Failed: {m}"
    print("All tests passed.")
