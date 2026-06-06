# Validate Binary Search Tree (LC 98)

Determine if a binary tree is a valid BST: left subtree contains only values strictly less than the node, right subtree only strictly greater, recursively.

## Approaches

### Range Validation (DFS with bounds)
- **Time:** O(n), **Space:** O(h)
- Pass a valid range `(lo, hi)` down the tree. Each node must satisfy `lo < node.val < hi`. Going left tightens the upper bound to `node.val`; going right tightens the lower bound.

### Inorder Traversal
- **Time:** O(n), **Space:** O(n)
- Inorder traversal of a valid BST produces a strictly increasing sequence. Collect all values and verify `result[i] < result[i+1]` for all i.

## Key Insight

The range approach is more efficient (O(h) space vs O(n)) and catches violations immediately without storing the full traversal. The critical insight is that BST validity is not just about parent-child relationships — a node in the right subtree must be greater than all ancestors above it, not just its direct parent. The `(lo, hi)` bounds encode this constraint.

## Edge Cases

- `[5, 1, 4, null, null, 3, 6]` → invalid because 4 < 5 (right child must be > root).
- Duplicate values → invalid (BST requires strict inequality).
- Values at `INT_MIN` or `INT_MAX` → use `float('-inf')` and `float('inf')` as initial bounds.
