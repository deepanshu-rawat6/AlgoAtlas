"""
# LC 49: Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return
the answer in any order.

## Examples

```text
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input:  strs = [""]
Output: [[""]]

Input:  strs = ["a"]
Output: [["a"]]
```

## Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        # Sorted string is a canonical key — all anagrams share the same key
        # O(n * k log k) time | O(n * k) space
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Character-frequency tuple is a canonical key without sorting cost
        # Build a 26-element count array per word, then use it as dict key
        # O(n * k) time | O(n * k) space
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    print("All tests passed.")
