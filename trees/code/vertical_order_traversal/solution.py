"""
LC 987 - Vertical Order Traversal of a Binary Tree

Problem: Return vertical order traversal column by column, top to bottom.
Nodes at the same (row, col) are sorted by value.

Example:
    Input:  [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]

Constraints:
    - Number of nodes: [1, 1000]
    - 0 <= Node.val <= 1000
"""
from typing import Optional, List
from collections import deque, defaultdict


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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach: BFS tracking (col, row); collect all, sort, group — O(n log n)
        if not root:
            return []

        nodes = []  # list of (col, row, val)
        queue = deque([(root, 0, 0)])  # (node, col, row)
        while queue:
            node, col, row = queue.popleft()
            nodes.append((col, row, node.val))
            if node.left:  queue.append((node.left,  col - 1, row + 1))
            if node.right: queue.append((node.right, col + 1, row + 1))

        # sort by col, then row, then val (handles ties at same position)
        nodes.sort()

        col_map = defaultdict(list)
        for col, _, val in nodes:
            col_map[col].append(val)

        return [col_map[c] for c in sorted(col_map)]


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert sol.verticalTraversal(root) == [[9], [3, 15], [20], [7]]

    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert sol.verticalTraversal(root2) == [[4], [2], [1, 5, 6], [3], [7]]

    print("All tests passed.")
