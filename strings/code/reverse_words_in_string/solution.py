class Solution:
    # Approach 1: split + reverse — O(n) time, O(n) space
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

    # Approach 2: manual reverse (O(1) extra space conceptually)
    # Reverse entire string, then reverse each word in-place.
    def reverseWords_inplace(self, s: str) -> str:
        chars = list(s.strip())
        # Step 1: reverse whole array
        chars.reverse()
        # Step 2: reverse each individual word
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                chars[start:i] = chars[start:i][::-1]
                start = i + 1
        # Collapse multiple spaces
        return ' '.join(''.join(chars).split())


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseWords("  hello world  ") == "world hello"
    assert sol.reverseWords("a good   example") == "example good a"
    assert sol.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    assert sol.reverseWords_inplace("  hello world  ") == "world hello"
    print("All tests passed.")
