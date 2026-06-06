"""
LC 2385 - Amount of Time for Binary Tree to Be Infected

Problem: Starting from node `start`, fire spreads to adjacent nodes each second.
Return the minimum time to burn the entire tree.

Example:
    Input:  [1,5,3,null,4,10,6,9,2], start=3
    Output: 4

Constraints:
    - Number of nodes: [1, 10^5], all unique
    - 1 <= start <= 10^5
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Approach: build parent map + locate start node,
        # then BFS spreading in all directions — O(n)
        parent = {}
        start_node = None

        def build(node, par=None):
            nonlocal start_node
            if not node: return
            parent[node] = par
            if node.val == start: start_node = node
            build(node.left, node)
            build(node.right, node)

        build(root)

        visited = {start_node}
        queue = deque([start_node])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nb in (node.left, node.right, parent[node]):
                    if nb and nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
        return time


if __name__ == "__main__":
    sol = Solution()
    assert sol.amountOfTime(build_tree([1, 5, 3, None, 4, 10, 6, 9, 2]), 3) == 4
    assert sol.amountOfTime(build_tree([1]), 1) == 0
    print("All tests passed.")
