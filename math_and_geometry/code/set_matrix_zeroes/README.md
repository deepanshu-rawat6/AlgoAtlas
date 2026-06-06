# LC 73 — Set Matrix Zeroes

Given an `m × n` matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

## Approaches

### 1. Extra Space (Sets)
- **Time:** O(m × n) | **Space:** O(m + n)
- First pass: record which rows and columns contain zeros. Second pass: zero out those rows and columns.

### 2. In-place with First Row/Column as Markers
- **Time:** O(m × n) | **Space:** O(1)
- Use `matrix[0][c]` and `matrix[r][0]` as markers for which rows/columns need zeroing. Handle the first row and column separately with boolean flags (since they're used as markers).

## Key Insight

The O(1) space trick reuses the first row and column as a marker array. Before using them as markers, record whether they themselves contain zeros (with `first_row_zero` and `first_col_zero` flags). Then mark, zero the interior, and finally zero the first row/column if needed. The order matters: zero the interior before zeroing the markers.

## Edge Cases

- Zero in the first row or column: The boolean flags handle this correctly.
- Multiple zeros in the same row/column: Marking is idempotent.
- All zeros: The entire matrix becomes zero.
- Single element that is zero: Zero the entire (1×1) matrix.
