import java.util.*;

public class Solution {
    public boolean makesquare(int[] matchsticks) {
        int total = 0;
        for (int m : matchsticks) total += m;
        if (total % 4 != 0) return false;
        int side = total / 4;
        // Sort descending for better pruning
        Integer[] arr = new Integer[matchsticks.length];
        for (int i = 0; i < matchsticks.length; i++) arr[i] = matchsticks[i];
        Arrays.sort(arr, Collections.reverseOrder());
        if (arr[0] > side) return false;
        return backtrack(arr, new int[4], 0, side);
    }

    private boolean backtrack(Integer[] matchsticks, int[] sides, int idx, int side) {
        if (idx == matchsticks.length) {
            return sides[0] == sides[1] && sides[1] == sides[2] && sides[2] == side;
        }
        for (int i = 0; i < 4; i++) {
            if (sides[i] + matchsticks[idx] <= side) {
                sides[i] += matchsticks[idx];
                if (backtrack(matchsticks, sides, idx + 1, side)) return true;
                sides[i] -= matchsticks[idx];
                if (sides[i] == 0) break; // prune symmetric branches
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        assert sol.makesquare(new int[]{1, 1, 2, 2, 2}) : "should be true";
        assert !sol.makesquare(new int[]{3, 3, 3, 3, 4}) : "should be false";
        assert sol.makesquare(new int[]{1, 1, 1, 1}) : "should be true";

        System.out.println("All tests passed.");
    }
}
