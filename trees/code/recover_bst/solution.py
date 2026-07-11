"""
# LC 99: Recover Binary Search Tree

Two nodes of a BST are swapped by mistake. Recover the tree without changing its
structure (fix the values in-place).

## Examples
```text
Input:  root = [1, 3, null, null, 2]
Output: [3, 1, null, null, 2]

Input:  root = [3, 1, 4, null, null, 2]
Output: [2, 1, 4, null, null, 3]
```

## Constraints
- The number of nodes in the tree is in the range [2, 1000].
- -2^31 <= Node.val <= 2^31 - 1
"""
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
    # --- Approach 1: Inorder to array, find swapped pair O(n) space ---
    def recoverTree_naive(self, root: Optional[TreeNode]) -> None:
        nodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
        inorder(root)

        first = second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                second = nodes[i + 1]        # always update second
                if first is None:
                    first = nodes[i]         # only set first once

        if first and second:
            first.val, second.val = second.val, first.val

    # --- Approach 2: Morris traversal O(1) space ---
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None

        curr = root
        while curr:
            if not curr.left:
                # visit curr
                if prev and prev.val > curr.val:
                    second = curr
                    if first is None:
                        first = prev
                prev = curr
                curr = curr.right
            else:
                # find inorder predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr        # create threaded link
                    curr = curr.left
                else:
                    pred.right = None        # remove threaded link
                    # visit curr
                    if prev and prev.val > curr.val:
                        second = curr
                        if first is None:
                            first = prev
                    prev = curr
                    curr = curr.right

        if first and second:
            first.val, second.val = second.val, first.val


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: adjacent swap [1,3,null,null,2] -> [3,1,null,null,2]
    root = build_tree([1, 3, None, None, 2])
    sol.recoverTree(root)
    assert tree_to_inorder(root) == [1, 2, 3], f"Got {tree_to_inorder(root)}"

    # Test 2: non-adjacent swap [3,1,4,null,null,2] -> [2,1,4,null,null,3]
    root = build_tree([3, 1, 4, None, None, 2])
    sol.recoverTree(root)
    assert tree_to_inorder(root) == [1, 2, 3, 4], f"Got {tree_to_inorder(root)}"

    # Test 3: naive approach
    root = build_tree([1, 3, None, None, 2])
    sol.recoverTree_naive(root)
    assert tree_to_inorder(root) == [1, 2, 3]

    print("All tests passed!")
