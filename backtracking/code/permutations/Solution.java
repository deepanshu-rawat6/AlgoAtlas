import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
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
            used[i] = true;
            current.add(nums[i]);
            backtrack(result, current, nums, used);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r = sol.permute(new int[]{1, 2, 3});
        r.sort((a, b) -> { for (int i = 0; i < Math.min(a.size(), b.size()); i++) if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i); return a.size() - b.size(); });
        assert r.size() == 6 : "size wrong";
        assert r.get(0).equals(Arrays.asList(1, 2, 3));

        List<List<Integer>> r2 = sol.permute(new int[]{1});
        assert r2.equals(Collections.singletonList(Collections.singletonList(1)));

        System.out.println("All tests passed.");
    }
}
