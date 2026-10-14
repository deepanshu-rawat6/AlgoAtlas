import java.util.*;

public class Solution {
    // LC 1976: Number of Ways to Arrive at Destination
    // Dijkstra + count: shorter path → reset ways; equal path → add ways
    // O((V+E) log V)
    public int countPaths(int n, int[][] roads) {
        final int MOD = 1_000_000_007;
        List<List<long[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] r : roads) {
            graph.get(r[0]).add(new long[]{r[1], r[2]});
            graph.get(r[1]).add(new long[]{r[0], r[2]});
        }

        long[] dist = new long[n];
        long[] ways = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0; ways[0] = 1;

        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, 0});

        while (!heap.isEmpty()) {
            long[] cur = heap.poll();
            long d = cur[0]; int u = (int) cur[1];
            if (d > dist[u]) continue;
            for (long[] nb : graph.get(u)) {
                int v = (int) nb[0]; long w = nb[1];
                long nd = dist[u] + w;
                if (nd < dist[v]) {
                    dist[v] = nd; ways[v] = ways[u];
                    heap.offer(new long[]{nd, v});
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return (int) ways[n - 1];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countPaths(7, new int[][]{{0,6,7},{0,1,2},{1,2,3},{1,3,3},{6,3,3},{3,5,1},{6,5,1},{2,5,1},{0,4,5},{4,6,2}}) == 4 : "t1";
        assert s.countPaths(2, new int[][]{{0,1,1}}) == 1 : "t2";
        assert s.countPaths(4, new int[][]{{0,1,1},{1,3,1},{0,2,1},{2,3,1}}) == 2 : "t3";
        System.out.println("All tests passed.");
    }
}
