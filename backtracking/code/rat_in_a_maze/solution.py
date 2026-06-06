"""
# Rat in a Maze

Given an n×n maze where 1 = open cell and 0 = blocked cell, find all paths
from (0,0) to (n-1,n-1). The rat can move Down, Left, Right, Up.
Return paths as strings of directions in lexicographical order.

## Examples

```text
Input:  maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
Output: ["DDRDRR","DRDDRR"]

Input:  maze = [[1,0],[1,1]]
Output: ["DR","RD"] — wait, (0,1) is blocked, so only "DR" isn't valid. Actually "DR" means down then right = (0,0)->(1,0)->(1,1) = valid
```

## Constraints
- 2 <= n <= 5
- maze[0][0] == 1 and maze[n-1][n-1] == 1
"""
from typing import List


class Solution:
    def findPaths(self, maze: List[List[int]]) -> List[str]:
        # Backtracking: try all 4 directions (D,L,R,U in sorted order for lex output)
        # Mark cell visited before exploring, unmark on backtrack
        # Base case: reached (n-1, n-1) → add path to result
        n = len(maze)
        result = []
        visited = [[False] * n for _ in range(n)]

        def backtrack(r, c, path):
            # Reached destination
            if r == n - 1 and c == n - 1:
                result.append(path)
                return

            # Try D, L, R, U (lexicographic order)
            for dr, dc, d in [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    backtrack(nr, nc, path + d)
                    visited[nr][nc] = False  # Backtrack

        if maze[0][0] == 1:
            visited[0][0] = True
            backtrack(0, 0, "")
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPaths([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))
    # Expected: ["DDRDRR", "DRDDRR"]
