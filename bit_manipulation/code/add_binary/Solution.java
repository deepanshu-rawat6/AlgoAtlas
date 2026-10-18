import java.util.*;

public class Solution {
    public String addBinary(String a, String b) {
        // Simulate binary addition from right to left with carry
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        StringBuilder sb = new StringBuilder();
        while (i >= 0 || j >= 0 || carry > 0) {
            int total = carry;
            if (i >= 0) total += a.charAt(i--) - '0';
            if (j >= 0) total += b.charAt(j--) - '0';
            sb.append(total % 2);
            carry = total / 2;
        }
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.addBinary("11", "1").equals("100");
        assert sol.addBinary("1010", "1011").equals("10101");
        assert sol.addBinary("0", "0").equals("0");
        assert sol.addBinary("1", "111").equals("1000");
        System.out.println("All tests passed.");
    }
}
