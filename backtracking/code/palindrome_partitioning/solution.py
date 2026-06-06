from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        ## 131. Palindrome Partitioning

        Given a string s, partition s such that every substring of the partition is a
        palindrome. Return all possible palindrome partitioning of s.

        ### Examples

        ```text
        Input:  s = "aab"
        Output: [["a","a","b"],["aa","b"]]

        Input:  s = "a"
        Output: [["a"]]
        ```

        ### Constraints
        - `1 <= s.length <= 16`
        - s consists only of lowercase English letters.
        """
        # Try every prefix of remaining string; if it's a palindrome, recurse on suffix
        # Add complete partition to result when entire string is consumed
        # O(n * 2^n) time, O(n) stack space
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def bt(start, current):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    current.append(substr)
                    bt(end, current)
                    current.pop()

        bt(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
    assert s.partition("a") == [["a"]]
    print("All tests passed.")
