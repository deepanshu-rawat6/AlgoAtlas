from typing import List
from collections import defaultdict, deque


class Solution:
    """
    ## 399. Evaluate Division

    You are given an array of variable pairs `equations` and an array of real numbers
    `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation
    `Ai / Bi = values[i]`.

    Given some `queries`, where `queries[j] = [Cj, Dj]`, return the answers to all
    queries. If the answer does not exist, return `-1.0`.

    ### Examples

    ```text
    Input:
      equations = [["a","b"],["b","c"]], values = [2.0,3.0]
      queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.0, 0.5, -1.0, 1.0, -1.0]

    Input:
      equations = [["a","b"],["b","c"]], values = [2.0,3.0]
      queries = [["a","c"]]
    Output: [6.0]
    ```

    ### Constraints

    - `1 <= equations.length <= 20`
    - `equations[i].length == 2`
    - `1 <= Ai.length, Bi.length <= 5`
    - `values[i] > 0.0`
    - `1 <= queries.length <= 20`
    """

    def calcEquation_bfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # O(Q*(V+E)) time, O(V+E) space
        graph: dict = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = set()
            queue = deque([(src, 1.0)])
            visited.add(src)
            while queue:
                node, product = queue.popleft()
                if node == dst:
                    return product
                for nei, weight in graph[node].items():
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, product * weight))
            return -1.0

        return [bfs(c, d) for c, d in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build weighted graph: a/b=k means edge a->b with weight k, b->a with 1/k
        # BFS/DFS for each query to find the product of weights along the path
        # O(E*alpha(V) + Q) time, O(V) space — Union-Find with weights
        parent: dict = {}
        weight: dict = {}  # weight[x] = x / find(x)

        def find(x: str):
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            if parent[x] != x:
                root, w = find(parent[x])
                parent[x] = root
                weight[x] *= w
            return parent[x], weight[x]

        def union(x: str, y: str, val: float) -> None:
            rx, wx = find(x)
            ry, wy = find(y)
            if rx != ry:
                parent[rx] = ry
                weight[rx] = val * wy / wx

        for (a, b), val in zip(equations, values):
            union(a, b, val)

        results = []
        for c, d in queries:
            if c not in parent or d not in parent:
                results.append(-1.0)
            else:
                rc, wc = find(c)
                rd, wd = find(d)
                results.append(wc / wd if rc == rd else -1.0)
        return results


if __name__ == '__main__':
    s = Solution()
    eq = [["a", "b"], ["b", "c"]]
    vals = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]

    res = s.calcEquation_bfs(eq, vals, queries)
    assert res == expected, res

    res2 = s.calcEquation(eq, vals, [["a", "c"]])
    assert abs(res2[0] - 6.0) < 1e-9
    print("All tests passed.")
