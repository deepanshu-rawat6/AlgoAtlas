import java.util.*;

public class Solution {
    // Multi-source BFS from all initially rotten oranges
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        int fresh = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) q.add(new int[]{r, c});
                else if (grid[r][c] == 1) fresh++;
            }
        if (fresh == 0) return 0;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        int minutes = 0;
        while (!q.isEmpty() && fresh > 0) {
            minutes++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cur = q.poll();
                for (int[] d : dirs) {
                    int nr = cur[0]+d[0], nc = cur[1]+d[1];
                    if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]==1) {
                        grid[nr][nc] = 2; fresh--; q.add(new int[]{nr, nc});
                    }
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.orangesRotting(new int[][]{{2,1,1},{1,1,0},{0,1,1}}) == 4 : "test 1";
        assert s.orangesRotting(new int[][]{{2,1,1},{0,1,1},{1,0,1}}) == -1 : "test 2";
        assert s.orangesRotting(new int[][]{{0,2}}) == 0 : "test 3";
        System.out.println("All tests passed.");
    }
}
