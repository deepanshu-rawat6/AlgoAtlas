#include <cassert>
#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        std::deque<int> dq;
        std::vector<int> result;
        for (int i = 0; i < (int)nums.size(); i++) {
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
            dq.push_back(i);
            if (dq.front() < i - k + 1) dq.pop_front();
            if (i >= k - 1) result.push_back(nums[dq.front()]);
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,3,-1,-3,5,3,6,7};
    assert((sol.maxSlidingWindow(a, 3) == std::vector<int>{3,3,5,5,6,7}));
    std::vector<int> b = {1};
    assert((sol.maxSlidingWindow(b, 1) == std::vector<int>{1}));
    std::vector<int> c = {1,-1};
    assert((sol.maxSlidingWindow(c, 1) == std::vector<int>{1,-1}));
    return 0;
}
