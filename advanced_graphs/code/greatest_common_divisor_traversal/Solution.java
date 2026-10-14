import java.util.*;

public class Solution {
    // LC 2709: GCD Traversal — Union-Find via shared prime factors
    // Union each index with any previous index sharing a prime factor
    // O(n * sqrt(max_val))
    public boolean canTraverseAllPairs(int[] nums) {
        int n = nums.length;
        if (n == 1) return true;

        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        Map<Integer, Integer> primeToIdx = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            for (int d = 2; (long) d * d <= val; d++) {
                if (val % d == 0) {
                    if (primeToIdx.containsKey(d)) union(parent, rank, i, primeToIdx.get(d));
                    else primeToIdx.put(d, i);
                    while (val % d == 0) val /= d;
                }
            }
            if (val > 1) {
                if (primeToIdx.containsKey(val)) union(parent, rank, i, primeToIdx.get(val));
                else primeToIdx.put(val, i);
            }
        }

        int root = find(parent, 0);
        for (int i = 1; i < n; i++) if (find(parent, i) != root) return false;
        return true;
    }

    private int find(int[] p, int x) {
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }

    private void union(int[] p, int[] rank, int x, int y) {
        int px = find(p, x), py = find(p, y);
        if (px == py) return;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        p[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.canTraverseAllPairs(new int[]{2, 3, 6}) : "t1";
        assert !s.canTraverseAllPairs(new int[]{3, 9, 5}) : "t2";
        assert s.canTraverseAllPairs(new int[]{4, 3, 12, 8}) : "t3";
        assert s.canTraverseAllPairs(new int[]{1}) : "t4";
        assert s.canTraverseAllPairs(new int[]{2, 2}) : "t5";
        System.out.println("All tests passed.");
    }
}
