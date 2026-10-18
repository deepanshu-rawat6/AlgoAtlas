import java.util.*;

public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<Integer, List<String>> memo = new HashMap<>();
        return backtrack(s, wordSet, memo, 0);
    }

    private List<String> backtrack(String s, Set<String> wordSet,
                                    Map<Integer, List<String>> memo, int start) {
        if (memo.containsKey(start)) return memo.get(start);
        if (start == s.length()) return Collections.singletonList("");
        List<String> sentences = new ArrayList<>();
        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);
            if (wordSet.contains(word)) {
                for (String rest : backtrack(s, wordSet, memo, end)) {
                    sentences.add(word + (rest.isEmpty() ? "" : ' ' + rest));
                }
            }
        }
        memo.put(start, sentences);
        return sentences;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<String> r1 = sol.wordBreak("catsanddog", Arrays.asList("cat","cats","and","sand","dog"));
        Collections.sort(r1);
        assert r1.equals(Arrays.asList("cat sand dog", "cats and dog")) : "wrong: " + r1;

        List<String> r2 = sol.wordBreak("catsandog", Arrays.asList("cats","dog","sand","and","cat"));
        assert r2.isEmpty() : "should be empty";

        System.out.println("All tests passed.");
    }
}
