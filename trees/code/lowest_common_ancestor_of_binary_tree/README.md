# Lowest Common Ancestor of a Binary Tree (LC 236)

Find the lowest common ancestor (LCA) of two nodes p and q in a general binary tree (not a BST). The LCA is the deepest node that has both p and q as descendants.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(h)
- If the current node is `None`, `p`, or `q`, return it. Recurse on left and right. If both return non-None, the current node is the LCA (p and q are in different subtrees). If only one side returns non-None, propagate that result upward.

## Key Insight

The recursion works because: if p and q are in different subtrees of a node, that node is their LCA. If both are in the same subtree, the LCA is deeper and the recursion finds it. The base case `root == p or root == q` handles the case where one node is an ancestor of the other — returning it immediately means the parent will see it as the "found" result from one side.

## Edge Cases

- One node is an ancestor of the other → the ancestor is returned as soon as it's encountered; the other side returns `None`; the ancestor propagates up as the LCA.
- p and q are the same node → returns that node (but problem guarantees p ≠ q).
- Both nodes guaranteed to exist in the tree (per constraints).
