import java.util.*;

public class Solution {
    public int[] countBitsNaive(int n) {
        // O(n*k) — count bits per number via n&(n-1)
        int[] res = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int x = i, c = 0;
            while (x != 0) { x &= x - 1; c++; }
            res[i] = c;
        }
        return res;
    }

    public int[] countBits(int n) {
        // dp[i] = dp[i>>1] + (i&1): shift removes last bit, add it back
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = dp[i >> 1] + (i & 1);
        return dp;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(sol.countBitsNaive(2), new int[]{0, 1, 1});
        assert Arrays.equals(sol.countBitsNaive(5), new int[]{0, 1, 1, 2, 1, 2});
        assert Arrays.equals(sol.countBits(2), new int[]{0, 1, 1});
        assert Arrays.equals(sol.countBits(5), new int[]{0, 1, 1, 2, 1, 2});
        System.out.println("All tests passed.");
    }
}
