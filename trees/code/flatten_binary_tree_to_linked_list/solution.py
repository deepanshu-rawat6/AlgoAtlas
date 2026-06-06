"""
LC 114 - Flatten Binary Tree to Linked List

Problem: Flatten a binary tree in-place into a linked list in preorder.
Use the right pointer; set all left pointers to None.

Example:
    Input:  [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

Constraints:
    - Number of nodes: [0, 2000]
    - -100 <= Node.val <= 100
    - Must be done in-place (O(1) extra space preferred)
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals: return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Approach 1: reverse postorder (right → left → root).
        # Track previously visited node; attach it as current's right child — O(n)
        self.prev = None

        def dfs(node):
            if not node: return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev   # attach previously processed node
            node.left  = None
            self.prev  = node

        dfs(root)

    def flatten_iterative(self, root: Optional[TreeNode]) -> None:
        # Approach 2: Morris-like iterative — O(n) time, O(1) space.
        # For each node with a left child, find the rightmost node of left subtree
        # and connect it to current's right; then move left subtree to right.
        curr = root
        while curr:
            if curr.left:
                # find rightmost node of left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = curr.right  # connect to original right subtree
                curr.right = curr.left        # move left subtree to right
                curr.left  = None
            curr = curr.right


if __name__ == "__main__":
    def to_list(root):
        res = []
        while root:
            res.append(root.val)
            assert root.left is None
            root = root.right
        return res

    sol = Solution()

    root = build_tree([1, 2, 5, 3, 4, None, 6])
    sol.flatten(root)
    assert to_list(root) == [1, 2, 3, 4, 5, 6]

    root2 = build_tree([1, 2, 5, 3, 4, None, 6])
    sol.flatten_iterative(root2)
    assert to_list(root2) == [1, 2, 3, 4, 5, 6]

    print("All tests passed.")
