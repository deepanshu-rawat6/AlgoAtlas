import java.util.*;

public class Solution {
    public boolean hasSubsequenceSum(int[] nums, int k) {
        return recurse(nums, 0, k);
    }

    private boolean recurse(int[] nums, int idx, int remaining) {
        if (remaining == 0) return true;
        if (idx == nums.length) return false;
        if (nums[idx] <= remaining && recurse(nums, idx + 1, remaining - nums[idx])) return true;
        return recurse(nums, idx + 1, remaining);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.hasSubsequenceSum(new int[]{1, 2, 3, 4}, 6) : "test failed";
        assert !sol.hasSubsequenceSum(new int[]{1, 2, 3}, 7) : "test failed";
        assert sol.hasSubsequenceSum(new int[]{1, 2, 1}, 2) : "test failed";
        assert sol.hasSubsequenceSum(new int[]{5}, 5) : "test failed";
        assert !sol.hasSubsequenceSum(new int[]{5}, 3) : "test failed";
        System.out.println("All tests passed.");
    }
}
