class Solution:
    # Approach 1: try all rotations — O(n^2)
    def rotateString_brute(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

    # Approach 2: s+s contains every rotation — O(n) with KMP/built-in
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.rotateString("abcde", "cdeab") == True
    assert sol.rotateString("abcde", "abced") == False
    assert sol.rotateString("", "") == True
    assert sol.rotateString("a", "a") == True
    assert sol.rotateString("aa", "a") == False
    assert sol.rotateString_brute("abcde", "cdeab") == True
    print("All tests passed.")
