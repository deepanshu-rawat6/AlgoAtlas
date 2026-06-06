"""
# 895. Maximum Frequency Stack

## Problem
Design a stack-like data structure that pushes and pops elements according to
a maximum frequency rule.

Implement the `FreqStack` class:
- `push(val)` — Pushes an integer `val` onto the stack.
- `pop()` — Removes and returns the most frequent element in the stack.
  - If there is a tie for the most frequent element, the element closest to
    the top of the stack (most recently pushed) is removed and returned.

## Examples
```text
Input:
  ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
  [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output:
  [null,null,null,null,null,null,null,5,7,5,4]

Explanation:
  After pushes: freq = {5:3, 7:2, 4:1}
  pop() -> 5 (freq 3, most frequent)
  pop() -> 7 (freq 2 tie between 5 and 7; 7 was pushed more recently at freq 2)
  pop() -> 5 (freq 2)
  pop() -> 4 (freq 1 tie; 4 was pushed most recently at freq 1)
```

## Constraints
- `0 <= val <= 10^9`
- At most `2 * 10^4` calls will be made to `push` and `pop`
- It is guaranteed that there will be at least one element in the stack before
  calling `pop`
"""

from collections import defaultdict


class FreqStack:
    """Approach 1: freq map + group map keyed by frequency — O(1) push and pop."""

    def __init__(self):
        self.freq: dict = defaultdict(int)          # val -> frequency
        self.group: dict = defaultdict(list)        # freq -> stack of vals
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        # Increment frequency of val; append to the group for that frequency
        # Update max_freq if this val's frequency is now the highest
        # O(1) — increment freq, append to corresponding group
        self.freq[val] += 1
        f = self.freq[val]
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(val)

    def pop(self) -> int:
        # Pop from the group at max_freq (most recently pushed among most frequent)
        # Decrement val's frequency; if max_freq group is now empty, decrease max_freq
        # O(1) — pop from max_freq group, decrement freq
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val


if __name__ == "__main__":
    fs = FreqStack()
    for v in [5, 7, 5, 7, 4, 5]:
        fs.push(v)
    assert fs.pop() == 5
    assert fs.pop() == 7
    assert fs.pop() == 5
    assert fs.pop() == 4
    print("All tests passed.")
