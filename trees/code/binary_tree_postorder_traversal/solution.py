from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    """
    ## 145. Binary Tree Postorder Traversal

    Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

    ### Examples

    ```text
    Input:  root = [1, null, 2, 3]
    Output: [3, 2, 1]

    Input:  root = []
    Output: []

    Input:  root = [1]
    Output: [1]
    ```

    ### Constraints

    - The number of nodes in the tree is in the range `[0, 100]`.
    - `-100 <= Node.val <= 100`
    """

    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), Space: O(n)
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive post-order: left subtree, right subtree, root
        # Time: O(n), Space: O(n)
        if not root:
            return []
        stack1, stack2 = [root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return stack2[::-1]


if __name__ == '__main__':
    s = Solution()

    assert s.postorderTraversal(build_tree([1, None, 2, 3])) == [3, 2, 1]
    assert s.postorderTraversal_recursive(build_tree([1, None, 2, 3])) == [3, 2, 1]

    assert s.postorderTraversal(None) == []
    assert s.postorderTraversal(build_tree([1])) == [1]

    print("All tests passed.")
