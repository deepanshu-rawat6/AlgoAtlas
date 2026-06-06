# Invert Binary Tree (LC 226)

Invert a binary tree (mirror it) and return its root.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(h)
- Swap left and right children at each node, then recursively invert both subtrees. The swap happens before or after recursion — both work since we're swapping references.

### Iterative BFS
- **Time:** O(n), **Space:** O(n)
- Level-order traversal with a queue. For each dequeued node, swap its children, then enqueue both children.

## Key Insight

Inverting a tree is purely structural — every node's children are swapped. The recursive approach is elegant: after swapping at the current node, the recursive calls handle the rest. BFS is equally valid and avoids recursion stack depth concerns for very deep trees.

## Edge Cases

- Empty tree → return `None`.
- Single node → return it unchanged (no children to swap).
- Already symmetric tree → still valid to invert (result is the same tree).
