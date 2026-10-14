import java.util.*;

public class Solution {
    // Union-Find
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;
        for (int[] e : edges) if (union(parent, rank, e[0], e[1])) components--;
        return components;
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

    // DFS
    public int countComponentsDfs(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) { graph.get(e[0]).add(e[1]); graph.get(e[1]).add(e[0]); }
        int count = 0;
        for (int i = 0; i < n; i++) if (!visited[i]) { dfs(graph, visited, i); count++; }
        return count;
    }

    private void dfs(List<List<Integer>> graph, boolean[] visited, int node) {
        visited[node] = true;
        for (int nei : graph.get(node)) if (!visited[nei]) dfs(graph, visited, nei);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countComponents(5, new int[][]{{0,1},{1,2},{3,4}}) == 2 : "test 1";
        assert s.countComponents(5, new int[][]{{0,1},{1,2},{2,3},{3,4}}) == 1 : "test 2";
        assert s.countComponents(3, new int[0][]) == 3 : "test 3";
        assert s.countComponentsDfs(5, new int[][]{{0,1},{1,2},{3,4}}) == 2 : "test 4";
        System.out.println("All tests passed.");
    }
}
