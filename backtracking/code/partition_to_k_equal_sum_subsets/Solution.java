import java.util.*;

public class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int n : nums) total += n;
        if (total % k != 0) return false;
        int target = total / k;
        Arrays.sort(nums);
        // reverse
        for (int i = 0, j = nums.length - 1; i < j; i++, j--) {
            int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
        }
        if (nums[0] > target) return false;
        int n = nums.length;
        Map<Integer, Boolean> memo = new HashMap<>();
        return backtrack(nums, 0, 0, target, memo, n);
    }

    private boolean backtrack(int[] nums, int mask, int currentSum, int target,
                               Map<Integer, Boolean> memo, int n) {
        if (mask == (1 << n) - 1) return true;
        if (memo.containsKey(mask)) return memo.get(mask);
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) continue;
            int nextSum = currentSum + nums[i];
            if (nextSum > target) continue;
            if (backtrack(nums, mask | (1 << i), nextSum % target, target, memo, n)) {
                memo.put(mask, true);
                return true;
            }
        }
        memo.put(mask, false);
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.canPartitionKSubsets(new int[]{4, 3, 2, 3, 5, 2, 1}, 4) : "should be true";
        assert !sol.canPartitionKSubsets(new int[]{1, 2, 3, 4}, 3) : "should be false";
        assert sol.canPartitionKSubsets(new int[]{2, 2, 2, 2}, 2) : "should be true";

        System.out.println("All tests passed.");
    }
}
