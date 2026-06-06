# Binary Tree Preorder Traversal (LC 144)

Return the preorder traversal (root → left → right) of a binary tree's node values.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(n) recursion stack
- Append current value, recurse left, recurse right.

### Iterative with Stack
- **Time:** O(n), **Space:** O(n)
- Push root to stack. Each iteration: pop, record value, push right child then left child (right first so left is processed first). This naturally produces root → left → right order.

## Key Insight

In preorder, the node is visited before its children. The iterative trick of pushing right before left exploits the LIFO nature of the stack: the left child is on top and gets processed next, matching the recursive order.

## Edge Cases

- Empty tree → return `[]`.
- Single node → return `[node.val]`.
- Left-skewed tree → stack grows to O(n) depth.
