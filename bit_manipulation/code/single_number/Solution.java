import java.util.*;

public class Solution {
    public int singleNumberSet(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) seen.remove(n);
        }
        return seen.iterator().next();
    }

    public int singleNumber(int[] nums) {
        // XOR all numbers: pairs cancel (a^a=0), leaving the single element
        int result = 0;
        for (int n : nums) result ^= n;
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.singleNumberSet(new int[]{2, 2, 1}) == 1;
        assert sol.singleNumberSet(new int[]{4, 1, 2, 1, 2}) == 4;
        assert sol.singleNumberSet(new int[]{1}) == 1;

        assert sol.singleNumber(new int[]{2, 2, 1}) == 1;
        assert sol.singleNumber(new int[]{4, 1, 2, 1, 2}) == 4;
        assert sol.singleNumber(new int[]{1}) == 1;

        System.out.println("All tests passed.");
    }
}
