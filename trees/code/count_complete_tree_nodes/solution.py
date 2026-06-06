"""
LC 222 - Count Complete Tree Nodes

Problem: Count nodes in a complete binary tree more efficiently than O(n).

Example:
    Input:  [1,2,3,4,5,6]
    Output: 6

Constraints:
    - Number of nodes: [0, 5 * 10^4]
    - Complete binary tree guaranteed
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Approach 1: simple DFS — O(n)
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes_fast(self, root: Optional[TreeNode]) -> int:
        # Approach 2: compare left-most and right-most heights.
        # If equal, left subtree is a perfect binary tree → skip it — O(log^2 n)
        if not root: return 0

        left_h, right_h = 0, 0
        l, r = root, root
        while l: left_h  += 1; l = l.left   # height going left
        while r: right_h += 1; r = r.right  # height going right

        if left_h == right_h:
            return (1 << left_h) - 1  # perfect tree: 2^h - 1 nodes

        # not perfect: recurse on both subtrees
        return 1 + self.countNodes_fast(root.left) + self.countNodes_fast(root.right)


if __name__ == "__main__":
    sol = Solution()
    assert sol.countNodes(build_tree([1, 2, 3, 4, 5, 6])) == 6
    assert sol.countNodes_fast(build_tree([1, 2, 3, 4, 5, 6])) == 6
    assert sol.countNodes_fast(build_tree([])) == 0
    assert sol.countNodes_fast(build_tree([1])) == 1
    print("All tests passed.")
