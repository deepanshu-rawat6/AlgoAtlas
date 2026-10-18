import java.util.*;

public class Solution {
    public int missingNumberSum(int[] nums) {
        // Expected sum minus actual sum
        int n = nums.length, sum = 0;
        for (int x : nums) sum += x;
        return n * (n + 1) / 2 - sum;
    }

    public int missingNumber(int[] nums) {
        // XOR all indices 0..n with all values; pairs cancel, leaving the missing number
        int result = nums.length;
        for (int i = 0; i < nums.length; i++) result ^= i ^ nums[i];
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.missingNumberSum(new int[]{3, 0, 1}) == 2;
        assert sol.missingNumberSum(new int[]{0, 1}) == 2;
        assert sol.missingNumberSum(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}) == 8;

        assert sol.missingNumber(new int[]{3, 0, 1}) == 2;
        assert sol.missingNumber(new int[]{0, 1}) == 2;
        assert sol.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}) == 8;

        System.out.println("All tests passed.");
    }
}
