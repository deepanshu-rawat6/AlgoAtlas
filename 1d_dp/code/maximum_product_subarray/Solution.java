import java.util.*;

public class Solution {
    // Track running min/max — O(n) time, O(1) space
    public int maxProduct(int[] nums) {
        int curMax = nums[0], curMin = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            int tmpMax = Math.max(num, Math.max(curMax * num, curMin * num));
            curMin = Math.min(num, Math.min(curMax * num, curMin * num));
            curMax = tmpMax;
            best = Math.max(best, curMax);
        }
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxProduct(new int[]{2, 3, -2, 4}) == 6 : "[2,3,-2,4]";
        assert sol.maxProduct(new int[]{-2, 0, -1}) == 0 : "[-2,0,-1]";
        assert sol.maxProduct(new int[]{-2}) == -2 : "single negative";
        assert sol.maxProduct(new int[]{0, 2}) == 2 : "[0,2]";
        System.out.println("All tests passed.");
    }
}
