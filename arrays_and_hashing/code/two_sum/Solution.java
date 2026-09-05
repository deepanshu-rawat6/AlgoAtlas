// LC 1: Two Sum
// Return indices of two numbers that add up to target.
// Time: O(n), Space: O(n)
import java.util.*;

public class Solution {
    // Brute: O(n^2) time | O(1) space
    public int[] twoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] + nums[j] == target)
                    return new int[]{i, j};
        return new int[]{};
    }

    // Optimal: O(n) time | O(n) space
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (seen.containsKey(diff))
                return new int[]{seen.get(diff), i};
            seen.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.twoSum(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1}) : "Test 1 failed";
        assert Arrays.equals(s.twoSum(new int[]{3, 2, 4}, 6), new int[]{1, 2}) : "Test 2 failed";
        assert Arrays.equals(s.twoSum(new int[]{3, 3}, 6), new int[]{0, 1}) : "Test 3 failed";
        assert Arrays.equals(s.twoSumBrute(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1}) : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
