# LC 547 - Number of Provinces

Count connected components in an adjacency matrix where `isConnected[i][j] = 1` means city i and j are directly connected.

## Approaches

**Approach 1: DFS — O(n²)**
Iterate over all nodes. For each unvisited node, run DFS to mark all reachable nodes as visited. Each DFS call = one new province.

**Approach 2: Union-Find — O(n²)**
Iterate over upper triangle of matrix. Union connected cities. Count distinct roots at the end.

## Key Insight
This is a standard connected components problem. The adjacency matrix is symmetric, so only scan `j > i` in Union-Find to avoid redundant unions.

## Edge Cases
- Single city: answer is 1
- All cities connected: answer is 1
- No connections (identity matrix): answer is n

## Example
```
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Cities 0 and 1 are connected → province 1
City 2 is isolated → province 2
Output: 2
```
