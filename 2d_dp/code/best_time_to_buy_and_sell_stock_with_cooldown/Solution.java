import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        // States: hold, sold (just sold, next day cooldown), rest (cooldown/idle)
        // hold = max(hold, rest - price); sold = hold + price; rest = max(rest, sold)
        // Time: O(n), Space: O(1)
        int hold = Integer.MIN_VALUE, sold = 0, rest = 0;
        for (int p : prices) {
            int prevHold = hold, prevSold = sold, prevRest = rest;
            hold = Math.max(prevHold, prevRest - p);
            sold = prevHold + p;
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxProfit(new int[]{1,2,3,0,2}) == 3 : "test 1 failed";
        assert sol.maxProfit(new int[]{1}) == 0 : "test 2 failed";
        assert sol.maxProfit(new int[]{2,1}) == 0 : "test 3 failed";
        assert sol.maxProfit(new int[]{1,2}) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
