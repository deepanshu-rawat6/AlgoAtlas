import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
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
            current.add(candidates[i]);
            backtrack(result, current, candidates, remaining - candidates[i], i);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r1 = sol.combinationSum(new int[]{2, 3, 6, 7}, 7);
        r1.forEach(Collections::sort);
        r1.sort(Comparator.comparingInt(a -> a.get(0)));
        assert r1.size() == 2 : "size wrong";
        assert r1.contains(Arrays.asList(2, 2, 3)) : "missing [2,2,3]";
        assert r1.contains(Arrays.asList(7)) : "missing [7]";

        List<List<Integer>> r2 = sol.combinationSum(new int[]{2}, 1);
        assert r2.isEmpty() : "should be empty";

        System.out.println("All tests passed.");
    }
}
