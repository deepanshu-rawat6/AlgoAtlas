import java.util.*;

public class Solution {
    public int numberOfSubstrings(String s) {
        int[] count = new int[3];
        int left = 0, result = 0;
        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'a']++;
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                count[s.charAt(left++) - 'a']--;
            }
            result += left;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numberOfSubstrings("abcabc") == 10;
        assert sol.numberOfSubstrings("aaacb") == 3;
        assert sol.numberOfSubstrings("abc") == 1;
        System.out.println("All tests passed.");
    }
}
