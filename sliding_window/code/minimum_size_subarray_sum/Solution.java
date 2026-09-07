import java.util.*;

public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, total = 0, best = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++) {
            total += nums[right];
            while (total >= target) {
                best = Math.min(best, right - left + 1);
                total -= nums[left++];
            }
        }
        return best == Integer.MAX_VALUE ? 0 : best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minSubArrayLen(7, new int[]{2,3,1,2,4,3}) == 2;
        assert sol.minSubArrayLen(4, new int[]{1,4,4}) == 1;
        assert sol.minSubArrayLen(11, new int[]{1,1,1,1,1,1,1,1}) == 0;
        System.out.println("All tests passed.");
    }
}
