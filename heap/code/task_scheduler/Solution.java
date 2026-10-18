import java.util.*;

public class Solution {
    public int leastInterval(char[] tasks, int n) {
        // Formula: (maxFreq-1)*(n+1) + countOfMaxFreq, but at least tasks.length
        int[] counts = new int[26];
        for (char t : tasks) counts[t - 'A']++;
        int maxFreq = 0;
        for (int c : counts) maxFreq = Math.max(maxFreq, c);
        int numMax = 0;
        for (int c : counts) if (c == maxFreq) numMax++;
        return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + numMax);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.leastInterval(new char[]{'A','A','A','B','B','B'}, 2) == 8;
        assert s.leastInterval(new char[]{'A','A','A','B','B','B'}, 0) == 6;
        assert s.leastInterval(new char[]{'A','A','A','A','A','A','B','C','D','E','F','G'}, 2) == 16;
        assert s.leastInterval(new char[]{'A','B','C','D','E','F'}, 2) == 6; // no idle needed
        System.out.println("All tests passed.");
    }
}
