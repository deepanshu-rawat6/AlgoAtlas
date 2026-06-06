from typing import List


class Solution:
    """
    **LC 2707: Extra Characters in a String**

    You are given a string `s` and a dictionary of words `dictionary`. Break `s`
    into one or more non-overlapping substrings such that each substring is in
    the dictionary. Some characters may be left over — return the **minimum**
    number of extra characters left over.

    Example 1:
    ```text
    Input:  s = "leetscode", dictionary = ["leet","code","leetcode"]
    Output: 1
    Explanation: Break into "leet" + "s" + "code". Extra = 1 character "s".
    ```

    Example 2:
    ```text
    Input:  s = "sayhelloworld", dictionary = ["hello","world"]
    Output: 3
    Explanation: Break into "say" + "hello" + "world". Extra = 3 characters "say".
    ```

    **Constraints:**
    * `1 <= s.length <= 50`
    * `1 <= dictionary.length <= 50`
    * `1 <= dictionary[i].length <= 50`
    * `dictionary[i]` and `s` consist of only lowercase English letters
    """

    def minExtraChar_dp(self, s: str, dictionary: List[str]) -> int:
        # O(n^2 * m) — DP with hash set lookup
        pass

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # DP: dp[i] = min extra chars in s[:i]
        # For each position, try all dictionary words ending at i; take minimum
        # O(n^2 * m) — DP with Trie for prefix matching
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: expected 1
    print(sol.minExtraChar("leetscode", ["leet", "code", "leetcode"]))

    # Example 2: expected 3
    print(sol.minExtraChar("sayhelloworld", ["hello", "world"]))
