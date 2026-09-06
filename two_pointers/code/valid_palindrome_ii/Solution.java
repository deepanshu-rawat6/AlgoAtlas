public class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return isPalin(s, l+1, r) || isPalin(s, l, r-1);
            }
            l++; r--;
        }
        return true;
    }

    private boolean isPalin(String s, int l, int r) {
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.validPalindrome("aba") == true;
        assert sol.validPalindrome("abca") == true;
        assert sol.validPalindrome("abc") == false;
        assert sol.validPalindrome("deeee") == true;
        System.out.println("All tests passed.");
    }
}
