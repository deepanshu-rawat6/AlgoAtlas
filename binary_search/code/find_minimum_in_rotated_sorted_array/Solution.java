// LC 153: Find Minimum in Rotated Sorted Array
// Binary search to find the pivot (minimum element).
// Time: O(log n), Space: O(1)
import java.util.*;

public class Solution {
    // Brute: O(n) linear scan
    public int findMinBrute(int[] nums) {
        int min = nums[0];
        for (int n : nums) min = Math.min(min, n);
        return min;
    }

    // Optimal: O(log n)
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
        }
        return nums[lo];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findMin(new int[]{3, 4, 5, 1, 2}) == 1 : "Test 1 failed";
        assert s.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}) == 0 : "Test 2 failed";
        assert s.findMin(new int[]{11, 13, 15, 17}) == 11 : "Test 3 failed";
        assert s.findMin(new int[]{2, 1}) == 1 : "Test 4 failed";
        assert s.findMin(new int[]{1}) == 1 : "Test 5 failed";
        System.out.println("All tests passed.");
    }
}
