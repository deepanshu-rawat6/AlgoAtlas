"""
# LC 297: Serialize and Deserialize Binary Tree

Design an algorithm to convert a binary tree to a string and reconstruct the original
tree from that string.

## Examples
```text
Input:  root = [1, 2, 3, null, null, 4, 5]
Output: [1, 2, 3, null, null, 4, 5]

Input:  root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""
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


def tree_to_list(root):
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
    while result and result[-1] is None:
        result.pop()
    return result


class Codec:
    """
    ## 297. Serialize and Deserialize Binary Tree

    Serialization is the process of converting a data structure or object into a sequence of
    bits so that it can be stored in a file or memory buffer, or transmitted across a network
    connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
    how your serialization/deserialization algorithm should work. You just need to ensure that
    a binary tree can be serialized to a string and this string can be deserialized to the
    original tree structure.

    ---

    ### Examples

    ```text
    Example 1:
        Input:  root = [1, 2, 3, null, null, 4, 5]
        Output: [1, 2, 3, null, null, 4, 5]
        Explanation: Serialize to a string, then deserialize back to the same tree.

    Example 2:
        Input:  root = []
        Output: []
    ```

    ---

    ### Constraints

    - The number of nodes in the tree is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000
    """

    # Approach 1: BFS level-order — O(n) time, O(n) space
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS level-order; encode None as 'N' to preserve structure
        if not root:
            return ''
        result, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        return ','.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # BFS reconstruction: split tokens, assign left/right children from queue
        if not data:
            return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


class CodecDFS:
    # Approach 2: DFS preorder — O(n) time, O(n) space
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS level-order; encode None as 'N' to preserve structure
        parts = []

        def dfs(node):
            if not node:
                parts.append('null')
                return
            parts.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(parts)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # BFS reconstruction: split tokens, assign left/right children from queue
        vals = iter(data.split(','))

        def dfs():
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


if __name__ == '__main__':
    codec = Codec()
    codec_dfs = CodecDFS()

    root1 = build_tree([1, 2, 3, None, None, 4, 5])
    serialized = codec.serialize(root1)
    assert tree_to_list(codec.deserialize(serialized)) == [1, 2, 3, None, None, 4, 5]

    serialized_dfs = codec_dfs.serialize(build_tree([1, 2, 3, None, None, 4, 5]))
    assert tree_to_list(codec_dfs.deserialize(serialized_dfs)) == [1, 2, 3, None, None, 4, 5]

    assert codec.serialize(None) == ''
    assert codec.deserialize('') is None

    print("All tests passed.")
