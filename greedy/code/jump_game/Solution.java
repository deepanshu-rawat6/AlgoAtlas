import java.util.*;

public class Solution {
    public boolean canJump(int[] nums) {
        int farthest = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > farthest) return false;
            farthest = Math.max(farthest, i + nums[i]);
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.canJump(new int[]{2, 3, 1, 1, 4}) == true;
        assert sol.canJump(new int[]{3, 2, 1, 0, 4}) == false;
        assert sol.canJump(new int[]{0}) == true;
        assert sol.canJump(new int[]{2, 0, 0}) == true;
        System.out.println("All tests passed.");
    }
}
