// LC 33: Search in Rotated Sorted Array
// Binary search on rotated sorted array — determine which half is sorted.
// Time: O(log n), Space: O(1)
#include <vector>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n) linear scan
    int search_brute(vector<int>& nums, int target) {
        for (int i = 0; i < (int)nums.size(); i++)
            if (nums[i] == target) return i;
        return -1;
    }

    // Optimal: O(log n) — figure out which half is sorted, then narrow
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = (int)nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            // left half is sorted
            if (nums[lo] <= nums[mid]) {
                if (nums[lo] <= target && target < nums[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else {
                // right half is sorted
                if (nums[mid] < target && target <= nums[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }
};

int main() {
    Solution s;
    vector<int> a = {4, 5, 6, 7, 0, 1, 2};
    assert(s.search(a, 0) == 4);
    assert(s.search(a, 3) == -1);
    vector<int> b = {1};
    assert(s.search(b, 0) == -1);
    assert(s.search(b, 1) == 0);
    vector<int> c = {3, 1};
    assert(s.search(c, 1) == 1);
    assert(s.search(c, 3) == 0);
    cout << "All tests passed." << endl;
    return 0;
}
