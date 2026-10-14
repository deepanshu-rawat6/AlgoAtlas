import java.util.*;

public class Solution {
    // LC 1631: Path With Minimum Effort
    // Binary search on effort + BFS to validate — O(m*n*log(10^6))
    public int minimumEffortPath(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        int lo = 0, hi = 1_000_000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (canReach(heights, rows, cols, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean canReach(int[][] h, int rows, int cols, int effort) {
        boolean[][] visited = new boolean[rows][cols];
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0}); visited[0][0] = true;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == rows - 1 && c == cols - 1) return true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]
                        && Math.abs(h[nr][nc] - h[r][c]) <= effort) {
                    visited[nr][nc] = true; q.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }

    // Dijkstra variant — O(m*n*log(m*n))
    public int minimumEffortPathDijkstra(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        int[][] effort = new int[rows][cols];
        for (int[] row : effort) Arrays.fill(row, Integer.MAX_VALUE);
        effort[0][0] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, 0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int e = cur[0], r = cur[1], c = cur[2];
            if (r == rows - 1 && c == cols - 1) return e;
            if (e > effort[r][c]) continue;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    int ne = Math.max(e, Math.abs(heights[nr][nc] - heights[r][c]));
                    if (ne < effort[nr][nc]) { effort[nr][nc] = ne; heap.offer(new int[]{ne, nr, nc}); }
                }
            }
        }
        return effort[rows - 1][cols - 1];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.minimumEffortPath(new int[][]{{1,2,2},{3,8,2},{5,3,5}}) == 2 : "t1";
        assert s.minimumEffortPath(new int[][]{{1,2,3},{3,8,4},{5,3,5}}) == 1 : "t2";
        assert s.minimumEffortPath(new int[][]{{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}}) == 0 : "t3";

        assert s.minimumEffortPathDijkstra(new int[][]{{1,2,2},{3,8,2},{5,3,5}}) == 2 : "d1";
        assert s.minimumEffortPathDijkstra(new int[][]{{1,2,3},{3,8,4},{5,3,5}}) == 1 : "d2";
        System.out.println("All tests passed.");
    }
}
