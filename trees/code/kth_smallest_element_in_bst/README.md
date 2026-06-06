# Kth Smallest Element in a BST (LC 230)

Return the k-th smallest value (1-indexed) in a BST.

## Approaches

### Inorder Traversal (collect all)
- **Time:** O(n), **Space:** O(n)
- Inorder traversal of a BST yields values in sorted ascending order. Collect all values, return index `k-1`.

### Iterative Inorder (early stop)
- **Time:** O(h + k), **Space:** O(h)
- Iterative inorder with an explicit stack. Maintain a counter; when the counter reaches k, return the current node's value immediately without traversing the rest of the tree.

## Key Insight

BST inorder traversal is inherently sorted. The k-th element visited in inorder is the k-th smallest. The iterative approach is optimal because it stops as soon as the k-th element is found — no need to traverse the entire tree. For a balanced BST, this is O(log n + k).

## Edge Cases

- k = 1 → return the leftmost node (minimum).
- k = n → return the rightmost node (maximum).
- BST with duplicate values → problem guarantees unique values per constraints.
