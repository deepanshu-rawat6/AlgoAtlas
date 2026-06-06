# Binary Tree Postorder Traversal (LC 145)

Return the postorder traversal (left → right → root) of a binary tree's node values.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(n) recursion stack
- Recurse left, recurse right, append current value.

### Iterative (Two-Stack / Reverse Preorder)
- **Time:** O(n), **Space:** O(n)
- Use a modified preorder (root → right → left) and reverse the result. Push root; each step: pop to `stack2`, push left then right to `stack1`. Reverse `stack2` at the end to get left → right → root.

## Key Insight

Postorder is the reverse of a "root → right → left" traversal. By collecting nodes in that order and reversing, we avoid the complexity of a true iterative postorder (which requires tracking whether the right subtree has been visited). The two-stack approach is a clean O(n) solution.

## Edge Cases

- Empty tree → return `[]`.
- Single node → return `[node.val]`.
- Right-skewed tree → `stack2` collects all nodes in reverse order.
