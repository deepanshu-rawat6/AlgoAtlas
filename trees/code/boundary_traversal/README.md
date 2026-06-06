# Boundary Traversal of Binary Tree (LC 545 / GFG)

Return the boundary of a binary tree anticlockwise starting from the root: left boundary (excluding leaves) + all leaves (left to right) + right boundary reversed (excluding leaves).

## Approaches

### Three-Pass DFS
- **Time:** O(n), **Space:** O(h)
- Split into three parts:
  1. **Left boundary**: walk left (prefer left child, fall back to right), skip leaves.
  2. **Leaves**: DFS collecting all leaf nodes left to right.
  3. **Right boundary**: walk right (prefer right child, fall back to left), skip leaves, then reverse.
- Combine: `[root] + left_boundary + leaves(left) + leaves(right) + right_boundary`.

## Key Insight

The boundary is defined by three distinct traversal patterns. Separating them makes the logic clean. The "prefer left/right, fall back to the other" rule for boundaries ensures we follow the outermost path. Leaves are excluded from boundaries to avoid double-counting (they're collected separately). The right boundary is reversed because we traverse it top-down but need it bottom-up for anticlockwise order.

## Edge Cases

- Single node → just `[root.val]` (it's both root and a leaf; no boundary or leaf passes needed).
- Root with only a left subtree → right boundary is empty.
- A leaf that is also the only child → it appears in the leaves pass, not the boundary pass.
