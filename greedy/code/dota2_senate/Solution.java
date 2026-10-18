import java.util.*;

public class Solution {
    public String predictPartyVictory(String senate) {
        Deque<Integer> radiant = new ArrayDeque<>();
        Deque<Integer> dire = new ArrayDeque<>();
        int n = senate.length();
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R') radiant.add(i);
            else dire.add(i);
        }
        while (!radiant.isEmpty() && !dire.isEmpty()) {
            int r = radiant.poll(), d = dire.poll();
            if (r < d) radiant.add(r + n);
            else dire.add(d + n);
        }
        return radiant.isEmpty() ? "Dire" : "Radiant";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.predictPartyVictory("RD").equals("Radiant");
        assert sol.predictPartyVictory("RDD").equals("Dire");
        assert sol.predictPartyVictory("R").equals("Radiant");
        assert sol.predictPartyVictory("DDRRR").equals("Dire");
        System.out.println("All tests passed.");
    }
}
