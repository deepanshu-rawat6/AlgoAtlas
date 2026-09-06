public class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        while (i < word1.length() && j < word2.length()) {
            sb.append(word1.charAt(i++));
            sb.append(word2.charAt(j++));
        }
        sb.append(word1.substring(i));
        sb.append(word2.substring(j));
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.mergeAlternately("abc", "pqr").equals("apbqcr");
        assert sol.mergeAlternately("ab", "pqrs").equals("apbqrs");
        assert sol.mergeAlternately("abcd", "pq").equals("apbqcd");
        System.out.println("All tests passed.");
    }
}
