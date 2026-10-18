import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), k, n, 1);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current,
                           int k, int remaining, int start) {
        if (current.size() == k && remaining == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (current.size() == k || remaining < 0) return;
        for (int num = start; num <= 9; num++) {
            current.add(num);
            backtrack(result, current, k, remaining - num, num + 1);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r1 = sol.combinationSum3(3, 7);
        assert r1.equals(Collections.singletonList(Arrays.asList(1, 2, 4))) : "wrong: " + r1;

        List<List<Integer>> r2 = sol.combinationSum3(3, 9);
        assert r2.size() == 3 : "size wrong: " + r2.size();
        assert r2.contains(Arrays.asList(1, 2, 6));
        assert r2.contains(Arrays.asList(1, 3, 5));
        assert r2.contains(Arrays.asList(2, 3, 4));

        assert sol.combinationSum3(4, 1).isEmpty() : "should be empty";

        System.out.println("All tests passed.");
    }
}
