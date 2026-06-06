# Construct Binary Tree from Preorder and Inorder Traversal (LC 105)

Given preorder and inorder traversal arrays of a binary tree (all values unique), reconstruct and return the tree.

## Approaches

### Recursive Slicing
- **Time:** O(n²) — `inorder.index()` is O(n) per call
- **Space:** O(n) recursion + O(n) for slices
- `preorder[0]` is always the root. Find it in `inorder` to split left/right subtrees. The left subtree has `mid` nodes in preorder; recurse on both halves.

### Recursive with HashMap (optimal)
- **Time:** O(n), **Space:** O(n)
- Pre-build a hashmap of `{value: index}` for inorder. Use a global preorder index pointer. At each call, look up the root's inorder position in O(1), recurse on left then right.

## Key Insight

Preorder gives the root first; inorder gives the split between left and right subtrees. The number of nodes in the left subtree (from inorder) tells us exactly how many elements in preorder belong to the left subtree. The hashmap eliminates the O(n) linear scan, making the overall algorithm O(n).

## Edge Cases

- Single node → preorder and inorder both have one element; return a leaf.
- Left-skewed tree → left subtree always has `mid` elements, right is empty.
- All values must be unique (guaranteed) — otherwise the inorder index lookup would be ambiguous.
