"""
LC 1358 - Number of Substrings Containing All Three Characters

Given a string s consisting only of characters 'a', 'b', and 'c', return
the number of substrings containing at least one occurrence of all three.

Examples:
```text
Input: s = "abcabc"
Output: 10

Input: s = "aaacb"
Output: 3

Input: s = "abc"
Output: 1
```

Constraints:
- 3 <= s.length <= 5 * 10^4
- s consists only of 'a', 'b', 'c'
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Sliding window: for each right, find smallest left where all 3 present
        # Every extension of that window to the left also forms a valid substring
        # so add (left + 1) to result
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Shrink from left while all 3 chars are present
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[left]] -= 1
                left += 1

            # left is now one past the smallest valid window end
            # so there are `left` valid starting positions for this right
            result += left

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.numberOfSubstrings("abcabc") == 10
    assert s.numberOfSubstrings("aaacb") == 3
    assert s.numberOfSubstrings("abc") == 1
    print("All tests passed.")
