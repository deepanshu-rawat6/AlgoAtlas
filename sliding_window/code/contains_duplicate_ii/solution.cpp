#include <cassert>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool containsNearbyDuplicate(std::vector<int>& nums, int k) {
        std::unordered_set<int> window;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (window.count(nums[i])) return true;
            window.insert(nums[i]);
            if ((int)window.size() > k) window.erase(nums[i - k]);
        }
        return false;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,3,1};
    assert(sol.containsNearbyDuplicate(a, 3) == true);
    std::vector<int> b = {1,0,1,1};
    assert(sol.containsNearbyDuplicate(b, 1) == true);
    std::vector<int> c = {1,2,3,1,2,3};
    assert(sol.containsNearbyDuplicate(c, 2) == false);
    return 0;
}
