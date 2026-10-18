import java.util.*;

public class Solution {
    // Boolean DP array — O(n * sum) time, O(sum) space
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int n : nums) total += n;
        if (total % 2 != 0) return false;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            // iterate right-to-left to avoid using same element twice
            for (int j = target; j >= num; j--) {
                if (dp[j - num]) dp[j] = true;
            }
        }
        return dp[target];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.canPartition(new int[]{1, 5, 11, 5}) : "[1,5,11,5]";
        assert !sol.canPartition(new int[]{1, 2, 3, 5}) : "[1,2,3,5]";
        assert sol.canPartition(new int[]{1, 1}) : "[1,1]";
        assert !sol.canPartition(new int[]{1, 3}) : "[1,3]";
        System.out.println("All tests passed.");
    }
}
