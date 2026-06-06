"""
# LC 37: Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
Each row, column, and 3×3 box must contain digits 1-9 without repetition.

## Examples

```text
Input:  board with '.' for empty cells
Output: board filled with valid solution
```

## Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'
- Input board has exactly one solution
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Backtracking: find empty cell, try digits 1-9, validate, recurse
        # Optimization: use sets for rows, cols, boxes for O(1) validity check

        # Pre-populate constraint sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    d = board[r][c]
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[(r // 3) * 3 + c // 3].add(d)

        def backtrack(pos):
            # Find next empty cell starting from pos
            while pos < 81:
                r, c = divmod(pos, 9)
                if board[r][c] == '.':
                    break
                pos += 1
            else:
                return True  # All cells filled

            r, c = divmod(pos, 9)
            box_id = (r // 3) * 3 + c // 3

            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_id]:
                    # Place digit
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box_id].add(d)

                    if backtrack(pos + 1):
                        return True

                    # Backtrack: remove digit
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box_id].remove(d)

            return False

        backtrack(0)


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    sol.solveSudoku(board)
    for row in board:
        print(row)
