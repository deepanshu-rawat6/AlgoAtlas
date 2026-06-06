# Construct Binary Tree from Inorder and Postorder Traversal (LC 106)

Given inorder and postorder traversal arrays (all values unique), reconstruct and return the binary tree.

## Approaches

### Recursive with HashMap + Postorder Pointer
- **Time:** O(n), **Space:** O(n)
- Pre-build a hashmap of `{value: index}` for inorder. The last element of postorder is always the current root. Find the root in inorder to split left/right subtrees. Build right subtree before left (postorder pops from the end, so right subtree elements come before left in the remaining postorder).

## Key Insight

Postorder gives the root last; inorder gives the left/right split. The critical ordering detail: when recursing, build the **right** subtree before the left, because postorder is `[left... | right... | root]` — after popping the root, the next element from the end is the right subtree's root. Building right first ensures the postorder pointer is consumed in the correct order.

## Edge Cases

- Single node → postorder and inorder both have one element; return a leaf.
- Left-skewed tree → right subtree is always empty; left subtree consumes all remaining elements.
- All values must be unique (guaranteed) — otherwise inorder index lookup would be ambiguous.
