import java.util.*;

public class Solution {
    // Iterative leaf removal — remaining 1-2 nodes are MHT roots
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);
        List<Set<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new HashSet<>());
        for (int[] e : edges) { graph.get(e[0]).add(e[1]); graph.get(e[1]).add(e[0]); }
        Queue<Integer> leaves = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (graph.get(i).size() == 1) leaves.add(i);
        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            Queue<Integer> newLeaves = new ArrayDeque<>();
            for (int leaf : leaves) {
                int nei = graph.get(leaf).iterator().next();
                graph.get(nei).remove(leaf);
                if (graph.get(nei).size() == 1) newLeaves.add(nei);
            }
            leaves = newLeaves;
        }
        return new ArrayList<>(leaves);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findMinHeightTrees(4, new int[][]{{1,0},{1,2},{1,3}})
            .equals(Collections.singletonList(1)) : "test 1";
        List<Integer> r2 = new ArrayList<>(s.findMinHeightTrees(6, new int[][]{{3,0},{3,1},{3,2},{3,4},{5,4}}));
        Collections.sort(r2);
        assert r2.equals(Arrays.asList(3, 4)) : "test 2";
        assert s.findMinHeightTrees(1, new int[0][]).equals(Collections.singletonList(0)) : "test 3";
        System.out.println("All tests passed.");
    }
}
