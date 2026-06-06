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
    def floor(self, root: Optional[TreeNode], key: int) -> int:
        """Largest value <= key. Returns -1 if no floor exists."""
        floor_val = -1
        while root:
            if root.val == key:
                return root.val              # exact match is the floor
            elif root.val < key:
                floor_val = root.val         # current is a candidate; go right for closer value
                root = root.right
            else:
                root = root.left             # current too large; go left
        return floor_val

    def ceil(self, root: Optional[TreeNode], key: int) -> int:
        """Smallest value >= key. Returns -1 if no ceil exists."""
        ceil_val = -1
        while root:
            if root.val == key:
                return root.val              # exact match is the ceil
            elif root.val > key:
                ceil_val = root.val          # current is a candidate; go left for closer value
                root = root.left
            else:
                root = root.right            # current too small; go right
        return ceil_val


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # BST: [8,4,12,2,6,10,14]
    root = build_tree([8, 4, 12, 2, 6, 10, 14])

    # Test 1: key between two nodes
    assert sol.floor(root, 5) == 4,  f"Expected 4, got {sol.floor(root, 5)}"
    assert sol.ceil(root, 5) == 6,   f"Expected 6, got {sol.ceil(root, 5)}"

    # Test 2: key exactly in tree
    assert sol.floor(root, 6) == 6
    assert sol.ceil(root, 6) == 6

    # Test 3: key smaller than all nodes
    assert sol.floor(root, 1) == -1
    assert sol.ceil(root, 1) == 2

    # Test 4: key larger than all nodes
    assert sol.floor(root, 15) == 14
    assert sol.ceil(root, 15) == -1

    # Test 5: empty tree
    assert sol.floor(None, 5) == -1
    assert sol.ceil(None, 5) == -1

    print("All tests passed!")
