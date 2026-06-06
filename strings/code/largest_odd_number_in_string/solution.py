class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Scan from right; first odd digit found → return prefix up to that index
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.largestOddNumber("52") == "5"
    assert sol.largestOddNumber("4206") == ""
    assert sol.largestOddNumber("35427") == "35427"
    assert sol.largestOddNumber("2") == ""
    assert sol.largestOddNumber("1") == "1"
    print("All tests passed.")
