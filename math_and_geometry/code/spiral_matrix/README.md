# LC 54 — Spiral Matrix

Given an `m × n` matrix, return all elements in spiral order (clockwise from top-left).

## Approaches

### 1. Shrinking Boundaries
- **Time:** O(m × n) | **Space:** O(1) extra
- Maintain `top`, `bottom`, `left`, `right` boundaries. Traverse: left-to-right along top, top-to-bottom along right, right-to-left along bottom (if rows remain), bottom-to-top along left (if columns remain). Shrink boundaries after each traversal.

### 2. Direction Simulation with Visited Marking
- **Time:** O(m × n) | **Space:** O(m × n)
- Use direction vectors `[(0,1),(1,0),(0,-1),(-1,0)]`. Move in current direction; when hitting a boundary or visited cell, turn right. Mark visited cells as `None`.

## Key Insight

The shrinking boundaries approach is cleaner: after traversing each side, shrink the corresponding boundary inward. The key subtlety is checking `if top < bottom` before the bottom traversal and `if left < right` before the left traversal — these prevent double-counting the single row/column case when the matrix has an odd dimension.

## Edge Cases

- Single row: Only left-to-right traversal.
- Single column: Only top-to-bottom traversal.
- Single element: Return `[matrix[0][0]]`.
- Non-square matrix: The boundary checks handle rectangular matrices correctly.
