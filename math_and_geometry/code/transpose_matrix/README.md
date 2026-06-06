# LC 867 — Transpose Matrix

Given a 2D matrix, return its transpose — the matrix flipped over its main diagonal, swapping row and column indices.

## Approaches

### 1. Build Transposed Matrix Directly
- **Time:** O(m × n) | **Space:** O(m × n)
- `result[j][i] = matrix[i][j]`. Build the new matrix with dimensions `n × m` using a list comprehension: `[[matrix[r][c] for r in range(m)] for c in range(n)]`.

## Key Insight

The transpose swaps the roles of rows and columns: element at `(i, j)` moves to `(j, i)`. For a non-square matrix, the output dimensions are `n × m` (swapped from `m × n`). The list comprehension iterates over columns of the original as rows of the result, which is the most direct expression of the transpose operation.

## Edge Cases

- Square matrix: Output has the same dimensions.
- Single row: Output is a single column (n rows of 1 element each).
- Single column: Output is a single row.
- `1 × 1` matrix: Returns the same matrix.
