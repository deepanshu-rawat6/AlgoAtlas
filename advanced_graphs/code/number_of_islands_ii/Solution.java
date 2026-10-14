import java.util.*;

public class Solution {
    // LC 305: Number of Islands II
    // Online Union-Find, lazy init; encode cell (r,c) as r*n+c — O(k * alpha(mn))
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        Map<Integer, Integer> parent = new HashMap<>(), rank = new HashMap<>();
        int[] count = {0};
        List<Integer> result = new ArrayList<>();
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        for (int[] pos : positions) {
            int r = pos[0], c = pos[1], cell = r * n + c;
            if (parent.containsKey(cell)) { result.add(count[0]); continue; }
            parent.put(cell, cell); rank.put(cell, 0);
            count[0]++;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1], nb = nr * n + nc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && parent.containsKey(nb))
                    union(parent, rank, cell, nb, count);
            }
            result.add(count[0]);
        }
        return result;
    }

    private int find(Map<Integer, Integer> parent, int x) {
        if (parent.get(x) != x) parent.put(x, find(parent, parent.get(x)));
        return parent.get(x);
    }

    private void union(Map<Integer, Integer> parent, Map<Integer, Integer> rank, int x, int y, int[] count) {
        int px = find(parent, x), py = find(parent, y);
        if (px == py) return;
        if (rank.get(px) < rank.get(py)) { int t = px; px = py; py = t; }
        parent.put(py, px);
        if (rank.get(px).equals(rank.get(py))) rank.put(px, rank.get(px) + 1);
        count[0]--;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.numIslands2(3, 3, new int[][]{{0,0},{0,1},{1,2},{2,1}}).equals(List.of(1,1,2,3)) : "t1";
        assert s.numIslands2(2, 2, new int[][]{{0,0},{0,0},{1,1}}).equals(List.of(1,1,2)) : "t2";
        assert s.numIslands2(1, 3, new int[][]{{0,0},{0,2},{0,1}}).equals(List.of(1,2,1)) : "t3";
        System.out.println("All tests passed.");
    }
}
