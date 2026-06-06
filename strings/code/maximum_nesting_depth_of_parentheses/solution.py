class Solution:
    def maxDepth(self, s: str) -> int:
        depth = max_depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ')':
                depth -= 1
        return max_depth


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert sol.maxDepth("(1)+((2))+(((3)))") == 3
    assert sol.maxDepth("1+(2*3)/(2-1)") == 1
    assert sol.maxDepth("1") == 0
    assert sol.maxDepth("()") == 1
    print("All tests passed.")
