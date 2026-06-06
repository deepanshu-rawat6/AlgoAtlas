"""
LC 545 / GFG - Boundary Traversal of Binary Tree

Problem: Return the boundary of a binary tree anticlockwise starting from root.
Boundary = left boundary (excl. leaves) + all leaves + right boundary reversed (excl. leaves).

Example:
    Input:  [1,2,3,4,5,6,7]
    Output: [1,2,4,5,6,7,3]

Constraints:
    - Number of nodes: [1, 10^4]
    - -1000 <= Node.val <= 1000
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
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: three passes — left boundary, leaves, right boundary — O(n)
        if not root:
            return []

        def is_leaf(node):
            return not node.left and not node.right

        def left_boundary(node):
            res = []
            while node:
                if not is_leaf(node):
                    res.append(node.val)
                # prefer left child, fall back to right
                node = node.left if node.left else node.right
            return res

        def leaves(node):
            if not node: return []
            if is_leaf(node): return [node.val]
            return leaves(node.left) + leaves(node.right)

        def right_boundary(node):
            res = []
            while node:
                if not is_leaf(node):
                    res.append(node.val)
                # prefer right child, fall back to left
                node = node.right if node.right else node.left
            return res[::-1]  # reverse so it goes bottom-up

        return (
            [root.val]
            + left_boundary(root.left)
            + leaves(root.left)
            + leaves(root.right)
            + right_boundary(root.right)
        )


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert sol.boundaryOfBinaryTree(root) == [1, 2, 4, 5, 6, 7, 3]

    root2 = build_tree([1])
    assert sol.boundaryOfBinaryTree(root2) == [1]

    print("All tests passed.")
