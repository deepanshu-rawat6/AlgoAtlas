from __future__ import annotations
from typing import Optional, Tuple
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
    # --- Approach 1: Check each subtree O(n^2) ---
    def _is_bst(self, node, lo=float('-inf'), hi=float('inf')) -> int:
        """Returns size of BST rooted at node, or -1 if not a valid BST."""
        if not node:
            return 0
        if not (lo < node.val < hi):
            return -1
        left = self._is_bst(node.left, lo, node.val)
        if left == -1:
            return -1
        right = self._is_bst(node.right, node.val, hi)
        if right == -1:
            return -1
        return left + right + 1

    def largestBSTSubtree_naive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        size = self._is_bst(root)
        if size != -1:
            return size                      # whole subtree is BST
        return max(self.largestBSTSubtree_naive(root.left),
                   self.largestBSTSubtree_naive(root.right))

    # --- Approach 2: Bottom-up post-order O(n) ---
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_size = 0

        def post_order(node) -> Tuple[bool, int, float, float]:
            """Returns (is_bst, size, min_val, max_val)."""
            if not node:
                return True, 0, float('inf'), float('-inf')

            l_bst, l_size, l_min, l_max = post_order(node.left)
            r_bst, r_size, r_min, r_max = post_order(node.right)

            # Current node forms a valid BST if both children are BSTs
            # and current value is greater than left max and less than right min
            if l_bst and r_bst and l_max < node.val < r_min:
                size = l_size + r_size + 1
                self.max_size = max(self.max_size, size)
                return True, size, min(l_min, node.val), max(r_max, node.val)

            # Not a valid BST; propagate invalid signal upward
            return False, 0, 0, 0

        post_order(root)
        return self.max_size


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: [10,5,15,1,8,null,7] -> largest BST is [5,1,8] size=3
    root = build_tree([10, 5, 15, 1, 8, None, 7])
    assert sol.largestBSTSubtree(root) == 3, f"Got {sol.largestBSTSubtree(root)}"
    assert sol.largestBSTSubtree_naive(root) == 3

    # Test 2: entire tree is a BST
    root = build_tree([4, 2, 6, 1, 3, 5, 7])
    assert sol.largestBSTSubtree(root) == 7

    # Test 3: single node
    root = build_tree([1])
    assert sol.largestBSTSubtree(root) == 1

    # Test 4: empty tree
    assert sol.largestBSTSubtree(None) == 0

    # Test 5: [3,2,4,1,null,null,5] -> entire tree is BST size=5
    root = build_tree([3, 2, 4, 1, None, None, 5])
    assert sol.largestBSTSubtree(root) == 5

    print("All tests passed!")
