"""
LC 340 - Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest
substring that contains at most k distinct characters.

Examples:
```text
Input: s = "eceba", k = 2
Output: 3

Input: s = "aa", k = 1
Output: 2

Input: s = "aabbcc", k = 2
Output: 4
```

Constraints:
- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Sliding window with freq map
        # Expand right always, shrink left when distinct count > k
        if k == 0:
            return 0

        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Too many distinct chars — shrink from left
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            result = max(result, right - left + 1)

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstringKDistinct("eceba", 2) == 3
    assert s.lengthOfLongestSubstringKDistinct("aa", 1) == 2
    assert s.lengthOfLongestSubstringKDistinct("aabbcc", 2) == 4
    assert s.lengthOfLongestSubstringKDistinct("abc", 0) == 0
    print("All tests passed.")
