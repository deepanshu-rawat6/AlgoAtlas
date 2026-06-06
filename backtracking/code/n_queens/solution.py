from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        ## 51. N-Queens

        The n-queens puzzle is the problem of placing n queens on an n x n chessboard
        such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle.
        You may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens' placement,
        where 'Q' and '.' both indicate a queen and an empty space, respectively.

        ### Examples

        ```text
        Input:  n = 4
        Output: [[".Q..","...Q","Q...","..Q."],
                 ["..Q.","Q...","...Q",".Q.."]]

        Input:  n = 1
        Output: [["Q"]]
        ```

        ### Constraints
        - `1 <= n <= 9`
        """
        # Place one queen per row; track occupied columns, diagonals, anti-diagonals
        # Backtrack by removing queen and clearing its column/diagonal markers
        # O(n!) time, O(n) space for tracking sets
        result = []
        cols, diag1, diag2 = set(), set(), set()
        board = [['.' ] * n for _ in range(n)]

        def bt(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                board[row][col] = 'Q'
                bt(row + 1)
                board[row][col] = '.'
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

        bt(0)
        return result


if __name__ == '__main__':
    s = Solution()
    res4 = s.solveNQueens(4)
    assert len(res4) == 2
    assert sorted(res4) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert s.solveNQueens(1) == [["Q"]]
    print("All tests passed.")
