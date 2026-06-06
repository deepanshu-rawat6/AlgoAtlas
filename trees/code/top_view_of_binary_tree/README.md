# Top View of Binary Tree (GFG)

Return the top view of a binary tree — the first node visible at each horizontal distance (column) when viewed from above, ordered left to right.

## Approaches

### BFS with Column Tracking
- **Time:** O(n log n) — sorting column keys
- **Space:** O(n)
- BFS tracking `(node, col)`. For each node, if its column hasn't been seen yet, record it (first seen = topmost). Left child gets `col - 1`, right child gets `col + 1`. Return values sorted by column.

## Key Insight

The top view is the first node encountered at each column during BFS (level-order). BFS processes nodes top-to-bottom, so the first node at each column is guaranteed to be the topmost. The `if col not in col_map` check ensures only the first (topmost) node per column is recorded.

## Edge Cases

- Single node → one column, returns `[root.val]`.
- Left-skewed tree → each node is at a unique column; all are visible from the top.
- Nodes directly above each other (same column) → only the topmost is in the top view.
- Negative column indices are handled correctly by `sorted(col_map)`.
