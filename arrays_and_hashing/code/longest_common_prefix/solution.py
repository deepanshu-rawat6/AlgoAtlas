"""
# LC 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Examples

```text
Input:  strs = ["flower","flow","flight"]
Output: "fl"

Input:  strs = ["dog","racecar","car"]
Output: ""
```

## Constraints
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix_vertical(self, strs: List[str]) -> str:
        # Check each character position across all strings simultaneously
        # Stop as soon as any string diverges or runs out of characters
        # O(S) time where S = sum of all characters | O(1) space
        if not strs:
            return ""
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # After sorting, only the first and last strings need to be compared
        # The common prefix of extremes is the common prefix of all strings
        # O(n log n * m) time | O(1) space
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["interview", "interact", "interface"]) == "inter"
    print("All tests passed.")
