class Solution:
    """
    ## 678. Valid Parenthesis String

    Given a string s containing '(', ')', and '*', return true if s is valid.
    '*' can be treated as '(', ')', or an empty string.

    ### Example
    ```text
    Input:  s = "(*)"
    Output: true

    Input:  s = "(*))"
    Output: true

    Input:  s = "(*())"
    Output: true
    ```

    ### Constraints
    - 1 <= s.length <= 100
    - s[i] is '(', ')' or '*'
    """

    def checkValidString_two_pass(self, s: str) -> bool:
        # O(n) time, O(1) space — two-pass left-to-right and right-to-left
        # Left pass: treat '*' as '('
        opens = 0
        for c in s:
            opens += 1 if c != ')' else -1
            if opens < 0:
                return False
        # Right pass: treat '*' as ')'
        closes = 0
        for c in reversed(s):
            closes += 1 if c != '(' else -1
            if closes < 0:
                return False
        return True

    def checkValidString(self, s: str) -> bool:
        # Track range [lo, hi] of possible open-paren counts
        # '(' increases both, ')' decreases both, '*' widens range by ±1
        # Valid if hi >= 0 throughout and lo == 0 at end
        # O(n) time, O(1) space — track range [lo, hi] of possible open counts
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1; hi += 1
            elif c == ')':
                lo -= 1; hi -= 1
            else:  # '*'
                lo -= 1; hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0


if __name__ == '__main__':
    s = Solution()
    assert s.checkValidString("(*)") == True
    assert s.checkValidString("(*))") == True
    assert s.checkValidString("(*()") == True
    assert s.checkValidString(")(") == False
    assert s.checkValidString_two_pass("(*)") == True
    assert s.checkValidString_two_pass("(*))") == True
    print("All tests passed.")
