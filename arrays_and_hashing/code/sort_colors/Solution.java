import java.util.*;

// LC 75: Sort Colors
public class Solution {
    public void sortColorsCounting(int[] nums) {
        // Count 0s/1s/2s then overwrite — O(n) time, O(1) space, two-pass
        int[] count = new int[3];
        for (int n : nums) count[n]++;
        int i = 0;
        for (int val = 0; val < 3; val++)
            for (int c = 0; c < count[val]; c++) nums[i++] = val;
    }

    public void sortColors(int[] nums) {
        // Dutch National Flag — O(n) time, O(1) space, one-pass
        int lo = 0, mid = 0, hi = nums.length - 1;
        while (mid <= hi) {
            if (nums[mid] == 0) {
                int tmp = nums[lo]; nums[lo] = nums[mid]; nums[mid] = tmp;
                lo++; mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int tmp = nums[mid]; nums[mid] = nums[hi]; nums[hi] = tmp;
                hi--;
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums;

        nums = new int[]{2,0,2,1,1,0};
        s.sortColors(nums);
        assert Arrays.equals(nums, new int[]{0,0,1,1,2,2}) : "test 1";

        nums = new int[]{2,0,1};
        s.sortColors(nums);
        assert Arrays.equals(nums, new int[]{0,1,2}) : "test 2";

        nums = new int[]{0};
        s.sortColors(nums);
        assert Arrays.equals(nums, new int[]{0}) : "test 3";

        System.out.println("All tests passed.");
    }
}
