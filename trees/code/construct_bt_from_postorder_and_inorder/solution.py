"""
LC 106 - Construct Binary Tree from Inorder and Postorder Traversal

Problem: Build a binary tree given its inorder and postorder traversals.

Example:
    Input:  inorder=[9,3,15,20,7], postorder=[9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]

Constraints:
    - 1 <= len(inorder) <= 3000, all values unique
"""
from typing import Optional, List
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Approach: last element of postorder is root; find it in inorder to
        # split left/right subtrees. Hash map gives O(1) lookup — O(n) total.
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(in_left, in_right):
            if in_left > in_right: return None
            root_val = postorder.pop()          # rightmost = current root
            root = TreeNode(root_val)
            mid = idx_map[root_val]
            # build right before left (postorder pops from end)
            root.right = helper(mid + 1, in_right)
            root.left  = helper(in_left, mid - 1)
            return root

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    from collections import deque

    def tree_to_list(root):
        if not root: return []
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            res.append(node.val if node else None)
            if node:
                q.append(node.left)
                q.append(node.right)
        while res and res[-1] is None: res.pop()
        return res

    sol = Solution()
    root = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    assert tree_to_list(root) == [3, 9, 20, None, None, 15, 7]
    print("All tests passed.")
