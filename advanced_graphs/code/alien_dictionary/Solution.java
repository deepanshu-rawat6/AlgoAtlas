import java.util.*;

public class Solution {
    // LC 269: Alien Dictionary — BFS Kahn's topological sort
    // O(C) — C = total characters across all words
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();
        for (String w : words) for (char c : w.toCharArray()) inDegree.putIfAbsent(c, 0);

        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            int minLen = Math.min(w1.length(), w2.length());
            if (w1.length() > w2.length() && w1.substring(0, minLen).equals(w2.substring(0, minLen))) return "";
            for (int j = 0; j < minLen; j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    char from = w1.charAt(j), to = w2.charAt(j);
                    adj.computeIfAbsent(from, k -> new HashSet<>());
                    if (!adj.get(from).contains(to)) {
                        adj.get(from).add(to);
                        inDegree.merge(to, 1, Integer::sum);
                    }
                    break;
                }
            }
        }

        Queue<Character> q = new LinkedList<>();
        for (char c : inDegree.keySet()) if (inDegree.get(c) == 0) q.offer(c);
        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            char c = q.poll();
            sb.append(c);
            for (char nb : adj.getOrDefault(c, Collections.emptySet())) {
                inDegree.merge(nb, -1, Integer::sum);
                if (inDegree.get(nb) == 0) q.offer(nb);
            }
        }
        return sb.length() == inDegree.size() ? sb.toString() : "";
    }

    // DFS topological sort variant
    public String alienOrderDfs(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Set<Character> chars = new HashSet<>();
        for (String w : words) for (char c : w.toCharArray()) { chars.add(c); adj.putIfAbsent(c, new HashSet<>()); }

        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            int minLen = Math.min(w1.length(), w2.length());
            if (w1.length() > w2.length() && w1.substring(0, minLen).equals(w2.substring(0, minLen))) return "";
            for (int j = 0; j < minLen; j++) {
                if (w1.charAt(j) != w2.charAt(j)) { adj.get(w1.charAt(j)).add(w2.charAt(j)); break; }
            }
        }

        Map<Character, Integer> state = new HashMap<>();
        for (char c : chars) state.put(c, 0);
        List<Character> result = new ArrayList<>();
        for (char c : chars) {
            if (state.get(c) == 0 && !dfs(c, adj, state, result)) return "";
        }
        Collections.reverse(result);
        StringBuilder sb = new StringBuilder();
        for (char c : result) sb.append(c);
        return sb.toString();
    }

    private boolean dfs(char c, Map<Character, Set<Character>> adj, Map<Character, Integer> state, List<Character> result) {
        if (state.get(c) == 1) return false;
        if (state.get(c) == 2) return true;
        state.put(c, 1);
        for (char nb : adj.getOrDefault(c, Collections.emptySet())) {
            if (!dfs(nb, adj, state, result)) return false;
        }
        state.put(c, 2);
        result.add(c);
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.alienOrder(new String[]{"wrt","wrf","er","ett","rftt"}).equals("wertf") : "test 1";
        assert s.alienOrder(new String[]{"z","x"}).equals("zx") : "test 2";
        assert s.alienOrder(new String[]{"z","x","z"}).equals("") : "test 3";

        String dfsRes = s.alienOrderDfs(new String[]{"wrt","wrf","er","ett","rftt"});
        assert dfsRes.length() == 5 : "dfs length";
        assert s.alienOrderDfs(new String[]{"z","x","z"}).equals("") : "dfs cycle";
        System.out.println("All tests passed.");
    }
}
