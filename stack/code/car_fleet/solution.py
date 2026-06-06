"""
# 853. Car Fleet

## Problem
There are `n` cars at given miles away from the starting point, all driving
towards the same `target` destination. Each car `i` has a position
`position[i]` and speed `speed[i]` (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and
drive bumper to bumper at the slower car's speed. Two cars that drive bumper
to bumper are considered a single car fleet.

Return the number of car fleets that will arrive at the destination.

## Examples
```text
Input:  target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
  Cars at 10 and 8 become a fleet (arrive at 12 at time 1 and 1).
  Car at 0 is its own fleet (arrives at time 12).
  Cars at 5 and 3 become a fleet (arrive at time 7 and 3 -> 3 catches 5).

Input:  target = 10, position = [3], speed = [3]
Output: 1

Input:  target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
```

## Constraints
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- All values of `position` are unique
- `0 < speed[i] <= 10^6`
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position descending (closest to target first)
        # Compute arrival time for each car; if it arrives before the car ahead, it joins that fleet
        # A new fleet forms only when a car arrives strictly later than the current top
        # O(n log n) time, O(n) space — sort by position, stack of arrival times
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            # if time <= stack[-1], this car catches the fleet ahead -> same fleet
        return len(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert s.carFleet(10, [3], [3]) == 1
    assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert s.carFleet(10, [6, 8], [3, 2]) == 2
    print("All tests passed.")
