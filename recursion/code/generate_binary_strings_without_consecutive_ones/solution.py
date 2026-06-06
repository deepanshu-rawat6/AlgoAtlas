"""
Generate Binary Strings Without Consecutive 1s

Problem: Generate all binary strings of length n that do not contain consecutive 1s.

Examples:
    n = 3 -> ["000", "001", "010", "100", "101"]
    n = 1 -> ["0", "1"]

Constraints:
    1 <= n <= 20

Approach: Backtracking O(2^n) — at each position decide '0' or '1',
    but if last character placed was '1', next must be '0'.
"""

from typing import List


class Solution:
    def generateStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str) -> None:
            # Base case: string has reached desired length
            if len(current) == n:
                result.append(current)
                return
            # Always allowed to place '0'
            backtrack(current + '0')
            # Place '1' only if last character is not '1'
            if not current or current[-1] != '1':
                backtrack(current + '1')

        backtrack("")
        return sorted(result)  # return in lexicographic order


if __name__ == '__main__':
    sol = Solution()
    assert sol.generateStrings(3) == ["000", "001", "010", "100", "101"]
    assert sol.generateStrings(1) == ["0", "1"]
    # Verify no consecutive 1s in any result
    for s in sol.generateStrings(5):
        assert "11" not in s
    print("All tests passed.")
