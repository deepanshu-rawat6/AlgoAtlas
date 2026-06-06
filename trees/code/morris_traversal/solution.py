"""
Morris Traversal - Inorder and Preorder (O(1) space, no stack/recursion)

Problem: Traverse a binary tree inorder and preorder using Morris threading.
Temporarily links each node to its inorder predecessor to avoid a stack.

Example:
    Input:  [1,2,3,4,5]
    Inorder:  [4,2,5,1,3]
    Preorder: [1,2,4,5,3]
"""
from typing import List
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
    def morrisInorder(self, root) -> List[int]:
        # For each node with a left child, find its inorder predecessor
        # (rightmost node in left subtree).
        # If predecessor has no right child → create thread, go left.
        # If predecessor's right child is current → remove thread, record, go right.
        result, curr = [], root
        while curr:
            if not curr.left:
                result.append(curr.val)   # no left subtree, visit and go right
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right     # find inorder predecessor

                if not pred.right:
                    pred.right = curr     # create thread to come back
                    curr = curr.left
                else:
                    pred.right = None     # remove thread
                    result.append(curr.val)
                    curr = curr.right
        return result

    def morrisPreorder(self, root) -> List[int]:
        # Same threading logic but record node BEFORE going left (not after).
        result, curr = [], root
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if not pred.right:
                    result.append(curr.val)  # record here (preorder = before left)
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right
        return result


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5])
    assert sol.morrisInorder(root)  == [4, 2, 5, 1, 3]
    assert sol.morrisPreorder(root) == [1, 2, 4, 5, 3]
    print("All tests passed.")
