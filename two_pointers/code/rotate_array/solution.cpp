#include <algorithm>
#include <cassert>
#include <vector>

class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin() + k);
        std::reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,3,4,5,6,7};
    sol.rotate(a, 3);
    assert((a == std::vector<int>{5,6,7,1,2,3,4}));
    std::vector<int> b = {-1,-100,3,99};
    sol.rotate(b, 2);
    assert((b == std::vector<int>{3,99,-1,-100}));
    std::vector<int> c = {1,2};
    sol.rotate(c, 3);
    assert((c == std::vector<int>{2,1}));
    return 0;
}
