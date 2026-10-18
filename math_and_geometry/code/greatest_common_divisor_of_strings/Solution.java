import java.util.*;

public class Solution {
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public String gcdOfStrings(String str1, String str2) {
        // If str1+str2 == str2+str1, a GCD string exists with length gcd(len1, len2)
        // O(n) time
        if (!(str1 + str2).equals(str2 + str1)) return "";
        return str1.substring(0, gcd(str1.length(), str2.length()));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.gcdOfStrings("ABCABC", "ABC").equals("ABC");
        assert sol.gcdOfStrings("ABABAB", "ABAB").equals("AB");
        assert sol.gcdOfStrings("LEET", "CODE").equals("");
        assert sol.gcdOfStrings("A", "A").equals("A");
        System.out.println("All tests passed.");
    }
}
