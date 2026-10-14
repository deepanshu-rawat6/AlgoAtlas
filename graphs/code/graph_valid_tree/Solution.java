import java.util.*;

public class Solution {
    // Union-Find: n-1 edges + no cycle = valid tree
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) if (!union(parent, rank, e[0], e[1])) return false;
        return true;
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

    // BFS: n-1 edges + all nodes visited from node 0
    public boolean validTreeBfs(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) { graph.get(e[0]).add(e[1]); graph.get(e[1]).add(e[0]); }
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0); visited.add(0);
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nei : graph.get(node)) if (visited.add(nei)) q.add(nei);
        }
        return visited.size() == n;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.validTree(5, new int[][]{{0,1},{0,2},{0,3},{1,4}}) : "test 1";
        assert !s.validTree(5, new int[][]{{0,1},{1,2},{2,3},{1,3},{1,4}}) : "test 2";
        assert s.validTree(1, new int[0][]) : "test 3";
        assert !s.validTree(4, new int[][]{{0,1},{2,3}}) : "test 4";
        assert s.validTreeBfs(5, new int[][]{{0,1},{0,2},{0,3},{1,4}}) : "test 5";
        assert !s.validTreeBfs(5, new int[][]{{0,1},{1,2},{2,3},{1,3},{1,4}}) : "test 6";
        System.out.println("All tests passed.");
    }
}
