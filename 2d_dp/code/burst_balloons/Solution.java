import java.util.*;

public class Solution {
    public int maxCoins(int[] nums) {
        // Interval DP: pad with sentinel 1s; dp[l][r] = max coins bursting all in (l,r)
        // k is the LAST balloon burst in range: coins = nums[l]*nums[k]*nums[r]
        // Time: O(n^3), Space: O(n^2)
        int n = nums.length;
        int[] padded = new int[n + 2];
        padded[0] = 1;
        padded[n + 1] = 1;
        for (int i = 0; i < n; i++) padded[i + 1] = nums[i];
        int len = padded.length;
        int[][] dp = new int[len][len];
        for (int length = 2; length < len; length++) {
            for (int left = 0; left < len - length; left++) {
                int right = left + length;
                for (int k = left + 1; k < right; k++) {
                    dp[left][right] = Math.max(dp[left][right],
                        padded[left] * padded[k] * padded[right] + dp[left][k] + dp[k][right]);
                }
            }
        }
        return dp[0][len - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxCoins(new int[]{3,1,5,8}) == 167 : "test 1 failed";
        assert sol.maxCoins(new int[]{1,5}) == 10 : "test 2 failed";
        assert sol.maxCoins(new int[]{1}) == 1 : "test 3 failed";
        assert sol.maxCoins(new int[]{0}) == 0 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
