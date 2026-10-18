import java.util.*;

public class Solution {
    // Bottom-up DP — O(target * n) time, O(target) space
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (num <= i) dp[i] += dp[i - num];
            }
        }
        return dp[target];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.combinationSum4(new int[]{1, 2, 3}, 4) == 7 : "[1,2,3] target=4";
        assert sol.combinationSum4(new int[]{9}, 3) == 0 : "[9] target=3";
        assert sol.combinationSum4(new int[]{1, 2, 3}, 0) == 1 : "target=0";
        assert sol.combinationSum4(new int[]{1}, 3) == 1 : "[1] target=3";
        System.out.println("All tests passed.");
    }
}
