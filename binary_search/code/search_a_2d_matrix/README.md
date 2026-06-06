# Search a 2D Matrix (LC 74)

Given an m×n matrix where each row is sorted and the first element of each row is greater than the last of the previous row, search for a target in O(log(m×n)) time.

## Approaches

### 1. Brute Force
- **Time:** O(m×n) | **Space:** O(1)
- Scan every element.

### 2. Binary Search on Flattened Index
- **Time:** O(log(m×n)) | **Space:** O(1)
- Treat the matrix as a 1D sorted array of length `m*n`. Binary search on indices `[0, m*n - 1]`.
- Convert flat index `mid` to 2D: `row = mid // n`, `col = mid % n`.
- Standard binary search from there.

## Key Insight

The two properties (each row sorted, first element of row i+1 > last of row i) mean the entire matrix is one continuous sorted sequence when read row by row. This lets us apply a single binary search over the virtual 1D array, using index math to map back to 2D coordinates. No need to binary search rows first, then columns.

## Edge Cases

- Single cell matrix (`m=1, n=1`): works correctly.
- Target smaller than `matrix[0][0]` → `hi` drops below 0 → False.
- Target larger than `matrix[m-1][n-1]` → `lo` exceeds last index → False.
- Target at corners or edges: handled by standard binary search.
