import java.util.*;

public class Solution {
    public boolean graphColoring(int n, int[][] edges, int m) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        int[] color = new int[n];
        return backtrack(0, n, m, color, graph);
    }

    private boolean backtrack(int node, int n, int m, int[] color, List<List<Integer>> graph) {
        if (node == n) return true;
        for (int c = 1; c <= m; c++) {
            if (isSafe(node, c, color, graph)) {
                color[node] = c;
                if (backtrack(node + 1, n, m, color, graph)) return true;
                color[node] = 0;
            }
        }
        return false;
    }

    private boolean isSafe(int node, int c, int[] color, List<List<Integer>> graph) {
        for (int neighbor : graph.get(node)) {
            if (color[neighbor] == c) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.graphColoring(4, new int[][]{{0,1},{1,2},{2,3},{3,0},{0,2}}, 3) : "should be true";
        assert !sol.graphColoring(3, new int[][]{{0,1},{1,2},{0,2}}, 2) : "should be false";
        assert sol.graphColoring(1, new int[][]{}, 1) : "single node";

        System.out.println("All tests passed.");
    }
}
