import java.util.*;

public class Solution {
    // BFS 2-coloring
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);
        for (int start = 0; start < n; start++) {
            if (color[start] != -1) continue;
            Queue<Integer> q = new ArrayDeque<>();
            q.add(start);
            color[start] = 0;
            while (!q.isEmpty()) {
                int node = q.poll();
                for (int nb : graph[node]) {
                    if (color[nb] == -1) {
                        color[nb] = 1 - color[node];
                        q.add(nb);
                    } else if (color[nb] == color[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    // DFS 2-coloring
    public boolean isBipartiteDfs(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);
        for (int i = 0; i < n; i++)
            if (color[i] == -1 && !dfs(graph, color, i, 0))
                return false;
        return true;
    }

    private boolean dfs(int[][] graph, int[] color, int node, int c) {
        color[node] = c;
        for (int nb : graph[node]) {
            if (color[nb] == -1) {
                if (!dfs(graph, color, nb, 1 - c)) return false;
            } else if (color[nb] == c) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.isBipartite(new int[][]{{1,3},{0,2},{1,3},{0,2}}) : "test 1";
        assert !s.isBipartite(new int[][]{{1,2,3},{0,2},{0,1,3},{0,2}}) : "test 2";
        assert s.isBipartiteDfs(new int[][]{{1,3},{0,2},{1,3},{0,2}}) : "test 3";
        assert !s.isBipartiteDfs(new int[][]{{1,2,3},{0,2},{0,1,3},{0,2}}) : "test 4";
        System.out.println("All tests passed.");
    }
}
