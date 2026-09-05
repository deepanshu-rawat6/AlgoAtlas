// LC 15: 3Sum
// Sort + fix one element + two-pointer for the other two; return unique triplets.
// Time: O(n^2), Space: O(1) excluding output
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n^3) + set to deduplicate
    vector<vector<int>> threeSum_brute(vector<int>& nums) {
        int n = nums.size();
        set<vector<int>> st;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> v = {nums[i], nums[j], nums[k]};
                        sort(v.begin(), v.end());
                        st.insert(v);
                    }
        return vector<vector<int>>(st.begin(), st.end());
    }

    // Optimal: O(n^2)
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < (int)nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l = i + 1, r = (int)nums.size() - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    l++; r--;
                } else if (sum < 0) l++;
                else r--;
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> a = {-1, 0, 1, 2, -1, -4};
    auto res1 = s.threeSum(a);
    assert((res1 == vector<vector<int>>{{-1,-1,2},{-1,0,1}}));

    vector<int> b = {0, 1, 1};
    assert(s.threeSum(b).empty());

    vector<int> c = {0, 0, 0};
    assert((s.threeSum(c) == vector<vector<int>>{{0,0,0}}));

    vector<int> d = {-2, 0, 0, 2, 2};
    assert((s.threeSum(d) == vector<vector<int>>{{-2,0,2}}));

    cout << "All tests passed." << endl;
    return 0;
}
