import java.util.*;

public class Solution {
    public int countSubsequences(int[] nums, int k) {
        Map<String, Integer> memo = new HashMap<>();
        return dp(nums, 0, k, memo);
    }

    private int dp(int[] nums, int idx, int remaining, Map<String, Integer> memo) {
        if (idx == nums.length) return remaining == 0 ? 1 : 0;
        String key = idx + "," + remaining;
        if (memo.containsKey(key)) return memo.get(key);
        int count = dp(nums, idx + 1, remaining, memo);
        if (nums[idx] <= remaining) count += dp(nums, idx + 1, remaining - nums[idx], memo);
        memo.put(key, count);
        return count;
    }

    public int countSubsequencesBacktrack(int[] nums, int k) {
        int[] count = {0};
        backtrack(nums, 0, 0, k, count);
        return count[0];
    }

    private void backtrack(int[] nums, int idx, int currentSum, int k, int[] count) {
        if (idx == nums.length) {
            if (currentSum == k) count[0]++;
            return;
        }
        backtrack(nums, idx + 1, currentSum + nums[idx], k, count);
        backtrack(nums, idx + 1, currentSum, k, count);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.countSubsequences(new int[]{1, 2, 1}, 2) == 2 : "test failed";
        assert sol.countSubsequences(new int[]{1, 1, 1}, 2) == 3 : "test failed";
        assert sol.countSubsequencesBacktrack(new int[]{1, 2, 1}, 2) == 2 : "test failed";
        assert sol.countSubsequencesBacktrack(new int[]{1, 1, 1}, 2) == 3 : "test failed";
        System.out.println("All tests passed.");
    }
}
