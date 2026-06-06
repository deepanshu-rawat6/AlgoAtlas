from typing import List
from collections import defaultdict


class Solution:
    """
    ## 332. Reconstruct Itinerary

    You are given a list of airline `tickets` represented by pairs of departure and arrival
    airports `[from, to]`. Reconstruct the itinerary in order. All of the tickets must be used
    once and only once.

    The itinerary must begin with `"JFK"`. If there are multiple valid itineraries, return the
    itinerary that has the **smallest lexical order** when read as a single string.

    You may assume all tickets form at least one valid itinerary. You must use all the tickets.

    ---

    ### Examples

    ```text
    Input:  tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]

    Input:  tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    ```

    ---

    ### Constraints

    - `1 <= tickets.length <= 300`
    - `tickets[i].length == 2`
    - `from_i` and `to_i` consist of uppercase English letters.
    - `from_i != to_i`
    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's algorithm for Eulerian path: DFS, add to result on backtrack
        # Sort destinations so lexicographically smallest path is found first
        # O(E^2) — DFS with backtracking on sorted adjacency lists
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        # Sort descending so we can pop from end (cheapest pop) in lex order
        for k in graph:
            graph[k].sort(reverse=True)

        result = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                dfs(graph[airport].pop())
            result.append(airport)

        dfs("JFK")
        return result[::-1]

    def findItinerary_hierholzer(self, tickets: List[List[str]]) -> List[str]:
        # O(E log E) — Hierholzer's iterative Eulerian path
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for k in graph:
            graph[k].sort(reverse=True)

        stack = ["JFK"]
        result = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            result.append(stack.pop())
        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert s.findItinerary(t1) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    t2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    assert s.findItinerary(t2) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    t3 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert s.findItinerary_hierholzer(t3) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    print("All tests passed.")
