import java.util.*;

public class Solution {
    // Space-optimized — O(n) time, O(1) space
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int i = 2; i <= cost.length; i++) {
            int c = Math.min(b + cost[i - 1], a + cost[i - 2]);
            a = b;
            b = c;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minCostClimbingStairs(new int[]{10, 15, 20}) == 15 : "[10,15,20]";
        assert sol.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}) == 6 : "long";
        assert sol.minCostClimbingStairs(new int[]{0, 0}) == 0 : "zeros";
        assert sol.minCostClimbingStairs(new int[]{1, 2}) == 1 : "two steps";
        System.out.println("All tests passed.");
    }
}
