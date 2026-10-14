import java.util.*;

public class Solution {
    // LC 1192: Critical Connections (Bridges) — Tarjan's bridge finding
    // Edge (u,v) is a bridge if low[v] > disc[u]; O(V+E)
    private int[] disc, low;
    private int timer;
    private List<List<Integer>> graph;
    private List<List<Integer>> bridges;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (List<Integer> e : connections) {
            graph.get(e.get(0)).add(e.get(1));
            graph.get(e.get(1)).add(e.get(0));
        }
        disc = new int[n]; low = new int[n];
        Arrays.fill(disc, -1);
        timer = 0;
        bridges = new ArrayList<>();

        for (int i = 0; i < n; i++) if (disc[i] == -1) dfs(i, -1);
        return bridges;
    }

    private void dfs(int node, int parent) {
        disc[node] = low[node] = timer++;
        for (int nb : graph.get(node)) {
            if (disc[nb] == -1) {
                dfs(nb, node);
                low[node] = Math.min(low[node], low[nb]);
                if (low[nb] > disc[node]) bridges.add(List.of(node, nb));
            } else if (nb != parent) {
                low[node] = Math.min(low[node], disc[nb]);
            }
        }
    }

    static List<List<Integer>> norm(List<List<Integer>> br) {
        List<List<Integer>> res = new ArrayList<>();
        for (List<Integer> e : br) {
            List<Integer> s = new ArrayList<>(e);
            Collections.sort(s);
            res.add(s);
        }
        res.sort(Comparator.comparingInt((List<Integer> l) -> l.get(0)).thenComparingInt(l -> l.get(1)));
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert norm(s.criticalConnections(4, List.of(List.of(0,1),List.of(1,2),List.of(2,0),List.of(1,3)))).equals(List.of(List.of(1,3))) : "test 1";
        assert norm(s.criticalConnections(4, List.of(List.of(0,1),List.of(1,2),List.of(2,3)))).equals(List.of(List.of(0,1),List.of(1,2),List.of(2,3))) : "test 2";
        assert norm(s.criticalConnections(3, List.of(List.of(0,1),List.of(1,2),List.of(2,0)))).equals(List.of()) : "test 3";
        System.out.println("All tests passed.");
    }
}
