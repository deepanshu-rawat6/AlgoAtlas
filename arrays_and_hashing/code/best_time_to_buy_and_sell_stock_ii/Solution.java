import java.util.*;

// LC 122: Best Time to Buy and Sell Stock II
public class Solution {
    public int maxProfitBrute(int[] prices) {
        // O(2^n) recursive DFS — illustrates decision tree
        return dfs(prices, 0, false);
    }

    private int dfs(int[] prices, int i, boolean holding) {
        if (i == prices.length) return 0;
        int best = dfs(prices, i + 1, holding);
        if (holding) best = Math.max(best, prices[i] + dfs(prices, i + 1, false));
        else         best = Math.max(best, -prices[i] + dfs(prices, i + 1, true));
        return best;
    }

    public int maxProfit(int[] prices) {
        // Greedy: capture every upward price movement — O(n) time, O(1) space
        int profit = 0;
        for (int i = 1; i < prices.length; i++)
            profit += Math.max(prices[i] - prices[i - 1], 0);
        return profit;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.maxProfit(new int[]{7,1,5,3,6,4}) == 7 : "test 1";
        assert s.maxProfit(new int[]{1,2,3,4,5}) == 4 : "test 2";
        assert s.maxProfit(new int[]{7,6,4,3,1}) == 0 : "test 3";
        assert s.maxProfit(new int[]{1}) == 0 : "test 4";
        System.out.println("All tests passed.");
    }
}
