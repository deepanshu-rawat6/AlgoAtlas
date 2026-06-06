from __future__ import annotations
from typing import Optional, List
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
    # --- Approach 1: Recursive with upper bound O(n) ---
    def bstFromPreorder_recursive(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0

        def build(upper: float) -> Optional[TreeNode]:
            # If all elements consumed or current value exceeds upper bound, stop
            if self.idx == len(preorder) or preorder[self.idx] > upper:
                return None
            val = preorder[self.idx]
            self.idx += 1
            node = TreeNode(val)
            node.left = build(val)        # left subtree: values < val
            node.right = build(upper)     # right subtree: values < upper
            return node

        return build(float('inf'))

    # --- Approach 2: Stack-based O(n) ---
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node      # smaller than top → left child
            else:
                # pop until we find the parent (last node smaller than val)
                parent = stack[-1]
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node        # attach as right child
            stack.append(node)

        return root


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard case
    preorder = [8, 5, 1, 7, 10, 12]
    expected_inorder = sorted(preorder)

    t1 = sol.bstFromPreorder(preorder)
    assert tree_to_inorder(t1) == expected_inorder, f"Got {tree_to_inorder(t1)}"

    t2 = sol.bstFromPreorder_recursive(preorder)
    assert tree_to_inorder(t2) == expected_inorder

    # Test 2: single element
    t = sol.bstFromPreorder([1])
    assert t.val == 1 and t.left is None and t.right is None

    # Test 3: sorted ascending (right-skewed)
    preorder = [1, 2, 3, 4]
    t = sol.bstFromPreorder(preorder)
    assert tree_to_inorder(t) == [1, 2, 3, 4]

    # Test 4: sorted descending (left-skewed)
    preorder = [4, 3, 2, 1]
    t = sol.bstFromPreorder(preorder)
    assert tree_to_inorder(t) == [1, 2, 3, 4]

    print("All tests passed!")
