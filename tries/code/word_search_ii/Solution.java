import java.util.*;

public class Solution {
    // LC 212: Word Search II
    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                if (node.children[c - 'a'] == null)
                    node.children[c - 'a'] = new TrieNode();
                node = node.children[c - 'a'];
            }
            node.word = w;
        }

        List<String> result = new ArrayList<>();
        int m = board.length, n = board[0].length;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                dfs(board, r, c, root, result);
        return result;
    }

    private void dfs(char[][] board, int r, int c, TrieNode node, List<String> result) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length) return;
        char ch = board[r][c];
        if (ch == '#' || node.children[ch - 'a'] == null) return;
        node = node.children[ch - 'a'];
        if (node.word != null) {
            result.add(node.word);
            node.word = null; // avoid duplicates
        }
        board[r][c] = '#';
        dfs(board, r + 1, c, node, result);
        dfs(board, r - 1, c, node, result);
        dfs(board, r, c + 1, node, result);
        dfs(board, r, c - 1, node, result);
        board[r][c] = ch;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] board1 = {
            {'o','a','a','n'},
            {'e','t','a','e'},
            {'i','h','k','r'},
            {'i','f','l','v'}
        };
        List<String> r1 = sol.findWords(board1, new String[]{"oath","pea","eat","rain"});
        Collections.sort(r1);
        assert r1.equals(Arrays.asList("eat","oath")) : r1;

        char[][] board2 = {{'a','b'},{'c','d'}};
        assert sol.findWords(board2, new String[]{"abcb"}).isEmpty();

        System.out.println("All tests passed.");
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    String word; // non-null if end of a word
}
