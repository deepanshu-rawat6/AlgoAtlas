from typing import List
from collections import deque


class Solution:
    """
    ## 1462. Course Schedule IV

    There are `numCourses` courses labeled `0` to `numCourses - 1`. You are given
    an array `prerequisites` where `prerequisites[i] = [ai, bi]` means course `ai`
    must be taken before course `bi`.

    Given a list of `queries` where `queries[j] = [uj, vj]`, answer whether course
    `uj` is a prerequisite of course `vj` (directly or indirectly).

    ### Examples

    ```text
    Input:  numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
    Output: [false, true]

    Input:  numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
    Output: [false, false]

    Input:  numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
    Output: [true, true]
    ```

    ### Constraints

    - `2 <= numCourses <= 100`
    - `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
    - `prerequisites[i].length == 2`
    - `0 <= ai, bi < numCourses`
    - `ai != bi`
    - All prerequisite pairs are distinct.
    - `1 <= queries.length <= 10^4`
    """

    def checkIfPrerequisite_bfs(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # O(V*(V+E)) time, O(V^2) space
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        def can_reach(src: int, dst: int) -> bool:
            visited = set()
            queue = deque([src])
            while queue:
                node = queue.popleft()
                if node == dst:
                    return True
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return False

        return [can_reach(u, v) for u, v in queries]

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build reachability matrix via DFS/BFS or Floyd-Warshall
        # reachable[u][v] = True if u can reach v through prerequisites
        # O(V^3) time, O(V^2) space — Floyd-Warshall transitive closure
        reach = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reach[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True
        return [reach[u][v] for u, v in queries]


if __name__ == '__main__':
    s = Solution()
    assert s.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
    assert s.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False]
    assert s.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]

    assert s.checkIfPrerequisite_bfs(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
    assert s.checkIfPrerequisite_bfs(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]
    print("All tests passed.")
