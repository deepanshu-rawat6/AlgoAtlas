import java.util.*;

public class Solution {
    public String multiply(String num1, String num2) {
        // Grade-school digit-by-digit multiplication; digit i*j maps to pos[i+j], pos[i+j+1]
        // O(m*n) time
        if (num1.equals("0") || num2.equals("0")) return "0";
        int m = num1.length(), n = num2.length();
        int[] pos = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int p1 = i + j, p2 = i + j + 1;
                int total = mul + pos[p2];
                pos[p2] = total % 10;
                pos[p1] += total / 10;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int d : pos) if (!(sb.length() == 0 && d == 0)) sb.append(d);
        return sb.length() == 0 ? "0" : sb.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.multiply("2", "3").equals("6");
        assert sol.multiply("123", "456").equals("56088");
        assert sol.multiply("0", "456").equals("0");
        assert sol.multiply("99", "99").equals("9801");
        System.out.println("All tests passed.");
    }
}
