import java.util.*;

public class Solution {
    // Standard BFS
    public int ladderLengthBfs(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;
        Queue<String> q = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        q.add(beginWord); visited.add(beginWord);
        int length = 1;
        while (!q.isEmpty()) {
            length++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String word = q.poll();
                char[] arr = word.toCharArray();
                for (int j = 0; j < arr.length; j++) {
                    char orig = arr[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) continue;
                        arr[j] = c;
                        String next = new String(arr);
                        if (next.equals(endWord)) return length;
                        if (wordSet.contains(next) && visited.add(next)) q.add(next);
                    }
                    arr[j] = orig;
                }
            }
        }
        return 0;
    }

    // Bidirectional BFS
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;
        Set<String> front = new HashSet<>(), back = new HashSet<>(), visited = new HashSet<>();
        front.add(beginWord); back.add(endWord);
        visited.add(beginWord); visited.add(endWord);
        int length = 1;
        while (!front.isEmpty() && !back.isEmpty()) {
            if (front.size() > back.size()) { Set<String> t = front; front = back; back = t; }
            length++;
            Set<String> next = new HashSet<>();
            for (String word : front) {
                char[] arr = word.toCharArray();
                for (int j = 0; j < arr.length; j++) {
                    char orig = arr[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) continue;
                        arr[j] = c;
                        String nw = new String(arr);
                        if (back.contains(nw)) return length;
                        if (wordSet.contains(nw) && visited.add(nw)) next.add(nw);
                    }
                    arr[j] = orig;
                }
            }
            front = next;
        }
        return 0;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> wl = Arrays.asList("hot","dot","dog","lot","log","cog");
        assert s.ladderLengthBfs("hit", "cog", wl) == 5 : "test 1";
        assert s.ladderLengthBfs("hit", "cog", Arrays.asList("hot","dot","dog","lot","log")) == 0 : "test 2";
        assert s.ladderLength("hit", "cog", wl) == 5 : "test 3";
        assert s.ladderLength("hit", "cog", Arrays.asList("hot","dot","dog","lot","log")) == 0 : "test 4";
        System.out.println("All tests passed.");
    }
}
