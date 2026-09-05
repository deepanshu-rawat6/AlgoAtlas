// LC 153: Find Minimum in Rotated Sorted Array
// Binary search to find the pivot (minimum element).
// Time: O(log n), Space: O(1)
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n) linear scan
    int findMin_brute(vector<int>& nums) {
        return *min_element(nums.begin(), nums.end());
    }

    // Optimal: O(log n) — unsorted half contains the minimum
    int findMin(vector<int>& nums) {
        int lo = 0, hi = (int)nums.size() - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
        }
        return nums[lo];
    }
};

int main() {
    Solution s;
    vector<int> a = {3, 4, 5, 1, 2};
    assert(s.findMin(a) == 1);
    vector<int> b = {4, 5, 6, 7, 0, 1, 2};
    assert(s.findMin(b) == 0);
    vector<int> c = {11, 13, 15, 17};
    assert(s.findMin(c) == 11);
    vector<int> d = {2, 1};
    assert(s.findMin(d) == 1);
    vector<int> e = {1};
    assert(s.findMin(e) == 1);
    cout << "All tests passed." << endl;
    return 0;
}
