import java.util.*;

public class Solution {
    // LC 947: Most Stones Removed with Same Row or Column
    // Union-Find: group stones sharing row or col; answer = stones - components
    // Offset col by 10001 to avoid collision with row indices — O(n)
    public int removeStones(int[][] stones) {
        Map<Integer, Integer> parent = new HashMap<>();

        for (int[] stone : stones) union(parent, stone[0], stone[1] + 10001);

        Set<Integer> roots = new HashSet<>();
        for (int[] stone : stones) roots.add(find(parent, stone[0]));
        return stones.length - roots.size();
    }

    private int find(Map<Integer, Integer> parent, int x) {
        parent.putIfAbsent(x, x);
        if (parent.get(x) != x) parent.put(x, find(parent, parent.get(x)));
        return parent.get(x);
    }

    private void union(Map<Integer, Integer> parent, int x, int y) {
        parent.put(find(parent, x), find(parent, y));
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.removeStones(new int[][]{{0,0},{0,1},{1,0},{1,2},{2,1},{2,2}}) == 5 : "t1";
        assert s.removeStones(new int[][]{{0,0},{0,2},{1,1},{2,0},{2,2}}) == 3 : "t2";
        assert s.removeStones(new int[][]{{0,0}}) == 0 : "t3";
        System.out.println("All tests passed.");
    }
}
