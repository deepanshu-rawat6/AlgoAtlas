import java.util.*;

public class Solution {
    public List<String> towerOfHanoi(int n, String src, String dest, String aux) {
        List<String> moves = new ArrayList<>();
        hanoi(n, src, dest, aux, moves);
        return moves;
    }

    private void hanoi(int n, String src, String dest, String aux, List<String> moves) {
        if (n == 1) { moves.add(src + "->" + dest); return; }
        hanoi(n - 1, src, aux, dest, moves);
        moves.add(src + "->" + dest);
        hanoi(n - 1, aux, dest, src, moves);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.towerOfHanoi(2, "A", "C", "B").equals(Arrays.asList("A->B", "A->C", "B->C")) : "test failed";
        assert sol.towerOfHanoi(1, "A", "C", "B").equals(Arrays.asList("A->C")) : "test failed";
        assert sol.towerOfHanoi(3, "A", "C", "B").size() == 7 : "test failed";
        System.out.println("All tests passed.");
    }
}
