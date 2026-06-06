# Count Complete Tree Nodes (LC 222)

Count the number of nodes in a complete binary tree more efficiently than O(n).

## Approaches

### Simple DFS
- **Time:** O(n), **Space:** O(h)
- `count(node) = 1 + count(left) + count(right)`. Visits every node.

### Height Comparison (optimal)
- **Time:** O(log² n), **Space:** O(log n)
- Compute the leftmost height and rightmost height of the current subtree.
  - If equal: the left subtree is a perfect binary tree with `2^h - 1` nodes. Return that directly.
  - If unequal: recurse on both subtrees (the last level is partially filled).
- At each level, one of the two recursive calls will hit the "equal heights" case and terminate in O(1).

## Key Insight

In a complete binary tree, if the leftmost depth equals the rightmost depth, the subtree is a perfect binary tree and its node count is `2^h - 1` (computable in O(1)). This allows skipping entire subtrees. The recursion depth is O(log n) and each level does O(log n) work for height computation, giving O(log² n) total.

## Edge Cases

- Empty tree → return 0.
- Single node → left_h = right_h = 1, returns `2^1 - 1 = 1`.
- Perfect binary tree → the root's heights are equal; returns `2^h - 1` immediately.
