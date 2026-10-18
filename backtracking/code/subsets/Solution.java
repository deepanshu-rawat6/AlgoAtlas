import java.util.*;

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), nums, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] nums, int start) {
        result.add(new ArrayList<>(current));
        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r = sol.subsets(new int[]{1, 2, 3});
        r.sort((a, b) -> { for (int i = 0; i < Math.min(a.size(), b.size()); i++) if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i); return a.size() - b.size(); });
        assert r.size() == 8 : "size wrong: " + r.size();
        assert r.get(0).isEmpty() : "first should be empty";

        List<List<Integer>> r2 = sol.subsets(new int[]{0});
        assert r2.size() == 2 : "size wrong";

        System.out.println("All tests passed.");
    }
}
