import java.util.*;

public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), nums, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] nums, int start) {
        result.add(new ArrayList<>(current));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            current.add(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r = sol.subsetsWithDup(new int[]{1, 2, 2});
        assert r.size() == 6 : "size wrong: " + r.size();
        assert r.contains(Arrays.asList(1, 2, 2));
        assert r.contains(Arrays.asList(2, 2));

        List<List<Integer>> r2 = sol.subsetsWithDup(new int[]{0});
        assert r2.size() == 2 : "size wrong";

        System.out.println("All tests passed.");
    }
}
