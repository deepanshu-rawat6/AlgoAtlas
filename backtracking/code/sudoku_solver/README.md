# Sudoku Solver (LC 37)

Fill empty cells (`'.'`) in a 9×9 Sudoku board so each row, column, and 3×3 box
contains digits 1-9 without repetition. The input has exactly one solution.

## Approaches

### 1. Backtracking with Constraint Sets
**Complexity:** O(9^m) time where m = empty cells, O(1) space (board is fixed size)

Pre-populate sets for each row, column, and 3×3 box with existing digits. Find the
next empty cell; try digits 1-9. Place a digit if it's not in the row/col/box sets.
Recurse; backtrack if no digit works.

**Why it works:** Constraint sets provide O(1) validity checking. Backtracking
exhaustively tries all valid placements. Since the problem guarantees a unique solution,
the first complete valid assignment is the answer.

## Key Insight

Pre-populating constraint sets (rows, cols, boxes) before backtracking avoids O(n)
validity scans at each step. The box index formula `(r//3)*3 + c//3` maps any cell to
its 3×3 box in O(1).

## Edge Cases

- Nearly complete board — very fast (few empty cells).
- Board with many empty cells — worst case O(9^81) but constraint propagation prunes heavily.
- The problem guarantees exactly one solution — no need to handle multiple solutions.
