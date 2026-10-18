import java.util.*;

public class Solution {
    public String convertToTitle(int columnNumber) {
        // Base-26 conversion, 1-indexed: subtract 1 before modulo to handle A=1..Z=26
        // O(log n) time
        StringBuilder sb = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--;
            sb.append((char) ('A' + columnNumber % 26));
            columnNumber /= 26;
        }
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.convertToTitle(1).equals("A");
        assert sol.convertToTitle(26).equals("Z");
        assert sol.convertToTitle(28).equals("AB");
        assert sol.convertToTitle(701).equals("ZY");
        System.out.println("All tests passed.");
    }
}
