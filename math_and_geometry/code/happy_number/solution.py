"""
# 202. Happy Number

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
- Numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

## Examples

```text
Input: n = 19
Output: true
Explanation: 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> ... -> 1

Input: n = 2
Output: false
```

## Constraints
- 1 <= n <= 2^31 - 1
"""


def _sum_of_squares(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total


class Solution:
    def isHappy_set(self, n: int) -> bool:
        # O(log n) time per step, O(log n) space — hash set to detect cycle
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = _sum_of_squares(n)
        return n == 1

    def isHappy(self, n: int) -> bool:
        # Repeatedly sum squares of digits; cycle detection via set or Floyd's
        # If we reach 1, it's happy; if we revisit a number, it's not
        # O(log n) time per step, O(1) space — Floyd's slow/fast cycle detection
        slow, fast = n, _sum_of_squares(n)
        while fast != 1 and slow != fast:
            slow = _sum_of_squares(slow)
            fast = _sum_of_squares(_sum_of_squares(fast))
        return fast == 1


if __name__ == '__main__':
    s = Solution()
    for method in (s.isHappy_set, s.isHappy):
        assert method(19) is True
        assert method(2) is False
        assert method(1) is True
    print("All tests passed.")
