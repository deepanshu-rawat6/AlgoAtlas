import java.util.*;

public class Solution {
    // Net trust score: +1 for being trusted, -1 for trusting; judge has score n-1
    public int findJudge(int n, int[][] trust) {
        int[] score = new int[n + 1];
        for (int[] t : trust) { score[t[0]]--; score[t[1]]++; }
        for (int i = 1; i <= n; i++) if (score[i] == n - 1) return i;
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findJudge(2, new int[][]{{1,2}}) == 2 : "test 1";
        assert s.findJudge(3, new int[][]{{1,3},{2,3}}) == 3 : "test 2";
        assert s.findJudge(3, new int[][]{{1,3},{2,3},{3,1}}) == -1 : "test 3";
        assert s.findJudge(1, new int[0][]) == 1 : "test 4";
        System.out.println("All tests passed.");
    }
}
