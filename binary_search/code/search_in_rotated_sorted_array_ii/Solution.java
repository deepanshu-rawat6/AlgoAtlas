import java.util.*;

public class Solution {
    public boolean search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return true;
            // can't determine sorted half — shrink bounds
            if (nums[lo] == nums[mid] && nums[mid] == nums[hi]) {
                lo++;
                hi--;
            } else if (nums[lo] <= nums[mid]) {  // left half sorted
                if (nums[lo] <= target && target < nums[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else {  // right half sorted
                if (nums[mid] < target && target <= nums[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.search(new int[]{2,5,6,0,0,1,2}, 0) : "test 1 failed";
        assert !sol.search(new int[]{2,5,6,0,0,1,2}, 3) : "test 2 failed";
        assert sol.search(new int[]{1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1}, 13) : "test 3 failed";
        assert !sol.search(new int[]{1,1,1}, 2) : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
