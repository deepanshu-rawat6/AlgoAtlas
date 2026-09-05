// LC 11: Container With Most Water
// Two pointers from both ends; move the shorter side inward.
// Time: O(n), Space: O(1)
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n^2) try every pair
    int maxArea_brute(vector<int>& height) {
        int res = 0;
        for (int i = 0; i < (int)height.size(); i++)
            for (int j = i + 1; j < (int)height.size(); j++)
                res = max(res, min(height[i], height[j]) * (j - i));
        return res;
    }

    // Optimal: O(n) two pointers
    int maxArea(vector<int>& height) {
        int l = 0, r = (int)height.size() - 1, res = 0;
        while (l < r) {
            res = max(res, min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) l++;
            else r--;
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> a = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    assert(s.maxArea(a) == 49);
    vector<int> b = {1, 1};
    assert(s.maxArea(b) == 1);
    vector<int> c = {4, 3, 2, 1, 4};
    assert(s.maxArea(c) == 16);
    vector<int> d = {1, 2, 1};
    assert(s.maxArea(d) == 2);
    cout << "All tests passed." << endl;
    return 0;
}
