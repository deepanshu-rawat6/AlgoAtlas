import java.util.*;

public class Solution {
    // DFS 3-color: 0=unvisited, 1=visiting, 2=safe
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] state = new int[n];
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (dfs(graph, state, i)) res.add(i);
        return res;
    }

    private boolean dfs(int[][] graph, int[] state, int node) {
        if (state[node] == 1) return false;
        if (state[node] == 2) return true;
        state[node] = 1;
        for (int nb : graph[node])
            if (!dfs(graph, state, nb)) return false;
        state[node] = 2;
        return true;
    }

    // Reverse graph + Kahn's (topological sort from terminal nodes)
    public List<Integer> eventualSafeNodesTopo(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> rev = new ArrayList<>();
        int[] outDeg = new int[n];
        for (int i = 0; i < n; i++) { rev.add(new ArrayList<>()); outDeg[i] = graph[i].length; }
        for (int u = 0; u < n; u++)
            for (int v : graph[u]) rev.get(v).add(u);
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (outDeg[i] == 0) q.add(i);
        Set<Integer> safe = new HashSet<>();
        while (!q.isEmpty()) {
            int node = q.poll();
            safe.add(node);
            for (int parent : rev.get(node))
                if (--outDeg[parent] == 0) q.add(parent);
        }
        List<Integer> res = new ArrayList<>(safe);
        Collections.sort(res);
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.eventualSafeNodes(new int[][]{{1,2},{2,3},{5},{0},{5},{},{}})
            .equals(Arrays.asList(2,4,5,6)) : "test 1";
        assert s.eventualSafeNodes(new int[][]{{1,2,3,4},{1,2},{3,4},{0,4},{}})
            .equals(Arrays.asList(4)) : "test 2";
        assert s.eventualSafeNodesTopo(new int[][]{{1,2},{2,3},{5},{0},{5},{},{}})
            .equals(Arrays.asList(2,4,5,6)) : "test 3";
        System.out.println("All tests passed.");
    }
}
