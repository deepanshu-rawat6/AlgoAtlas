import java.util.*;

public class Solution {
    public int rangeBitwiseAndShift(int left, int right) {
        // Right-shift both until equal: finds common bit prefix
        int shift = 0;
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left << shift;
    }

    public int rangeBitwiseAnd(int left, int right) {
        // Brian Kernighan: strip lowest set bit of right until right <= left
        while (right > left) right &= right - 1;
        return right;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.rangeBitwiseAndShift(5, 7) == 4;
        assert sol.rangeBitwiseAndShift(0, 0) == 0;
        assert sol.rangeBitwiseAndShift(1, 2147483647) == 0;

        assert sol.rangeBitwiseAnd(5, 7) == 4;
        assert sol.rangeBitwiseAnd(0, 0) == 0;
        assert sol.rangeBitwiseAnd(1, 2147483647) == 0;

        System.out.println("All tests passed.");
    }
}
