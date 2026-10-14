import java.util.*;

public class Solution {
    // LC 1319: Number of Operations to Make Network Connected
    // Union-Find: if < n-1 edges return -1; else answer = components - 1 — O(n + e)
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;

        int[] parent = new int[n], rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int components = n;

        for (int[] c : connections) {
            int px = find(parent, c[0]), py = find(parent, c[1]);
            if (px != py) {
                if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
                parent[py] = px;
                if (rank[px] == rank[py]) rank[px]++;
                components--;
            }
        }
        return components - 1;
    }

    private int find(int[] p, int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.makeConnected(4, new int[][]{{0,1},{0,2},{1,2}}) == 1 : "t1";
        assert s.makeConnected(6, new int[][]{{0,1},{0,2},{0,3},{1,2},{1,3}}) == 2 : "t2";
        assert s.makeConnected(6, new int[][]{{0,1},{0,2},{0,3},{1,2}}) == -1 : "t3";
        assert s.makeConnected(1, new int[][]{}) == 0 : "t4";
        System.out.println("All tests passed.");
    }
}
