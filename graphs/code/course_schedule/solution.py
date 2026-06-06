"""
# 207. Course Schedule

## Problem
There are a total of `numCourses` courses you have to take, labeled from `0` to
`numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]`
indicates that you must take course `b` first if you want to take course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples
```text
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0 first, then course 1.
```

```text
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Courses 0 and 1 are mutually dependent — impossible.
```

```text
Input:  numCourses = 5, prerequisites = [[1,0],[2,1],[3,2],[4,3]]
Output: true
```

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a, b < numCourses`
- All the pairs `prerequisites[i]` are unique
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V+E) time, O(V+E) space — DFS cycle detection with 3-color marking
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        # 0=unvisited, 1=visiting, 2=done
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False   # back edge → cycle
            if state[node] == 2:
                return True
            state[node] = 1
            for nb in graph[node]:
                if not dfs(nb):
                    return False
            state[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list; detect cycle using DFS with 3-state coloring
        # States: 0=unvisited, 1=in-progress (cycle if revisited), 2=done
        # O(V+E) time, O(V+E) space — BFS topological sort (Kahn's algorithm)
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        processed = 0
        while q:
            node = q.popleft()
            processed += 1
            for nb in graph[node]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        return processed == numCourses


if __name__ == '__main__':
    s = Solution()
    assert s.canFinish_dfs(2, [[1,0]]) == True
    assert s.canFinish_dfs(2, [[1,0],[0,1]]) == False
    assert s.canFinish_dfs(5, [[1,0],[2,1],[3,2],[4,3]]) == True
    assert s.canFinish(2, [[1,0]]) == True
    assert s.canFinish(2, [[1,0],[0,1]]) == False
    assert s.canFinish(1, []) == True
    print("All tests passed.")
