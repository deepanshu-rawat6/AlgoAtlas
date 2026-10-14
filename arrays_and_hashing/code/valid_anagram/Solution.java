import java.util.*;

// LC 242: Valid Anagram
public class Solution {
    public boolean isAnagramSort(String s, String t) {
        // Sort both; identical iff anagram — O(n log n) time, O(1) space
        char[] a = s.toCharArray(), b = t.toCharArray();
        Arrays.sort(a); Arrays.sort(b);
        return Arrays.equals(a, b);
    }

    public boolean isAnagram(String s, String t) {
        // Increment for s, decrement for t; all zeros = anagram — O(n) time, O(1) space
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) if (c != 0) return false;
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.isAnagram("anagram", "nagaram") : "test 1";
        assert !s.isAnagram("rat", "car") : "test 2";
        assert !s.isAnagram("a", "ab") : "test 3";
        System.out.println("All tests passed.");
    }
}
