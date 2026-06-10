from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Inorder + Two Pointers — O(n+m) time, O(n+m) space
def twoSumBSTs_inorder(root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    l1, l2 = inorder(root1), inorder(root2)
    i, j = 0, len(l2) - 1

    while i < len(l1) and j >= 0:
        s = l1[i] + l2[j]
        if s == target:
            return True
        elif s < target:
            i += 1
        else:
            j -= 1

    return False


# Approach 2: DFS + BST Search — O(n·log m) time, O(h) space
def twoSumBSTs_bst(root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
    def search(node, val):
        if not node:
            return False
        if node.val == val:
            return True
        return search(node.left, val) if val < node.val else search(node.right, val)

    def dfs(node):
        if not node:
            return False
        return search(root2, target - node.val) or dfs(node.left) or dfs(node.right)

    return dfs(root1)
