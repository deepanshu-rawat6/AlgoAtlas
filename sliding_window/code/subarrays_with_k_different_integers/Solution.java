import java.util.*;

public class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    private int atMost(int[] nums, int limit) {
        Map<Integer,Integer> count = new HashMap<>();
        int left = 0, res = 0;
        for (int right = 0; right < nums.length; right++) {
            count.merge(nums[right], 1, Integer::sum);
            while (count.size() > limit) {
                if (count.merge(nums[left], -1, Integer::sum) == 0) count.remove(nums[left]);
                left++;
            }
            res += right - left + 1;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.subarraysWithKDistinct(new int[]{1,2,1,2,3}, 2) == 7;
        assert sol.subarraysWithKDistinct(new int[]{1,2,1,3,4}, 3) == 3;
        assert sol.subarraysWithKDistinct(new int[]{1,1,1,1}, 1) == 10;
        System.out.println("All tests passed.");
    }
}
