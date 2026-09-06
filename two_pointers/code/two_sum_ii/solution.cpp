#include <cassert>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        int l = 0, r = (int)numbers.size() - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s == target) return {l+1, r+1};
            else if (s < target) l++;
            else r--;
        }
        return {};
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {2,7,11,15};
    assert((sol.twoSum(a, 9) == std::vector<int>{1,2}));
    std::vector<int> b = {2,3,4};
    assert((sol.twoSum(b, 6) == std::vector<int>{1,3}));
    std::vector<int> c = {-1,0};
    assert((sol.twoSum(c, -1) == std::vector<int>{1,2}));
    return 0;
}
