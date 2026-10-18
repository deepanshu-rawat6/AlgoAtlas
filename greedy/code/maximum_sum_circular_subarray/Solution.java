import java.util.*;

public class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        int maxSum = nums[0], curMax = nums[0];
        int minSum = nums[0], curMin = nums[0];
        for (int i = 1; i < nums.length; i++) {
            total += nums[i - 1]; // accumulate total as we go (add nums[0] after loop)
            curMax = Math.max(nums[i], curMax + nums[i]);
            maxSum = Math.max(maxSum, curMax);
            curMin = Math.min(nums[i], curMin + nums[i]);
            minSum = Math.min(minSum, curMin);
        }
        total += nums[nums.length - 1];
        // If all negative, maxSum is the answer
        return maxSum > 0 ? Math.max(maxSum, total - minSum) : maxSum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxSubarraySumCircular(new int[]{1, -2, 3, -2}) == 3;
        assert sol.maxSubarraySumCircular(new int[]{5, -3, 5}) == 10;
        assert sol.maxSubarraySumCircular(new int[]{-3, -2, -3}) == -2;
        assert sol.maxSubarraySumCircular(new int[]{3, -1, 2, -1}) == 4;
        System.out.println("All tests passed.");
    }
}
