import java.util.*;

public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            total += diff;
            tank += diff;
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start : -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.canCompleteCircuit(new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}) == 3;
        assert sol.canCompleteCircuit(new int[]{2, 3, 4}, new int[]{3, 4, 3}) == -1;
        assert sol.canCompleteCircuit(new int[]{5}, new int[]{4}) == 0;
        assert sol.canCompleteCircuit(new int[]{3, 1, 1}, new int[]{1, 2, 2}) == 0;
        System.out.println("All tests passed.");
    }
}
