import java.util.*;

public class Solution {
    public int searchInsert(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return lo;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.searchInsert(new int[]{1,3,5,6}, 5) == 2 : "test 1 failed";
        assert sol.searchInsert(new int[]{1,3,5,6}, 2) == 1 : "test 2 failed";
        assert sol.searchInsert(new int[]{1,3,5,6}, 7) == 4 : "test 3 failed";
        assert sol.searchInsert(new int[]{1,3,5,6}, 0) == 0 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
