"""
## LC 881 — Boats to Save People

You are given an array `people` where `people[i]` is the weight of the `i`-th person,
and an infinite number of boats where each boat can carry at most two people at a time,
provided the sum of their weights is at most `limit`.
Return the minimum number of boats to carry every given person.

### Examples

```text
Input:  people = [1, 2], limit = 3
Output: 1

Input:  people = [3, 2, 2, 1], limit = 3
Output: 3

Input:  people = [3, 5, 3, 4], limit = 5
Output: 4
```

### Constraints

- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""
from typing import List


class Solution:
    def method_brute_force(self, people: List[int], limit: int) -> int:
        """O(n^2) time | O(n) space — greedy without sorting"""
        # Greedily pair heaviest with lightest that fits — O(n^2) without sorting
        remaining = people[:]
        boats = 0
        while remaining:
            heaviest = max(remaining)
            remaining.remove(heaviest)
            boats += 1
            for i, w in enumerate(remaining):
                if heaviest + w <= limit:
                    remaining.pop(i)
                    break
        return boats

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """O(n log n) time | O(1) space"""
        # Sort so lightest and heaviest are at opposite ends
        # Always send the heaviest person; pair with lightest if they fit together
        # Each iteration uses exactly one boat — count boats until all rescued
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats


if __name__ == "__main__":
    sol = Solution()
    print(sol.numRescueBoats([1, 2], 3))          # 1
    print(sol.numRescueBoats([3, 2, 2, 1], 3))    # 3
    print(sol.numRescueBoats([3, 5, 3, 4], 5))    # 4
