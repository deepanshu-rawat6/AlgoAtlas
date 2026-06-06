"""
LC 216 - Combination Sum III

Problem: Find all combinations of exactly k numbers from 1-9 that sum to n.
Each number may be used at most once.

Examples:
    k=3, n=7  -> [[1,2,4]]
    k=3, n=9  -> [[1,2,6],[1,3,5],[2,3,4]]

Constraints:
    2 <= k <= 9
    1 <= n <= 60

Approach: Backtracking O(C(9,k)) — pick from 1-9 in increasing order,
    prune branch when current sum exceeds n or remaining slots can't be filled.
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, combo: List[int], remaining: int) -> None:
            # Found valid combination of exactly k numbers summing to n
            if len(combo) == k and remaining == 0:
                result.append(combo[:])
                return
            # Prune: too many numbers already, or impossible to reach sum
            if len(combo) == k or remaining < 0:
                return
            for num in range(start, 10):
                combo.append(num)
                backtrack(num + 1, combo, remaining - num)  # no reuse: start = num+1
                combo.pop()

        backtrack(1, [], n)
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.combinationSum3(3, 7) == [[1, 2, 4]]
    assert sol.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert sol.combinationSum3(4, 1) == []
    print("All tests passed.")
