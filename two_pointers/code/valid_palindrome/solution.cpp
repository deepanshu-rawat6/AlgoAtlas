// LC 125: Valid Palindrome
// Alphanumeric-only check, ignoring case, using two pointers from both ends.
// Time: O(n), Space: O(1)
#include <string>
#include <algorithm>
#include <cctype>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n) build filtered string then compare
    bool isPalindrome_brute(string s) {
        string filtered;
        for (char c : s)
            if (isalnum(c)) filtered += tolower(c);
        string rev = filtered;
        reverse(rev.begin(), rev.end());
        return filtered == rev;
    }

    // Optimal: O(n) two pointers, no extra string
    bool isPalindrome(string s) {
        int l = 0, r = (int)s.size() - 1;
        while (l < r) {
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
        }
        return true;
    }
};

int main() {
    Solution s;
    assert(s.isPalindrome("A man, a plan, a canal: Panama") == true);
    assert(s.isPalindrome("race a car") == false);
    assert(s.isPalindrome(" ") == true);
    assert(s.isPalindrome("") == true);
    assert(s.isPalindrome("0P") == false);
    cout << "All tests passed." << endl;
    return 0;
}
