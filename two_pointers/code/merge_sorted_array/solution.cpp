#include <cassert>
#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
            else nums1[k--] = nums2[j--];
        }
        while (j >= 0) nums1[k--] = nums2[j--];
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,3,0,0,0}, b = {2,5,6};
    sol.merge(a, 3, b, 3);
    assert((a == std::vector<int>{1,2,2,3,5,6}));
    std::vector<int> c = {1}, d = {};
    sol.merge(c, 1, d, 0);
    assert((c == std::vector<int>{1}));
    std::vector<int> e = {0}, f = {1};
    sol.merge(e, 0, f, 1);
    assert((e == std::vector<int>{1}));
    return 0;
}
