import java.util.*;

public class Solution {
    // Solution IS the Trie (LC 208)
    private TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null)
                node.children[c - 'a'] = new TrieNode();
            node = node.children[c - 'a'];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return node.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return true;
    }

    public static void main(String[] args) {
        Solution trie = new Solution();
        trie.insert("apple");
        assert trie.search("apple")    : "search apple";
        assert !trie.search("app")     : "search app before insert";
        assert trie.startsWith("app")  : "startsWith app";
        trie.insert("app");
        assert trie.search("app")      : "search app after insert";
        System.out.println("All tests passed.");
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
