import java.util.*;

public class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE, maxP = 0;
        for (int p : prices) {
            minPrice = Math.min(minPrice, p);
            maxP = Math.max(maxP, p - minPrice);
        }
        return maxP;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxProfit(new int[]{7,1,5,3,6,4}) == 5;
        assert sol.maxProfit(new int[]{7,6,4,3,1}) == 0;
        assert sol.maxProfit(new int[]{1,2}) == 1;
        System.out.println("All tests passed.");
    }
}
