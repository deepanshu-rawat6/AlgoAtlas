"""
# 130. Surrounded Regions

## Problem
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are
4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s into
`'X'`s in that surrounded region.

An `'O'` is not captured if it is on the border or connected to a border `'O'`.

## Examples
```text
Input:  board = [["X","X","X","X"],
                 ["X","O","O","X"],
                 ["X","X","O","X"],
                 ["X","O","X","X"]]
Output:         [["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","O","X","X"]]
Explanation: The bottom 'O' is on the border and not captured.
```

```text
Input:  board = [["X"]]
Output: [["X"]]
```

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`
"""

from typing import List
from collections import deque


class Solution:
    def solve_dfs(self, board: List[List[str]]) -> None:
        # O(m*n) time, O(m*n) space — DFS mark border-connected O's, then flip rest
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'S'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

    def solve(self, board: List[List[str]]) -> None:
        # Mark all 'O' cells connected to the border as safe (DFS/BFS from borders)
        # Flip remaining 'O' cells to 'X'; restore safe cells back to 'O'
        # O(m*n) time, O(m*n) space — BFS mark border-connected O's, then flip rest
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == 'O':
                    board[r][c] = 'S'
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    q.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 'O' if board[r][c] == 'S' else 'X'


if __name__ == '__main__':
    import copy
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    b1 = copy.deepcopy(board)
    s.solve_dfs(b1)
    assert b1 == expected

    b2 = copy.deepcopy(board)
    s.solve(b2)
    assert b2 == expected

    print("All tests passed.")
