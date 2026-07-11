"""
# LC 473: Matchsticks to Square

Given an array `matchsticks` of stick lengths, determine whether you can use every
matchstick exactly once to form a square (each of the four sides equal in length).
You may not break any stick. Return true if a square can be formed, otherwise false.

## Examples
```text
Input:  matchsticks = [1, 1, 2, 2, 2]
Output: true

Input:  matchsticks = [3, 3, 3, 3, 4]
Output: false
```

## Constraints
- 1 <= matchsticks.length <= 15
- 1 <= matchsticks[i] <= 10^8
"""
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        ## 473. Matchsticks to Square

        You are given an integer array matchsticks where matchsticks[i] is the length of
        the ith matchstick. You want to use all the matchsticks to make one square. You
        should not break any stick, but you can link them up, and each matchstick must be
        used exactly one time.

        Return true if you can make this square and false otherwise.

        ### Examples

        ```text
        Input:  matchsticks = [1, 1, 2, 2, 2]
        Output: true
        Explanation: 1+2=3, 1+2=3, 2=2... wait, side = 8/4 = 2. [2],[2],[2],[1,1] -> true

        Input:  matchsticks = [3, 3, 3, 3, 4]
        Output: false
        ```

        ### Constraints
        - `1 <= matchsticks.length <= 15`
        - `1 <= matchsticks[i] <= 10^8`
        """
        # Special case of partition into 4 equal subsets (k=4)
        # Sort descending for better pruning; skip duplicate bucket sums
        # O(4^n) time, O(n) stack space
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        sides = [0] * 4

        def bt(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == side
            for i in range(4):
                if sides[i] + matchsticks[idx] <= side:
                    sides[i] += matchsticks[idx]
                    if bt(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
                    if sides[i] == 0:
                        break  # prune symmetric branches
            return False

        return bt(0)


if __name__ == '__main__':
    s = Solution()
    assert s.makesquare([1, 1, 2, 2, 2]) is True
    assert s.makesquare([3, 3, 3, 3, 4]) is False
    assert s.makesquare([1, 1, 1, 1]) is True
    print("All tests passed.")
