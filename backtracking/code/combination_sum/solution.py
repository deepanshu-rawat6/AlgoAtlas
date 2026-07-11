"""
# LC 39: Combination Sum

Given an array of distinct integers `candidates` and a target integer `target`, return
a list of all unique combinations of candidates where the chosen numbers sum to target.
The same number may be chosen an unlimited number of times. Two combinations are unique
if the frequency of at least one chosen number differs.

## Examples
```text
Input:  candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Input:  candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Input:  candidates = [2], target = 1
Output: []
```

## Constraints
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        ## 39. Combination Sum

        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers
        sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen
        numbers is different.

        ### Examples

        ```text
        Input:  candidates = [2, 3, 6, 7], target = 7
        Output: [[2, 2, 3], [7]]

        Input:  candidates = [2, 3, 5], target = 8
        Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        Input:  candidates = [2], target = 1
        Output: []
        ```

        ### Constraints
        - `1 <= candidates.length <= 30`
        - `2 <= candidates[i] <= 40`
        - All elements of candidates are distinct.
        - `1 <= target <= 40`
        """
        # Candidates can be reused: recurse with same index i
        # Prune when remaining < 0; record when remaining == 0
        # O(n^(t/m)) time where t=target, m=min candidate; O(t/m) stack space
        candidates.sort()
        result = []

        def bt(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                bt(i, remaining - candidates[i], current)
                current.pop()

        bt(0, target, [])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]])
    assert sorted(s.combinationSum([2, 3, 5], 8)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert s.combinationSum([2], 1) == []
    print("All tests passed.")
