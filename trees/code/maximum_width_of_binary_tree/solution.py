"""
LC 662 - Maximum Width of Binary Tree

Problem: Find the maximum width (leftmost to rightmost node, including nulls) at any level.

Example:
    Input:  [1,3,2,5,3,null,9]
    Output: 4

Constraints:
    - Number of nodes: [1, 3000]
    - -100 <= Node.val <= 100
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Approach: BFS with position index (left=2*i, right=2*i+1)
        # Normalize index at each level to prevent integer overflow — O(n)
        if not root: return 0
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            level_len = len(queue)
            _, first_idx = queue[0]
            for _ in range(level_len):
                node, idx = queue.popleft()
                idx -= first_idx  # normalize to avoid overflow
                if node.left:  queue.append((node.left,  2 * idx))
                if node.right: queue.append((node.right, 2 * idx + 1))
            max_width = max(max_width, idx + 1)
        return max_width


if __name__ == "__main__":
    sol = Solution()
    assert sol.widthOfBinaryTree(build_tree([1, 3, 2, 5, 3, None, 9])) == 4
    assert sol.widthOfBinaryTree(build_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
    assert sol.widthOfBinaryTree(build_tree([1])) == 1
    print("All tests passed.")
