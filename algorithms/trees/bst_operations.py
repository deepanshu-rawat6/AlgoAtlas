"""
BST Operations
==============
Binary Search Tree: left subtree < node < right subtree.

Operations:
  - Search:      O(h) time — follow BST property
  - Insert:      O(h) time — find correct leaf position
  - Delete:      O(h) time — three cases (leaf, one child, two children)
  - Min/Max:     O(h) time — leftmost/rightmost node
  - Successor:   O(h) time — smallest node greater than given
  - Predecessor: O(h) time — largest node smaller than given
  - Validate:    O(n) time — check BST invariant with bounds

h = O(log n) balanced, O(n) worst case (skewed tree)
Space: O(h) for recursion stack
"""

from typing import Optional, Tuple
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Search ───────────────────────────────────────────────────────────────────

def search(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """Iterative BST search — avoids recursion overhead."""
    while root:
        if target == root.val:
            return root
        root = root.left if target < root.val else root.right
    return None


# ─── Insert ───────────────────────────────────────────────────────────────────

def insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """Returns root of modified tree. Duplicates are ignored."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


# ─── Delete ───────────────────────────────────────────────────────────────────

def delete(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Three cases:
      1. Node is a leaf → simply remove
      2. Node has one child → replace with that child
      3. Node has two children → replace value with inorder successor,
         then delete successor from right subtree
    """
    if not root:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # case 1 & 2
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # case 3: find inorder successor (min of right subtree)
        successor = _find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)
    return root


# ─── Min / Max ────────────────────────────────────────────────────────────────

def _find_min(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node


def _find_max(node: TreeNode) -> TreeNode:
    while node.right:
        node = node.right
    return node


def find_min(root: Optional[TreeNode]) -> Optional[int]:
    return _find_min(root).val if root else None


def find_max(root: Optional[TreeNode]) -> Optional[int]:
    return _find_max(root).val if root else None


# ─── Successor / Predecessor ──────────────────────────────────────────────────

def inorder_successor(root: Optional[TreeNode], target: int) -> Optional[int]:
    """
    If node has right subtree → min of right subtree.
    Otherwise → lowest ancestor for which node is in left subtree.
    """
    successor = None
    while root:
        if target < root.val:
            successor = root   # potential successor
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            if root.right:
                return _find_min(root.right).val
            break
    return successor.val if successor else None


def inorder_predecessor(root: Optional[TreeNode], target: int) -> Optional[int]:
    """Mirror of successor: if left subtree → max of left; else lowest right-ancestor."""
    predecessor = None
    while root:
        if target > root.val:
            predecessor = root
            root = root.right
        elif target < root.val:
            root = root.left
        else:
            if root.left:
                return _find_max(root.left).val
            break
    return predecessor.val if predecessor else None


# ─── Validate BST ─────────────────────────────────────────────────────────────

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Pass valid range [lo, hi] down the tree.
    Each node must satisfy lo < node.val < hi.
    """
    def validate(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

    return validate(root, float('-inf'), float('inf'))


# ─── Helpers ──────────────────────────────────────────────────────────────────

def inorder(root: Optional[TreeNode]):
    """Return sorted list — useful for verifying BST."""
    res = []
    def dfs(n):
        if n:
            dfs(n.left); res.append(n.val); dfs(n.right)
    dfs(root)
    return res


if __name__ == "__main__":
    root = None
    for v in [5, 3, 7, 1, 4, 6, 8]:
        root = insert(root, v)

    print("Inorder (sorted):", inorder(root))          # [1,3,4,5,6,7,8]
    print("Min:", find_min(root), "Max:", find_max(root))  # 1, 8

    print("Search 4:", search(root, 4).val)            # 4
    print("Search 9:", search(root, 9))                # None

    print("Successor of 4:", inorder_successor(root, 4))      # 5
    print("Predecessor of 4:", inorder_predecessor(root, 4))  # 3
    print("Successor of 8:", inorder_successor(root, 8))      # None

    root = delete(root, 5)   # delete node with two children
    print("After deleting 5:", inorder(root))          # [1,3,4,6,7,8]

    root = delete(root, 1)   # delete leaf
    print("After deleting 1:", inorder(root))          # [3,4,6,7,8]

    print("Is valid BST:", is_valid_bst(root))         # True

    # invalid BST
    bad = TreeNode(5, TreeNode(6), TreeNode(7))        # 6 > 5 on left — invalid
    print("Bad tree valid:", is_valid_bst(bad))        # False
