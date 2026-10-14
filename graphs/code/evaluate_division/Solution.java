import java.util.*;

public class Solution {
    // BFS per query on weighted graph
    public double[] calcEquationBfs(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, values[i]);
            graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / values[i]);
        }
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++)
            res[i] = bfs(graph, queries.get(i).get(0), queries.get(i).get(1));
        return res;
    }

    private double bfs(Map<String, Map<String, Double>> graph, String src, String dst) {
        if (!graph.containsKey(src) || !graph.containsKey(dst)) return -1.0;
        if (src.equals(dst)) return 1.0;
        Set<String> visited = new HashSet<>();
        Queue<Object[]> q = new ArrayDeque<>();
        q.add(new Object[]{src, 1.0});
        visited.add(src);
        while (!q.isEmpty()) {
            Object[] cur = q.poll();
            String node = (String) cur[0];
            double product = (double) cur[1];
            if (node.equals(dst)) return product;
            for (Map.Entry<String, Double> e : graph.get(node).entrySet()) {
                if (visited.add(e.getKey()))
                    q.add(new Object[]{e.getKey(), product * e.getValue()});
            }
        }
        return -1.0;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> eq = Arrays.asList(Arrays.asList("a","b"), Arrays.asList("b","c"));
        double[] vals = {2.0, 3.0};
        List<List<String>> queries = Arrays.asList(
            Arrays.asList("a","c"), Arrays.asList("b","a"),
            Arrays.asList("a","e"), Arrays.asList("a","a"), Arrays.asList("x","x")
        );
        double[] res = s.calcEquationBfs(eq, vals, queries);
        assert Math.abs(res[0] - 6.0) < 1e-9 : "test 1";
        assert Math.abs(res[1] - 0.5) < 1e-9 : "test 2";
        assert res[2] == -1.0 : "test 3";
        assert res[3] == 1.0 : "test 4";
        assert res[4] == -1.0 : "test 5";
        System.out.println("All tests passed.");
    }
}
