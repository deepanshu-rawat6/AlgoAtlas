"""
# LC 1214: Two Sum BSTs

Given the roots of two BSTs and an integer `target`, return true if there exists a node
in the first tree and a node in the second tree such that their values sum to `target`.

## Examples
```text
Input:  root1 = [2, 1, 4], root2 = [1, 0, 3], target = 5
Output: true

Input:  root1 = [0, -10, 10], root2 = [5, 1, 7, 0, 2], target = 18
Output: false
```

## Constraints
- The number of nodes in each tree is in the range [1, 5000].
- -10^9 <= Node.val, target <= 10^9
"""
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


if __name__ == "__main__":
    # Example 1: root1 = [2, 1, 4], root2 = [1, 0, 3], target = 5 -> True (2 + 3)
    t1 = TreeNode(2, TreeNode(1), TreeNode(4))
    t2 = TreeNode(1, TreeNode(0), TreeNode(3))
    assert twoSumBSTs_inorder(t1, t2, 5) is True
    assert twoSumBSTs_bst(t1, t2, 5) is True

    # Example 2: root1 = [0, -10, 10], root2 = [5, 1, 7, 0, 2], target = 18 -> False
    t3 = TreeNode(0, TreeNode(-10), TreeNode(10))
    t4 = TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7))
    assert twoSumBSTs_inorder(t3, t4, 18) is False
    assert twoSumBSTs_bst(t3, t4, 18) is False

    # Single-node trees: 3 + 4 == 7
    assert twoSumBSTs_inorder(TreeNode(3), TreeNode(4), 7) is True
    assert twoSumBSTs_bst(TreeNode(3), TreeNode(4), 7) is True
    assert twoSumBSTs_inorder(TreeNode(3), TreeNode(4), 8) is False
    assert twoSumBSTs_bst(TreeNode(3), TreeNode(4), 8) is False

    print("All tests passed.")
