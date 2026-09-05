// LC 704: Binary Search
// Classic binary search on a sorted array; return index or -1.
// Time: O(log n), Space: O(1)
import java.util.*;

public class Solution {
    // Brute: O(n) linear scan
    public int searchBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            if (nums[i] == target) return i;
        return -1;
    }

    // Optimal: O(log n) binary search
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.search(new int[]{-1, 0, 3, 5, 9, 12}, 9) == 4 : "Test 1 failed";
        assert s.search(new int[]{-1, 0, 3, 5, 9, 12}, 2) == -1 : "Test 2 failed";
        assert s.search(new int[]{5}, 5) == 0 : "Test 3 failed";
        assert s.search(new int[]{5}, -5) == -1 : "Test 4 failed";
        assert s.search(new int[]{1, 3, 5, 7, 9, 11}, 1) == 0 : "Test 5 failed";
        assert s.search(new int[]{1, 3, 5, 7, 9, 11}, 11) == 5 : "Test 6 failed";
        System.out.println("All tests passed.");
    }
}
