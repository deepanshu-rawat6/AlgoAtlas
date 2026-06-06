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


def tree_to_inorder(root: Optional[TreeNode]) -> list:
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    dfs(root)
    return result


class Solution:
    def _inorder(self, root: Optional[TreeNode]) -> list:
        """Extract sorted values from BST via inorder traversal."""
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(root)
        return result

    def _merge_sorted(self, a: list, b: list) -> list:
        """Merge two sorted arrays into one sorted array."""
        merged, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    def _sorted_to_bst(self, nums: list) -> Optional[TreeNode]:
        """Build a height-balanced BST from a sorted array (mid as root)."""
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self._sorted_to_bst(nums[:mid])
        node.right = self._sorted_to_bst(nums[mid + 1:])
        return node

    def mergeBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: get sorted arrays from both BSTs
        sorted1 = self._inorder(root1)
        sorted2 = self._inorder(root2)
        # Step 2: merge the two sorted arrays
        merged = self._merge_sorted(sorted1, sorted2)
        # Step 3: build balanced BST from merged sorted array
        return self._sorted_to_bst(merged)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard case
    root1 = build_tree([3, 1, 5])
    root2 = build_tree([4, 2, 6])
    merged = sol.mergeBSTs(root1, root2)
    assert tree_to_inorder(merged) == [1, 2, 3, 4, 5, 6], f"Got {tree_to_inorder(merged)}"

    # Test 2: one empty tree
    root1 = build_tree([1, None, 2])
    merged = sol.mergeBSTs(root1, None)
    assert tree_to_inorder(merged) == [1, 2]

    # Test 3: both empty
    assert sol.mergeBSTs(None, None) is None

    # Test 4: overlapping values
    root1 = build_tree([2, 1, 3])
    root2 = build_tree([2, 1, 3])
    merged = sol.mergeBSTs(root1, root2)
    assert tree_to_inorder(merged) == [1, 1, 2, 2, 3, 3]

    print("All tests passed!")
