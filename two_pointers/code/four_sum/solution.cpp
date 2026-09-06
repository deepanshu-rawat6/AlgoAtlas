#include <algorithm>
#include <cassert>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, long long target) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        std::vector<std::vector<int>> result;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;
                int lo = j + 1, hi = n - 1;
                while (lo < hi) {
                    long long s = (long long)nums[i] + nums[j] + nums[lo] + nums[hi];
                    if (s == target) {
                        result.push_back({nums[i], nums[j], nums[lo], nums[hi]});
                        while (lo < hi && nums[lo] == nums[lo+1]) lo++;
                        while (lo < hi && nums[hi] == nums[hi-1]) hi--;
                        lo++; hi--;
                    } else if (s < target) lo++;
                    else hi--;
                }
            }
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1, 0, -1, 0, -2, 2};
    assert(sol.fourSum(a, 0).size() == 3);
    std::vector<int> b = {2, 2, 2, 2, 2};
    auto r2 = sol.fourSum(b, 8);
    assert(r2.size() == 1 && r2[0] == std::vector<int>({2,2,2,2}));
    std::vector<int> c = {0, 0, 0, 0};
    assert(sol.fourSum(c, 0).size() == 1);
    return 0;
}
