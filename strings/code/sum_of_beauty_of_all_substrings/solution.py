"""
# LC 1781: Sum of Beauty of All Substrings

The *beauty* of a string is the difference between the maximum frequency and the
minimum frequency of any character in it. Return the sum of beauty of all substrings
of `s`.

## Examples

```text
Input:  s = "aabcb"
Output: 5

Input:  s = "aabcbaa"
Output: 17
```

## Constraints
- 1 <= s.length <= 500
- s consists of lowercase English letters only
"""


class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                # Compute beauty in O(26): max_freq - min_freq (ignore zeros)
                active = [f for f in freq if f > 0]
                total += max(active) - min(active)
        return total


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.beautySum("aabcb") == 5
    assert sol.beautySum("aabcbaa") == 17
    assert sol.beautySum("a") == 0
    assert sol.beautySum("aa") == 0
    print("All tests passed.")
