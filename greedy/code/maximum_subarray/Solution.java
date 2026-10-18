import java.util.*;

public class Solution {
    public int maxSubArray(int[] nums) {
        int best = nums[0], curr = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curr = Math.max(nums[i], curr + nums[i]);
            best = Math.max(best, curr);
        }
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6;
        assert sol.maxSubArray(new int[]{1}) == 1;
        assert sol.maxSubArray(new int[]{5, 4, -1, 7, 8}) == 23;
        assert sol.maxSubArray(new int[]{-1, -2, -3}) == -1;
        System.out.println("All tests passed.");
    }
}
