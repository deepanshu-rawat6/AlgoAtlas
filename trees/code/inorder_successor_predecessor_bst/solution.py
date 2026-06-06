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
    # --- Approach 1: Inorder traversal O(n) ---
    def _inorder(self, root):
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node)
                dfs(node.right)
        dfs(root)
        return result

    def inorderSuccessor_naive(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        nodes = self._inorder(root)
        for i, node in enumerate(nodes):
            if node.val == p.val and i + 1 < len(nodes):
                return nodes[i + 1]
        return None

    def inorderPredecessor_naive(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        nodes = self._inorder(root)
        for i, node in enumerate(nodes):
            if node.val == p.val and i - 1 >= 0:
                return nodes[i - 1]
        return None

    # --- Approach 2: BST property O(h) ---
    def inorderSuccessor(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val < root.val:
                successor = root             # root could be successor; go left for closer one
                root = root.left
            else:
                root = root.right            # p is >= root; successor must be in right subtree
        return successor

    def inorderPredecessor(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        predecessor = None
        while root:
            if p.val > root.val:
                predecessor = root           # root could be predecessor; go right for closer one
                root = root.right
            else:
                root = root.left             # p is <= root; predecessor must be in left subtree
        return predecessor


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # BST: [5,3,6,2,4,null,null,1]
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])

    p3 = TreeNode(3)
    succ = sol.inorderSuccessor(root, p3)
    pred = sol.inorderPredecessor(root, p3)
    assert succ is not None and succ.val == 4,  f"Expected successor=4, got {succ}"
    assert pred is not None and pred.val == 2,  f"Expected predecessor=2, got {pred}"

    # Test: successor of max node
    p6 = TreeNode(6)
    assert sol.inorderSuccessor(root, p6) is None

    # Test: predecessor of min node
    p1 = TreeNode(1)
    assert sol.inorderPredecessor(root, p1) is None

    # Test: root node
    p5 = TreeNode(5)
    assert sol.inorderSuccessor(root, p5).val == 6
    assert sol.inorderPredecessor(root, p5).val == 4

    # Verify naive approach matches
    assert sol.inorderSuccessor_naive(root, p3).val == 4
    assert sol.inorderPredecessor_naive(root, p3).val == 2

    print("All tests passed!")
