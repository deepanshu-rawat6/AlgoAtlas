// LC 15: 3Sum
// Sort + fix one element + two-pointer for the other two; return unique triplets.
// Time: O(n^2), Space: O(1) excluding output
import java.util.*;

public class Solution {
    // Brute: O(n^3) + set to deduplicate
    public List<List<Integer>> threeSumBrute(int[] nums) {
        Set<List<Integer>> st = new HashSet<>();
        int n = nums.length;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> v = Arrays.asList(nums[i], nums[j], nums[k]);
                        Collections.sort(v);
                        st.add(v);
                    }
        return new ArrayList<>(st);
    }

    // Optimal: O(n^2)
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    l++; r--;
                } else if (sum < 0) l++;
                else r--;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<Integer>> res1 = s.threeSum(new int[]{-1, 0, 1, 2, -1, -4});
        assert res1.equals(Arrays.asList(Arrays.asList(-1,-1,2), Arrays.asList(-1,0,1))) : "Test 1 failed";

        List<List<Integer>> res2 = s.threeSum(new int[]{0, 1, 1});
        assert res2.isEmpty() : "Test 2 failed";

        List<List<Integer>> res3 = s.threeSum(new int[]{0, 0, 0});
        assert res3.equals(Arrays.asList(Arrays.asList(0,0,0))) : "Test 3 failed";

        List<List<Integer>> res4 = s.threeSum(new int[]{-2, 0, 0, 2, 2});
        assert res4.equals(Arrays.asList(Arrays.asList(-2,0,2))) : "Test 4 failed";

        System.out.println("All tests passed.");
    }
}
