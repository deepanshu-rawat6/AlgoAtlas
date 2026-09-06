#include <cassert>
#include <string>

class Solution {
public:
    bool validPalindrome(std::string s) {
        auto isPalin = [&](int l, int r) {
            while (l < r) if (s[l++] != s[r--]) return false;
            return true;
        };
        int l = 0, r = (int)s.size() - 1;
        while (l < r) {
            if (s[l] != s[r]) return isPalin(l+1, r) || isPalin(l, r-1);
            l++; r--;
        }
        return true;
    }
};

int main() {
    Solution sol;
    assert(sol.validPalindrome("aba") == true);
    assert(sol.validPalindrome("abca") == true);
    assert(sol.validPalindrome("abc") == false);
    assert(sol.validPalindrome("deeee") == true);
    return 0;
}
