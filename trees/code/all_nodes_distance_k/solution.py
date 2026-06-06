"""
LC 863 - All Nodes Distance K in Binary Tree

Problem: Find all nodes at distance k from a target node.

Example:
    Input:  [3,5,1,6,2,0,8,null,null,7,4], target=5, k=2
    Output: [7,4,1]

Constraints:
    - Number of nodes: [1, 500], all unique values
    - 0 <= k <= 1000
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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Approach: build parent map so we can traverse upward,
        # then BFS from target in all 3 directions (left, right, parent) — O(n)
        parent = {}

        def build_parents(node, par=None):
            if not node: return
            parent[node] = par
            build_parents(node.left, node)
            build_parents(node.right, node)

        build_parents(root)

        # BFS from target, avoid revisiting
        queue = deque([(target, 0)])
        visited = {target}
        result = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
                continue
            for neighbor in (node.left, node.right, parent[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return result


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    def find(node, val):
        if not node: return None
        if node.val == val: return node
        return find(node.left, val) or find(node.right, val)

    assert sorted(sol.distanceK(root, find(root, 5), 2)) == sorted([7, 4, 1])
    assert sol.distanceK(root, find(root, 5), 0) == [5]
    print("All tests passed.")
