from math import ceil


class Solution:
    def countRev(self, s: str) -> int:
        """
        Approach 1: Stack-based O(n) time, O(n) space
        Remove matched {} pairs; remaining is }}}...{{{
        Answer: ceil(close/2) + ceil(open/2)
        """
        if len(s) % 2 != 0:
            return -1  # odd length can never be balanced

        stack = []
        for ch in s:
            if ch == '{':
                stack.append(ch)
            else:  # ch == '}'
                if stack and stack[-1] == '{':
                    stack.pop()  # matched pair, cancel out
                else:
                    stack.append(ch)

        # remaining stack is all }'s followed by all {'s
        close = sum(1 for c in stack if c == '}')
        open_ = sum(1 for c in stack if c == '{')
        return ceil(close / 2) + ceil(open_ / 2)


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.countRev("}{") == 2       # }{ -> {{ (1 rev) -> {} (1 rev)
    assert sol.countRev("{{}}") == 0     # already balanced
    assert sol.countRev("{{{") == -1     # odd length
    assert sol.countRev("}}{{") == 2     # }}{{ -> 2 reversals
    assert sol.countRev("}{{}}{") == 2
    print("All tests passed")
