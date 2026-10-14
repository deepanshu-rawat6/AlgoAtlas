import java.util.*;

// LC 205: Isomorphic Strings — bijection via two maps O(n)
public class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> sToT = new HashMap<>(), tToS = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char cs = s.charAt(i), ct = t.charAt(i);
            if (sToT.getOrDefault(cs, ct) != ct || tToS.getOrDefault(ct, cs) != cs)
                return false;
            sToT.put(cs, ct);
            tToS.put(ct, cs);
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.isIsomorphic("egg", "add") : "test 1";
        assert !s.isIsomorphic("foo", "bar") : "test 2";
        assert s.isIsomorphic("paper", "title") : "test 3";
        assert !s.isIsomorphic("badc", "baba") : "test 4";
        assert s.isIsomorphic("a", "a") : "test 5";
        System.out.println("All tests passed.");
    }
}
