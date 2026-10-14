import java.util.*;

public class Solution {
    // LC 1584: Min Cost to Connect All Points
    // Prim's MST with Manhattan distance — O(n^2)
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, 0}); // (cost, index)
        int total = 0, added = 0;

        while (added < n) {
            int[] cur = heap.poll();
            int cost = cur[0], i = cur[1];
            if (visited[i]) continue;
            visited[i] = true;
            total += cost; added++;
            for (int j = 0; j < n; j++) {
                if (!visited[j]) {
                    int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                    heap.offer(new int[]{dist, j});
                }
            }
        }
        return total;
    }

    // Kruskal's variant — O(n^2 log n)
    public int minCostConnectPointsKruskal(int[][] points) {
        int n = points.length;
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                edges.add(new int[]{Math.abs(points[i][0]-points[j][0])+Math.abs(points[i][1]-points[j][1]), i, j});
        edges.sort(Comparator.comparingInt(a -> a[0]));

        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int total = 0, used = 0;

        for (int[] e : edges) {
            if (union(parent, rank, e[1], e[2])) {
                total += e[0];
                if (++used == n - 1) break;
            }
        }
        return total;
    }

    private int find(int[] p, int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }
    private boolean union(int[] p, int[] rank, int x, int y) {
        int px = find(p, x), py = find(p, y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        p[py] = px; if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.minCostConnectPoints(new int[][]{{0,0},{2,2},{3,10},{5,2},{7,0}}) == 20 : "t1";
        assert s.minCostConnectPoints(new int[][]{{3,12},{-2,5},{-4,1}}) == 18 : "t2";
        assert s.minCostConnectPoints(new int[][]{{0,0}}) == 0 : "t3";

        assert s.minCostConnectPointsKruskal(new int[][]{{0,0},{2,2},{3,10},{5,2},{7,0}}) == 20 : "k1";
        assert s.minCostConnectPointsKruskal(new int[][]{{3,12},{-2,5},{-4,1}}) == 18 : "k2";
        System.out.println("All tests passed.");
    }
}
