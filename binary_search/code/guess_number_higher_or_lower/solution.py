"""
LC 374 - Guess Number Higher or Lower
======================================

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is
higher or lower than your guess.

You call a pre-defined API `guess(num: int) -> int` which returns three
possible results:
  -1 : Your guess is higher than the number I picked (i.e. num > pick)
   1 : Your guess is lower than the number I picked (i.e. num < pick)
   0 : Your guess is equal to the number I picked (i.e. num == pick)

Return the number that I picked.

Examples
--------
```text
Input:  n = 10, pick = 6
Output: 6

Input:  n = 1, pick = 1
Output: 1
```

Constraints
-----------
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n
"""

_PICK = 0  # set before each test


def guess(num: int) -> int:
    if num > _PICK:
        return -1
    elif num < _PICK:
        return 1
    return 0


class Solution:
    def method_linear(self, n: int) -> int:
        # O(n) time | O(1) space
        for i in range(1, n + 1):
            if guess(i) == 0:
                return i
        return -1

    def guessNumber(self, n: int) -> int:
        # Binary search using the guess() API: -1 means too high, 1 means too low
        # O(log n) time | O(1) space
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == "__main__":
    import sys
    s = Solution()

    for n, pick in [(10, 6), (1, 1), (2, 2)]:
        globals()["_PICK"] = pick
        assert s.guessNumber(n) == pick, f"guessNumber({n}) failed"
        globals()["_PICK"] = pick
        assert s.method_linear(n) == pick, f"method_linear({n}) failed"

    print("All tests passed.")
