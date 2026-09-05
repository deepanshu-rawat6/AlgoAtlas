// LC 200: Number of Islands
// DFS from each unvisited '1', mark visited by sinking to '0'. Count starts.
// Time: O(m*n), Space: O(m*n) recursion stack
import java.util.*;

public class Solution {
    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r+1, c); dfs(grid, r-1, c);
        dfs(grid, r, c+1); dfs(grid, r, c-1);
    }

    public int numIslands(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++)
                if (grid[r][c] == '1') { dfs(grid, r, c); count++; }
        return count;
    }

    static char[][] g(String... rows) {
        char[][] grid = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) grid[i] = rows[i].toCharArray();
        return grid;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.numIslands(g("11110","11010","11000","00000")) == 1 : "Test 1 failed";
        assert s.numIslands(g("11000","11000","00100","00011")) == 3 : "Test 2 failed";
        assert s.numIslands(g("0")) == 0 : "Test 3 failed";
        assert s.numIslands(g("1")) == 1 : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
