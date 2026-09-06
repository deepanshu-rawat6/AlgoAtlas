#include <cassert>
#include <vector>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int l = 0, r = (int)s.size() - 1;
        while (l < r) { std::swap(s[l++], s[r--]); }
    }
};

int main() {
    Solution sol;
    std::vector<char> a = {'h','e','l','l','o'};
    sol.reverseString(a);
    assert((a == std::vector<char>{'o','l','l','e','h'}));
    std::vector<char> b = {'H','a','n','n','a','h'};
    sol.reverseString(b);
    assert((b == std::vector<char>{'h','a','n','n','a','H'}));
    std::vector<char> c = {'a'};
    sol.reverseString(c);
    assert((c == std::vector<char>{'a'}));
    return 0;
}
