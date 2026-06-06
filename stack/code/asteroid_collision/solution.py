"""
# 735. Asteroid Collision

## Problem
We are given an array `asteroids` of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive = right, negative = left). All asteroids
move at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one explodes. If both are the same size, both explode. Two
asteroids moving in the same direction never meet.

## Examples
```text
Input:  asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 10 and -5 collide -> 10 survives. 5 and 10 never collide.

Input:  asteroids = [8, -8]
Output: []
Explanation: 8 and -8 collide -> both explode.

Input:  asteroids = [10, 2, -5]
Output: [10]
Explanation: 2 and -5 collide -> -5 wins. 10 and -5 collide -> 10 wins.
```

## Constraints
- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Only collisions happen when a left-moving asteroid meets a right-moving one on stack
        # Keep destroying top of stack while it's smaller than the incoming asteroid
        # Equal sizes destroy both; larger stack top destroys incoming
        # O(n) time, O(n) space — stack simulation of collisions
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()          # right asteroid destroyed
                elif stack[-1] == -a:
                    stack.pop()          # both destroyed
                    alive = False
                else:
                    alive = False        # left asteroid destroyed
            if alive:
                stack.append(a)
        return stack


if __name__ == "__main__":
    s = Solution()
    assert s.asteroidCollision([5, 10, -5]) == [5, 10]
    assert s.asteroidCollision([8, -8]) == []
    assert s.asteroidCollision([10, 2, -5]) == [10]
    assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert s.asteroidCollision([1, -1]) == []
    print("All tests passed.")
