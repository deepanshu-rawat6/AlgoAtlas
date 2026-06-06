# Bottom View of Binary Tree (GFG)

Return the bottom view of a binary tree — the last node visible at each horizontal distance (column) when viewed from below, ordered left to right.

## Approaches

### BFS with Column Tracking
- **Time:** O(n log n) — sorting column keys
- **Space:** O(n)
- BFS tracking `(node, col)`. For each node, always overwrite `col_map[col]` with the current node's value (last seen = bottommost). Left child gets `col - 1`, right child gets `col + 1`. Return values sorted by column.

## Key Insight

The bottom view is the last node encountered at each column during BFS. Since BFS processes nodes top-to-bottom, always overwriting `col_map[col]` ensures the final value is the bottommost node at that column. This is the complement of top view — the only difference is `if col not in col_map` (top) vs always overwrite (bottom).

## Edge Cases

- Single node → one column, returns `[root.val]`.
- Nodes directly above each other (same column) → only the bottommost is in the bottom view.
- For a complete binary tree, the bottom view shows the leaf level nodes.
- Negative column indices are handled correctly by `sorted(col_map)`.
