from typing import List

class Solution:
    # Tarjan's bridge finding: edge (u,v) is bridge if low[v] > disc[u]
    # low[v] = min discovery time reachable from subtree of v (excluding parent edge)
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n   # discovery time
        low = [0] * n     # lowest disc reachable
        timer = [0]
        bridges = []

        def dfs(node, parent):
            disc[node] = low[node] = timer[0]
            timer[0] += 1
            for neighbor in graph[node]:
                if disc[neighbor] == -1:  # unvisited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])  # bridge found
                elif neighbor != parent:  # back edge (not to direct parent)
                    low[node] = min(low[node], disc[neighbor])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return bridges
