public class Solution {
    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while (l < r) {
            char tmp = s[l]; s[l] = s[r]; s[r] = tmp;
            l++; r--;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        char[] a = {'h','e','l','l','o'};
        sol.reverseString(a);
        assert new String(a).equals("olleh");
        char[] b = {'H','a','n','n','a','h'};
        sol.reverseString(b);
        assert new String(b).equals("hannaH");
        char[] c = {'a'};
        sol.reverseString(c);
        assert c[0] == 'a';
        System.out.println("All tests passed.");
    }
}
