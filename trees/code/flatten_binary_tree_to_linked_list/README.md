# Flatten Binary Tree to Linked List (LC 114)

Flatten a binary tree in-place into a linked list following preorder traversal. Use the right pointer; set all left pointers to None.

## Approaches

### Reverse Postorder DFS
- **Time:** O(n), **Space:** O(h)
- Traverse in reverse preorder (right → left → root). Track the previously visited node (`prev`). At each node: set `node.right = prev`, `node.left = None`, update `prev = node`. After the full traversal, the tree is flattened in preorder.

### Morris-like Iterative (O(1) space)
- **Time:** O(n), **Space:** O(1)
- For each node with a left child: find the rightmost node of the left subtree, connect it to the current node's right subtree, move the left subtree to the right, set left to None. Advance to the right child.

## Key Insight

The reverse postorder approach works because processing right → left → root means when we visit a node, its entire right subtree has already been flattened and `prev` points to the correct next node. The Morris-like approach is the in-place O(1) solution: it "threads" the left subtree into the right by finding where the left subtree ends and connecting it to the original right subtree.

## Edge Cases

- Empty tree → no-op.
- Single node → already flat.
- No left children → already flat (Morris loop skips all nodes).
- Tree with only left children → each node's left subtree is a single node; Morris connects it to the right.
