import java.util.*;

public class Solution {
    public long uniquePaths(int m, int n) {
        // Math: C(m+n-2, n-1) — robot must make exactly (m-1) down and (n-1) right moves
        // Time: O(min(m,n)), Space: O(1)
        long num = 1;
        int k = Math.min(m - 1, n - 1);
        int total = m + n - 2;
        for (int i = 0; i < k; i++) {
            num = num * (total - i) / (i + 1);
        }
        return num;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.uniquePaths(3, 7) == 28 : "test 1 failed";
        assert sol.uniquePaths(3, 2) == 3 : "test 2 failed";
        assert sol.uniquePaths(1, 1) == 1 : "test 3 failed";
        assert sol.uniquePaths(100, 1) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
