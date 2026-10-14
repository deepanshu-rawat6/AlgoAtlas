import java.util.*;

public class Solution {
    // Floyd-Warshall transitive closure
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] reach = new boolean[numCourses][numCourses];
        for (int[] p : prerequisites) reach[p[0]][p[1]] = true;
        for (int k = 0; k < numCourses; k++)
            for (int i = 0; i < numCourses; i++)
                for (int j = 0; j < numCourses; j++)
                    if (reach[i][k] && reach[k][j]) reach[i][j] = true;
        List<Boolean> res = new ArrayList<>();
        for (int[] q : queries) res.add(reach[q[0]][q[1]]);
        return res;
    }

    // BFS per query
    public List<Boolean> checkIfPrerequisiteBfs(int numCourses, int[][] prerequisites, int[][] queries) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        for (int[] p : prerequisites) graph.get(p[0]).add(p[1]);
        List<Boolean> res = new ArrayList<>();
        for (int[] q : queries) res.add(canReach(graph, q[0], q[1]));
        return res;
    }

    private boolean canReach(List<List<Integer>> graph, int src, int dst) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> q = new ArrayDeque<>();
        q.add(src);
        while (!q.isEmpty()) {
            int node = q.poll();
            if (node == dst) return true;
            for (int nei : graph.get(node))
                if (visited.add(nei)) q.add(nei);
        }
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.checkIfPrerequisite(2, new int[][]{{1,0}}, new int[][]{{0,1},{1,0}})
            .equals(Arrays.asList(false, true)) : "test 1";
        assert s.checkIfPrerequisite(2, new int[0][], new int[][]{{1,0},{0,1}})
            .equals(Arrays.asList(false, false)) : "test 2";
        assert s.checkIfPrerequisite(3, new int[][]{{1,2},{1,0},{2,0}}, new int[][]{{1,0},{1,2}})
            .equals(Arrays.asList(true, true)) : "test 3";
        assert s.checkIfPrerequisiteBfs(2, new int[][]{{1,0}}, new int[][]{{0,1},{1,0}})
            .equals(Arrays.asList(false, true)) : "test 4";
        System.out.println("All tests passed.");
    }
}
