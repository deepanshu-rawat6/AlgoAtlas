class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Track depth; skip char when transitioning 0->1 (open) or 1->0 (close)
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:          # not the outermost open
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:          # not the outermost close
                    result.append(ch)
        return ''.join(result)


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.removeOuterParentheses("(()())(())") == "()()()"
    assert sol.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert sol.removeOuterParentheses("()()") == ""
    assert sol.removeOuterParentheses("((()))") == "(())"
    print("All tests passed.")
