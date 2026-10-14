import java.util.*;

public class Solution {
    // Kahn's BFS topological sort
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        for (int[] p : prerequisites) {
            graph.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++)
            if (indegree[i] == 0) q.add(i);
        int[] order = new int[numCourses];
        int idx = 0;
        while (!q.isEmpty()) {
            int node = q.poll();
            order[idx++] = node;
            for (int nei : graph.get(node))
                if (--indegree[nei] == 0) q.add(nei);
        }
        return idx == numCourses ? order : new int[0];
    }

    // DFS post-order (reverse = topological order)
    public int[] findOrderDfs(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        for (int[] p : prerequisites) graph.get(p[1]).add(p[0]);
        int[] state = new int[numCourses]; // 0=unvisited,1=visiting,2=done
        List<Integer> order = new ArrayList<>();
        for (int i = 0; i < numCourses; i++)
            if (!dfs(graph, state, order, i)) return new int[0];
        Collections.reverse(order);
        return order.stream().mapToInt(Integer::intValue).toArray();
    }

    private boolean dfs(List<List<Integer>> graph, int[] state, List<Integer> order, int node) {
        if (state[node] == 1) return false;
        if (state[node] == 2) return true;
        state[node] = 1;
        for (int nei : graph.get(node))
            if (!dfs(graph, state, order, nei)) return false;
        state[node] = 2;
        order.add(node);
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] r1 = s.findOrder(2, new int[][]{{1,0}});
        assert Arrays.equals(r1, new int[]{0,1}) : "test 1";
        int[] r2 = s.findOrder(4, new int[][]{{1,0},{2,0},{3,1},{3,2}});
        assert r2.length == 4 && r2[0] == 0 && r2[3] == 3 : "test 2";
        assert s.findOrder(2, new int[][]{{1,0},{0,1}}).length == 0 : "test 3";
        assert Arrays.equals(s.findOrder(1, new int[0][]), new int[]{0}) : "test 4";
        assert Arrays.equals(s.findOrderDfs(2, new int[][]{{1,0}}), new int[]{0,1}) : "test 5";
        assert s.findOrderDfs(2, new int[][]{{1,0},{0,1}}).length == 0 : "test 6";
        System.out.println("All tests passed.");
    }
}
