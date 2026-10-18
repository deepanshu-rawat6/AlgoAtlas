import java.util.*;

public class Solution {
    public int subsetXORSum(int[] nums) {
        int orAll = 0;
        for (int x : nums) orAll |= x;
        return orAll * (1 << (nums.length - 1));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.subsetXORSum(new int[]{1, 3}) == 6 : "wrong for [1,3]";
        assert sol.subsetXORSum(new int[]{5, 1, 6}) == 28 : "wrong for [5,1,6]";
        assert sol.subsetXORSum(new int[]{3, 4, 5, 6, 7, 8}) == 480 : "wrong for longer";

        System.out.println("All tests passed.");
    }
}
