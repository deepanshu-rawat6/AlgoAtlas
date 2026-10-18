import java.util.*;

public class Solution {
    public int[] plusOne(int[] digits) {
        // Add 1 from the last digit; propagate carry leftward — O(n)
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(sol.plusOne(new int[]{1, 2, 3}), new int[]{1, 2, 4});
        assert Arrays.equals(sol.plusOne(new int[]{9}), new int[]{1, 0});
        assert Arrays.equals(sol.plusOne(new int[]{9, 9}), new int[]{1, 0, 0});
        assert Arrays.equals(sol.plusOne(new int[]{4, 3, 2, 1}), new int[]{4, 3, 2, 2});
        System.out.println("All tests passed.");
    }
}
