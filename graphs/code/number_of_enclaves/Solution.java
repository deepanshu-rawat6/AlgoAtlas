import java.util.*;

public class Solution {
    // Multi-source BFS from boundary land cells, sink connected land, count remaining
    public int numEnclaves(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ((r == 0 || r == rows-1 || c == 0 || c == cols-1) && grid[r][c] == 1) {
                    grid[r][c] = 0;
                    q.add(new int[]{r, c});
                }
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int nr = cur[0]+d[0], nc = cur[1]+d[1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]==1) {
                    grid[nr][nc] = 0; q.add(new int[]{nr, nc});
                }
            }
        }
        int count = 0;
        for (int[] row : grid) for (int v : row) count += v;
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.numEnclaves(new int[][]{{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}}) == 3 : "test 1";
        assert s.numEnclaves(new int[][]{{0,1,1,0},{0,0,1,0},{0,0,1,0},{0,0,0,0}}) == 0 : "test 2";
        System.out.println("All tests passed.");
    }
}
