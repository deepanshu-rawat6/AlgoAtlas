import java.util.*;

public class Solution {
    // Counting: each land cell adds 4 sides, subtract 2 per shared edge
    public int islandPerimeterCounting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, perimeter = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1) {
                    perimeter += 4;
                    if (r > 0 && grid[r-1][c] == 1) perimeter -= 2;
                    if (c > 0 && grid[r][c-1] == 1) perimeter -= 2;
                }
        return perimeter;
    }

    // DFS: count boundary sides (out-of-bounds or water neighbor = 1 side)
    public int islandPerimeter(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1) return dfs(grid, visited, r, c, rows, cols);
        return 0;
    }

    private int dfs(int[][] grid, boolean[][] visited, int r, int c, int rows, int cols) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0) return 1;
        if (visited[r][c]) return 0;
        visited[r][c] = true;
        return dfs(grid, visited, r+1, c, rows, cols)
             + dfs(grid, visited, r-1, c, rows, cols)
             + dfs(grid, visited, r, c+1, rows, cols)
             + dfs(grid, visited, r, c-1, rows, cols);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.islandPerimeter(new int[][]{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}}) == 16 : "test 1";
        assert s.islandPerimeter(new int[][]{{1}}) == 4 : "test 2";
        assert s.islandPerimeter(new int[][]{{1,0}}) == 4 : "test 3";
        assert s.islandPerimeterCounting(new int[][]{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}}) == 16 : "test 4";
        System.out.println("All tests passed.");
    }
}
