import java.util.*;

public class Solution {
    public List<List<Integer>> powerSet(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        recurse(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void recurse(int[] nums, int idx, List<Integer> current, List<List<Integer>> result) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        recurse(nums, idx + 1, current, result);
        current.add(nums[idx]);
        recurse(nums, idx + 1, current, result);
        current.remove(current.size() - 1);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<List<Integer>> result = sol.powerSet(new int[]{1, 2, 3});
        assert result.size() == 8 : "test failed";
        assert result.contains(new ArrayList<>()) : "test failed";
        assert result.contains(Arrays.asList(1, 2, 3)) : "test failed";
        assert sol.powerSet(new int[]{1}).size() == 2 : "test failed";
        assert sol.powerSet(new int[]{}).equals(Arrays.asList(new ArrayList<>())) : "test failed";
        System.out.println("All tests passed.");
    }
}
