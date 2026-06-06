"""
# 953. Verifying an Alien Dictionary

## Problem
In an alien language, the alphabet uses the same letters as English but in a possibly
different order. Given a sequence of `words` written in the alien language and the `order`
of the alphabet, return `true` if and only if the given `words` are sorted lexicographically
in this alien language.

## Examples
```text
Input:  words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: 'h' comes before 'l' in the alien alphabet.
```

```text
Input:  words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: 'd' comes after 'l' in the alien alphabet, so "word" > "world".
```

```text
Input:  words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: "apple" > "app" because the first word is longer.
```

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `order.length == 26`
- All characters in `words[i]` and `order` are English lowercase letters
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Build order map from alien alphabet; compare adjacent words character by character
        # If a word is a prefix of the next word but longer, it's invalid
        # O(n*m) time, O(1) space — compare each adjacent pair character by character
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):          # w2 is prefix of w1 → not sorted
                    return False
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
    assert s.isAlienSorted(["z","z"], "abcdefghijklmnopqrstuvwxyz") == True
    print("All tests passed.")
