"""
LC 257 - Binary Tree Paths

Problem: Return all root-to-leaf paths in a binary tree as strings joined by "->".

Example:
    Input:  [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

Constraints:
    - Number of nodes: [1, 100]
    - -100 <= Node.val <= 100
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Approach: DFS with path accumulation; record on reaching a leaf — O(n)
        result = []

        def dfs(node, path):
            if not node.left and not node.right:  # leaf
                result.append(path)
                return
            if node.left:  dfs(node.left,  path + "->" + str(node.left.val))
            if node.right: dfs(node.right, path + "->" + str(node.right.val))

        if root:
            dfs(root, str(root.val))
        return result


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([1, 2, 3, None, 5])
    assert sorted(sol.binaryTreePaths(root)) == sorted(["1->2->5", "1->3"])

    root2 = build_tree([1])
    assert sol.binaryTreePaths(root2) == ["1"]

    print("All tests passed.")
