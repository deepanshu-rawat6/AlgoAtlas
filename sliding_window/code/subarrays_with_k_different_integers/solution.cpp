#include <cassert>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int subarraysWithKDistinct(std::vector<int>& nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
private:
    int atMost(std::vector<int>& nums, int limit) {
        std::unordered_map<int,int> count;
        int left = 0, res = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            count[nums[right]]++;
            while ((int)count.size() > limit) {
                if (--count[nums[left]] == 0) count.erase(nums[left]);
                left++;
            }
            res += right - left + 1;
        }
        return res;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,1,2,3};
    assert(sol.subarraysWithKDistinct(a, 2) == 7);
    std::vector<int> b = {1,2,1,3,4};
    assert(sol.subarraysWithKDistinct(b, 3) == 3);
    std::vector<int> c = {1,1,1,1};
    assert(sol.subarraysWithKDistinct(c, 1) == 10);
    return 0;
}
