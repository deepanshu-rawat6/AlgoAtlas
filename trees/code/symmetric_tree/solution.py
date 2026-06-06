"""
LC 101 - Symmetric Tree

Problem: Check whether a binary tree is a mirror of itself (symmetric around its center).

Example:
    Input:  [1,2,2,3,4,4,3]
    Output: True

    Input:  [1,2,2,null,3,null,3]
    Output: False

Constraints:
    - Number of nodes: [1, 1000]
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
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Approach 1: Recursive — compare mirror positions — O(n)
        def is_mirror(left, right):
            if not left and not right: return True
            if not left or not right:  return False
            return (
                left.val == right.val
                and is_mirror(left.left,  right.right)  # outer pair
                and is_mirror(left.right, right.left)   # inner pair
            )
        return is_mirror(root.left, root.right)

    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        # Approach 2: Iterative BFS with queue of mirror pairs — O(n)
        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if not left and not right: continue
            if not left or not right:  return False
            if left.val != right.val:  return False
            queue.append((left.left,  right.right))  # outer pair
            queue.append((left.right, right.left))   # inner pair
        return True


if __name__ == "__main__":
    sol = Solution()

    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    assert sol.isSymmetric(root) is True
    assert sol.isSymmetric_iterative(root) is True

    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    assert sol.isSymmetric(root2) is False
    assert sol.isSymmetric_iterative(root2) is False

    print("All tests passed.")
