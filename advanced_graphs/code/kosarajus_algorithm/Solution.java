import java.util.*;

public class Solution {
    // Kosaraju's SCC: 1) DFS finish order, 2) transpose graph, 3) DFS in reverse finish
    // O(V+E)
    public List<List<Integer>> findSCCs(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>(), rev = new ArrayList<>();
        for (int i = 0; i < n; i++) { graph.add(new ArrayList<>()); rev.add(new ArrayList<>()); }
        for (int[] e : edges) { graph.get(e[0]).add(e[1]); rev.get(e[1]).add(e[0]); }

        boolean[] visited = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();

        // Pass 1: iterative DFS, push in finish order
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs1(i, graph, visited, stack);
        }

        // Pass 2: process in reverse finish order on transposed graph
        Arrays.fill(visited, false);
        List<List<Integer>> sccs = new ArrayList<>();
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (!visited[node]) {
                List<Integer> comp = new ArrayList<>();
                dfs2(node, rev, visited, comp);
                Collections.sort(comp);
                sccs.add(comp);
            }
        }
        return sccs;
    }

    private void dfs1(int start, List<List<Integer>> g, boolean[] visited, Deque<Integer> stack) {
        Deque<int[]> dfsStack = new ArrayDeque<>(); // [node, neighborIdx]
        dfsStack.push(new int[]{start, 0});
        visited[start] = true;
        while (!dfsStack.isEmpty()) {
            int[] cur = dfsStack.peek();
            int node = cur[0];
            if (cur[1] < g.get(node).size()) {
                int nb = g.get(node).get(cur[1]++);
                if (!visited[nb]) { visited[nb] = true; dfsStack.push(new int[]{nb, 0}); }
            } else {
                stack.push(node);
                dfsStack.pop();
            }
        }
    }

    private void dfs2(int start, List<List<Integer>> g, boolean[] visited, List<Integer> comp) {
        Deque<Integer> dfsStack = new ArrayDeque<>();
        dfsStack.push(start);
        visited[start] = true;
        while (!dfsStack.isEmpty()) {
            int node = dfsStack.pop();
            comp.add(node);
            for (int nb : g.get(node)) if (!visited[nb]) { visited[nb] = true; dfsStack.push(nb); }
        }
    }

    static List<List<Integer>> sortedSccs(List<List<Integer>> sccs) {
        List<List<Integer>> copy = new ArrayList<>(sccs);
        copy.sort(Comparator.comparingInt(l -> l.get(0)));
        return copy;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert sortedSccs(s.findSCCs(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}})).equals(List.of(List.of(0,1,2),List.of(3),List.of(4))) : "t1";
        assert sortedSccs(s.findSCCs(3, new int[][]{{0,1},{1,2},{2,0}})).equals(List.of(List.of(0,1,2))) : "t2";
        assert sortedSccs(s.findSCCs(3, new int[][]{{0,1},{1,2}})).equals(List.of(List.of(0),List.of(1),List.of(2))) : "t3";
        System.out.println("All tests passed.");
    }
}
