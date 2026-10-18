import java.util.*;

public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), n, k, 1);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current,
                           int n, int k, int start) {
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }
        // prune: need at least (k - current.size()) more numbers
        for (int i = start; i <= n - (k - current.size()) + 1; i++) {
            current.add(i);
            backtrack(result, current, n, k, i + 1);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<Integer>> r1 = sol.combine(4, 2);
        assert r1.size() == 6 : "size wrong: " + r1.size();
        assert r1.contains(Arrays.asList(1, 2));
        assert r1.contains(Arrays.asList(3, 4));

        List<List<Integer>> r2 = sol.combine(1, 1);
        assert r2.equals(Collections.singletonList(Collections.singletonList(1)));

        System.out.println("All tests passed.");
    }
}
