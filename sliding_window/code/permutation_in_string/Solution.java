import java.util.*;

public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] need = new int[26], have = new int[26];
        for (char c : s1.toCharArray()) need[c - 'a']++;
        int m = s1.length();
        for (int i = 0; i < s2.length(); i++) {
            have[s2.charAt(i) - 'a']++;
            if (i >= m) have[s2.charAt(i - m) - 'a']--;
            if (Arrays.equals(have, need)) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.checkInclusion("ab", "eidbaooo") == true;
        assert sol.checkInclusion("ab", "eidboaoo") == false;
        assert sol.checkInclusion("a", "a") == true;
        System.out.println("All tests passed.");
    }
}
