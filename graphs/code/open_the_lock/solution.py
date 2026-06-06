"""
# 752. Open the Lock

## Problem
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
`'0', '1', '2', ..., '9'`. The wheels can rotate freely and wrap around (e.g., `'9'`
goes to `'0'` and vice versa). The lock initially starts at `'0000'`.

You are given a list of `deadends` — if the lock displays any of these codes, the wheels
will stop turning. Given a `target` representing the value of the wheels that will unlock
the lock, return the minimum total number of turns required to open the lock, or `-1` if
it is impossible.

## Examples
```text
Input:  deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: A sequence of valid moves: 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202
```

```text
Input:  deadends = ["8888"], target = "0009"
Output: 1
```

```text
Input:  deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
```

## Constraints
- `1 <= deadends.length <= 500`
- `deadends[i].length == 4`
- `target.length == 4`
- `target` will not be in the range of `deadends`
- `target != "0000"`
"""

from typing import List
from collections import deque


class Solution:
    def openLock_bfs(self, deadends: List[str], target: str) -> int:
        # O(10^4 * 4) time, O(10^4) space — standard BFS
        dead = set(deadends)
        if '0000' in dead:
            return -1
        visited = {'0000'}
        q = deque([('0000', 0)])
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                d = int(state[i])
                for delta in (1, -1):
                    nxt = state[:i] + str((d + delta) % 10) + state[i+1:]
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        q.append((nxt, turns + 1))
        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS from '0000'; each step turns one wheel up or down
        # Skip deadends; return number of steps when target is reached
        # O(10^4) time, O(10^4) space — bidirectional BFS
        dead = set(deadends)
        if '0000' in dead:
            return -1
        if target == '0000':
            return 0

        def neighbors(state):
            for i in range(4):
                d = int(state[i])
                for delta in (1, -1):
                    yield state[:i] + str((d + delta) % 10) + state[i+1:]

        front, back = {'0000'}, {target}
        visited = {'0000', target}
        turns = 0
        while front and back:
            # always expand the smaller frontier
            if len(front) > len(back):
                front, back = back, front
            turns += 1
            nxt = set()
            for state in front:
                for nb in neighbors(state):
                    if nb in dead:
                        continue
                    if nb in back:
                        return turns
                    if nb not in visited:
                        visited.add(nb)
                        nxt.add(nb)
            front = nxt
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.openLock_bfs(["0201","0101","0102","1212","2002"], "0202") == 6
    assert s.openLock_bfs(["8888"], "0009") == 1
    assert s.openLock_bfs(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888") == -1
    assert s.openLock(["0201","0101","0102","1212","2002"], "0202") == 6
    print("All tests passed.")
