# Range Sum Query 2D - Immutable (LC 304)

Given a 2D matrix, handle multiple queries: return the sum of elements inside a rectangle
defined by its upper-left `(row1, col1)` and lower-right `(row2, col2)` corners.

## Approaches

### 1. Brute Force — O(m·n) per query, O(1) extra space
Sum all elements in the rectangle on each query.

**Why it works:** Correct but slow for many queries — recomputes the same sums repeatedly.

### 2. 2D Prefix Sum — O(m·n) build, O(1) per query
Precompute `prefix[r][c]` = sum of all elements in the rectangle from `(0,0)` to `(r-1, c-1)`. Answer any query with inclusion-exclusion: `prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`.

**Why it works:** The 2D prefix sum encodes all rectangle sums from the origin. Any arbitrary rectangle sum is recovered in O(1) using inclusion-exclusion on four corner values.

## Key Insight
2D inclusion-exclusion: `sum(rect) = prefix[bottom-right] - prefix[top-right] - prefix[bottom-left] + prefix[top-left]`. The `+` at the end corrects for double-subtracting the top-left corner.

## Edge Cases
- Single cell query (`row1==row2`, `col1==col2`)
- Query covering the entire matrix
- Matrix with negative values (prefix sum still works)
- 1×1 matrix
