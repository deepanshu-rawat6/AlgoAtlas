# Vertical Order Traversal of a Binary Tree (LC 987)

Return the vertical order traversal of a binary tree. Nodes in the same column are ordered top-to-bottom; ties (same row and column) are broken by value.

## Approaches

### BFS + Sort
- **Time:** O(n log n), **Space:** O(n)
- BFS tracking `(col, row)` for each node. Collect all `(col, row, val)` tuples. Sort by `(col, row, val)` — this handles column order, top-to-bottom within a column, and value-based tie-breaking. Group by column and return.

## Key Insight

The sort on `(col, row, val)` is the entire solution. Column determines the output group; row ensures top-to-bottom ordering within a column; value breaks ties at the same position. BFS is used (vs DFS) to naturally assign row numbers level by level, though DFS with explicit row tracking works equally well.

## Edge Cases

- Single node → one column with one value.
- Nodes at the same `(col, row)` → sorted by value (e.g., `[1, 5, 6]` in the example).
- Negative column indices → `sorted(col_map)` handles negative keys correctly.
- Perfectly balanced tree → root is at col 0, left children at col -1, right at col +1.
