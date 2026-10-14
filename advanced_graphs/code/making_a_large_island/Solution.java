import java.util.*;

public class Solution {
    // LC 827: Making A Large Island
    // Label islands with unique ids (starting at 2), record sizes, try each 0 flip
    // O(n^2)
    public int largestIsland(int[][] grid) {
        int n = grid.length;
        Map<Integer, Integer> islandSize = new HashMap<>();
        int islandId = 2;

        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1) {
                    islandSize.put(islandId, dfs(grid, r, c, n, islandId));
                    islandId++;
                }

        int result = islandSize.values().stream().mapToInt(Integer::intValue).max().orElse(0);
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    Set<Integer> seen = new HashSet<>();
                    int size = 1;
                    for (int[] d : dirs) {
                        int nr = r + d[0], nc = c + d[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] > 1) {
                            int id = grid[nr][nc];
                            if (seen.add(id)) size += islandSize.get(id);
                        }
                    }
                    result = Math.max(result, size);
                }
            }
        }
        return result;
    }

    private int dfs(int[][] grid, int r, int c, int n, int id) {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return 0;
        grid[r][c] = id;
        return 1 + dfs(grid, r+1, c, n, id) + dfs(grid, r-1, c, n, id)
                 + dfs(grid, r, c+1, n, id) + dfs(grid, r, c-1, n, id);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.largestIsland(new int[][]{{1,0},{0,1}}) == 3 : "t1";
        assert s.largestIsland(new int[][]{{1,1},{1,0}}) == 4 : "t2";
        assert s.largestIsland(new int[][]{{1,1},{1,1}}) == 4 : "t3";
        assert s.largestIsland(new int[][]{{0,0},{0,0}}) == 1 : "t4";
        System.out.println("All tests passed.");
    }
}
