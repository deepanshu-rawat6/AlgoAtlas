import java.util.*;

public class Solution {
    // LC 332: Reconstruct Itinerary
    // Hierholzer's iterative Eulerian path; TreeMap keeps lex order, poll gives min — O(E log E)
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, TreeMap<String, Integer>> graph = new HashMap<>();
        for (List<String> t : tickets) {
            graph.computeIfAbsent(t.get(0), k -> new TreeMap<>()).merge(t.get(1), 1, Integer::sum);
        }

        Deque<String> stack = new ArrayDeque<>();
        List<String> result = new ArrayList<>();
        stack.push("JFK");

        while (!stack.isEmpty()) {
            String airport = stack.peek();
            TreeMap<String, Integer> dests = graph.get(airport);
            if (dests == null || dests.isEmpty()) {
                result.add(stack.pop());
            } else {
                String next = dests.firstKey();
                int cnt = dests.get(next);
                if (cnt == 1) dests.remove(next); else dests.put(next, cnt - 1);
                stack.push(next);
            }
        }
        Collections.reverse(result);
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findItinerary(List.of(List.of("MUC","LHR"),List.of("JFK","MUC"),List.of("SFO","SJC"),List.of("LHR","SFO")))
                .equals(List.of("JFK","MUC","LHR","SFO","SJC")) : "t1";
        assert s.findItinerary(List.of(List.of("JFK","SFO"),List.of("JFK","ATL"),List.of("SFO","ATL"),List.of("ATL","JFK"),List.of("ATL","SFO")))
                .equals(List.of("JFK","ATL","JFK","SFO","ATL","SFO")) : "t2";
        System.out.println("All tests passed.");
    }
}
