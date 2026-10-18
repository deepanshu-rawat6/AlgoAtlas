import java.util.*;

public class Solution {
    public List<String> generateStrings(int n) {
        List<String> result = new ArrayList<>();
        backtrack("", n, result);
        Collections.sort(result);
        return result;
    }

    private void backtrack(String current, int n, List<String> result) {
        if (current.length() == n) {
            result.add(current);
            return;
        }
        backtrack(current + "0", n, result);
        if (current.isEmpty() || current.charAt(current.length() - 1) != '1') {
            backtrack(current + "1", n, result);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.generateStrings(3).equals(Arrays.asList("000", "001", "010", "100", "101")) : "test failed";
        assert sol.generateStrings(1).equals(Arrays.asList("0", "1")) : "test failed";
        for (String s : sol.generateStrings(5)) {
            assert !s.contains("11") : "consecutive 1s found: " + s;
        }
        System.out.println("All tests passed.");
    }
}
