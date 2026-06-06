from typing import List
from collections import deque


class Solution:
    """
    ## 210. Course Schedule II

    There are `numCourses` courses labeled `0` to `numCourses - 1`. You are given
    an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates you must
    take course `bi` first if you want to take course `ai`.

    Return the ordering of courses you should take to finish all courses. If there
    are many valid answers, return any of them. If it is impossible to finish all
    courses, return an empty array.

    ### Examples

    ```text
    Input:  numCourses = 2, prerequisites = [[1,0]]
    Output: [0, 1]

    Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]

    Input:  numCourses = 1, prerequisites = []
    Output: [0]
    ```

    ### Constraints

    - `1 <= numCourses <= 2000`
    - `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
    - `prerequisites[i].length == 2`
    - `0 <= ai, bi < numCourses`
    - `ai != bi`
    - All pairs `[ai, bi]` are distinct.
    """

    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(V+E) time, O(V+E) space
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # 0=unvisited, 1=visiting, 2=visited
        state = [0] * numCourses
        order = []

        def dfs(node: int) -> bool:
            if state[node] == 1:
                return False  # cycle
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort via DFS post-order; cycle detection aborts
        # Reverse post-order gives valid course order
        # O(V+E) time, O(V+E) space — Kahn's BFS
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return order if len(order) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    result = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result[0] == 0 and result[-1] == 3
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    assert s.findOrder(1, []) == [0]

    assert s.findOrder_dfs(2, [[1, 0]]) == [0, 1]
    assert s.findOrder_dfs(2, [[1, 0], [0, 1]]) == []
    print("All tests passed.")
