class Solution:
    """
    ## 1871. Jump Game VII

    Given a binary string s and integers minJump and maxJump, you start at index 0
    (which is '0'). Return true if you can reach the last index, where you can jump
    from index i to any index j such that i + minJump <= j <= i + maxJump and s[j] == '0'.

    ### Example
    ```text
    Input:  s = "011010", minJump = 2, maxJump = 3
    Output: true  (0 -> 3 -> 5)

    Input:  s = "01101110", minJump = 2, maxJump = 3
    Output: false
    ```

    ### Constraints
    - 2 <= s.length <= 10^5
    - s[i] is either '0' or '1'
    - s[0] == '0'
    - 1 <= minJump <= maxJump < s.length
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # BFS/sliding window: track reachable positions; from each, jump [minJump, maxJump]
        # Use a pointer to avoid re-processing already-covered positions
        # O(n) time, O(n) space — DP with prefix sum sliding window
        n = len(s)
        reach = [False] * n
        reach[0] = True
        prefix = 0  # count of reachable positions in current window
        for i in range(1, n):
            if i >= minJump:
                prefix += reach[i - minJump]
            if i > maxJump:
                prefix -= reach[i - maxJump - 1]
            reach[i] = prefix > 0 and s[i] == '0'
        return reach[-1]


if __name__ == '__main__':
    s = Solution()
    assert s.canReach("011010", 2, 3) == True
    assert s.canReach("01101110", 2, 3) == False
    assert s.canReach("00", 1, 1) == True
    print("All tests passed.")
