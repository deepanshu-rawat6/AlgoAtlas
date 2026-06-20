"""
# LC 451: Sort Characters By Frequency

Given a string `s`, sort it in decreasing order based on the frequency of
characters. If two characters have the same frequency, either order is acceptable.
Return the sorted string.

## Examples

```text
Input:  s = "tree"
Output: "eert"

Input:  s = "cccaaa"
Output: "cccaaa"

Input:  s = "Aabb"
Output: "bbAa"
```

## Constraints
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits
"""
from collections import Counter

class Solution:
    # Approach 1: Counter + sort — O(n log n)
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        # Sort characters by frequency descending, then build result
        return ''.join(ch * cnt for ch, cnt in freq.most_common())

    # Approach 2: Bucket sort — O(n)
    def frequencySort_bucket(self, s: str) -> str:
        freq = Counter(s)
        # Buckets indexed by frequency (max freq = len(s))
        buckets = [''] * (len(s) + 1)
        for ch, cnt in freq.items():
            buckets[cnt] += ch * cnt
        return ''.join(reversed(buckets))


# Tests
if __name__ == '__main__':
    sol = Solution()
    # Multiple valid outputs; check sorted freq property
    res = sol.frequencySort("tree")
    assert res[0] == res[1] == 'e' and set(res) == {'e', 'r', 't'}
    assert sol.frequencySort("cccaaa") in ("cccaaa", "aaaccc")
    assert sol.frequencySort("Aabb") in ("bbAa", "bbaA")
    res2 = sol.frequencySort_bucket("tree")
    assert res2[0] == res2[1] == 'e'
    print("All tests passed.")
