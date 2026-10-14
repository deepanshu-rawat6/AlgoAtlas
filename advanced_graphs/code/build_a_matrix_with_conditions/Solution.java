import java.util.*;

public class Solution {
    // LC 2392: Build a Matrix With Conditions
    // Topo sort rows and cols independently (Kahn's BFS); place val at intersection
    // O(k + conditions)
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        List<Integer> rowOrder = topoSort(k, rowConditions);
        List<Integer> colOrder = topoSort(k, colConditions);
        if (rowOrder.isEmpty() || colOrder.isEmpty()) return new int[0][0];

        int[] rowPos = new int[k + 1], colPos = new int[k + 1];
        for (int i = 0; i < k; i++) rowPos[rowOrder.get(i)] = i;
        for (int i = 0; i < k; i++) colPos[colOrder.get(i)] = i;

        int[][] matrix = new int[k][k];
        for (int val = 1; val <= k; val++) matrix[rowPos[val]][colPos[val]] = val;
        return matrix;
    }

    private List<Integer> topoSort(int k, int[][] conditions) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDeg = new int[k + 1];
        for (int i = 0; i <= k; i++) adj.add(new ArrayList<>());
        for (int[] c : conditions) { adj.get(c[0]).add(c[1]); inDeg[c[1]]++; }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= k; i++) if (inDeg[i] == 0) q.offer(i);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int node = q.poll();
            order.add(node);
            for (int nb : adj.get(node)) if (--inDeg[nb] == 0) q.offer(nb);
        }
        return order.size() == k ? order : Collections.emptyList();
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] res = s.buildMatrix(3, new int[][]{{1,2},{3,2}}, new int[][]{{2,1},{3,2}});
        assert res.length == 3 && res[0].length == 3 : "shape";
        List<Integer> flat = new ArrayList<>();
        for (int[] row : res) for (int v : row) if (v != 0) flat.add(v);
        Collections.sort(flat);
        assert flat.equals(List.of(1, 2, 3)) : "values";

        assert s.buildMatrix(3, new int[][]{{1,2},{2,3},{3,1}}, new int[][]{{1,2}}).length == 0 : "cycle";
        System.out.println("All tests passed.");
    }
}
