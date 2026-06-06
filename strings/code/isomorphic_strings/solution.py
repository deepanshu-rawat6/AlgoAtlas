class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Two maps enforce bijection: s->t and t->s
        s_to_t, t_to_s = {}, {}
        for cs, ct in zip(s, t):
            if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") == True
    assert sol.isIsomorphic("foo", "bar") == False
    assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("badc", "baba") == False
    assert sol.isIsomorphic("a", "a") == True
    print("All tests passed.")
