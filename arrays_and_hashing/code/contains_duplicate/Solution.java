// LC 217: Contains Duplicate
// Return true if any value appears at least twice in the array.
// Time: O(n), Space: O(n)
import java.util.*;

public class Solution {
    // Brute: O(n^2) time | O(1) space
    public boolean containsDuplicateBrute(int[] nums) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] == nums[j]) return true;
        return false;
    }

    // Optimal: O(n) time | O(n) space
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.containsDuplicate(new int[]{1, 2, 3, 1}) == true : "Test 1 failed";
        assert s.containsDuplicate(new int[]{1, 2, 3, 4}) == false : "Test 2 failed";
        assert s.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}) == true : "Test 3 failed";
        assert s.containsDuplicate(new int[]{1}) == false : "Test 4 failed";
        System.out.println("All tests passed.");
    }
}
