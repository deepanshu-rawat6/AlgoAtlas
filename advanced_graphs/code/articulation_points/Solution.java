import java.util.*;

public class Solution {
    // Articulation Points — Tarjan's algorithm
    // Non-root: AP if low[v] >= disc[u]; Root: AP if 2+ DFS-tree children
    // O(V+E)
    private int[] disc, low;
    private boolean[] isAp;
    private int timer;
    private List<List<Integer>> graph;

    public List<Integer> articulationPoints(int n, int[][] edges) {
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) { graph.get(e[0]).add(e[1]); graph.get(e[1]).add(e[0]); }

        disc = new int[n]; low = new int[n]; isAp = new boolean[n];
        Arrays.fill(disc, -1);
        timer = 0;

        for (int i = 0; i < n; i++) if (disc[i] == -1) dfs(i, -1);

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) if (isAp[i]) result.add(i);
        return result;
    }

    private void dfs(int node, int parent) {
        disc[node] = low[node] = timer++;
        int children = 0;
        for (int nb : graph.get(node)) {
            if (disc[nb] == -1) {
                children++;
                dfs(nb, node);
                low[node] = Math.min(low[node], low[nb]);
                if (parent != -1 && low[nb] >= disc[node]) isAp[node] = true;
                if (parent == -1 && children > 1) isAp[node] = true;
            } else if (nb != parent) {
                low[node] = Math.min(low[node], disc[nb]);
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.articulationPoints(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}}).equals(List.of(1, 3)) : "test 1";
        assert s.articulationPoints(3, new int[][]{{0,1},{1,2}}).equals(List.of(1)) : "test 2";
        assert s.articulationPoints(3, new int[][]{{0,1},{1,2},{2,0}}).equals(List.of()) : "test 3";
        assert s.articulationPoints(1, new int[][]{}).equals(List.of()) : "test 4";
        System.out.println("All tests passed.");
    }
}
