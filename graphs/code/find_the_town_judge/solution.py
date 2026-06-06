"""
# 997. Find the Town Judge

## Problem
In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of
these people is secretly the town judge. If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

Given an array `trust` where `trust[i] = [a, b]` means person `a` trusts person `b`,
return the label of the town judge if the town judge exists, otherwise return `-1`.

## Examples
```text
Input:  n = 2, trust = [[1,2]]
Output: 2
```

```text
Input:  n = 3, trust = [[1,3],[2,3]]
Output: 3
```

```text
Input:  n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

## Constraints
- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- All the pairs in `trust` are unique
- `a != b`
"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Judge trusts nobody (out-degree 0) and is trusted by everyone else (in-degree n-1)
        # Track trust counts: net_trust[i] = in_degree[i] - out_degree[i]; judge has n-1
        # O(n+e) time, O(n) space — net trust score: +1 for being trusted, -1 for trusting
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.findJudge(2, [[1,2]]) == 2
    assert s.findJudge(3, [[1,3],[2,3]]) == 3
    assert s.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
    assert s.findJudge(1, []) == 1
    print("All tests passed.")
