"""
LC 236 - Lowest Common Ancestor of a Binary Tree

Problem: Find LCA of nodes p and q in a general binary tree.

Example:
    Input:  [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1
    Output: 3

Constraints:
    - Number of nodes: [2, 10^5], all unique
    - p != q, both exist in the tree
"""
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Approach: recursive — if current node is p or q return it;
        # if both subtrees return non-null, current node is the LCA — O(n)
        if not root or root == p or root == q:
            return root
        left  = self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # both sides found a target → current node is LCA
        if left and right: return root
        return left or right


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    def find(node, val):
        if not node: return None
        if node.val == val: return node
        return find(node.left, val) or find(node.right, val)

    assert sol.lowestCommonAncestor(root, find(root, 5), find(root, 1)).val == 3
    assert sol.lowestCommonAncestor(root, find(root, 5), find(root, 4)).val == 5
    print("All tests passed.")
