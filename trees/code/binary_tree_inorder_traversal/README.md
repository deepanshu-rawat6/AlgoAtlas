# Binary Tree Inorder Traversal (LC 94)

Return the inorder traversal (left → root → right) of a binary tree's node values.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(n) recursion stack
- Recurse left, append current value, recurse right. Clean but uses implicit stack.

### Iterative with Explicit Stack
- **Time:** O(n), **Space:** O(n)
- Use a stack and a `curr` pointer. Drill left as far as possible, pushing nodes. When `curr` is None, pop from stack (this is the "visit" step), then move to the right child.

## Key Insight

The iterative approach simulates the call stack manually. The key pattern: keep going left until you can't, then process the node, then go right. The stack holds the "return address" — nodes whose left subtrees have been fully processed but the node itself hasn't been visited yet.

## Edge Cases

- Empty tree → return `[]`.
- Single node → return `[node.val]`.
- Right-skewed tree → stack never holds more than one node at a time.
