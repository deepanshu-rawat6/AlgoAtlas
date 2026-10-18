import java.util.*;

public class Solution {
    public int jump(int[] nums) {
        int jumps = 0, curEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == curEnd) {
                jumps++;
                curEnd = farthest;
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.jump(new int[]{2, 3, 1, 1, 4}) == 2;
        assert sol.jump(new int[]{2, 3, 0, 1, 4}) == 2;
        assert sol.jump(new int[]{1}) == 0;
        assert sol.jump(new int[]{1, 2, 3}) == 2;
        System.out.println("All tests passed.");
    }
}
