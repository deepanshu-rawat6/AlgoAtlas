import java.util.*;

public class Solution {
    // DFS on adjacency matrix
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinces = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) { visited[i] = true; dfs(isConnected, visited, i); provinces++; }
        }
        return provinces;
    }

    private void dfs(int[][] isConnected, boolean[] visited, int node) {
        for (int j = 0; j < isConnected.length; j++)
            if (isConnected[node][j] == 1 && !visited[j]) { visited[j] = true; dfs(isConnected, visited, j); }
    }

    // Union-Find
    public int findCircleNumUf(int[][] isConnected) {
        int n = isConnected.length;
        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;
        for (int i = 0; i < n; i++)
            for (int j = i+1; j < n; j++)
                if (isConnected[i][j] == 1 && union(parent, rank, i, j)) components--;
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

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findCircleNum(new int[][]{{1,1,0},{1,1,0},{0,0,1}}) == 2 : "test 1";
        assert s.findCircleNum(new int[][]{{1,0,0},{0,1,0},{0,0,1}}) == 3 : "test 2";
        assert s.findCircleNumUf(new int[][]{{1,1,0},{1,1,0},{0,0,1}}) == 2 : "test 3";
        System.out.println("All tests passed.");
    }
}
