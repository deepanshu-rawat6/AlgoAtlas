"""
# LC 947: Most Stones Removed with Same Row or Column

A stone can be removed if it shares a row or column with another remaining
stone. Return the maximum number of stones that can be removed.

## Examples
```text
Input: stones=[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
# All 6 stones form one connected component → remove 6 - 1 = 5.
```

## Constraints
- Union-Find grouping stones that share a row or column — O(n)
- Offset column indices to keep row and column keys in a shared namespace
- Answer = total_stones - number_of_components
"""
from typing import List

class Solution:
    # Union-Find: group stones sharing row or col. Each group can be reduced to 1 stone.
    # Answer = total_stones - number_of_groups
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for r, c in stones:
            # offset col by 10001 to avoid collision with row indices
            union(r, c + 10001)

        # count distinct components among stones
        components = len({find(r) for r, c in stones})
        return len(stones) - components


if __name__ == "__main__":
    sol = Solution()

    # Example from README: one big component → remove all but one
    assert sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5

    # LC example 2: two components → remove 5 - 2 = 3
    assert sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3

    # Single stone → nothing to remove
    assert sol.removeStones([[0, 0]]) == 0

    print("All tests passed.")
