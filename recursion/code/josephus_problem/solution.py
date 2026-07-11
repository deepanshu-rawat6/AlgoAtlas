"""
# Josephus Problem

Given `n` people standing in a circle (0-indexed), every `k`th person is
eliminated until only one remains. Return the 0-indexed position of the survivor.

## Examples
```text
Input:  n = 7, k = 3
Output: 3

Input:  n = 5, k = 2
Output: 2
```

## Constraints
- n >= 1, k >= 1.
- Recurrence: J(1, k) = 0; J(n, k) = (J(n-1, k) + k) % n.
"""
from typing import List


class Solution:
    def josephus_simulation(self, n: int, k: int) -> int:
        # Approach 1: Simulation O(n*k) — maintain a list, remove every kth person
        people = list(range(n))
        idx = 0
        while len(people) > 1:
            idx = (idx + k - 1) % len(people)  # move k-1 steps forward
            people.pop(idx)
            if idx == len(people):  # wrap around after removal
                idx = 0
        return people[0]

    def josephus(self, n: int, k: int) -> int:
        # Approach 2: Recursive formula O(n)
        # J(1, k) = 0  (only one person, 0-indexed position)
        # J(n, k) = (J(n-1, k) + k) % n
        # After eliminating the kth person, the circle shrinks to n-1 people.
        # The result for n-1 people is shifted by k positions in the original indexing.
        if n == 1:
            return 0
        return (self.josephus(n - 1, k) + k) % n


if __name__ == "__main__":
    sol = Solution()
    # n=7, k=3 -> 3 (0-indexed)
    assert sol.josephus(7, 3) == 3
    assert sol.josephus_simulation(7, 3) == 3
    # n=1 -> only one person, position 0
    assert sol.josephus(1, 1) == 0
    # n=5, k=2 -> 2
    assert sol.josephus(5, 2) == 2
    assert sol.josephus_simulation(5, 2) == 2
    print("All tests passed.")
