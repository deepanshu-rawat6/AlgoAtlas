"""
# LC 796: Rotate String

Given two strings `s` and `goal`, return `true` if and only if `s` can become
`goal` after some number of *shifts* (rotating left by one position moves the first
character to the end).

## Examples

```text
Input:  s = "abcde", goal = "cdeab"
Output: true

Input:  s = "abcde", goal = "abced"
Output: false
```

## Constraints
- 1 <= s.length <= 100
- s.length == goal.length
- s and goal consist of lowercase English letters
"""


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
