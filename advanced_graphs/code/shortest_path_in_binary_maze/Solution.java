import java.util.*;

public class Solution {
    // LC 1091: Shortest Path in Binary Matrix
    // BFS in 8 directions; mark visited by setting to 1 — O(n^2)
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        if (n == 1) return 1;

        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 1});
        grid[0][0] = 1;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0], c = cur[1], dist = cur[2];
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) continue;
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        if (nr == n - 1 && nc == n - 1) return dist + 1;
                        grid[nr][nc] = 1;
                        queue.offer(new int[]{nr, nc, dist + 1});
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.shortestPathBinaryMatrix(new int[][]{{0,1},{1,0}}) == 2 : "t1";
        assert s.shortestPathBinaryMatrix(new int[][]{{0}}) == 1 : "t2";
        assert s.shortestPathBinaryMatrix(new int[][]{{0,0,0},{1,1,0},{1,1,0}}) == 4 : "t3";
        assert s.shortestPathBinaryMatrix(new int[][]{{1,0},{0,0}}) == -1 : "t4";
        System.out.println("All tests passed.");
    }
}
