# Binary Tree Maximum Path Sum (LC 124)

Find the maximum sum of any path in a binary tree. A path is any sequence of nodes connected by edges; it doesn't need to pass through the root.

## Approaches

### DFS with Global Max
- **Time:** O(n), **Space:** O(h)
- For each node, compute the max gain from the left and right subtrees (clamped to 0 — negative branches are skipped). The path sum through this node = `node.val + left_gain + right_gain`. Update the global max. Return `node.val + max(left_gain, right_gain)` to the parent (a path can only extend in one direction upward).

## Key Insight

A path through a node can use both its left and right subtrees (forming an arch), but when contributing to a parent's path, only one side can be chosen (a path can't branch). This is why we update the global max with `left + right + node.val` but return only `node.val + max(left, right)`. Clamping gains to 0 handles negative subtrees — it's better to not include them.

## Edge Cases

- All negative values → the answer is the single largest (least negative) node value. The global max is initialized to `-inf` and the 0-clamp ensures we still consider single-node paths.
- Single node → return its value.
- Path doesn't pass through root → the global max is updated at every node, not just the root.
