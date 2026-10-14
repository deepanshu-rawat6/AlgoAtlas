import java.util.*;

public class Solution {
    // Union-Find: first edge that connects already-connected nodes is redundant
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n+1], rank = new int[n+1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int[] e : edges) if (!union(parent, rank, e[0], e[1])) return e;
        return new int[0];
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }

    private boolean union(int[] parent, int[] rank, int x, int y) {
        int px = find(parent, x), py = find(parent, y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    // DFS: check if path exists before adding each edge
    public int[] findRedundantConnectionDfs(int[][] edges) {
        int n = edges.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) {
            if (hasPath(graph, e[0], e[1], new HashSet<>())) return e;
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        return new int[0];
    }

    private boolean hasPath(List<List<Integer>> graph, int src, int dst, Set<Integer> visited) {
        if (src == dst) return true;
        visited.add(src);
        for (int nei : graph.get(src)) if (!visited.contains(nei) && hasPath(graph, nei, dst, visited)) return true;
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.findRedundantConnection(new int[][]{{1,2},{1,3},{2,3}}), new int[]{2,3}) : "test 1";
        assert Arrays.equals(s.findRedundantConnection(new int[][]{{1,2},{2,3},{3,4},{1,4},{1,5}}), new int[]{1,4}) : "test 2";
        assert Arrays.equals(s.findRedundantConnectionDfs(new int[][]{{1,2},{1,3},{2,3}}), new int[]{2,3}) : "test 3";
        System.out.println("All tests passed.");
    }
}
