import java.util.*;

// LC 271: Encode and Decode Strings — length-prefix protocol
public class Solution {
    public String encode(List<String> strs) {
        // Prefix each string with "<len>#" — handles any character including '#'
        StringBuilder sb = new StringBuilder();
        for (String s : strs) sb.append(s.length()).append('#').append(s);
        return sb.toString();
    }

    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            int j = s.indexOf('#', i);
            int len = Integer.parseInt(s.substring(i, j));
            result.add(s.substring(j + 1, j + 1 + len));
            i = j + 1 + len;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> cases = new ArrayList<>();
        cases.add(Arrays.asList("Hello", "World"));
        cases.add(Arrays.asList(""));
        cases.add(new ArrayList<>());
        cases.add(Arrays.asList("a#b", "c#d"));
        cases.add(Arrays.asList("with spaces", "and\nnewlines"));
        for (List<String> strs : cases)
            assert s.decode(s.encode(strs)).equals(strs) : "failed for " + strs;
        System.out.println("All tests passed.");
    }
}
