from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    # --- Approach 1: Inorder + two pointers O(n) time, O(n) space ---
    def findTarget_two_pointer(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)
        inorder(root)                        # sorted array from BST

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == k:
                return True
            elif s < k:
                lo += 1                      # need larger sum
            else:
                hi -= 1                      # need smaller sum
        return False

    # --- Approach 2: DFS + hash set O(n) time, O(n) space ---
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node) -> bool:
            if not node:
                return False
            complement = k - node.val
            if complement in seen:
                return True                  # found a pair
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: pair exists (2+7=9)
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    assert sol.findTarget(root, 9) is True
    assert sol.findTarget_two_pointer(root, 9) is True

    # Test 2: no pair
    assert sol.findTarget(root, 28) is False
    assert sol.findTarget_two_pointer(root, 28) is False

    # Test 3: k=11 (5+6)
    assert sol.findTarget(root, 11) is True

    # Test 4: single node
    single = build_tree([1])
    assert sol.findTarget(single, 2) is False

    # Test 5: two nodes that sum to k
    root2 = build_tree([1, None, 2])
    assert sol.findTarget(root2, 3) is True

    print("All tests passed!")
