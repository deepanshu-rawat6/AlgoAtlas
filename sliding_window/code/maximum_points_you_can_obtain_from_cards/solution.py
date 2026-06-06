"""
LC 1423 - Maximum Points You Can Obtain from Cards

There are several cards arranged in a row. In each step you may take one
card from the beginning or end of the row. You take exactly k cards.
Return the maximum score you can obtain.

Examples:
```text
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12

Input: cardPoints = [2,2,2], k = 2
Output: 4

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
```

Constraints:
- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length
"""

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Approach 1: minimize the sum of the middle window of size n-k
        # Taking k from edges = leaving n-k in the middle
        n = len(cardPoints)
        window = n - k

        if window == 0:
            return sum(cardPoints)

        # Compute sum of first window
        curr = sum(cardPoints[:window])
        min_mid = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            min_mid = min(min_mid, curr)

        return sum(cardPoints) - min_mid

    def maxScore_prefix(self, cardPoints: List[int], k: int) -> int:
        # Approach 2: prefix sum from both ends — try all splits of k cards
        # take i from front, k-i from back
        total = sum(cardPoints)
        n = len(cardPoints)
        prefix = [0] * (k + 1)
        suffix = [0] * (k + 1)

        for i in range(1, k + 1):
            prefix[i] = prefix[i - 1] + cardPoints[i - 1]
            suffix[i] = suffix[i - 1] + cardPoints[n - i]

        return max(prefix[i] + suffix[k - i] for i in range(k + 1))


if __name__ == '__main__':
    s = Solution()
    assert s.maxScore([1,2,3,4,5,6,1], 3) == 12
    assert s.maxScore([2,2,2], 2) == 4
    assert s.maxScore([9,7,7,9,7,7,9], 7) == 55
    assert s.maxScore_prefix([1,2,3,4,5,6,1], 3) == 12
    assert s.maxScore_prefix([2,2,2], 2) == 4
    print("All tests passed.")
