from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list) -> Optional[TreeNode]:
    """Build tree from level-order list; None represents missing nodes."""
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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Serialize tree to level-order list for easy comparison."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # strip trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    # --- Approach 1: Recursive O(h) ---
    def searchBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None                      # val not found
        if root.val == val:
            return root                      # found it
        if val < root.val:
            return self.searchBST_recursive(root.left, val)   # go left
        return self.searchBST_recursive(root.right, val)      # go right

    # --- Approach 2: Iterative O(h) ---
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root                  # found
            elif val < root.val:
                root = root.left             # move left
            else:
                root = root.right            # move right
        return None                          # not found


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: val exists in tree
    root = build_tree([4, 2, 7, 1, 3])
    result = sol.searchBST(root, 2)
    assert tree_to_list(result) == [2, 1, 3], f"Expected [2,1,3], got {tree_to_list(result)}"

    # Test 2: val not in tree
    result = sol.searchBST(root, 5)
    assert result is None

    # Test 3: search root value
    result = sol.searchBST(root, 4)
    assert result is not None and result.val == 4

    # Test 4: single node
    single = build_tree([1])
    assert sol.searchBST(single, 1).val == 1
    assert sol.searchBST(single, 2) is None

    # Test 5: empty tree
    assert sol.searchBST(None, 1) is None

    # Verify recursive gives same results
    root = build_tree([4, 2, 7, 1, 3])
    assert tree_to_list(sol.searchBST_recursive(root, 2)) == [2, 1, 3]
    assert sol.searchBST_recursive(root, 5) is None

    print("All tests passed!")
