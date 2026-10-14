import java.util.*;

public class Solution {
    // BFS flood fill — mark visited by setting to 0
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, best = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1) {
                    grid[r][c] = 0;
                    int area = 1;
                    Queue<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{r, c});
                    while (!q.isEmpty()) {
                        int[] cur = q.poll();
                        for (int[] d : dirs) {
                            int nr = cur[0]+d[0], nc = cur[1]+d[1];
                            if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]==1) {
                                grid[nr][nc] = 0; area++; q.add(new int[]{nr,nc});
                            }
                        }
                    }
                    best = Math.max(best, area);
                }
        return best;
    }

    // DFS flood fill
    public int maxAreaOfIslandDfs(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, best = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1)
                    best = Math.max(best, dfs(grid, r, c, rows, cols));
        return best;
    }

    private int dfs(int[][] grid, int r, int c, int rows, int cols) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != 1) return 0;
        grid[r][c] = 0;
        return 1 + dfs(grid, r+1, c, rows, cols) + dfs(grid, r-1, c, rows, cols)
                 + dfs(grid, r, c+1, rows, cols) + dfs(grid, r, c-1, rows, cols);
    }

    static int[][] copy(int[][] g) {
        int[][] c = new int[g.length][];
        for (int i = 0; i < g.length; i++) c[i] = g[i].clone();
        return c;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] g = {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                     {0,0,0,0,0,0,0,1,1,1,0,0,0},
                     {0,1,1,0,1,0,0,0,0,0,0,0,0},
                     {0,1,0,0,1,1,0,0,1,0,1,0,0},
                     {0,1,0,0,1,1,0,0,1,1,1,0,0},
                     {0,0,0,0,0,0,0,0,0,0,1,0,0},
                     {0,0,0,0,0,0,0,1,1,1,0,0,0},
                     {0,0,0,0,0,0,0,1,1,0,0,0,0}};
        assert s.maxAreaOfIslandDfs(copy(g)) == 6 : "test 1";
        assert s.maxAreaOfIsland(copy(g)) == 6 : "test 2";
        assert s.maxAreaOfIsland(new int[][]{{0,0,0,0,0,0,0,0}}) == 0 : "test 3";
        System.out.println("All tests passed.");
    }
}
