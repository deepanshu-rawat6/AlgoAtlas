# Binary Tree Paths (LC 257)

Return all root-to-leaf paths in a binary tree as strings in the format `"1->2->5"`.

## Approaches

### DFS with Path Accumulation
- **Time:** O(n * h) — string concatenation at each node
- **Space:** O(h) recursion + O(n * h) for result strings
- DFS passing the current path string. When a leaf is reached, append the path to results. For non-leaves, recurse on each child with the path extended by `"->" + child.val`.

## Key Insight

The path is built top-down as a string. Leaf detection (`not node.left and not node.right`) is the termination condition. String concatenation creates a new string at each step, so each path is independent — no backtracking needed. Using a list and joining at the end would be more efficient for very long paths.

## Edge Cases

- Single node → one path containing just the root value.
- Left-skewed tree → one path containing all nodes.
- A node with only one child → only one recursive call is made.
