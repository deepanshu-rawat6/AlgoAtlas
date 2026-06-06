# Diameter of Binary Tree (LC 543)

Return the length of the longest path between any two nodes in a binary tree. The path may or may not pass through the root. Length = number of edges.

## Approaches

### DFS with Global Max
- **Time:** O(n), **Space:** O(h)
- For each node, the diameter through it = `left_height + right_height`. Track a global maximum. The helper returns the height (`1 + max(left, right)`) so the parent can use it. The diameter is updated at every node, not just the root.

## Key Insight

The diameter through any node equals the sum of the heights of its left and right subtrees. The longest path in the entire tree passes through exactly one node as its "peak." By computing heights bottom-up and updating the global max at each node, we find the answer in a single O(n) pass without needing to re-root the tree.

## Edge Cases

- Single node → diameter is 0 (no edges).
- Linear tree (all left or all right) → diameter equals n-1.
- The longest path doesn't pass through the root — the global max handles this since it's updated at every node.
