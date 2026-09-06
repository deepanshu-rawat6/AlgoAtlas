#include <cassert>
#include <algorithm>
#include <vector>

class Solution {
public:
    int longestOnes(std::vector<int>& nums, int k) {
        int left = 0, zeros = 0, result = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            result = std::max(result, right - left + 1);
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,1,1,0,0,0,1,1,1,1,0};
    assert(sol.longestOnes(a, 2) == 6);
    std::vector<int> b = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    assert(sol.longestOnes(b, 3) == 10);
    std::vector<int> c = {1,1,1};
    assert(sol.longestOnes(c, 0) == 3);
    return 0;
}
