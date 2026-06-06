"""
# LC 242: Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`,
and `false` otherwise.

## Examples

```text
Input:  s = "anagram", t = "nagaram"
Output: true

Input:  s = "rat", t = "car"
Output: false
```

## Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters
"""


class Solution:
    def isAnagram_sort(self, s: str, t: str) -> bool:
        # Sorting both strings makes them identical iff they're anagrams
        # O(n log n) time | O(1) space
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ — anagrams must have same length
        # Increment count for s's char, decrement for t's char simultaneously
        # All zeros at the end means every character balanced out
        # O(n) time | O(1) space — at most 26 keys
        if len(s) != len(t):
            return False
        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - ord('a')] += 1
            count[ord(b) - ord('a')] -= 1
        return all(c == 0 for c in count)


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    assert s.isAnagram("a", "ab") == False
    print("All tests passed.")
