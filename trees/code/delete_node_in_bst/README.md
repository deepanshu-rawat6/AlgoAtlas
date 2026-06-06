# Delete Node in a BST (LC 450)

Delete a node with a given key from a BST and return the root.

## Approaches

### Recursive with In-Order Successor
- **Time:** O(h), **Space:** O(h)
- Navigate to the target node using BST ordering. Three cases on deletion:
  1. No left child → return right child.
  2. No right child → return left child.
  3. Two children → replace node's value with its in-order successor (leftmost node of right subtree), then delete the successor from the right subtree.

## Key Insight

The in-order successor is the smallest value greater than the deleted node — it's the correct replacement to maintain BST ordering. After copying the successor's value up, we delete the successor (which has at most one child — no left child by definition of "leftmost"), making the deletion clean.

## Edge Cases

- Key not found → tree is unchanged (recursion reaches None and returns None).
- Deleting a leaf → both children are None, return None.
- Deleting the root with two children → root value is replaced by successor, successor is deleted from right subtree.
- Empty tree → return None.
