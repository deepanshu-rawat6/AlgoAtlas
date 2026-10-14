import java.util.*;

public class Solution {
    // BFS to build parent map, DFS to backtrack all shortest paths
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return new ArrayList<>();

        Map<String, Set<String>> parents = new HashMap<>();
        Set<String> currentLayer = new HashSet<>();
        currentLayer.add(beginWord);
        boolean found = false;

        while (!currentLayer.isEmpty() && !found) {
            wordSet.removeAll(currentLayer);
            Set<String> nextLayer = new HashSet<>();
            for (String word : currentLayer) {
                char[] arr = word.toCharArray();
                for (int i = 0; i < arr.length; i++) {
                    char orig = arr[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) continue;
                        arr[i] = c;
                        String nw = new String(arr);
                        if (wordSet.contains(nw)) {
                            nextLayer.add(nw);
                            parents.computeIfAbsent(nw, k -> new HashSet<>()).add(word);
                            if (nw.equals(endWord)) found = true;
                        }
                    }
                    arr[i] = orig;
                }
            }
            currentLayer = nextLayer;
        }

        if (!found) return new ArrayList<>();
        List<List<String>> result = new ArrayList<>();
        dfs(parents, result, new LinkedList<>(Arrays.asList(endWord)), endWord, beginWord);
        return result;
    }

    private void dfs(Map<String, Set<String>> parents, List<List<String>> result,
                     LinkedList<String> path, String word, String beginWord) {
        if (word.equals(beginWord)) {
            result.add(new ArrayList<>(path)); // path is already beginWord→endWord via addFirst
            return;
        }
        if (!parents.containsKey(word)) return;
        for (String parent : parents.get(word)) {
            path.addFirst(parent);
            dfs(parents, result, path, parent, beginWord);
            path.removeFirst();
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> result = s.findLadders("hit", "cog",
            Arrays.asList("hot","dot","dog","lot","log","cog"));
        List<List<String>> expected = Arrays.asList(
            Arrays.asList("hit","hot","dot","dog","cog"),
            Arrays.asList("hit","hot","lot","log","cog")
        );
        List<List<String>> sortedResult = new ArrayList<>(result);
        sortedResult.sort(Comparator.comparing(Object::toString));
        List<List<String>> sortedExpected = new ArrayList<>(expected);
        sortedExpected.sort(Comparator.comparing(Object::toString));
        assert sortedResult.equals(sortedExpected) : "test 1";
        assert s.findLadders("hit", "cog", Arrays.asList("hot","dot","dog","lot","log")).isEmpty() : "test 2";
        System.out.println("All tests passed.");
    }
}
