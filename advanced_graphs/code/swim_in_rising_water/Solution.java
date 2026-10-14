import java.util.*;

public class Solution {
    // LC 778: Swim in Rising Water
    // Binary search on time t + BFS to check reachability — O(n^2 log n)
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        int lo = grid[0][0], hi = n * n - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (canReach(grid, n, mid)) hi = mid; else lo = mid + 1;
        }
        return lo;
    }

    private boolean canReach(int[][] grid, int n, int t) {
        if (grid[0][0] > t) return false;
        boolean[][] visited = new boolean[n][n];
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0}); visited[0][0] = true;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == n - 1 && c == n - 1) return true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc] && grid[nr][nc] <= t) {
                    visited[nr][nc] = true; q.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }

    // Dijkstra variant: min-heap on max elevation — O(n^2 log n)
    public int swimInWaterDijkstra(int[][] grid) {
        int n = grid.length;
        boolean[][] visited = new boolean[n][n];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{grid[0][0], 0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int t = cur[0], r = cur[1], c = cur[2];
            if (visited[r][c]) continue;
            visited[r][c] = true;
            if (r == n - 1 && c == n - 1) return t;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc])
                    heap.offer(new int[]{Math.max(t, grid[nr][nc]), nr, nc});
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.swimInWater(new int[][]{{0,2},{1,3}}) == 3 : "t1";
        assert s.swimInWater(new int[][]{{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}) == 16 : "t2";

        assert s.swimInWaterDijkstra(new int[][]{{0,2},{1,3}}) == 3 : "d1";
        assert s.swimInWaterDijkstra(new int[][]{{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}) == 16 : "d2";
        System.out.println("All tests passed.");
    }
}
