import java.util.*;

public class Solution {
    // Two linear passes (exclude first or last) — O(n) time, O(1) space
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(robRange(nums, 0, nums.length - 2),
                        robRange(nums, 1, nums.length - 1));
    }

    private int robRange(int[] nums, int lo, int hi) {
        int prev2 = 0, prev1 = 0;
        for (int i = lo; i <= hi; i++) {
            int cur = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.rob(new int[]{2, 3, 2}) == 3 : "[2,3,2]";
        assert sol.rob(new int[]{1, 2, 3}) == 3 : "[1,2,3]";
        assert sol.rob(new int[]{1, 2, 3, 1}) == 4 : "[1,2,3,1]";
        assert sol.rob(new int[]{1}) == 1 : "single";
        System.out.println("All tests passed.");
    }
}
