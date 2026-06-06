from typing import List
from collections import defaultdict, deque


class Solution:
    """
    ## 2392. Build a Matrix With Conditions

    You are given a positive integer `k`. You are also given:
    - a 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above_i, below_i]`,
      meaning row of `above_i` must appear **above** row of `below_i`.
    - a 2D integer array `colConditions` of size `m` where `colConditions[i] = [left_i, right_i]`,
      meaning column of `left_i` must appear to the **left** of column of `right_i`.

    The matrix contains each of the integers from `1` to `k` exactly once. Return **any** matrix
    of size `k x k` satisfying the conditions. If no answer exists, return an empty matrix.

    ---

    ### Examples

    ```text
    Input:  k=3, rowConditions=[[1,2],[3,2]], colConditions=[[2,1],[3,2]]
    Output: [[3,0,0],[0,0,1],[0,2,0]]

    Input:  k=3, rowConditions=[[1,2],[2,3],[3,1]], colConditions=[[1,2]]
    Output: []
    Explanation: Row conditions form a cycle.
    ```

    ---

    ### Constraints

    - `2 <= k <= 400`
    - `1 <= rowConditions.length, colConditions.length <= 10^4`
    - `rowConditions[i].length == colConditions[i].length == 2`
    - `1 <= above_i, below_i, left_i, right_i <= k`
    - `above_i != below_i`
    - `left_i != right_i`
    """

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological sort row conditions to get row order, col conditions for col order
        # Place each number at (row_pos[num], col_pos[num]) in the k×k matrix
        # Return empty if either topological sort detects a cycle
        # O(k + conditions) — Kahn's BFS topological sort for rows and columns independently
        def topo_sort(conditions: List[List[int]]) -> List[int]:
            adj = defaultdict(list)
            in_deg = defaultdict(int)
            nodes = set(range(1, k + 1))
            for u, v in conditions:
                adj[u].append(v)
                in_deg[v] += 1
                nodes.add(u)
                nodes.add(v)
            q = deque([node for node in range(1, k + 1) if in_deg[node] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nb in adj[node]:
                    in_deg[nb] -= 1
                    if in_deg[nb] == 0:
                        q.append(nb)
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []

        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: i for i, val in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for val in range(1, k + 1):
            matrix[row_pos[val]][col_pos[val]] = val
        return matrix


if __name__ == '__main__':
    s = Solution()

    res = s.buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]])
    assert len(res) == 3 and len(res[0]) == 3
    # Verify each number 1-3 appears exactly once
    flat = [x for row in res for x in row]
    assert sorted(x for x in flat if x != 0) == [1, 2, 3]

    # Cycle in row conditions -> empty
    assert s.buildMatrix(3, [[1, 2], [2, 3], [3, 1]], [[1, 2]]) == []

    print("All tests passed.")
