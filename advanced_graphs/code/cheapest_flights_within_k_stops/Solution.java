import java.util.*;

public class Solution {
    // LC 787: Cheapest Flights Within K Stops
    // Bellman-Ford with k+1 relaxation rounds — O(k*E)
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;

        for (int i = 0; i <= k; i++) {
            int[] tmp = Arrays.copyOf(prices, n);
            for (int[] f : flights) {
                int u = f[0], v = f[1], w = f[2];
                if (prices[u] != Integer.MAX_VALUE && prices[u] + w < tmp[v])
                    tmp[v] = prices[u] + w;
            }
            prices = tmp;
        }
        return prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];
    }

    // Modified Dijkstra tracking stops — O(V*E)
    public int findCheapestPriceDijkstra(int n, int[][] flights, int src, int dst, int k) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] f : flights) graph.get(f[0]).add(new int[]{f[1], f[2]});

        int[][] dist = new int[n][k + 2];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[src][0] = 0;
        // (cost, node, stops)
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, src, 0});

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int cost = cur[0], u = cur[1], stops = cur[2];
            if (u == dst) return cost;
            if (stops > k) continue;
            for (int[] nb : graph.get(u)) {
                int v = nb[0], w = nb[1];
                int newCost = cost + w;
                if (newCost < dist[v][stops + 1]) {
                    dist[v][stops + 1] = newCost;
                    heap.offer(new int[]{newCost, v, stops + 1});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findCheapestPrice(4, new int[][]{{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}, 0, 3, 1) == 700 : "t1";
        assert s.findCheapestPrice(3, new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 1) == 200 : "t2";
        assert s.findCheapestPrice(3, new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 0) == 500 : "t3";

        assert s.findCheapestPriceDijkstra(4, new int[][]{{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}, 0, 3, 1) == 700 : "d1";
        assert s.findCheapestPriceDijkstra(3, new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 1) == 200 : "d2";
        assert s.findCheapestPriceDijkstra(3, new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 0) == 500 : "d3";
        System.out.println("All tests passed.");
    }
}
