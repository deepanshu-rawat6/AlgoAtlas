import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;
                int lo = j + 1, hi = n - 1;
                while (lo < hi) {
                    long s = (long)nums[i] + nums[j] + nums[lo] + nums[hi];
                    if (s == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[lo], nums[hi]));
                        while (lo < hi && nums[lo] == nums[lo+1]) lo++;
                        while (lo < hi && nums[hi] == nums[hi-1]) hi--;
                        lo++; hi--;
                    } else if (s < target) lo++;
                    else hi--;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.fourSum(new int[]{1,0,-1,0,-2,2}, 0).size() == 3;
        assert sol.fourSum(new int[]{2,2,2,2,2}, 8).size() == 1;
        assert sol.fourSum(new int[]{0,0,0,0}, 0).size() == 1;
        System.out.println("All tests passed.");
    }
}
