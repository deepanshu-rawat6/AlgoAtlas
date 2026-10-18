import java.util.*;

public class Solution {
    public int kthGrammar(int n, int k) {
        if (n == 1 && k == 1) return 0;
        int mid = 1 << (n - 2); // 2^(n-2)
        if (k <= mid) return kthGrammar(n - 1, k);
        return kthGrammar(n - 1, k - mid) ^ 1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.kthGrammar(1, 1) == 0 : "test failed";
        assert sol.kthGrammar(2, 1) == 0 : "test failed";
        assert sol.kthGrammar(2, 2) == 1 : "test failed";
        assert sol.kthGrammar(4, 5) == 1 : "test failed";
        System.out.println("All tests passed.");
    }
}
