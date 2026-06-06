# Morris Traversal (Inorder and Preorder)

Traverse a binary tree in inorder or preorder using O(1) extra space — no stack, no recursion. Uses temporary threading of the tree.

## Approaches

### Morris Inorder
- **Time:** O(n), **Space:** O(1)
- For each node: if no left child, visit and go right. Otherwise, find the inorder predecessor (rightmost node of left subtree). If predecessor has no right child, create a thread (`pred.right = curr`) and go left. If predecessor's right child is `curr` (thread exists), remove the thread, visit `curr`, go right.

### Morris Preorder
- **Time:** O(n), **Space:** O(1)
- Same threading logic, but visit the node **before** going left (when creating the thread, not when removing it).

## Key Insight

Morris traversal uses the tree's own null right pointers as temporary "threads" to return to ancestor nodes without a stack. The inorder predecessor's right pointer is normally null — Morris temporarily sets it to the current node as a return path. The second visit (when the thread is detected) is the "visit" moment for inorder; the first visit is the "visit" moment for preorder.

## Edge Cases

- Empty tree → returns `[]`.
- Single node → no left child, visited immediately, goes right (None), loop ends.
- All threads are restored before the traversal ends — the tree structure is unchanged after traversal.
- Right-skewed tree → no left children, no threads created; pure right traversal.
