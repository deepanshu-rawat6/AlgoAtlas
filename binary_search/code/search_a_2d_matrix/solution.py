"""
LC 74 - Search a 2D Matrix
===========================

You are given an m x n integer matrix `matrix` with the following two
properties:
  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the
    previous row.

Given an integer `target`, return true if `target` is in `matrix`, or false
otherwise.

Examples
--------
```text
Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

Constraints
-----------
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    def method_brute_force(self, matrix: List[List[int]], target: int) -> bool:
        # O(m*n) time | O(1) space
        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the 2D matrix as a 1D sorted array using index math
        # mid // n gives row, mid % n gives column
        # O(log(m*n)) time | O(1) space
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(mat, 3) is True
    assert s.searchMatrix(mat, 13) is False
    assert s.method_brute_force(mat, 3) is True
    assert s.method_brute_force(mat, 13) is False
    print("All tests passed.")
