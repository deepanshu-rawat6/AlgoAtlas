import java.util.*;

public class Solution {
    // LC 743: Network Delay Time
    // Dijkstra from source k; max shortest path = signal arrival time — O((V+E) log V)
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] t : times) graph.get(t[0]).add(new int[]{t[1], t[2]});

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, k});

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int d = cur[0], u = cur[1];
            if (d > dist[u]) continue;
            for (int[] nb : graph.get(u)) {
                int v = nb[0], w = nb[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    heap.offer(new int[]{dist[v], v});
                }
            }
        }

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            ans = Math.max(ans, dist[i]);
        }
        return ans;
    }

    // Bellman-Ford variant — O(V*E)
    public int networkDelayTimeBellmanFord(int[][] times, int n, int k) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        for (int i = 0; i < n - 1; i++)
            for (int[] t : times)
                if (dist[t[0]] != Integer.MAX_VALUE && dist[t[0]] + t[2] < dist[t[1]])
                    dist[t[1]] = dist[t[0]] + t[2];

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            ans = Math.max(ans, dist[i]);
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.networkDelayTime(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2) == 2 : "t1";
        assert s.networkDelayTime(new int[][]{{1,2,1}}, 2, 1) == 1 : "t2";
        assert s.networkDelayTime(new int[][]{{1,2,1}}, 2, 2) == -1 : "t3";

        assert s.networkDelayTimeBellmanFord(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2) == 2 : "b1";
        assert s.networkDelayTimeBellmanFord(new int[][]{{1,2,1}}, 2, 1) == 1 : "b2";
        assert s.networkDelayTimeBellmanFord(new int[][]{{1,2,1}}, 2, 2) == -1 : "b3";
        System.out.println("All tests passed.");
    }
}
