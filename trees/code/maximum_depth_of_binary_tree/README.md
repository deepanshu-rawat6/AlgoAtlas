# Maximum Depth of Binary Tree (LC 104)

Return the maximum depth (number of nodes along the longest root-to-leaf path) of a binary tree.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(h) where h = height
- `depth(node) = 0` if None, else `1 + max(depth(left), depth(right))`. The recursion naturally computes the longest path.

### Iterative BFS
- **Time:** O(n), **Space:** O(n)
- Level-order traversal; increment a depth counter for each level processed. The final counter is the maximum depth.

## Key Insight

Depth is defined recursively: a node's depth is one more than the deeper of its two subtrees. The base case (None → 0) handles leaves cleanly. BFS counts levels directly, which is intuitive but uses more memory for wide trees.

## Edge Cases

- Empty tree → return 0.
- Single node → return 1.
- Completely unbalanced (linked list shape) → depth equals n.
