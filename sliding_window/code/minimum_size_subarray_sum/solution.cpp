#include <cassert>
#include <climits>
#include <algorithm>
#include <vector>

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int left = 0, total = 0, best = INT_MAX;
        for (int right = 0; right < (int)nums.size(); right++) {
            total += nums[right];
            while (total >= target) {
                best = std::min(best, right - left + 1);
                total -= nums[left++];
            }
        }
        return best == INT_MAX ? 0 : best;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {2,3,1,2,4,3};
    assert(sol.minSubArrayLen(7, a) == 2);
    std::vector<int> b = {1,4,4};
    assert(sol.minSubArrayLen(4, b) == 1);
    std::vector<int> c = {1,1,1,1,1,1,1,1};
    assert(sol.minSubArrayLen(11, c) == 0);
    return 0;
}
