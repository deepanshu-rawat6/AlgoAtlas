import java.util.*;

public class Solution {
    // Rolling variables — O(n) time, O(1) space
    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;
        for (int num : nums) {
            int cur = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.rob(new int[]{1, 2, 3, 1}) == 4 : "[1,2,3,1]";
        assert sol.rob(new int[]{2, 7, 9, 3, 1}) == 12 : "[2,7,9,3,1]";
        assert sol.rob(new int[]{1}) == 1 : "single";
        assert sol.rob(new int[]{2, 1}) == 2 : "two houses";
        System.out.println("All tests passed.");
    }
}
