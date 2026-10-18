import java.util.*;

public class Solution {
    public int subsetXORSum(int[] nums) {
        // Math shortcut: OR of all elements << (n-1)
        int orAll = 0;
        for (int x : nums) orAll |= x;
        return orAll << (nums.length - 1);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.subsetXORSum(new int[]{1, 3}) == 6 : "test failed";
        assert sol.subsetXORSum(new int[]{5, 1, 6}) == 28 : "test failed";
        assert sol.subsetXORSum(new int[]{3, 4, 5, 6, 7, 8}) == 480 : "test failed";
        System.out.println("All tests passed.");
    }
}
