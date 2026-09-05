// LC 33: Search in Rotated Sorted Array
// Binary search on rotated sorted array — determine which half is sorted.
// Time: O(log n), Space: O(1)
import java.util.*;

public class Solution {
    // Brute: O(n) linear scan
    public int searchBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            if (nums[i] == target) return i;
        return -1;
    }

    // Optimal: O(log n)
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[lo] <= nums[mid]) {
                if (nums[lo] <= target && target < nums[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 0) == 4 : "Test 1 failed";
        assert s.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 3) == -1 : "Test 2 failed";
        assert s.search(new int[]{1}, 0) == -1 : "Test 3 failed";
        assert s.search(new int[]{1}, 1) == 0 : "Test 4 failed";
        assert s.search(new int[]{3, 1}, 1) == 1 : "Test 5 failed";
        assert s.search(new int[]{3, 1}, 3) == 0 : "Test 6 failed";
        System.out.println("All tests passed.");
    }
}
