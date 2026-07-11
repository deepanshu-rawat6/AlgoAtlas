"""
# LC 427: Construct Quad Tree

Given an n x n binary grid (n is a power of 2), construct a Quad-Tree. Each node is a
leaf if its region is uniform (all 0s or all 1s); otherwise split into four equal
quadrants and recurse.

## Examples
```text
Input:  grid = [[0, 1], [1, 0]]
Output: [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]

Input:  grid = [[1, 1], [1, 1]]
Output: [[1, 1]]
```

## Constraints
- n == grid.length == grid[i].length
- n == 2^x where 0 <= x <= 6
- grid[i][j] is 0 or 1.
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


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    ## 427. Construct Quad Tree

    Given a `n * n` matrix `grid` of `0`s and `1`s, return the corresponding Quad-Tree.

    A Quad-Tree is a tree data structure in which each internal node has exactly four children.
    Each node has two attributes:
    - `val`: `True` if the node represents a grid of all `1`s, or `False` if all `0`s. For
      non-leaf nodes, the value can be either `True` or `False`.
    - `isLeaf`: `True` if the node is a leaf node, or `False` if it has four children.

    We can construct a Quad-Tree from a 2D area using the following steps:
    1. If the current grid has the same value (all `1`s or all `0`s), set `isLeaf` to `True`
       and set `val` to the value of the grid and set the four children to `None`.
    2. If the current grid has different values, set `isLeaf` to `False` and set `val` to any
       value and divide the current grid into four sub-grids.
    3. Recurse for each of the children with the proper sub-grid.

    ### Examples

    ```text
    Example 1:
    Input:  grid = [[0,1],[1,0]]
    Output: [[False,False],[True,1],[True,1],[True,1],[True,0]]
    (Serialized quad-tree format)

    Example 2:
    Input:  grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],
                    [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    Output: [[False,False],[True,1],[True,1],[False,False],[True,1],[True,1],[True,0],[True,0],[True,0]]
    ```

    ### Constraints
    - `n == grid.length == grid[i].length`
    - `n == 2^x` where `0 <= x <= 6`
    """

    def construct(self, grid: List[List[int]]) -> 'Node':
        # Check if all values in region are the same — if so, create leaf node
        # Otherwise split into 4 quadrants and recurse on each
        # Time: O(n^2 log n), Space: O(log n) — recursively split grid into four quadrants
        def build(r: int, c: int, size: int) -> Node:
            val = grid[r][c]
            all_same = all(grid[r + dr][c + dc] == val
                           for dr in range(size) for dc in range(size))
            if all_same:
                return Node(bool(val), True)
            half = size // 2
            return Node(
                True, False,
                build(r, c, half),
                build(r, c + half, half),
                build(r + half, c, half),
                build(r + half, c + half, half),
            )

        return build(0, 0, len(grid))


if __name__ == '__main__':
    sol = Solution()

    result = sol.construct([[0, 1], [1, 0]])
    assert result.isLeaf == False
    assert result.topLeft.isLeaf == True and result.topLeft.val == False
    assert result.topRight.isLeaf == True and result.topRight.val == True

    result2 = sol.construct([[1]])
    assert result2.isLeaf == True and result2.val == True

    result3 = sol.construct([[0]])
    assert result3.isLeaf == True and result3.val == False

    print("All tests passed.")
