import java.util.*;

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(result, new ArrayList<>(), nums, used);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current,
                           int[] nums, boolean[] used) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            current.add(nums[i]);
            backtrack(result, current, nums, used);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r = sol.permuteUnique(new int[]{1, 1, 2});
        assert r.size() == 3 : "size wrong: " + r.size();
        assert r.contains(Arrays.asList(1, 1, 2));
        assert r.contains(Arrays.asList(1, 2, 1));
        assert r.contains(Arrays.asList(2, 1, 1));

        assert sol.permuteUnique(new int[]{1, 2, 3}).size() == 6 : "size wrong";

        System.out.println("All tests passed.");
    }
}
