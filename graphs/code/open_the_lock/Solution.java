import java.util.*;

public class Solution {
    // Standard BFS
    public int openLockBfs(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;
        Set<String> visited = new HashSet<>();
        Queue<String> q = new ArrayDeque<>();
        q.add("0000"); visited.add("0000");
        int turns = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String state = q.poll();
                if (state.equals(target)) return turns;
                for (String nb : neighbors(state)) {
                    if (!visited.contains(nb) && !dead.contains(nb)) {
                        visited.add(nb); q.add(nb);
                    }
                }
            }
            turns++;
        }
        return -1;
    }

    // Bidirectional BFS
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;
        if (target.equals("0000")) return 0;
        Set<String> front = new HashSet<>(), back = new HashSet<>(), visited = new HashSet<>();
        front.add("0000"); back.add(target);
        visited.add("0000"); visited.add(target);
        int turns = 0;
        while (!front.isEmpty() && !back.isEmpty()) {
            if (front.size() > back.size()) { Set<String> t = front; front = back; back = t; }
            turns++;
            Set<String> next = new HashSet<>();
            for (String state : front) {
                for (String nb : neighbors(state)) {
                    if (dead.contains(nb)) continue;
                    if (back.contains(nb)) return turns;
                    if (visited.add(nb)) next.add(nb);
                }
            }
            front = next;
        }
        return -1;
    }

    private List<String> neighbors(String state) {
        List<String> result = new ArrayList<>();
        char[] arr = state.toCharArray();
        for (int i = 0; i < 4; i++) {
            char orig = arr[i];
            arr[i] = (char)((orig - '0' + 1) % 10 + '0');
            result.add(new String(arr));
            arr[i] = (char)((orig - '0' + 9) % 10 + '0');
            result.add(new String(arr));
            arr[i] = orig;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.openLockBfs(new String[]{"0201","0101","0102","1212","2002"}, "0202") == 6 : "test 1";
        assert s.openLockBfs(new String[]{"8888"}, "0009") == 1 : "test 2";
        assert s.openLockBfs(new String[]{"8887","8889","8878","8898","8788","8988","7888","9888"}, "8888") == -1 : "test 3";
        assert s.openLock(new String[]{"0201","0101","0102","1212","2002"}, "0202") == 6 : "test 4";
        System.out.println("All tests passed.");
    }
}
