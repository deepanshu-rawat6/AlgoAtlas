import java.util.*;

public class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, result = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.longestOnes(new int[]{1,1,1,0,0,0,1,1,1,1,0}, 2) == 6;
        assert sol.longestOnes(new int[]{0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1}, 3) == 10;
        assert sol.longestOnes(new int[]{1,1,1}, 0) == 3;
        System.out.println("All tests passed.");
    }
}
