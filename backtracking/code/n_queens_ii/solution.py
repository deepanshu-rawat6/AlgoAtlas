"""
# LC 52: N-Queens II

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard so
that no two queens attack each other. Given an integer `n`, return the number of
distinct solutions to the n-queens puzzle.

## Examples
```text
Input:  n = 4
Output: 2

Input:  n = 1
Output: 1
```

## Constraints
- 1 <= n <= 9
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        ## 52. N-Queens II

        The n-queens puzzle is the problem of placing n queens on an n x n chessboard
        such that no two queens attack each other.

        Given an integer n, return the number of distinct solutions to the n-queens puzzle.

        ### Examples

        ```text
        Input:  n = 4
        Output: 2

        Input:  n = 1
        Output: 1
        ```

        ### Constraints
        - `1 <= n <= 9`
        """
        # Same as N-Queens but only count solutions, don't store board state
        # O(n!) time, O(n) space
        cols, diag1, diag2 = set(), set(), set()
        count = 0

        def bt(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                bt(row + 1)
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

        bt(0)
        return count


if __name__ == '__main__':
    s = Solution()
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(1) == 1
    assert s.totalNQueens(8) == 92
    print("All tests passed.")
