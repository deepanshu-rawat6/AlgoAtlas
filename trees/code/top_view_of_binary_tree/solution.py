"""
GFG - Top View of Binary Tree

Problem: Return the top view of a binary tree — the first node visible at each
horizontal distance when viewed from above.

Example:
    Input:  [1,2,3,4,5,6,7]
    Output: [4,2,1,3,7]

Constraints:
    - Number of nodes: [1, 10^5]
    - 1 <= Node.val <= 10^5
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
    def topView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: BFS with column tracking; keep FIRST seen per column — O(n)
        if not root:
            return []

        col_map = {}  # col -> first node val seen (top-most)
        queue = deque([(root, 0)])  # (node, col)
        while queue:
            node, col = queue.popleft()
            if col not in col_map:  # first time seeing this column = top view
                col_map[col] = node.val
            if node.left:  queue.append((node.left,  col - 1))
            if node.right: queue.append((node.right, col + 1))

        return [col_map[c] for c in sorted(col_map)]


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert sol.topView(root) == [4, 2, 1, 3, 7]

    root2 = build_tree([1, 2, 3])
    assert sol.topView(root2) == [2, 1, 3]

    print("All tests passed.")
