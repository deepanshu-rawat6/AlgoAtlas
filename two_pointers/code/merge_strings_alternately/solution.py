class Solution:
    """
    ## LC 1768: Merge Strings Alternately

    You are given two strings `word1` and `word2`. Merge the strings by adding letters
    in alternating order, starting with `word1`. If a string is longer than the other,
    append the additional letters onto the end of the merged string.

    Return the merged string.

    ### Examples

    ```text
    Input:  word1 = "abc", word2 = "pqr"
    Output: "apbqcr"

    Input:  word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"

    Input:  word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    ```

    ### Constraints

    - `1 <= word1.length, word2.length <= 100`
    - `word1` and `word2` consist of lowercase English letters.
    """

    def method_index(self, word1: str, word2: str) -> str:
        """O(n+m) time — index-based loop."""
        # Use a single index up to max length, conditionally append from each string
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return "".join(result)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """O(n+m) time, O(1) extra space (excluding output)."""
        # Advance both pointers together while both strings have characters
        # Append remaining tail of whichever string is longer
        result = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()

    assert sol.mergeAlternately("abc", "pqr") == "apbqcr"
    assert sol.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert sol.mergeAlternately("abcd", "pq") == "apbqcd"

    print("All tests passed.")
