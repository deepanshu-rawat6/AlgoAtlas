# Valid Sudoku (LC 36)

Determine if a 9×9 Sudoku board is valid. Each row, column, and 3×3 box must contain
digits 1–9 without repetition. Empty cells (`.`) are ignored.

## Approaches

### 1. Separate Checks — O(1) time, O(1) space
Check each row, each column, and each 3×3 box independently for duplicates using sets.

**Why it works:** Three independent passes each verify one constraint. Board size is fixed at 81 cells so complexity is truly O(1).

### 2. Single Pass with Hash Sets — O(1) time, O(1) space
One pass over all 81 cells. For each digit, check and record it in three sets simultaneously: `rows[r]`, `cols[c]`, `boxes[(r//3, c//3)]`.

**Why it works:** All three constraints are checked in one traversal. The box index `(r//3, c//3)` maps each cell to its 3×3 region in O(1).

## Key Insight
Box index `(r//3, c//3)` is the key trick — it maps any cell to one of the nine 3×3 boxes without extra computation.

## Edge Cases
- Mostly empty board → valid
- Duplicate in a box but not in its row or column → invalid
- Digit appearing in both a row and a column at different cells → two separate violations
- Board can be valid but unsolvable (problem only asks for validity)
