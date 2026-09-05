// LC 200: Number of Islands
// DFS from each unvisited '1', mark visited by sinking to '0'. Count starts.
// Time: O(m*n), Space: O(m*n) recursion stack
#include <vector>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
    void dfs(vector<vector<char>>& grid, int r, int c) {
        if (r < 0 || r >= (int)grid.size() || c < 0 || c >= (int)grid[0].size() || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r+1, c); dfs(grid, r-1, c);
        dfs(grid, r, c+1); dfs(grid, r, c-1);
    }
public:
    // Brute and optimal are effectively the same DFS/BFS pattern at O(m*n)
    int numIslands(vector<vector<char>> grid) {
        int count = 0;
        for (int r = 0; r < (int)grid.size(); r++)
            for (int c = 0; c < (int)grid[0].size(); c++)
                if (grid[r][c] == '1') { dfs(grid, r, c); count++; }
        return count;
    }
};

int main() {
    Solution s;
    assert(s.numIslands({{'1','1','1','1','0'},
                          {'1','1','0','1','0'},
                          {'1','1','0','0','0'},
                          {'0','0','0','0','0'}}) == 1);
    assert(s.numIslands({{'1','1','0','0','0'},
                          {'1','1','0','0','0'},
                          {'0','0','1','0','0'},
                          {'0','0','0','1','1'}}) == 3);
    assert(s.numIslands({{'0'}}) == 0);
    assert(s.numIslands({{'1'}}) == 1);
    cout << "All tests passed." << endl;
    return 0;
}
