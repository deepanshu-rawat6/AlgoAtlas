#include <cassert>
#include <vector>

class Solution {
public:
    int trap(std::vector<int>& height) {
        int lo = 0, hi = (int)height.size() - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (lo <= hi) {
            if (height[lo] <= height[hi]) {
                if (height[lo] >= leftMax) leftMax = height[lo];
                else water += leftMax - height[lo];
                lo++;
            } else {
                if (height[hi] >= rightMax) rightMax = height[hi];
                else water += rightMax - height[hi];
                hi--;
            }
        }
        return water;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {0,1,0,2,1,0,1,3,2,1,2,1};
    assert(sol.trap(a) == 6);
    std::vector<int> b = {4,2,0,3,2,5};
    assert(sol.trap(b) == 9);
    std::vector<int> c = {3,0,3};
    assert(sol.trap(c) == 3);
    return 0;
}
