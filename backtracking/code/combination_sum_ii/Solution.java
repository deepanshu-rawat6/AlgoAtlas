import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current,
                           int[] candidates, int remaining, int start) {
        if (remaining == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            current.add(candidates[i]);
            backtrack(result, current, candidates, remaining - candidates[i], i + 1);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r1 = sol.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8);
        assert r1.size() == 4 : "size wrong: " + r1.size();
        assert r1.contains(Arrays.asList(1, 1, 6)) : "missing [1,1,6]";
        assert r1.contains(Arrays.asList(1, 7)) : "missing [1,7]";

        List<List<Integer>> r2 = sol.combinationSum2(new int[]{2, 5, 2, 1, 2}, 5);
        assert r2.size() == 2 : "size wrong";

        System.out.println("All tests passed.");
    }
}
