# Lowest Common Ancestor of a Binary Search Tree (LC 235)

Find the lowest common ancestor (LCA) of two nodes p and q in a BST. The LCA is the deepest node that has both p and q as descendants (a node is a descendant of itself).

## Approaches

### Recursive BST Navigation
- **Time:** O(h), **Space:** O(h)
- If both p and q are less than root, LCA is in the left subtree. If both are greater, LCA is in the right subtree. Otherwise, root is the LCA (the paths to p and q diverge here).

### Iterative BST Navigation
- **Time:** O(h), **Space:** O(1)
- Same logic without recursion — walk down the tree with a pointer.

## Key Insight

The BST property makes LCA trivial: the LCA is the first node where p and q are on different sides (or one of them is the node itself). No need to search both subtrees — the BST ordering tells you exactly which direction to go. This is O(h) vs O(n) for a general binary tree.

## Edge Cases

- One node is an ancestor of the other → the ancestor is the LCA (the condition `p.val < root.val and q.val < root.val` fails at the ancestor, returning it).
- p and q are the same node → returns that node.
- p or q is the root → root is the LCA immediately.
