import java.util.*;

public class Solution {
    // Solution IS the WordDictionary (LC 211)
    private TrieNode root = new TrieNode();

    public void addWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null)
                node.children[c - 'a'] = new TrieNode();
            node = node.children[c - 'a'];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int i) {
        if (i == word.length()) return node.isEnd;
        char c = word.charAt(i);
        if (c == '.') {
            for (TrieNode child : node.children)
                if (child != null && dfs(child, word, i + 1)) return true;
            return false;
        }
        if (node.children[c - 'a'] == null) return false;
        return dfs(node.children[c - 'a'], word, i + 1);
    }

    public static void main(String[] args) {
        Solution wd = new Solution();
        wd.addWord("bad");
        wd.addWord("dad");
        wd.addWord("mad");
        assert !wd.search("pad") : "pad";
        assert  wd.search("bad") : "bad";
        assert  wd.search(".ad") : ".ad";
        assert  wd.search("b..") : "b..";
        System.out.println("All tests passed.");
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
