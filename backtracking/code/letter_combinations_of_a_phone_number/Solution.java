import java.util.*;

public class Solution {
    private static final Map<Character, String> PHONE = new HashMap<>();
    static {
        PHONE.put('2', "abc"); PHONE.put('3', "def"); PHONE.put('4', "ghi");
        PHONE.put('5', "jkl"); PHONE.put('6', "mno"); PHONE.put('7', "pqrs");
        PHONE.put('8', "tuv"); PHONE.put('9', "wxyz");
    }

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();
        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), digits, 0);
        return result;
    }

    private void backtrack(List<String> result, StringBuilder current, String digits, int idx) {
        if (idx == digits.length()) {
            result.add(current.toString());
            return;
        }
        for (char ch : PHONE.get(digits.charAt(idx)).toCharArray()) {
            current.append(ch);
            backtrack(result, current, digits, idx + 1);
            current.deleteCharAt(current.length() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<String> r = sol.letterCombinations("23");
        Collections.sort(r);
        List<String> expected = Arrays.asList("ad","ae","af","bd","be","bf","cd","ce","cf");
        Collections.sort(expected);
        assert r.equals(expected) : "wrong: " + r;

        assert sol.letterCombinations("").isEmpty() : "should be empty";

        List<String> r2 = sol.letterCombinations("2");
        Collections.sort(r2);
        assert r2.equals(Arrays.asList("a","b","c")) : "wrong: " + r2;

        System.out.println("All tests passed.");
    }
}
