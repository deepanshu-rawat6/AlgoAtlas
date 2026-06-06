"""
# LC 36: Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

## Examples

```text
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board with "8" appearing twice in the first row -> false
```

## Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'
"""
from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku_brute(self, board: List[List[str]]) -> bool:
        """Check rows, cols, boxes separately — O(1) time/space."""
        # Check each row, column, and 3x3 box for duplicates separately
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            col = [board[r][i] for r in range(9) if board[r][i] != "."]
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        for br in range(3):
            for bc in range(3):
                box = [
                    board[br * 3 + r][bc * 3 + c]
                    for r in range(3)
                    for c in range(3)
                    if board[br * 3 + r][bc * 3 + c] != "."
                ]
                if len(box) != len(set(box)):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Single pass with hash sets — O(1) time/space."""
        # Single pass: track seen values per row, column, and box simultaneously
        # Box index is (r//3, c//3) — maps each cell to its 3x3 region
        # If a value already exists in any of the three sets, board is invalid
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True


if __name__ == "__main__":
    s = Solution()

    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(valid_board) is True

    invalid_board = [row[:] for row in valid_board]
    invalid_board[0][1] = "5"  # duplicate 5 in row 0
    assert s.isValidSudoku(invalid_board) is False

    print("All tests passed.")
